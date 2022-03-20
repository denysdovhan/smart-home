"""
The Snowtire binary sensor.

For more details about this platform, please refer to the documentation at
https://github.com/Limych/ha-snowtire/
"""

from typing import Final

# Base component constants
NAME: Final = "Snowtire Sensor"
DOMAIN: Final = "snowtire"
VERSION: Final = "1.4.2"
ISSUE_URL: Final = "https://github.com/Limych/ha-snowtire/issues"

STARTUP_MESSAGE: Final = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have ANY issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

# Icons
ICON_WINTER: Final = "mdi:snowflake"
ICON_SUMMER: Final = "mdi:white-balance-sunny"

# Configuration and options
CONF_WEATHER: Final = "weather"
CONF_DAYS: Final = "days"

# Defaults
DEFAULT_NAME: Final = "Snowtire"
DEFAULT_DAYS: Final = 7
