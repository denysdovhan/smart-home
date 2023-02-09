#  Copyright (c) 2019-2021, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
#  Creative Commons BY-NC-SA 4.0 International Public License
#  (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)
"""The Car Wash binary sensor.

For more details about this platform, please refer to the documentation at
https://github.com/Limych/ha-car_wash/
"""

from collections.abc import Callable
from datetime import datetime
import logging
from typing import Optional

import voluptuous as vol

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.components.weather import (
    ATTR_FORECAST,
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_WEATHER_TEMPERATURE,
)
from homeassistant.const import (
    CONF_NAME,
    CONF_UNIQUE_ID,
    EVENT_HOMEASSISTANT_START,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.event import async_track_state_change
from homeassistant.helpers.typing import ConfigType
from homeassistant.util import dt as dt_util
from homeassistant.util.unit_conversion import TemperatureConverter

from .const import (
    BAD_CONDITIONS,
    CONF_DAYS,
    CONF_WEATHER,
    DEFAULT_DAYS,
    DEFAULT_NAME,
    DOMAIN,
    ICON,
    STARTUP_MESSAGE,
)

_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = cv.PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_WEATHER): cv.entity_id,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_DAYS, default=DEFAULT_DAYS): cv.positive_int,
        vol.Optional(CONF_UNIQUE_ID): cv.string,
    }
)


# pylint: disable=unused-argument
async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: Callable,
    discovery_info=None,
):
    """Set up the Car Wash sensor."""
    # Print startup message
    _LOGGER.info(STARTUP_MESSAGE)

    async_add_entities(
        [
            CarWashBinarySensor(
                config.get(CONF_UNIQUE_ID),
                config.get(CONF_NAME),
                config.get(CONF_WEATHER),
                config.get(CONF_DAYS),
            )
        ]
    )


class CarWashBinarySensor(BinarySensorEntity):
    """Implementation of an Car Wash binary sensor."""

    def __init__(
        self,
        unique_id: Optional[str],
        friendly_name: str,
        weather_entity: str,
        days: int,
    ):
        """Initialize the sensor."""
        self._weather_entity = weather_entity
        self._days = days

        self._attr_should_poll = False  # No polling needed
        self._attr_name = friendly_name
        self._attr_is_on = None
        self._attr_icon = ICON
        self._attr_device_class = f"{DOMAIN}__"
        #
        self._attr_unique_id = (
            DOMAIN + "-" + str(self._weather_entity).split(".")[1]
            if unique_id == "__legacy__"
            else unique_id
        )

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._attr_is_on is not None

    async def async_added_to_hass(self):
        """Register callbacks."""

        # pylint: disable=unused-argument
        @callback
        def sensor_state_listener(entity, old_state, new_state):
            """Handle device state changes."""
            self.async_schedule_update_ha_state(True)

        # pylint: disable=unused-argument
        @callback
        def sensor_startup(event):
            """Update template on startup."""
            async_track_state_change(
                self.hass, [self._weather_entity], sensor_state_listener
            )

            self.async_schedule_update_ha_state(True)

        self.hass.bus.async_listen_once(EVENT_HOMEASSISTANT_START, sensor_startup)

    @staticmethod
    def _temp2c(temperature: Optional[float], temperature_unit: str) -> Optional[float]:
        """Convert weather temperature to Celsius degree."""
        if temperature is not None and temperature_unit != UnitOfTemperature.CELSIUS:
            temperature = TemperatureConverter.convert(temperature, temperature_unit, UnitOfTemperature.CELSIUS)
        return temperature

    # pylint: disable=too-many-branches,too-many-statements
    async def async_update(self):
        """Update the sensor state."""
        wdata = self.hass.states.get(self._weather_entity)

        if wdata is None:
            raise HomeAssistantError(
                f"Unable to find an entity called {self._weather_entity}"
            )

        tmpu = self.hass.config.units.temperature_unit
        temp = wdata.attributes.get(ATTR_WEATHER_TEMPERATURE)
        cond = wdata.state
        forecast = wdata.attributes.get(ATTR_FORECAST)

        if forecast is None:
            self._attr_is_on = None
            raise HomeAssistantError(
                "Can't get forecast data! Are you sure it's the weather provider?"
            )

        _LOGGER.debug("Current temperature %s, condition '%s'", temp, cond)

        temp = self._temp2c(temp, tmpu)

        if cond in BAD_CONDITIONS:
            _LOGGER.debug("Detected bad weather condition")
            self._attr_is_on = False
            return

        today = dt_util.start_of_local_day()
        cur_date = today.strftime("%F")
        stop_date = datetime.fromtimestamp(
            today.timestamp() + 86400 * (self._days + 1)
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

            if prec and prec != "null":
                _LOGGER.debug("Precipitation detected")
                self._attr_is_on = False
                return
            if cond in BAD_CONDITIONS:
                _LOGGER.debug("Detected bad weather condition")
                self._attr_is_on = False
                return
            if tmin is not None and fc_date != cur_date:
                tmin = self._temp2c(tmin, tmpu)
                if temp < 0 <= tmin:
                    _LOGGER.debug(
                        "Detected passage of temperature through melting point"
                    )
                    self._attr_is_on = False
                    return
                temp = tmin
            if tmax is not None:
                tmax = self._temp2c(tmax, tmpu)
                if temp < 0 <= tmax:
                    _LOGGER.debug(
                        "Detected passage of temperature through melting point"
                    )
                    self._attr_is_on = False
                    return
                temp = tmax

        _LOGGER.debug("Inspection done. No bad forecast detected")
        self._attr_is_on = True
