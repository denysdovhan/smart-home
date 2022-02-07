"""
Support for SSH access.

For more details about this platform, please refer to the documentation at
https://github.com/custom-components/sensor.ssh

"""
import logging
import voluptuous as vol
from datetime import timedelta
import json
import asyncio

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.util import Throttle
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME, CONF_HOST, CONF_USERNAME, CONF_PASSWORD,
    CONF_VALUE_TEMPLATE, CONF_COMMAND, CONF_PORT,
    STATE_UNKNOWN, CONF_UNIT_OF_MEASUREMENT)

__version__ = '0.1.3'

_LOGGER = logging.getLogger(__name__)
DOMAIN = 'sensor'

DEFAULT_NAME = 'SSH'
DEFAULT_SSH_PORT = 22

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
    vol.Required(CONF_USERNAME): cv.string,
    vol.Optional(CONF_PORT, default=DEFAULT_SSH_PORT): cv.port,
    vol.Required(CONF_COMMAND): cv.string,
    vol.Required(CONF_UNIT_OF_MEASUREMENT): cv.string,
    vol.Optional(CONF_VALUE_TEMPLATE): cv.template,
})

@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):

    dev = []
    dev.append(SSHSensor(hass, config))
    async_add_devices(dev, True)


class SSHSensor(Entity):

    def __init__(self, hass, config):
        """Initialize the scanner."""
        self._name = config.get(CONF_NAME)
        self._host = config.get(CONF_HOST)
        self._username = config.get(CONF_USERNAME)
        self._password = config.get(CONF_PASSWORD)
        self._port = config.get(CONF_PORT)
        self._command = config.get(CONF_COMMAND)
        self._value_template = config.get(CONF_VALUE_TEMPLATE)
        self._unit_of_measurement = config.get(CONF_UNIT_OF_MEASUREMENT)
        self._ssh = None
        self._connected = False
        self._connect()
        self._attributes = {}

        if self._value_template is not None:
            self._value_template.hass = hass

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return 'mdi:folder-key-network'

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    @property
    def state_attributes(self):
        """Return the device state attributes."""
        return self._attributes

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return self._unit_of_measurement
    
    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        from pexpect import pxssh, exceptions

        try:
            if not self._connected:
                self._connect()
            # If we still aren't connected at this point
            # don't try to send anything to the AP.
            if not self._connected:
                return None
            self._ssh.sendline(self._command)
            self._ssh.prompt()

            value = self._ssh.before.decode("utf-8")

            if self._value_template is not None:
                self._state = self._value_template.render_with_possible_json_value(
                    value, STATE_UNKNOWN)
            else:
                self._state = value

            _LOGGER.debug(self._state)

        except pxssh.ExceptionPxssh as err:
            _LOGGER.error("Unexpected SSH error: %s", str(err))
            self._disconnect()
            return None
        except (AssertionError, exceptions.EOF) as err:
            _LOGGER.error("Connection unavailable: %s", str(err))
            self._disconnect()
            return None

    def _connect(self):
        """Connect to the Unifi AP SSH server."""
        from pexpect import pxssh, exceptions

        self._ssh = pxssh.pxssh()
        try:
            self._ssh.login(self._host, self._username,
                           password=self._password, port=self._port)
            self._connected = True
        except exceptions.EOF:
            _LOGGER.error("Connection refused. SSH enabled?")
            self._disconnect()

    def _disconnect(self):
        """Disconnect the current SSH connection."""
        # pylint: disable=broad-except
        try:
            self._ssh.logout()
        except Exception:
            pass
        finally:
            self._ssh = None

        self._connected = False

