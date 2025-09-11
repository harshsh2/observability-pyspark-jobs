from .api_tests import search
from .api_tests import init
from .api_tests import confirm
from .api_tests import status
from .api_tests import track
from .api_tests import cancel
from .api_tests import update
from .api_tests import on_search
from .api_tests import on_init
from .api_tests import on_confirm
from .api_tests import on_track
from .api_tests import on_cancel
from .api_tests import on_update
from .api_tests import on_status
from .api_tests import issue
from .api_tests import on_issue
from .types.test_config import ValidationConfig

def perform_l1_validations(action, payload,config: ValidationConfig = None, external_data=None):
    """
Perform Level-1 validations for a given `action`.

Args:
    action: string identifier of the action to validate against.
    payload: Any JSON-like structure to validate (dict/list/nested).
    config: Partial configuration. Can be:
        - a plain dict (snake_case or camelCase keys),
        - a dataclass/pydantic/object with fields,
        - or a `ValidationConfig` TypedDict.
        Missing fields are filled with defaults.
    external_data: Optional dict of extra data available to rules.
        `_SELF` is automatically set to the normalized payload.

Config fields (merged with defaults):
    - only_invalid (bool, default: True)
    - hide_parent_errors (bool, default: True)
    - _debug (bool, default: False)

Returns:
    ValidationOutput: a list of validation results, each shaped like:
        {
            "test_name": str,
            "valid": bool,
            "code": int,
            "description"?: str,
            "_debug_info"?: {
            "fed_config"?: str,
            "output_code"?: Any
            }
        }

Raises:
    ValueError: if the action is unknown.

Example:
    >>> out = perform_l1_validations("search", payload, {"only_invalid": False})
    >>> out[0]["test_name"]
    'REGEX_CONTEXT_LOCATION_CITY_CODE'
"""

    if external_data is None:
        external_data = {}

    from .utils.json_normalizer import normalize_keys
    normalized_payload = normalize_keys(payload.copy())
    external_data["_SELF"] = normalized_payload
    default_config = {
        "only_invalid": True,
        "standard_logs": False,
        "_debug": False,
        "hide_parent_errors": True,
    }
    # Merge user config with default config
    if config is None:
        config = default_config
    else:
        config = {**default_config, **config}

    input_data = {
        "payload": normalized_payload,
        "external_data": external_data,
        "config": config,
    }

    if action == "search":
        return search(input_data)
    elif action == "init":
        return init(input_data)
    elif action == "confirm":
        return confirm(input_data)
    elif action == "status":
        return status(input_data)
    elif action == "track":
        return track(input_data)
    elif action == "cancel":
        return cancel(input_data)
    elif action == "update":
        return update(input_data)
    elif action == "on_search":
        return on_search(input_data)
    elif action == "on_init":
        return on_init(input_data)
    elif action == "on_confirm":
        return on_confirm(input_data)
    elif action == "on_track":
        return on_track(input_data)
    elif action == "on_cancel":
        return on_cancel(input_data)
    elif action == "on_update":
        return on_update(input_data)
    elif action == "on_status":
        return on_status(input_data)
    elif action == "issue":
        return issue(input_data)
    elif action == "on_issue":
        return on_issue(input_data)
    else:
        raise Exception("Action not found")
