#
#  Copyright (c) 2019, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
#  Creative Commons BY-NC-SA 4.0 International Public License
#  (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)
#
"""
The Car Wash binary sensor.

For more details about this platform, please refer to the documentation at
https://github.com/Limych/ha-car_wash/
"""
import logging
from datetime import datetime

import voluptuous as vol

try:
    from homeassistant.components.binary_sensor import BinarySensorEntity
except ImportError:
    from homeassistant.components.binary_sensor import (
        BinarySensorDevice as BinarySensorEntity,
    )
from homeassistant.components.weather import (
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_CONDITION,
    ATTR_WEATHER_TEMPERATURE,
    ATTR_FORECAST,
)
from homeassistant.const import CONF_NAME, EVENT_HOMEASSISTANT_START, TEMP_CELSIUS
from homeassistant.core import callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.event import async_track_state_change
from homeassistant.util import dt as dt_util
from homeassistant.util.temperature import convert as convert_temperature

from . import (
    VERSION,
    ISSUE_URL,
)
from .const import (
    CONF_WEATHER,
    DEFAULT_NAME,
    DEFAULT_DAYS,
    CONF_DAYS,
    BAD_CONDITIONS,
)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = cv.PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_WEATHER): cv.entity_id,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_DAYS, default=DEFAULT_DAYS): vol.Coerce(int),
    }
)


# pylint: disable=w0613
async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Car Wash sensor."""
    # Print startup message
    _LOGGER.info("Version %s", VERSION)
    _LOGGER.info(
        "If you have ANY issues with this, please report them here: %s", ISSUE_URL
    )

    name = config.get(CONF_NAME)
    weather = config.get(CONF_WEATHER)
    days = config.get(CONF_DAYS)

    async_add_entities([CarWashBinarySensor(hass, name, weather, days)])


class CarWashBinarySensor(BinarySensorEntity):
    """Implementation of an Car Wash binary sensor."""

    def __init__(self, hass, friendly_name, weather_entity, days):
        """Initialize the sensor."""
        self._hass = hass
        self._name = friendly_name
        self._weather_entity = weather_entity
        self._days = days
        self._state = None

    async def async_added_to_hass(self):
        """Register callbacks."""

        @callback
        def sensor_state_listener(  # pylint: disable=w0613
            entity, old_state, new_state
        ):
            """Handle device state changes."""
            self.async_schedule_update_ha_state(True)

        @callback
        def sensor_startup(event):  # pylint: disable=w0613
            """Update template on startup."""
            async_track_state_change(
                self._hass, [self._weather_entity], sensor_state_listener
            )

            self.async_schedule_update_ha_state(True)

        self._hass.bus.async_listen_once(EVENT_HOMEASSISTANT_START, sensor_startup)

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def is_on(self):
        """Return True if sensor is on."""
        return self._state

    @property
    def icon(self):
        """Return the icon to use in the frontend, if any."""
        return "mdi:car-wash"

    @staticmethod
    def _temp2c(temperature: float, temperature_unit: str) -> float:
        """Convert weather temperature to Celsius degree."""
        if temperature is not None and temperature_unit != TEMP_CELSIUS:
            temperature = convert_temperature(
                temperature, temperature_unit, TEMP_CELSIUS
            )

        return temperature

    async def async_update(self):  # pylint: disable=r0912,r0915
        """Update the sensor state."""
        wdata = self._hass.states.get(self._weather_entity)

        if wdata is None:
            raise HomeAssistantError(
                f"Unable to find an entity called {self._weather_entity}"
            )

        tmpu = self._hass.config.units.temperature_unit
        temp = wdata.attributes.get(ATTR_WEATHER_TEMPERATURE)
        cond = wdata.state
        forecast = wdata.attributes.get(ATTR_FORECAST)

        if forecast is None:
            raise HomeAssistantError(
                "Can't get forecast data! Are you sure it's the weather provider?"
            )

        _LOGGER.debug("Current temperature %s, condition '%s'", temp, cond)

        temp = self._temp2c(temp, tmpu)

        if cond in BAD_CONDITIONS:
            _LOGGER.debug("Detected bad weather condition")
            self._state = False
            return

        cur_date = datetime.now().strftime("%F")
        stop_date = datetime.fromtimestamp(
            datetime.now().timestamp() + 86400 * (self._days + 1)
        ).strftime("%F")

        _LOGGER.debug("Inspect weather forecast from now till %s", stop_date)
        for fcast in forecast:
            fc_date = fcast.get(ATTR_FORECAST_TIME)
            if isinstance(fc_date, int):
                fc_date = dt_util.as_local(
                    datetime.utcfromtimestamp(fc_date / 1000)
                ).isoformat()
            elif isinstance(fc_date, datetime):
                fc_date = dt_util.as_local(fc_date).isoformat()
            fc_date = fc_date[:10]
            if fc_date < cur_date:
                continue
            if fc_date == stop_date:
                break
            _LOGGER.debug("Inspect weather forecast for %s", fc_date)

            prec = fcast.get(ATTR_FORECAST_PRECIPITATION)
            cond = fcast.get(ATTR_FORECAST_CONDITION)
            tmin = fcast.get(ATTR_FORECAST_TEMP_LOW)
            tmax = fcast.get(ATTR_FORECAST_TEMP)
            _LOGGER.debug(
                "Precipitation %s, Condition '%s',"
                " Min temperature: %s, Max temperature %s",
                prec,
                cond,
                tmin,
                tmax,
            )

            if prec:
                _LOGGER.debug("Precipitation detected")
                self._state = False
                return
            if cond in BAD_CONDITIONS:
                _LOGGER.debug("Detected bad weather condition")
                self._state = False
                return
            if tmin is not None and fc_date != cur_date:
                tmin = self._temp2c(tmin, tmpu)
                if temp < 0 <= tmin:
                    _LOGGER.debug(
                        "Detected passage of temperature through melting point"
                    )
                    self._state = False
                    return
                temp = tmin
            if tmax is not None:
                tmax = self._temp2c(tmax, tmpu)
                if temp < 0 <= tmax:
                    _LOGGER.debug(
                        "Detected passage of temperature through melting point"
                    )
                    self._state = False
                    return
                temp = tmax

        _LOGGER.debug("Inspection done. No bad forecast detected")
        self._state = True
