from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_environment

"""
This takes env variable with a matching prefix, strips out the prefix
then adds it to the global, E.g.
export CORESETTINGS_IN_DOCKER=True (environment variable)
Could be referenced as a global dictionary of variables
IN_DOCKER (where the value would be True)
"""

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore
