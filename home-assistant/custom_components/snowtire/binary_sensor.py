#
#  Copyright (c) 2020, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
#  Creative Commons BY-NC-SA 4.0 International Public License
#  (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)
#
"""
The Snowtire binary sensor.

For more details about this platform, please refer to the documentation at
https://github.com/Limych/ha-snowtire/
"""
import logging
from datetime import datetime
from typing import Optional

import voluptuous as vol

try:
    from homeassistant.components.binary_sensor import BinarySensorEntity
except ImportError:  # pragma: no cover
    from homeassistant.components.binary_sensor import (
        BinarySensorDevice as BinarySensorEntity,
    )

from homeassistant.components.weather import (
    ATTR_FORECAST,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_WEATHER_TEMPERATURE,
)
from homeassistant.components.weather import DOMAIN as WEATHER
from homeassistant.const import CONF_NAME, EVENT_HOMEASSISTANT_START, TEMP_CELSIUS
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.event import async_track_state_change
from homeassistant.util import dt as dt_util
from homeassistant.util.temperature import convert as convert_temperature

from .const import (
    ATTR_TYRE_TYPE,
    CONF_DAYS,
    CONF_WEATHER,
    DEFAULT_DAYS,
    DEFAULT_NAME,
    ICON,
    STARTUP_MESSAGE,
)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = cv.PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_WEATHER): cv.entity_domain(WEATHER),
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_DAYS, default=DEFAULT_DAYS): cv.positive_int,
    }
)


# pylint: disable=w0613
async def async_setup_platform(
    hass: HomeAssistant, config, async_add_entities, discovery_info=None
):
    """Set up the Snowtire sensor."""
    # Print startup message
    _LOGGER.info(STARTUP_MESSAGE)

    name = config.get(CONF_NAME)
    weather = config.get(CONF_WEATHER)
    days = config.get(CONF_DAYS)

    async_add_entities([SnowtireBinarySensor(hass, name, weather, days)])


class SnowtireBinarySensor(BinarySensorEntity):
    """Implementation of an Snowtire binary sensor."""

    def __init__(self, hass: HomeAssistant, friendly_name, weather_entity, days):
        """Initialize the sensor."""
        self._hass = hass
        self._name = friendly_name
        self._weather_entity = weather_entity
        self._days = days
        self._state = None

    async def async_added_to_hass(self):
        """Register callbacks."""

        @callback
        # pylint: disable=w0613
        def sensor_state_listener(entity, old_state, new_state):
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
        return ICON

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            ATTR_TYRE_TYPE: "Winter" if self.is_on else "Summer",
        }

    @staticmethod
    def _temp2c(
        temperature: Optional[float], temperature_unit: Optional[str]
    ) -> Optional[float]:
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
        forecast = wdata.attributes.get(ATTR_FORECAST)

        if forecast is None:
            raise HomeAssistantError(
                "Can't get forecast data! Are you sure it's the weather provider?"
            )

        _LOGGER.debug("Current temperature %.1f°C", temp)

        cur_date = datetime.now().strftime("%F")
        stop_date = datetime.fromtimestamp(
            datetime.now().timestamp() + 86400 * (self._days + 1)
        ).strftime("%F")

        _LOGGER.debug("Inspect weather forecast from now till %s", stop_date)
        temp = [self._temp2c(temp, tmpu)]
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

            tmin = fcast.get(ATTR_FORECAST_TEMP_LOW)
            tmax = fcast.get(ATTR_FORECAST_TEMP)

            if tmin is not None and fc_date != cur_date:
                temp.append(self._temp2c(tmin, tmpu))
            if tmax is not None:
                temp.append(self._temp2c(tmax, tmpu))

        _LOGGER.debug("Temperature vector: %s", temp)
        temp = sum(temp) / len(temp)
        _LOGGER.debug("Average temperature: %.1f°C", temp)
        self._state = temp < 7
