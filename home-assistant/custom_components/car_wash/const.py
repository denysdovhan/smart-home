#  Copyright (c) 2019-2021, Andrey "Limych" Khrolenok <andrey@khrolenok.ru>
#  Creative Commons BY-NC-SA 4.0 International Public License
#  (see LICENSE.md or https://creativecommons.org/licenses/by-nc-sa/4.0/)
"""
The Car Wash binary sensor.

For more details about this platform, please refer to the documentation at
https://github.com/Limych/ha-car_wash/
"""

from homeassistant.components.weather import (
    ATTR_CONDITION_EXCEPTIONAL,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
)

# Base component constants
NAME = "Car Wash"
DOMAIN = "car_wash"
VERSION = "1.5.0"
ISSUE_URL = "https://github.com/Limych/ha-car_wash/issues"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have ANY issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

# Icons
ICON = "mdi:car-wash"

# Configuration and options
CONF_WEATHER = "weather"
CONF_DAYS = "days"

# Defaults
DEFAULT_NAME = "Car Wash"
DEFAULT_DAYS = 2


BAD_CONDITIONS = [
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_EXCEPTIONAL,
]
