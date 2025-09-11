from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_track_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_track_validations_obj in scope:
        on_track_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def ON_TRACK_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_TRACK_CONTEXT_obj in scope:
                ON_TRACK_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["on_track"]

                def CONTEXT_REQUIRED(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for CONTEXT_REQUIRED_obj in scope:
                        CONTEXT_REQUIRED_obj["_EXTERNAL"] = input_data["external_data"]

                        def CONTEXT_REQUIRED_DOMAIN(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_DOMAIN_obj in scope:
                                CONTEXT_REQUIRED_DOMAIN_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_DOMAIN_obj, "$.context.domain")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_DOMAIN_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_DOMAIN",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_DOMAIN**: $.context.domain must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_DOMAIN_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_DOMAIN",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_ACTION**: $.context.action must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_ACTION",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_COUNTRY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_COUNTRY**: $.context.country must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_COUNTRY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def REQUIRED_CONTEXT_CODE_14(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for REQUIRED_CONTEXT_CODE_14_obj in scope:
                                REQUIRED_CONTEXT_CODE_14_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_CODE_14_obj, "$.context.city")
                                reg = ["^(std:\\d{3,5}|\\*)$"]
                                action = ["on_track"]

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del REQUIRED_CONTEXT_CODE_14_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "REQUIRED_CONTEXT_CODE_14",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition REQUIRED_CONTEXT_CODE_14**: all elements of $.context.city must follow every regex in ["^(std:\\d{3,5}|\\*)$"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del REQUIRED_CONTEXT_CODE_14_obj["_EXTERNAL"]

                            return [{
                                "test_name": "REQUIRED_CONTEXT_CODE_14",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_VERSION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_VERSION**: $.context.core_version must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_VERSION",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_BAP_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_BAP_ID**: $.context.bap_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_BAP_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_BAP_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_BAP_URI**: $.context.bap_uri must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_BAP_URI",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BPP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BPP_ID_obj in scope:
                                CONTEXT_REQUIRED_BPP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                search = ["search"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BPP_ID_obj, "$.context.bpp_id")
                                action = ["on_track"]

                                skip_check = validation_utils["equal_to"](action, search)
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_BPP_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_BPP_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_BPP_ID**: $.context.bpp_id must be present in the payload

                        	> Note: **Condition CONTEXT_REQUIRED_BPP_ID** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: ["on_track"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_BPP_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_BPP_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BPP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BPP_URI_obj in scope:
                                CONTEXT_REQUIRED_BPP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                search = ["search"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BPP_URI_obj, "$.context.bpp_uri")
                                action = ["on_track"]

                                skip_check = validation_utils["equal_to"](action, search)
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_BPP_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_BPP_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_BPP_URI**: $.context.bpp_uri must be present in the payload

                        	> Note: **Condition CONTEXT_REQUIRED_BPP_URI** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: ["on_track"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_BPP_URI_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_BPP_URI",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_TRANSACTION_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_TRANSACTION_ID**: $.context.transaction_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_TRANSACTION_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["on_track"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_MESSAGE_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_MESSAGE_ID**: $.context.message_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_MESSAGE_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]
                                action = ["on_track"]

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_TIMESTAMP",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_TIMESTAMP**: all elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_TIMESTAMP",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TTL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TTL_obj in scope:
                                CONTEXT_REQUIRED_TTL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TTL_obj, "$.context.ttl")
                                optional_vars = ["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"]
                                action = ["on_track"]

                                skip_check = validation_utils["all_in"](action, optional_vars)
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_TTL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_TTL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REQUIRED_TTL**: $.context.ttl must be present in the payload

                        	> Note: **Condition CONTEXT_REQUIRED_TTL** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: every element of ["on_track"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_TTL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_TTL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_track"]}
                        """
                            }}] + sub_results

                        test_functions = [
                            CONTEXT_REQUIRED_DOMAIN,
                            CONTEXT_REQUIRED_ACTION,
                            CONTEXT_REQUIRED_COUNTRY,
                            REQUIRED_CONTEXT_CODE_14,
                            CONTEXT_REQUIRED_VERSION,
                            CONTEXT_REQUIRED_BAP_ID,
                            CONTEXT_REQUIRED_BAP_URI,
                            CONTEXT_REQUIRED_BPP_ID,
                            CONTEXT_REQUIRED_BPP_URI,
                            CONTEXT_REQUIRED_TRANSACTION_ID,
                            CONTEXT_REQUIRED_MESSAGE_ID,
                            CONTEXT_REQUIRED_TIMESTAMP,
                            CONTEXT_REQUIRED_TTL,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del CONTEXT_REQUIRED_obj["_EXTERNAL"]

                    return [{
                        "test_name": "CONTEXT_REQUIRED",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_track"]}]}
                """
                    }}] + sub_results

                def CONTEXT_ENUM(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for CONTEXT_ENUM_obj in scope:
                        CONTEXT_ENUM_obj["_EXTERNAL"] = input_data["external_data"]

                        def CONTEXT_ENUM_DOMAIN(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_DOMAIN_obj in scope:
                                CONTEXT_ENUM_DOMAIN_obj["_EXTERNAL"] = input_data["external_data"]
                                domain = ["ONDC:RET10"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_DOMAIN_obj, "$.context.domain")
                                action = ["on_track"]

                                validate = validation_utils["equal_to"](attr, domain)

                                if not validate:
                                    del CONTEXT_ENUM_DOMAIN_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_DOMAIN",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_ENUM_DOMAIN**: $.context.domain must be equal to ["ONDC:RET10"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_ENUM_DOMAIN_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_ENUM_DOMAIN",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["on_track"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_track"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_ENUM_ACTION",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_VERSION_obj in scope:
                                CONTEXT_ENUM_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                version = ["1.2.5"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_VERSION_obj, "$.context.core_version")
                                action = ["on_track"]

                                validate = validation_utils["all_in"](attr, version)

                                if not validate:
                                    del CONTEXT_ENUM_VERSION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_VERSION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_ENUM_VERSION**: every element of $.context.core_version must be in ["1.2.5"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_ENUM_VERSION_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_ENUM_VERSION",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REG_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REG_BAP_URI_obj in scope:
                                CONTEXT_REG_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REG_BAP_URI_obj, "$.context.bap_uri")
                                reg = ["^https?\\:\\/\\/"]
                                action = ["on_track"]

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del CONTEXT_REG_BAP_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REG_BAP_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REG_BAP_URI**: all elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REG_BAP_URI_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REG_BAP_URI",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REG_BPP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REG_BPP_URI_obj in scope:
                                CONTEXT_REG_BPP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REG_BPP_URI_obj, "$.context.bpp_uri")
                                reg = ["^https?\\:\\/\\/"]
                                search = ["search"]
                                action = ["on_track"]

                                skip_check = validation_utils["equal_to"](action, search)
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del CONTEXT_REG_BPP_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REG_BPP_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REG_BPP_URI**: all elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]

                        	> Note: **Condition CONTEXT_REG_BPP_URI** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: ["on_track"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REG_BPP_URI_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REG_BPP_URI",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_track"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REG_TTL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REG_TTL_obj in scope:
                                CONTEXT_REG_TTL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REG_TTL_obj, "$.context.ttl")
                                reg = ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]
                                optional_vars = ["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"]
                                action = ["on_track"]

                                skip_check = validation_utils["all_in"](action, optional_vars)
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del CONTEXT_REG_TTL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REG_TTL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_REG_TTL**: all elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

                        	> Note: **Condition CONTEXT_REG_TTL** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: every element of ["on_track"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REG_TTL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REG_TTL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_track"]}
                        """
                            }}] + sub_results

                        test_functions = [
                            CONTEXT_ENUM_DOMAIN,
                            CONTEXT_ENUM_ACTION,
                            CONTEXT_ENUM_VERSION,
                            CONTEXT_REG_BAP_URI,
                            CONTEXT_REG_BPP_URI,
                            CONTEXT_REG_TTL,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del CONTEXT_ENUM_obj["_EXTERNAL"]

                    return [{
                        "test_name": "CONTEXT_ENUM",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_track"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_track"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_track"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_track"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_track"]}]}
                """
                    }}] + sub_results

                test_functions = [
                    CONTEXT_REQUIRED,
                    CONTEXT_ENUM,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del ON_TRACK_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_TRACK_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_TRACK_CONTEXT","_DESCRIPTION_":"Validate on_track context","action":["on_track"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_track"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_track"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_track"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_track"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_track"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_track"]}]}]}
        """
            }}] + sub_results

        def ON_TRACK_TRACKING(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_TRACK_TRACKING_obj in scope:
                ON_TRACK_TRACKING_obj["_EXTERNAL"] = input_data["external_data"]

                def TRACKING_ID(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TRACKING_ID_obj in scope:
                        TRACKING_ID_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](TRACKING_ID_obj, "$.message.tracking.id")

                        validate = validation_utils["are_present"](attr)

                        if not validate:
                            del TRACKING_ID_obj["_EXTERNAL"]
                            return [{
                                "test_name": "TRACKING_ID",
                                "valid": False,
                                "code": 30000,
                                "description": r"""- **condition TRACKING_ID**: $.message.tracking.id must be present in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"TRACKING_ID","attr":"$.message.tracking.id","_RETURN_":"attr are present"}
                """
                                }
                            }]

                        # del TRACKING_ID_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TRACKING_ID",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TRACKING_ID","attr":"$.message.tracking.id","_RETURN_":"attr are present"}
                """
                    }}] + sub_results

                def TRACKING_STATUS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TRACKING_STATUS_obj in scope:
                        TRACKING_STATUS_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](TRACKING_STATUS_obj, "$.message.tracking.status")
                        var_enum = ["active","inactive"]

                        validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                        if not validate:
                            del TRACKING_STATUS_obj["_EXTERNAL"]
                            return [{
                                "test_name": "TRACKING_STATUS",
                                "valid": False,
                                "code": 30000,
                                "description": r"""- **condition TRACKING_STATUS**: all of the following sub conditions must be met:

                  - **condition TRACKING_STATUS.1**: $.message.tracking.status must be present in the payload
                  - **condition TRACKING_STATUS.2**: every element of $.message.tracking.status must be in ["active", "inactive"]""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"TRACKING_STATUS","attr":"$.message.tracking.status","var_enum":["active","inactive"],"_RETURN_":"attr are present && attr all in var_enum"}
                """
                                }
                            }]

                        # del TRACKING_STATUS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TRACKING_STATUS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TRACKING_STATUS","attr":"$.message.tracking.status","var_enum":["active","inactive"],"_RETURN_":"attr are present && attr all in var_enum"}
                """
                    }}] + sub_results

                def TRACKING_LOCATION(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TRACKING_LOCATION_obj in scope:
                        TRACKING_LOCATION_obj["_EXTERNAL"] = input_data["external_data"]

                        def TRACKING_LOCATION_GPS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_LOCATION_GPS_obj in scope:
                                TRACKING_LOCATION_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TRACKING_LOCATION_GPS_obj, "$.message.tracking.location.gps")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del TRACKING_LOCATION_GPS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TRACKING_LOCATION_GPS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition TRACKING_LOCATION_GPS**: $.message.tracking.location.gps must be present in the payload

                        	> Note: **Condition TRACKING_LOCATION_GPS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.tracking.location.gps must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TRACKING_LOCATION_GPS","attr":"$.message.tracking.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del TRACKING_LOCATION_GPS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_LOCATION_GPS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_LOCATION_GPS","attr":"$.message.tracking.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def TRACKING_LOCATION_TIME_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_LOCATION_TIME_TIMESTAMP_obj in scope:
                                TRACKING_LOCATION_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TRACKING_LOCATION_TIME_TIMESTAMP_obj, "$.message.tracking.location.time.timestamp")
                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del TRACKING_LOCATION_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TRACKING_LOCATION_TIME_TIMESTAMP",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition TRACKING_LOCATION_TIME_TIMESTAMP**: all elements of $.message.tracking.location.time.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        	> Note: **Condition TRACKING_LOCATION_TIME_TIMESTAMP** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.tracking.location.time.timestamp must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TRACKING_LOCATION_TIME_TIMESTAMP","attr":"$.message.tracking.location.time.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}
                        """
                                        }
                                    }]

                                # del TRACKING_LOCATION_TIME_TIMESTAMP_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_LOCATION_TIME_TIMESTAMP",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_LOCATION_TIME_TIMESTAMP","attr":"$.message.tracking.location.time.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}
                        """
                            }}] + sub_results

                        def TRACKING_LOCATION_UPDATED_AT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_LOCATION_UPDATED_AT_obj in scope:
                                TRACKING_LOCATION_UPDATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TRACKING_LOCATION_UPDATED_AT_obj, "$.message.tracking.location.updated_at")
                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del TRACKING_LOCATION_UPDATED_AT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TRACKING_LOCATION_UPDATED_AT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition TRACKING_LOCATION_UPDATED_AT**: all elements of $.message.tracking.location.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        	> Note: **Condition TRACKING_LOCATION_UPDATED_AT** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.tracking.location.updated_at must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TRACKING_LOCATION_UPDATED_AT","attr":"$.message.tracking.location.updated_at","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}
                        """
                                        }
                                    }]

                                # del TRACKING_LOCATION_UPDATED_AT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_LOCATION_UPDATED_AT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_LOCATION_UPDATED_AT","attr":"$.message.tracking.location.updated_at","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TRACKING_LOCATION_GPS,
                            TRACKING_LOCATION_TIME_TIMESTAMP,
                            TRACKING_LOCATION_UPDATED_AT,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TRACKING_LOCATION_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TRACKING_LOCATION",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TRACKING_LOCATION","_RETURN_":[{"_NAME_":"TRACKING_LOCATION_GPS","attr":"$.message.tracking.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_LOCATION_TIME_TIMESTAMP","attr":"$.message.tracking.location.time.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"},{"_NAME_":"TRACKING_LOCATION_UPDATED_AT","attr":"$.message.tracking.location.updated_at","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}]}
                """
                    }}] + sub_results

                def TRACKING_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TRACKING_TAGS_obj in scope:
                        TRACKING_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TRACKING_VALID_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_VALID_TAGS_obj in scope:
                                TRACKING_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TRACKING_VALID_TAGS_obj, "$.message.tracking.tags[*].code")
                                valid = ["id","config","path"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, valid)

                                if not validate:
                                    del TRACKING_VALID_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TRACKING_VALID_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition TRACKING_VALID_TAGS**: every element of $.message.tracking.tags[*].code must be in ["id", "config", "path"]

                        	> Note: **Condition TRACKING_VALID_TAGS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.tracking.tags[*].code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TRACKING_VALID_TAGS","attr":"$.message.tracking.tags[*].code","valid":["id","config","path"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"}
                        """
                                        }
                                    }]

                                # del TRACKING_VALID_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_VALID_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_VALID_TAGS","attr":"$.message.tracking.tags[*].code","valid":["id","config","path"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"}
                        """
                            }}] + sub_results

                        def TRACKING_ORDER_TAG(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_ORDER_TAG_obj in scope:
                                TRACKING_ORDER_TAG_obj["_EXTERNAL"] = input_data["external_data"]

                                def ORDER_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ORDER_ID_obj in scope:
                                        ORDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ORDER_ID_obj, "$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ORDER_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ORDER_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ORDER_ID**: $.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value must be present in the payload

                                	> Note: **Condition ORDER_ID** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ORDER_ID","attr":"$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ORDER_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ORDER_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ORDER_ID","attr":"$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    ORDER_ID,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del TRACKING_ORDER_TAG_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_ORDER_TAG",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_ORDER_TAG","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def TRACKING_CONFIG_TAG(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_CONFIG_TAG_obj in scope:
                                TRACKING_CONFIG_TAG_obj["_EXTERNAL"] = input_data["external_data"]

                                def TRACKING_CONFIG_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TRACKING_CONFIG_VALID_TAGS_obj in scope:
                                        TRACKING_CONFIG_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TRACKING_CONFIG_VALID_TAGS_obj, "$.message.tracking.tags[?(@.code=='config')].list[*].code")
                                        valid = ["attr","type"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TRACKING_CONFIG_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TRACKING_CONFIG_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TRACKING_CONFIG_VALID_TAGS**: every element of $.message.tracking.tags[?(@.code=='config')].list[*].code must be in ["attr", "type"]

                                	> Note: **Condition TRACKING_CONFIG_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='config')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TRACKING_CONFIG_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='config')].list[*].code","_CONTINUE_":"!(attr are present)","valid":["attr","type"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TRACKING_CONFIG_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TRACKING_CONFIG_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TRACKING_CONFIG_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='config')].list[*].code","_CONTINUE_":"!(attr are present)","valid":["attr","type"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def CONFIG_ATTR(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for CONFIG_ATTR_obj in scope:
                                        CONFIG_ATTR_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](CONFIG_ATTR_obj, "$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del CONFIG_ATTR_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "CONFIG_ATTR",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition CONFIG_ATTR**: $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value must be present in the payload

                                	> Note: **Condition CONFIG_ATTR** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"CONFIG_ATTR","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del CONFIG_ATTR_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "CONFIG_ATTR",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"CONFIG_ATTR","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def CONFIG_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for CONFIG_TYPE_obj in scope:
                                        CONFIG_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](CONFIG_TYPE_obj, "$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value")
                                        var_enum = ["live_poll","deferred"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del CONFIG_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "CONFIG_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition CONFIG_TYPE**: every element of $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value must be in ["live_poll", "deferred"]

                                	> Note: **Condition CONFIG_TYPE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"CONFIG_TYPE","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value","_CONTINUE_":"!(attr are present)","var_enum":["live_poll","deferred"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del CONFIG_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "CONFIG_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"CONFIG_TYPE","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value","_CONTINUE_":"!(attr are present)","var_enum":["live_poll","deferred"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TRACKING_CONFIG_VALID_TAGS,
                                    CONFIG_ATTR,
                                    CONFIG_TYPE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del TRACKING_CONFIG_TAG_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_CONFIG_TAG",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_CONFIG_TAG","_RETURN_":[{"_NAME_":"TRACKING_CONFIG_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='config')].list[*].code","_CONTINUE_":"!(attr are present)","valid":["attr","type"],"_RETURN_":"attr all in valid"},{"_NAME_":"CONFIG_ATTR","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"CONFIG_TYPE","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value","_CONTINUE_":"!(attr are present)","var_enum":["live_poll","deferred"],"_RETURN_":"attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        def TRACKING_PATH_TAG(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TRACKING_PATH_TAG_obj in scope:
                                TRACKING_PATH_TAG_obj["_EXTERNAL"] = input_data["external_data"]

                                def TRACKING_PATH_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TRACKING_PATH_VALID_TAGS_obj in scope:
                                        TRACKING_PATH_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TRACKING_PATH_VALID_TAGS_obj, "$.message.tracking.tags[?(@.code=='path')].list[*].code")
                                        valid = ["lat_lng","sequence"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TRACKING_PATH_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TRACKING_PATH_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TRACKING_PATH_VALID_TAGS**: every element of $.message.tracking.tags[?(@.code=='path')].list[*].code must be in ["lat_lng", "sequence"]

                                	> Note: **Condition TRACKING_PATH_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='path')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TRACKING_PATH_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='path')].list[*].code","valid":["lat_lng","sequence"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TRACKING_PATH_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TRACKING_PATH_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TRACKING_PATH_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='path')].list[*].code","valid":["lat_lng","sequence"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def PATH_LAT_LNG(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PATH_LAT_LNG_obj in scope:
                                        PATH_LAT_LNG_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PATH_LAT_LNG_obj, "$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PATH_LAT_LNG_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PATH_LAT_LNG",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PATH_LAT_LNG**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value must be present in the payload

                                	> Note: **Condition PATH_LAT_LNG** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PATH_LAT_LNG","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PATH_LAT_LNG_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PATH_LAT_LNG",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PATH_LAT_LNG","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PATH_SEQUENCE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PATH_SEQUENCE_obj in scope:
                                        PATH_SEQUENCE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PATH_SEQUENCE_obj, "$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value")
                                        var_enum = ["1","2","3"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                        if not validate:
                                            del PATH_SEQUENCE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PATH_SEQUENCE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PATH_SEQUENCE**: all of the following sub conditions must be met:

                                  - **condition PATH_SEQUENCE.1**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value must be present in the payload
                                  - **condition PATH_SEQUENCE.2**: every element of $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value must be in ["1", "2", "3"]

                                	> Note: **Condition PATH_SEQUENCE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PATH_SEQUENCE","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value","var_enum":["1","2","3"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present && attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del PATH_SEQUENCE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PATH_SEQUENCE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PATH_SEQUENCE","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value","var_enum":["1","2","3"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present && attr all in var_enum"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TRACKING_PATH_VALID_TAGS,
                                    PATH_LAT_LNG,
                                    PATH_SEQUENCE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del TRACKING_PATH_TAG_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TRACKING_PATH_TAG",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TRACKING_PATH_TAG","_RETURN_":[{"_NAME_":"TRACKING_PATH_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='path')].list[*].code","valid":["lat_lng","sequence"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"PATH_LAT_LNG","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PATH_SEQUENCE","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value","var_enum":["1","2","3"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present && attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            TRACKING_VALID_TAGS,
                            TRACKING_ORDER_TAG,
                            TRACKING_CONFIG_TAG,
                            TRACKING_PATH_TAG,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TRACKING_TAGS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TRACKING_TAGS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TRACKING_TAGS","_RETURN_":[{"_NAME_":"TRACKING_VALID_TAGS","attr":"$.message.tracking.tags[*].code","valid":["id","config","path"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"TRACKING_ORDER_TAG","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"TRACKING_CONFIG_TAG","_RETURN_":[{"_NAME_":"TRACKING_CONFIG_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='config')].list[*].code","_CONTINUE_":"!(attr are present)","valid":["attr","type"],"_RETURN_":"attr all in valid"},{"_NAME_":"CONFIG_ATTR","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"CONFIG_TYPE","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value","_CONTINUE_":"!(attr are present)","var_enum":["live_poll","deferred"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TRACKING_PATH_TAG","_RETURN_":[{"_NAME_":"TRACKING_PATH_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='path')].list[*].code","valid":["lat_lng","sequence"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"PATH_LAT_LNG","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PATH_SEQUENCE","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value","var_enum":["1","2","3"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present && attr all in var_enum"}]}]}
                """
                    }}] + sub_results

                test_functions = [
                    TRACKING_ID,
                    TRACKING_STATUS,
                    TRACKING_LOCATION,
                    TRACKING_TAGS,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del ON_TRACK_TRACKING_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_TRACK_TRACKING",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_TRACK_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_ID","attr":"$.message.tracking.id","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_STATUS","attr":"$.message.tracking.status","var_enum":["active","inactive"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"TRACKING_LOCATION","_RETURN_":[{"_NAME_":"TRACKING_LOCATION_GPS","attr":"$.message.tracking.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_LOCATION_TIME_TIMESTAMP","attr":"$.message.tracking.location.time.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"},{"_NAME_":"TRACKING_LOCATION_UPDATED_AT","attr":"$.message.tracking.location.updated_at","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TRACKING_TAGS","_RETURN_":[{"_NAME_":"TRACKING_VALID_TAGS","attr":"$.message.tracking.tags[*].code","valid":["id","config","path"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"TRACKING_ORDER_TAG","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"TRACKING_CONFIG_TAG","_RETURN_":[{"_NAME_":"TRACKING_CONFIG_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='config')].list[*].code","_CONTINUE_":"!(attr are present)","valid":["attr","type"],"_RETURN_":"attr all in valid"},{"_NAME_":"CONFIG_ATTR","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"CONFIG_TYPE","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value","_CONTINUE_":"!(attr are present)","var_enum":["live_poll","deferred"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TRACKING_PATH_TAG","_RETURN_":[{"_NAME_":"TRACKING_PATH_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='path')].list[*].code","valid":["lat_lng","sequence"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"PATH_LAT_LNG","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PATH_SEQUENCE","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value","var_enum":["1","2","3"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present && attr all in var_enum"}]}]}]}
        """
            }}] + sub_results

        test_functions = [
            ON_TRACK_CONTEXT,
            ON_TRACK_TRACKING,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_track_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_track_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_track_validations","_RETURN_":[{"_NAME_":"ON_TRACK_CONTEXT","_DESCRIPTION_":"Validate on_track context","action":["on_track"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_track"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_track"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_track"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_track"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_track"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_track"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_track"]}]}]},{"_NAME_":"ON_TRACK_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_ID","attr":"$.message.tracking.id","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_STATUS","attr":"$.message.tracking.status","var_enum":["active","inactive"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"TRACKING_LOCATION","_RETURN_":[{"_NAME_":"TRACKING_LOCATION_GPS","attr":"$.message.tracking.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_LOCATION_TIME_TIMESTAMP","attr":"$.message.tracking.location.time.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"},{"_NAME_":"TRACKING_LOCATION_UPDATED_AT","attr":"$.message.tracking.location.updated_at","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TRACKING_TAGS","_RETURN_":[{"_NAME_":"TRACKING_VALID_TAGS","attr":"$.message.tracking.tags[*].code","valid":["id","config","path"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"TRACKING_ORDER_TAG","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.tracking.tags[?(@.code=='order')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"TRACKING_CONFIG_TAG","_RETURN_":[{"_NAME_":"TRACKING_CONFIG_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='config')].list[*].code","_CONTINUE_":"!(attr are present)","valid":["attr","type"],"_RETURN_":"attr all in valid"},{"_NAME_":"CONFIG_ATTR","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='attr')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"CONFIG_TYPE","attr":"$.message.tracking.tags[?(@.code=='config')].list[?(@.code=='type')].value","_CONTINUE_":"!(attr are present)","var_enum":["live_poll","deferred"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TRACKING_PATH_TAG","_RETURN_":[{"_NAME_":"TRACKING_PATH_VALID_TAGS","attr":"$.message.tracking.tags[?(@.code=='path')].list[*].code","valid":["lat_lng","sequence"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in valid"},{"_NAME_":"PATH_LAT_LNG","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='lat_lng')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PATH_SEQUENCE","attr":"$.message.tracking.tags[?(@.code=='path')].list[?(@.code=='sequence')].value","var_enum":["1","2","3"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present && attr all in var_enum"}]}]}]}]}
"""
    }}] + sub_results

def on_track(input_data):
    total_results = on_track_validations(input_data)

    if input_data["config"].get("_debug") is False:
        for r in total_results:
            if "_debug_info" in r:
                del r["_debug_info"]

    if input_data["config"].get("hide_parent_errors") is True:
        # delete results with valid false and no description
        total_results = [r for r in total_results if not (r["valid"] is False and "description" not in r)]

    if input_data["config"].get("only_invalid") is True:
        res = [r for r in total_results if r["valid"] is False]
        if len(res) == 0:
            target_success = next((r for r in total_results if r["test_name"] == "on_track_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
