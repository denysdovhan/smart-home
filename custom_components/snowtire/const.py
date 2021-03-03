"""
The Snowtire binary sensor.

For more details about this platform, please refer to the documentation at
https://github.com/Limych/ha-snowtire/
"""

# Base component constants
NAME = "Snowtire Sensor"
DOMAIN = "snowtire"
VERSION = "0.1.0"
ISSUE_URL = "https://github.com/Limych/ha-snowtire/issues"

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
ICON = "mdi:snowflake"

# Configuration and options
CONF_WEATHER = "weather"
CONF_DAYS = "days"

# Defaults
DEFAULT_NAME = "Snowtire"
DEFAULT_DAYS = 7

# Attributes
ATTR_TYRE_TYPE = "Tyre type"
