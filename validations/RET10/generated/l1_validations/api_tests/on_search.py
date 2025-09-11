from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_search_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_search_validations_obj in scope:
        on_search_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def ON_SEARCH_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_SEARCH_CONTEXT_obj in scope:
                ON_SEARCH_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["on_search"]

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
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_search"]}
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
                                action = ["on_search"]

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
                        {"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                        {"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_search"]}
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
                                action = ["on_search"]

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
                        	> - **condition B**: ["on_search"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_search"]}
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
                                action = ["on_search"]

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
                        	> - **condition B**: ["on_search"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_search"]}
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
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                                action = ["on_search"]

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
                        	> - **condition B**: every element of ["on_search"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_search"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_search"]}]}
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
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["on_search"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_search"]}
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
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_search"]}
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
                                action = ["on_search"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                                action = ["on_search"]

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
                        	> - **condition B**: ["on_search"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_search"]}
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
                                action = ["on_search"]

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
                        	> - **condition B**: every element of ["on_search"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_search"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_search"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_search"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_search"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_search"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_search"]}]}
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

                # del ON_SEARCH_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_SEARCH_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_SEARCH_CONTEXT","_DESCRIPTION_":"Validate on_search context","action":["on_search"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_search"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_search"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_search"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_search"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_search"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_search"]}]}]}
        """
            }}] + sub_results

        def ON_SEARCH_CATALOG(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_SEARCH_CATALOG_obj in scope:
                ON_SEARCH_CATALOG_obj["_EXTERNAL"] = input_data["external_data"]

                def CATALOG_BPP_DESCRIPTOR(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for CATALOG_BPP_DESCRIPTOR_obj in scope:
                        CATALOG_BPP_DESCRIPTOR_obj["_EXTERNAL"] = input_data["external_data"]

                        def BPP_DESCRIPTOR_NAME(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_DESCRIPTOR_NAME_obj in scope:
                                BPP_DESCRIPTOR_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BPP_DESCRIPTOR_NAME_obj, "$.message.catalog['bpp/descriptor'].name")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BPP_DESCRIPTOR_NAME_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BPP_DESCRIPTOR_NAME",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BPP_DESCRIPTOR_NAME**: $.message.catalog['bpp/descriptor'].name must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BPP_DESCRIPTOR_NAME_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_DESCRIPTOR_NAME",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BPP_DESCRIPTOR_SYMBOL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_DESCRIPTOR_SYMBOL_obj in scope:
                                BPP_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BPP_DESCRIPTOR_SYMBOL_obj, "$.message.catalog['bpp/descriptor'].symbol")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BPP_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BPP_DESCRIPTOR_SYMBOL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BPP_DESCRIPTOR_SYMBOL**: $.message.catalog['bpp/descriptor'].symbol must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/descriptor'].symbol","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BPP_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_DESCRIPTOR_SYMBOL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/descriptor'].symbol","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BPP_DESCRIPTOR_SHORT_DESC(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_DESCRIPTOR_SHORT_DESC_obj in scope:
                                BPP_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BPP_DESCRIPTOR_SHORT_DESC_obj, "$.message.catalog['bpp/descriptor'].short_desc")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BPP_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BPP_DESCRIPTOR_SHORT_DESC",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BPP_DESCRIPTOR_SHORT_DESC**: $.message.catalog['bpp/descriptor'].short_desc must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/descriptor'].short_desc","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BPP_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_DESCRIPTOR_SHORT_DESC",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/descriptor'].short_desc","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BPP_DESCRIPTOR_LONG_DESC(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_DESCRIPTOR_LONG_DESC_obj in scope:
                                BPP_DESCRIPTOR_LONG_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BPP_DESCRIPTOR_LONG_DESC_obj, "$.message.catalog['bpp/descriptor'].long_desc")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BPP_DESCRIPTOR_LONG_DESC_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BPP_DESCRIPTOR_LONG_DESC",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BPP_DESCRIPTOR_LONG_DESC**: $.message.catalog['bpp/descriptor'].long_desc must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/descriptor'].long_desc","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BPP_DESCRIPTOR_LONG_DESC_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_DESCRIPTOR_LONG_DESC",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/descriptor'].long_desc","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BPP_DESCRIPTOR_IMAGES(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_DESCRIPTOR_IMAGES_obj in scope:
                                BPP_DESCRIPTOR_IMAGES_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BPP_DESCRIPTOR_IMAGES_obj, "$.message.catalog['bpp/descriptor'].images[*]")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BPP_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BPP_DESCRIPTOR_IMAGES",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BPP_DESCRIPTOR_IMAGES**: $.message.catalog['bpp/descriptor'].images[*] must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/descriptor'].images[*]","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BPP_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_DESCRIPTOR_IMAGES",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/descriptor'].images[*]","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BPP_DESCRIPTOR_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_DESCRIPTOR_TAGS_obj in scope:
                                BPP_DESCRIPTOR_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_BPP_DESCRIPTORS_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_DESCRIPTORS_VALID_TAGS_obj in scope:
                                        TAGS_BPP_DESCRIPTORS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_DESCRIPTORS_VALID_TAGS_obj, "$.message.catalog['bpp/descriptor'].tags[*].code")
                                        valid = ["bpp_terms"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_BPP_DESCRIPTORS_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_DESCRIPTORS_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_DESCRIPTORS_VALID_TAGS**: every element of $.message.catalog['bpp/descriptor'].tags[*].code must be in ["bpp_terms"]

                                	> Note: **Condition TAGS_BPP_DESCRIPTORS_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/descriptor'].tags[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[*].code","valid":["bpp_terms"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_DESCRIPTORS_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_DESCRIPTORS_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[*].code","valid":["bpp_terms"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_DESCRIPTORS_VALID_ENUMS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_DESCRIPTORS_VALID_ENUMS_obj in scope:
                                        TAGS_BPP_DESCRIPTORS_VALID_ENUMS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_DESCRIPTORS_VALID_ENUMS_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code")
                                        valid = ["np_type","accept_bap_terms","collect_payment"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_BPP_DESCRIPTORS_VALID_ENUMS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_DESCRIPTORS_VALID_ENUMS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_DESCRIPTORS_VALID_ENUMS**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code must be in ["np_type", "accept_bap_terms", "collect_payment"]

                                	> Note: **Condition TAGS_BPP_DESCRIPTORS_VALID_ENUMS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_ENUMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code","valid":["np_type","accept_bap_terms","collect_payment"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_DESCRIPTORS_VALID_ENUMS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_DESCRIPTORS_VALID_ENUMS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_ENUMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code","valid":["np_type","accept_bap_terms","collect_payment"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def BPP_DESCRIPTOR_TAGS_BPP_TERMS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BPP_DESCRIPTOR_TAGS_BPP_TERMS_obj in scope:
                                        BPP_DESCRIPTOR_TAGS_BPP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_BPP_TERMS_NP_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_BPP_TERMS_NP_TYPE_obj in scope:
                                                TAGS_BPP_TERMS_NP_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_NP_TYPE_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value")
                                                var_enum = ["ISN","MSN"]

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_BPP_TERMS_NP_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_BPP_TERMS_NP_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_BPP_TERMS_NP_TYPE**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must be in ["ISN", "MSN"]""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_BPP_TERMS_NP_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_NP_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_BPP_TERMS_ACCEPT_BAP_TERMS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj in scope:
                                                TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value")
                                                var_enum = ["Y","N"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_BPP_TERMS_ACCEPT_BAP_TERMS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_BPP_TERMS_ACCEPT_BAP_TERMS**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value must be in ["Y", "N"]

                                        	> Note: **Condition TAGS_BPP_TERMS_ACCEPT_BAP_TERMS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_ACCEPT_BAP_TERMS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_BPP_TERMS_COLLECT_PAYMENT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_BPP_TERMS_COLLECT_PAYMENT_obj in scope:
                                                TAGS_BPP_TERMS_COLLECT_PAYMENT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_COLLECT_PAYMENT_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value")
                                                var_enum = ["Y","N"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_BPP_TERMS_COLLECT_PAYMENT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_BPP_TERMS_COLLECT_PAYMENT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_BPP_TERMS_COLLECT_PAYMENT**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value must be in ["Y", "N"]

                                        	> Note: **Condition TAGS_BPP_TERMS_COLLECT_PAYMENT** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_BPP_TERMS_COLLECT_PAYMENT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_COLLECT_PAYMENT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_BPP_TERMS_MANDATORY_ARBITRATION(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj in scope:
                                                TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value")
                                                var_enum = ["True","False"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_BPP_TERMS_MANDATORY_ARBITRATION",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_BPP_TERMS_MANDATORY_ARBITRATION**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value must be in ["true", "false"]

                                        	> Note: **Condition TAGS_BPP_TERMS_MANDATORY_ARBITRATION** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_MANDATORY_ARBITRATION",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_BPP_TERMS_NP_TYPE,
                                            TAGS_BPP_TERMS_ACCEPT_BAP_TERMS,
                                            TAGS_BPP_TERMS_COLLECT_PAYMENT,
                                            TAGS_BPP_TERMS_MANDATORY_ARBITRATION,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del BPP_DESCRIPTOR_TAGS_BPP_TERMS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BPP_DESCRIPTOR_TAGS_BPP_TERMS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BPP_DESCRIPTOR_TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_BPP_DESCRIPTORS_VALID_TAGS,
                                    TAGS_BPP_DESCRIPTORS_VALID_ENUMS,
                                    BPP_DESCRIPTOR_TAGS_BPP_TERMS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del BPP_DESCRIPTOR_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_DESCRIPTOR_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_DESCRIPTOR_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[*].code","valid":["bpp_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_ENUMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code","valid":["np_type","accept_bap_terms","collect_payment"],"_RETURN_":"attr all in valid"},{"_NAME_":"BPP_DESCRIPTOR_TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}]}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            BPP_DESCRIPTOR_NAME,
                            BPP_DESCRIPTOR_SYMBOL,
                            BPP_DESCRIPTOR_SHORT_DESC,
                            BPP_DESCRIPTOR_LONG_DESC,
                            BPP_DESCRIPTOR_IMAGES,
                            BPP_DESCRIPTOR_TAGS,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del CATALOG_BPP_DESCRIPTOR_obj["_EXTERNAL"]

                    return [{
                        "test_name": "CATALOG_BPP_DESCRIPTOR",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"CATALOG_BPP_DESCRIPTOR","_RETURN_":[{"_NAME_":"BPP_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/descriptor'].symbol","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/descriptor'].short_desc","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/descriptor'].long_desc","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/descriptor'].images[*]","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[*].code","valid":["bpp_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_ENUMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code","valid":["np_type","accept_bap_terms","collect_payment"],"_RETURN_":"attr all in valid"},{"_NAME_":"BPP_DESCRIPTOR_TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}]}]}]}
                """
                    }}] + sub_results

                def CATALOG_BPP_PROVIDERS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for CATALOG_BPP_PROVIDERS_obj in scope:
                        CATALOG_BPP_PROVIDERS_obj["_EXTERNAL"] = input_data["external_data"]

                        def PROVIDERS_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_ID_obj in scope:
                                PROVIDERS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PROVIDERS_ID_obj, "$.message.catalog['bpp/providers'][*].id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PROVIDERS_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PROVIDERS_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PROVIDERS_ID**: $.message.catalog['bpp/providers'][*].id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PROVIDERS_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PROVIDERS_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PROVIDERS_RATING(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_RATING_obj in scope:
                                PROVIDERS_RATING_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PROVIDERS_RATING_obj, "$.message.catalog['bpp/providers'][*].rating")
                                rating_reg = ["^(?:[1-4](?:\\.\\d+)?|5(?:\\.0+)?|\\s*)$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, rating_reg)

                                if not validate:
                                    del PROVIDERS_RATING_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PROVIDERS_RATING",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PROVIDERS_RATING**: all elements of $.message.catalog['bpp/providers'][*].rating must follow every regex in ["^(?:[1-4](?:\\.\\d+)?|5(?:\\.0+)?|\\s*)$"]

                        	> Note: **Condition PROVIDERS_RATING** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.catalog['bpp/providers'][*].rating must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PROVIDERS_RATING","attr":"$.message.catalog['bpp/providers'][*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"}
                        """
                                        }
                                    }]

                                # del PROVIDERS_RATING_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_RATING",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_RATING","attr":"$.message.catalog['bpp/providers'][*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"}
                        """
                            }}] + sub_results

                        def PROVIDERS_TIME_LABEL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_TIME_LABEL_obj in scope:
                                PROVIDERS_TIME_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PROVIDERS_TIME_LABEL_obj, "$.message.catalog['bpp/providers'][*].time.label")
                                var_enum = ["enable","disable"]

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del PROVIDERS_TIME_LABEL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PROVIDERS_TIME_LABEL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PROVIDERS_TIME_LABEL**: every element of $.message.catalog['bpp/providers'][*].time.label must be in ["enable", "disable"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PROVIDERS_TIME_LABEL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_TIME_LABEL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PROVIDERS_TIME_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_TIME_TIMESTAMP_obj in scope:
                                PROVIDERS_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PROVIDERS_TIME_TIMESTAMP_obj, "$.message.catalog['bpp/providers'][*].time.timestamp")
                                time_reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                validate = validation_utils["follow_regex"](attr, time_reg)

                                if not validate:
                                    del PROVIDERS_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PROVIDERS_TIME_TIMESTAMP",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PROVIDERS_TIME_TIMESTAMP**: all elements of $.message.catalog['bpp/providers'][*].time.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"}
                        """
                                        }
                                    }]

                                # del PROVIDERS_TIME_TIMESTAMP_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_TIME_TIMESTAMP",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"}
                        """
                            }}] + sub_results

                        def PROVIDERS_TAGS_VALID_ENUMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_TAGS_VALID_ENUMS_obj in scope:
                                PROVIDERS_TAGS_VALID_ENUMS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PROVIDERS_TAGS_VALID_ENUMS_obj, "$.message.catalog['bpp/providers'][*].tags[*].code")
                                var_enum = ["timing","close_timing","serviceability","order_value","np_fees"]

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del PROVIDERS_TAGS_VALID_ENUMS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PROVIDERS_TAGS_VALID_ENUMS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PROVIDERS_TAGS_VALID_ENUMS**: every element of $.message.catalog['bpp/providers'][*].tags[*].code must be in ["timing", "close_timing", "serviceability", "order_value", "np_fees"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TAGS_VALID_ENUMS","attr":"$.message.catalog['bpp/providers'][*].tags[*].code","var_enum":["timing","close_timing","serviceability","order_value","np_fees"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PROVIDERS_TAGS_VALID_ENUMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_TAGS_VALID_ENUMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TAGS_VALID_ENUMS","attr":"$.message.catalog['bpp/providers'][*].tags[*].code","var_enum":["timing","close_timing","serviceability","order_value","np_fees"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PROVIDERS_FULFILLMENTS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_FULFILLMENTS_obj in scope:
                                PROVIDERS_FULFILLMENTS_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_ID_obj in scope:
                                        FULFILLMENTS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_ID_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].id")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_ID**: $.message.catalog['bpp/providers'][*].fulfillments[*].id must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_ID","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_ID","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TYPE_obj in scope:
                                        FULFILLMENTS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TYPE_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].type")
                                        var_enum = ["Delivery","Self-Pickup","Buyer-Delivery"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del FULFILLMENTS_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_TYPE**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].type must be in ["Delivery", "Self-Pickup", "Buyer-Delivery"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_CONTACT_PHONE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_CONTACT_PHONE_obj in scope:
                                        FULFILLMENTS_CONTACT_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_CONTACT_PHONE_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone")
                                        phone = ["^\\d{10,11}$"]

                                        validate = validation_utils["follow_regex"](attr, phone)

                                        if not validate:
                                            del FULFILLMENTS_CONTACT_PHONE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_CONTACT_PHONE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_CONTACT_PHONE**: all elements of $.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone must follow every regex in ["^\\d{10,11}$"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_CONTACT_PHONE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone","phone":["^\\\\d{10,11}$"],"_RETURN_":"attr follow regex phone"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_CONTACT_PHONE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_CONTACT_PHONE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_CONTACT_PHONE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone","phone":["^\\\\d{10,11}$"],"_RETURN_":"attr follow regex phone"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_CONTACT_EMAIL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_CONTACT_EMAIL_obj in scope:
                                        FULFILLMENTS_CONTACT_EMAIL_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_CONTACT_EMAIL_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email")
                                        email = ["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"]

                                        validate = validation_utils["follow_regex"](attr, email)

                                        if not validate:
                                            del FULFILLMENTS_CONTACT_EMAIL_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_CONTACT_EMAIL",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_CONTACT_EMAIL**: all elements of $.message.catalog['bpp/providers'][*].fulfillments[*].contact.email must follow every regex in ["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_CONTACT_EMAIL","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email","email":["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"],"_RETURN_":"attr follow regex email"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_CONTACT_EMAIL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_CONTACT_EMAIL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_CONTACT_EMAIL","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email","email":["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"],"_RETURN_":"attr follow regex email"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_ID,
                                    FULFILLMENTS_TYPE,
                                    FULFILLMENTS_CONTACT_PHONE,
                                    FULFILLMENTS_CONTACT_EMAIL,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_FULFILLMENTS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_FULFILLMENTS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_CONTACT_PHONE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone","phone":["^\\\\d{10,11}$"],"_RETURN_":"attr follow regex phone"},{"_NAME_":"FULFILLMENTS_CONTACT_EMAIL","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email","email":["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"],"_RETURN_":"attr follow regex email"}]}
                        """
                            }}] + sub_results

                        def PROVIDERS_DESCRIPTOR(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_DESCRIPTOR_obj in scope:
                                PROVIDERS_DESCRIPTOR_obj["_EXTERNAL"] = input_data["external_data"]

                                def PROVIDERS_DESCRIPTOR_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PROVIDERS_DESCRIPTOR_NAME_obj in scope:
                                        PROVIDERS_DESCRIPTOR_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PROVIDERS_DESCRIPTOR_NAME_obj, "$.message.catalog['bpp/providers'][*].descriptor.name")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PROVIDERS_DESCRIPTOR_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PROVIDERS_DESCRIPTOR_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PROVIDERS_DESCRIPTOR_NAME**: $.message.catalog['bpp/providers'][*].descriptor.name must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PROVIDERS_DESCRIPTOR_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PROVIDERS_DESCRIPTOR_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PROVIDERS_DESCRIPTOR_SYMBOL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PROVIDERS_DESCRIPTOR_SYMBOL_obj in scope:
                                        PROVIDERS_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PROVIDERS_DESCRIPTOR_SYMBOL_obj, "$.message.catalog['bpp/providers'][*].descriptor.symbol")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PROVIDERS_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PROVIDERS_DESCRIPTOR_SYMBOL",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PROVIDERS_DESCRIPTOR_SYMBOL**: $.message.catalog['bpp/providers'][*].descriptor.symbol must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].descriptor.symbol","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PROVIDERS_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PROVIDERS_DESCRIPTOR_SYMBOL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].descriptor.symbol","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PROVIDERS_DESCRIPTOR_SHORT_DESC(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PROVIDERS_DESCRIPTOR_SHORT_DESC_obj in scope:
                                        PROVIDERS_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PROVIDERS_DESCRIPTOR_SHORT_DESC_obj, "$.message.catalog['bpp/providers'][*].descriptor.short_desc")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PROVIDERS_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PROVIDERS_DESCRIPTOR_SHORT_DESC",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PROVIDERS_DESCRIPTOR_SHORT_DESC**: $.message.catalog['bpp/providers'][*].descriptor.short_desc must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PROVIDERS_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PROVIDERS_DESCRIPTOR_SHORT_DESC",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PROVIDERS_DESCRIPTOR_LONG_DESC(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PROVIDERS_DESCRIPTOR_LONG_DESC_obj in scope:
                                        PROVIDERS_DESCRIPTOR_LONG_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PROVIDERS_DESCRIPTOR_LONG_DESC_obj, "$.message.catalog['bpp/providers'][*].descriptor.long_desc")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PROVIDERS_DESCRIPTOR_LONG_DESC_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PROVIDERS_DESCRIPTOR_LONG_DESC",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PROVIDERS_DESCRIPTOR_LONG_DESC**: $.message.catalog['bpp/providers'][*].descriptor.long_desc must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PROVIDERS_DESCRIPTOR_LONG_DESC_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PROVIDERS_DESCRIPTOR_LONG_DESC",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PROVIDERS_DESCRIPTOR_IMAGES(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PROVIDERS_DESCRIPTOR_IMAGES_obj in scope:
                                        PROVIDERS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PROVIDERS_DESCRIPTOR_IMAGES_obj, "$.message.catalog['bpp/providers'][*].descriptor.images[*]")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PROVIDERS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PROVIDERS_DESCRIPTOR_IMAGES",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PROVIDERS_DESCRIPTOR_IMAGES**: $.message.catalog['bpp/providers'][*].descriptor.images[*] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].descriptor.images[*]","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PROVIDERS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PROVIDERS_DESCRIPTOR_IMAGES",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PROVIDERS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].descriptor.images[*]","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    PROVIDERS_DESCRIPTOR_NAME,
                                    PROVIDERS_DESCRIPTOR_SYMBOL,
                                    PROVIDERS_DESCRIPTOR_SHORT_DESC,
                                    PROVIDERS_DESCRIPTOR_LONG_DESC,
                                    PROVIDERS_DESCRIPTOR_IMAGES,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_DESCRIPTOR_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_DESCRIPTOR",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_DESCRIPTOR","_RETURN_":[{"_NAME_":"PROVIDERS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].descriptor.images[*]","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def PROVIDERS_TTL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_TTL_obj in scope:
                                PROVIDERS_TTL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PROVIDERS_TTL_obj, "$.message.catalog['bpp/providers'][*].ttl")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PROVIDERS_TTL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PROVIDERS_TTL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PROVIDERS_TTL**: $.message.catalog['bpp/providers'][*].ttl must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TTL","attr":"$.message.catalog['bpp/providers'][*].ttl","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PROVIDERS_TTL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_TTL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TTL","attr":"$.message.catalog['bpp/providers'][*].ttl","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PROVIDERS_LOCATIONS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_LOCATIONS_obj in scope:
                                PROVIDERS_LOCATIONS_obj["_EXTERNAL"] = input_data["external_data"]

                                def LOCATIONS_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_ID_obj in scope:
                                        LOCATIONS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_ID_obj, "$.message.catalog['bpp/providers'][*].locations[*].id")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del LOCATIONS_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_ID**: $.message.catalog['bpp/providers'][*].locations[*].id must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ID","attr":"$.message.catalog['bpp/providers'][*].locations[*].id","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ID","attr":"$.message.catalog['bpp/providers'][*].locations[*].id","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_LABEL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_LABEL_obj in scope:
                                        LOCATIONS_TIME_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_TIME_LABEL_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.label")
                                        var_enum = ["enable","disable"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del LOCATIONS_TIME_LABEL_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_LABEL",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_LABEL**: every element of $.message.catalog['bpp/providers'][*].locations[*].time.label must be in ["enable", "disable"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_LABEL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_LABEL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_TIMESTAMP(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_TIMESTAMP_obj in scope:
                                        LOCATIONS_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_TIME_TIMESTAMP_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.timestamp")
                                        time_reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        validate = validation_utils["follow_regex"](attr, time_reg)

                                        if not validate:
                                            del LOCATIONS_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_TIMESTAMP",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_TIMESTAMP**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_TIMESTAMP_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_TIMESTAMP",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_SCHEDULE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_SCHEDULE_obj in scope:
                                        LOCATIONS_TIME_SCHEDULE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_TIME_SCHEDULE_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]")
                                        time_reg = ["^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["follow_regex"](attr, time_reg)

                                        if not validate:
                                            del LOCATIONS_TIME_SCHEDULE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_SCHEDULE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_SCHEDULE**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*] must follow every regex in ["^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$"]

                                	> Note: **Condition LOCATIONS_TIME_SCHEDULE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*] must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_SCHEDULE","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]","time_reg":["^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex time_reg"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_SCHEDULE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_SCHEDULE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_SCHEDULE","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]","time_reg":["^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex time_reg"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_SCHEDULE_TIMES(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_SCHEDULE_TIMES_obj in scope:
                                        LOCATIONS_TIME_SCHEDULE_TIMES_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_TIME_SCHEDULE_TIMES_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]")
                                        time_reg = ["^(?:[01]\\d|2[0-3])[0-5]\\d$"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["follow_regex"](attr, time_reg)

                                        if not validate:
                                            del LOCATIONS_TIME_SCHEDULE_TIMES_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_SCHEDULE_TIMES",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_SCHEDULE_TIMES**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*] must follow every regex in ["^(?:[01]\\d|2[0-3])[0-5]\\d$"]

                                	> Note: **Condition LOCATIONS_TIME_SCHEDULE_TIMES** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*] must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_SCHEDULE_TIMES","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","_CONTINUE_":"!(attr are present)","time_reg":["^(?:[01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"attr follow regex time_reg"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_SCHEDULE_TIMES_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_SCHEDULE_TIMES",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_SCHEDULE_TIMES","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","_CONTINUE_":"!(attr are present)","time_reg":["^(?:[01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"attr follow regex time_reg"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_DAYS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_DAYS_obj in scope:
                                        LOCATIONS_TIME_DAYS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_TIME_DAYS_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.days")
                                        days_reg = ["^(?!.*\\b([1-7]),.*\\b\\1\\b)([1-7](,[1-7]){0,6})$"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["follow_regex"](attr, days_reg)

                                        if not validate:
                                            del LOCATIONS_TIME_DAYS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_DAYS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_DAYS**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.days must follow every regex in ["^(?!.*\\b([1-7]),.*\\b\\1\\b)([1-7](,[1-7]){0,6})$"]

                                	> Note: **Condition LOCATIONS_TIME_DAYS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.days must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_DAYS","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.days","_CONTINUE_":"!(attr are present)","days_reg":["^(?!.*\\\\b([1-7]),.*\\\\b\\\\1\\\\b)([1-7](,[1-7]){0,6})$"],"_RETURN_":"attr follow regex days_reg"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_DAYS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_DAYS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_DAYS","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.days","_CONTINUE_":"!(attr are present)","days_reg":["^(?!.*\\\\b([1-7]),.*\\\\b\\\\1\\\\b)([1-7](,[1-7]){0,6})$"],"_RETURN_":"attr follow regex days_reg"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_FREQUENCY_RANGE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_FREQUENCY_RANGE_obj in scope:
                                        LOCATIONS_TIME_FREQUENCY_RANGE_obj["_EXTERNAL"] = input_data["external_data"]
                                        frequency = payload_utils["get_json_path"](LOCATIONS_TIME_FREQUENCY_RANGE_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.frequency")
                                        times = payload_utils["get_json_path"](LOCATIONS_TIME_FREQUENCY_RANGE_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]")
                                        range = payload_utils["get_json_path"](LOCATIONS_TIME_FREQUENCY_RANGE_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.range.start")

                                        validate = ((validation_utils["are_present"](frequency)) and (validation_utils["are_present"](times))) or (validation_utils["are_present"](range))

                                        if not validate:
                                            del LOCATIONS_TIME_FREQUENCY_RANGE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_FREQUENCY_RANGE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_FREQUENCY_RANGE**: any one of the following sub conditions must be met:

                                  - **condition LOCATIONS_TIME_FREQUENCY_RANGE.1**: all of the following sub conditions must be met:

                                    - **condition LOCATIONS_TIME_FREQUENCY_RANGE.1.1**: $.message.catalog['bpp/providers'][*].locations[*].time.frequency must be present in the payload
                                    - **condition LOCATIONS_TIME_FREQUENCY_RANGE.1.2**: $.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*] must be present in the payload
                                  - **condition LOCATIONS_TIME_FREQUENCY_RANGE.2**: $.message.catalog['bpp/providers'][*].locations[*].time.range.start must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_FREQUENCY_RANGE","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","times":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","range":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","_RETURN_":"(frequency are present && times are present) || range are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_FREQUENCY_RANGE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_FREQUENCY_RANGE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_FREQUENCY_RANGE","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","times":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","range":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","_RETURN_":"(frequency are present && times are present) || range are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_TIME_FREQUENCY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_TIME_FREQUENCY_obj in scope:
                                        LOCATIONS_TIME_FREQUENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                        frequency = payload_utils["get_json_path"](LOCATIONS_TIME_FREQUENCY_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.frequency")
                                        reg = ["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"]

                                        skip_check = not (validation_utils["are_present"](frequency))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["follow_regex"](frequency, reg)

                                        if not validate:
                                            del LOCATIONS_TIME_FREQUENCY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_TIME_FREQUENCY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_TIME_FREQUENCY**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.frequency must follow every regex in ["^P(?=\d|T)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)W)?(?:(\d+)D)?(?:T(?=\d)(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?$"]

                                	> Note: **Condition LOCATIONS_TIME_FREQUENCY** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].time.frequency must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_FREQUENCY","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","_CONTINUE_":"!(frequency are present)","reg":["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"],"_RETURN_":"frequency follow regex reg"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_TIME_FREQUENCY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_TIME_FREQUENCY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_TIME_FREQUENCY","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","_CONTINUE_":"!(frequency are present)","reg":["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"],"_RETURN_":"frequency follow regex reg"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_GPS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_GPS_obj in scope:
                                        LOCATIONS_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_GPS_obj, "$.message.catalog['bpp/providers'][*].locations[*].gps")
                                        reg = ["^\\d{2}\\.\\d{4,}\\s*,\\s*\\d{2}\\.\\d{4,}$"]

                                        validate = validation_utils["follow_regex"](attr, reg)

                                        if not validate:
                                            del LOCATIONS_GPS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_GPS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_GPS**: all elements of $.message.catalog['bpp/providers'][*].locations[*].gps must follow every regex in ["^\\d{2}\\.\\d{4,}\\s*,\\s*\\d{2}\\.\\d{4,}$"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_GPS","attr":"$.message.catalog['bpp/providers'][*].locations[*].gps","reg":["^\\\\d{2}\\\\.\\\\d{4,}\\\\s*,\\\\s*\\\\d{2}\\\\.\\\\d{4,}$"],"_RETURN_":"attr follow regex reg"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_GPS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_GPS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_GPS","attr":"$.message.catalog['bpp/providers'][*].locations[*].gps","reg":["^\\\\d{2}\\\\.\\\\d{4,}\\\\s*,\\\\s*\\\\d{2}\\\\.\\\\d{4,}$"],"_RETURN_":"attr follow regex reg"}
                                """
                                    }}] + sub_results

                                def RANGE_START_AND_END(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for RANGE_START_AND_END_obj in scope:
                                        RANGE_START_AND_END_obj["_EXTERNAL"] = input_data["external_data"]
                                        start = payload_utils["get_json_path"](RANGE_START_AND_END_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.range.start")
                                        end = payload_utils["get_json_path"](RANGE_START_AND_END_obj, "$.message.catalog['bpp/providers'][*].locations[*].time.range.end")
                                        reg = ["^([01]\\d|2[0-3])[0-5]\\d$"]

                                        validate = (validation_utils["follow_regex"](start, reg)) and (validation_utils["follow_regex"](end, reg))

                                        if not validate:
                                            del RANGE_START_AND_END_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "RANGE_START_AND_END",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition RANGE_START_AND_END**: all of the following sub conditions must be met:

                                  - **condition RANGE_START_AND_END.1**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.range.start must follow every regex in ["^([01]\\d|2[0-3])[0-5]\\d$"]
                                  - **condition RANGE_START_AND_END.2**: all elements of $.message.catalog['bpp/providers'][*].locations[*].time.range.end must follow every regex in ["^([01]\\d|2[0-3])[0-5]\\d$"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"RANGE_START_AND_END","start":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","end":"$.message.catalog['bpp/providers'][*].locations[*].time.range.end","reg":["^([01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"start follow regex reg && end follow regex reg"}
                                """
                                                }
                                            }]

                                        # del RANGE_START_AND_END_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "RANGE_START_AND_END",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"RANGE_START_AND_END","start":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","end":"$.message.catalog['bpp/providers'][*].locations[*].time.range.end","reg":["^([01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"start follow regex reg && end follow regex reg"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_ADDRESS_LOCALITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_ADDRESS_LOCALITY_obj in scope:
                                        LOCATIONS_ADDRESS_LOCALITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_ADDRESS_LOCALITY_obj, "$.message.catalog['bpp/providers'][*].locations[*].address.locality")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del LOCATIONS_ADDRESS_LOCALITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_ADDRESS_LOCALITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_ADDRESS_LOCALITY**: $.message.catalog['bpp/providers'][*].locations[*].address.locality must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_LOCALITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.locality","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_ADDRESS_LOCALITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_ADDRESS_LOCALITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_LOCALITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.locality","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_ADDRESS_STREET(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_ADDRESS_STREET_obj in scope:
                                        LOCATIONS_ADDRESS_STREET_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_ADDRESS_STREET_obj, "$.message.catalog['bpp/providers'][*].locations[*].address.street")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del LOCATIONS_ADDRESS_STREET_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_ADDRESS_STREET",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_ADDRESS_STREET**: $.message.catalog['bpp/providers'][*].locations[*].address.street must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_STREET","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.street","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_ADDRESS_STREET_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_ADDRESS_STREET",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_STREET","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.street","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_ADDRESS_CITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_ADDRESS_CITY_obj in scope:
                                        LOCATIONS_ADDRESS_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_ADDRESS_CITY_obj, "$.message.catalog['bpp/providers'][*].locations[*].address.city")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del LOCATIONS_ADDRESS_CITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_ADDRESS_CITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_ADDRESS_CITY**: $.message.catalog['bpp/providers'][*].locations[*].address.city must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_CITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.city","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_ADDRESS_CITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_ADDRESS_CITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_CITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.city","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_ADDRESS_AREA_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_ADDRESS_AREA_CODE_obj in scope:
                                        LOCATIONS_ADDRESS_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_ADDRESS_AREA_CODE_obj, "$.message.catalog['bpp/providers'][*].locations[*].address.area_code")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del LOCATIONS_ADDRESS_AREA_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_ADDRESS_AREA_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_ADDRESS_AREA_CODE**: $.message.catalog['bpp/providers'][*].locations[*].address.area_code must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_AREA_CODE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.area_code","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_ADDRESS_AREA_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_ADDRESS_AREA_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_AREA_CODE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.area_code","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_ADDRESS_STATE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_ADDRESS_STATE_obj in scope:
                                        LOCATIONS_ADDRESS_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_ADDRESS_STATE_obj, "$.message.catalog['bpp/providers'][*].locations[*].address.state")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del LOCATIONS_ADDRESS_STATE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_ADDRESS_STATE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_ADDRESS_STATE**: $.message.catalog['bpp/providers'][*].locations[*].address.state must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_STATE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.state","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_ADDRESS_STATE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_ADDRESS_STATE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_ADDRESS_STATE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.state","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def LOCATIONS_CIRCLE_RADIUS_UNIT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for LOCATIONS_CIRCLE_RADIUS_UNIT_obj in scope:
                                        LOCATIONS_CIRCLE_RADIUS_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](LOCATIONS_CIRCLE_RADIUS_UNIT_obj, "$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit")
                                        var_enum = ["km"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del LOCATIONS_CIRCLE_RADIUS_UNIT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "LOCATIONS_CIRCLE_RADIUS_UNIT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition LOCATIONS_CIRCLE_RADIUS_UNIT**: every element of $.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit must be in ["km"]

                                	> Note: **Condition LOCATIONS_CIRCLE_RADIUS_UNIT** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"LOCATIONS_CIRCLE_RADIUS_UNIT","attr":"$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit","var_enum":["km"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del LOCATIONS_CIRCLE_RADIUS_UNIT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "LOCATIONS_CIRCLE_RADIUS_UNIT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"LOCATIONS_CIRCLE_RADIUS_UNIT","attr":"$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit","var_enum":["km"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    LOCATIONS_ID,
                                    LOCATIONS_TIME_LABEL,
                                    LOCATIONS_TIME_TIMESTAMP,
                                    LOCATIONS_TIME_SCHEDULE,
                                    LOCATIONS_TIME_SCHEDULE_TIMES,
                                    LOCATIONS_TIME_DAYS,
                                    LOCATIONS_TIME_FREQUENCY_RANGE,
                                    LOCATIONS_TIME_FREQUENCY,
                                    LOCATIONS_GPS,
                                    RANGE_START_AND_END,
                                    LOCATIONS_ADDRESS_LOCALITY,
                                    LOCATIONS_ADDRESS_STREET,
                                    LOCATIONS_ADDRESS_CITY,
                                    LOCATIONS_ADDRESS_AREA_CODE,
                                    LOCATIONS_ADDRESS_STATE,
                                    LOCATIONS_CIRCLE_RADIUS_UNIT,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_LOCATIONS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_LOCATIONS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_LOCATIONS","_RETURN_":[{"_NAME_":"LOCATIONS_ID","attr":"$.message.catalog['bpp/providers'][*].locations[*].id","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LOCATIONS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]","time_reg":["^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE_TIMES","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","_CONTINUE_":"!(attr are present)","time_reg":["^(?:[01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_DAYS","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.days","_CONTINUE_":"!(attr are present)","days_reg":["^(?!.*\\\\b([1-7]),.*\\\\b\\\\1\\\\b)([1-7](,[1-7]){0,6})$"],"_RETURN_":"attr follow regex days_reg"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY_RANGE","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","times":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","range":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","_RETURN_":"(frequency are present && times are present) || range are present"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","_CONTINUE_":"!(frequency are present)","reg":["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"],"_RETURN_":"frequency follow regex reg"},{"_NAME_":"LOCATIONS_GPS","attr":"$.message.catalog['bpp/providers'][*].locations[*].gps","reg":["^\\\\d{2}\\\\.\\\\d{4,}\\\\s*,\\\\s*\\\\d{2}\\\\.\\\\d{4,}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RANGE_START_AND_END","start":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","end":"$.message.catalog['bpp/providers'][*].locations[*].time.range.end","reg":["^([01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"start follow regex reg && end follow regex reg"},{"_NAME_":"LOCATIONS_ADDRESS_LOCALITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.locality","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STREET","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.street","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_CITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.city","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_AREA_CODE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.area_code","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STATE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.state","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_CIRCLE_RADIUS_UNIT","attr":"$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit","var_enum":["km"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        def PROVIDERS_CATEGORIES(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_CATEGORIES_obj in scope:
                                PROVIDERS_CATEGORIES_obj["_EXTERNAL"] = input_data["external_data"]

                                def CATEGORIES_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for CATEGORIES_ID_obj in scope:
                                        CATEGORIES_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](CATEGORIES_ID_obj, "$.message.catalog['bpp/providers'][*].categories[*].id")
                                        reg = ["^[a-zA-Z0-9]{1,12}$"]

                                        validate = validation_utils["follow_regex"](attr, reg)

                                        if not validate:
                                            del CATEGORIES_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "CATEGORIES_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition CATEGORIES_ID**: all elements of $.message.catalog['bpp/providers'][*].categories[*].id must follow every regex in ["^[a-zA-Z0-9]{1,12}$"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"CATEGORIES_ID","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","reg":["^[a-zA-Z0-9]{1,12}$"],"_RETURN_":"attr follow regex reg"}
                                """
                                                }
                                            }]

                                        # del CATEGORIES_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "CATEGORIES_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"CATEGORIES_ID","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","reg":["^[a-zA-Z0-9]{1,12}$"],"_RETURN_":"attr follow regex reg"}
                                """
                                    }}] + sub_results

                                def CATEGORIES_DESCRIPTOR_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for CATEGORIES_DESCRIPTOR_NAME_obj in scope:
                                        CATEGORIES_DESCRIPTOR_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](CATEGORIES_DESCRIPTOR_NAME_obj, "$.message.catalog['bpp/providers'][*].categories[*].descriptor.name")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del CATEGORIES_DESCRIPTOR_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "CATEGORIES_DESCRIPTOR_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition CATEGORIES_DESCRIPTOR_NAME**: $.message.catalog['bpp/providers'][*].categories[*].descriptor.name must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"CATEGORIES_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].categories[*].descriptor.name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del CATEGORIES_DESCRIPTOR_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "CATEGORIES_DESCRIPTOR_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"CATEGORIES_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].categories[*].descriptor.name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BPP_PROVIDER_CATEGORIES_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BPP_PROVIDER_CATEGORIES_TAGS_obj in scope:
                                        BPP_PROVIDER_CATEGORIES_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS_obj in scope:
                                                TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[*].code")
                                                tag_enum = ["type","attr","np_fees"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, tag_enum)

                                                if not validate:
                                                    del TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[*].code must be in ["type", "attr", "np_fees"]

                                        	> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDER_CATEGORY_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_CATEGORY_TYPE_obj in scope:
                                                TAGS_PROVIDER_CATEGORY_TYPE_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_PROVIDER_CATEGORY_TYPE_TYPE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_PROVIDER_CATEGORY_TYPE_TYPE_obj in scope:
                                                        TAGS_PROVIDER_CATEGORY_TYPE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_TYPE_TYPE_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code")
                                                        tag_enum = ["type","attr"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_PROVIDER_CATEGORY_TYPE_TYPE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_TYPE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_PROVIDER_CATEGORY_TYPE_TYPE**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code must be in ["type", "attr"]

                                                	> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_TYPE** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_PROVIDER_CATEGORY_TYPE_TYPE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_TYPE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1_obj in scope:
                                                        TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value")
                                                        var_enum = ["variant_group","category"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must be in ["variant_group", "category"]

                                                	> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2_obj in scope:
                                                        TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value")
                                                        var_enum = ["variant_group","category"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must be in ["variant_group", "category"]

                                                	> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_PROVIDER_CATEGORY_TYPE_TYPE,
                                                    TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1,
                                                    TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_PROVIDER_CATEGORY_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}]}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDER_CATEGORY_NP_FEES(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_CATEGORY_NP_FEES_obj in scope:
                                                TAGS_PROVIDER_CATEGORY_NP_FEES_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES_obj in scope:
                                                        TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code")
                                                        tag_enum = ["channel_margin_type","channel_margin_value"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code must be in ["channel_margin_type", "channel_margin_value"]

                                                	> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE_obj in scope:
                                                        TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value")
                                                        var_enum = ["percent","amount"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]

                                                	> Note: **Condition TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES,
                                                    TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_PROVIDER_CATEGORY_NP_FEES_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_CATEGORY_NP_FEES",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDER_CATEGORY_ATTR(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_CATEGORY_ATTR_obj in scope:
                                                TAGS_PROVIDER_CATEGORY_ATTR_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_PROVIDER_CATEGORY_TYPE_ATTR(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_PROVIDER_CATEGORY_TYPE_ATTR_obj in scope:
                                                        TAGS_PROVIDER_CATEGORY_TYPE_ATTR_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_PROVIDER_CATEGORY_TYPE_ATTR_obj, "$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code")
                                                        tag_enum = ["name","seq"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_PROVIDER_CATEGORY_TYPE_ATTR_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_ATTR",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_PROVIDER_CATEGORY_TYPE_ATTR**: every element of $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code must be in ["name", "seq"]

                                                	> Note: **Condition TAGS_PROVIDER_CATEGORY_TYPE_ATTR** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_PROVIDER_CATEGORY_TYPE_ATTR_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_CATEGORY_TYPE_ATTR",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_PROVIDER_CATEGORY_TYPE_ATTR,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_PROVIDER_CATEGORY_ATTR_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_CATEGORY_ATTR",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_CATEGORY_ATTR","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS,
                                            TAGS_PROVIDER_CATEGORY_TYPE,
                                            TAGS_PROVIDER_CATEGORY_NP_FEES,
                                            TAGS_PROVIDER_CATEGORY_ATTR,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del BPP_PROVIDER_CATEGORIES_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BPP_PROVIDER_CATEGORIES_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BPP_PROVIDER_CATEGORIES_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_ATTR","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}]}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    CATEGORIES_ID,
                                    CATEGORIES_DESCRIPTOR_NAME,
                                    BPP_PROVIDER_CATEGORIES_TAGS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_CATEGORIES_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_CATEGORIES",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_CATEGORIES","_RETURN_":[{"_NAME_":"CATEGORIES_ID","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","reg":["^[a-zA-Z0-9]{1,12}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"CATEGORIES_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].categories[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"BPP_PROVIDER_CATEGORIES_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_ATTR","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}]}]}]}
                        """
                            }}] + sub_results

                        def PROVIDERS_ITEMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_ITEMS_obj in scope:
                                PROVIDERS_ITEMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def ITEMS_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_ID_obj in scope:
                                        ITEMS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].id")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_ID**: $.message.catalog['bpp/providers'][*].items[*].id must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_RATING(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_RATING_obj in scope:
                                        ITEMS_RATING_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_RATING_obj, "$.message.catalog['bpp/providers'][*].items[*].rating")
                                        rating_reg = ["^(?:[1-4](?:\\.\\d+)?|5(?:\\.0+)?|\\s*)$"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["follow_regex"](attr, rating_reg)

                                        if not validate:
                                            del ITEMS_RATING_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_RATING",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_RATING**: all elements of $.message.catalog['bpp/providers'][*].items[*].rating must follow every regex in ["^(?:[1-4](?:\\.\\d+)?|5(?:\\.0+)?|\\s*)$"]

                                	> Note: **Condition ITEMS_RATING** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].rating must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_RATING","attr":"$.message.catalog['bpp/providers'][*].items[*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"}
                                """
                                                }
                                            }]

                                        # del ITEMS_RATING_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_RATING",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_RATING","attr":"$.message.catalog['bpp/providers'][*].items[*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"}
                                """
                                    }}] + sub_results

                                def ITEMS_TIME_LABEL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TIME_LABEL_obj in scope:
                                        ITEMS_TIME_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_TIME_LABEL_obj, "$.message.catalog['bpp/providers'][*].items[*].time.label")
                                        var_enum = ["enable","disable"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del ITEMS_TIME_LABEL_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_TIME_LABEL",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_TIME_LABEL**: every element of $.message.catalog['bpp/providers'][*].items[*].time.label must be in ["enable", "disable"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].items[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del ITEMS_TIME_LABEL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_TIME_LABEL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].items[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def ITEMS_TIME_TIMESTAMP(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TIME_TIMESTAMP_obj in scope:
                                        ITEMS_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_TIME_TIMESTAMP_obj, "$.message.catalog['bpp/providers'][*].items[*].time.timestamp")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_TIME_TIMESTAMP",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_TIME_TIMESTAMP**: $.message.catalog['bpp/providers'][*].items[*].time.timestamp must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].items[*].time.timestamp","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_TIME_TIMESTAMP_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_TIME_TIMESTAMP",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].items[*].time.timestamp","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_DESCRIPTOR_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_DESCRIPTOR_NAME_obj in scope:
                                        ITEMS_DESCRIPTOR_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_DESCRIPTOR_NAME_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.name")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_DESCRIPTOR_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_DESCRIPTOR_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_DESCRIPTOR_NAME**: $.message.catalog['bpp/providers'][*].items[*].descriptor.name must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_DESCRIPTOR_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_DESCRIPTOR_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_DESCRIPTOR_SYMBOL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_DESCRIPTOR_SYMBOL_obj in scope:
                                        ITEMS_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_DESCRIPTOR_SYMBOL_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_DESCRIPTOR_SYMBOL",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_DESCRIPTOR_SYMBOL**: $.message.catalog['bpp/providers'][*].items[*].descriptor.symbol must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_DESCRIPTOR_SYMBOL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_DESCRIPTOR_SYMBOL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_DESCRIPTOR_SHORT_DESC(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_DESCRIPTOR_SHORT_DESC_obj in scope:
                                        ITEMS_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_DESCRIPTOR_SHORT_DESC_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_DESCRIPTOR_SHORT_DESC",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_DESCRIPTOR_SHORT_DESC**: $.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_DESCRIPTOR_SHORT_DESC_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_DESCRIPTOR_SHORT_DESC",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_DESCRIPTOR_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_DESCRIPTOR_CODE_obj in scope:
                                        ITEMS_DESCRIPTOR_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_DESCRIPTOR_CODE_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.code")
                                        reg = ["^(1|5):"]

                                        validate = validation_utils["follow_regex"](attr, reg)

                                        if not validate:
                                            del ITEMS_DESCRIPTOR_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_DESCRIPTOR_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_DESCRIPTOR_CODE**: all elements of $.message.catalog['bpp/providers'][*].items[*].descriptor.code must follow every regex in ["^(1|5):"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.code","reg":["^(1|5):"],"_RETURN_":"attr follow regex reg"}
                                """
                                                }
                                            }]

                                        # del ITEMS_DESCRIPTOR_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_DESCRIPTOR_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.code","reg":["^(1|5):"],"_RETURN_":"attr follow regex reg"}
                                """
                                    }}] + sub_results

                                def ITEMS_DESCRIPTOR_IMAGES(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_DESCRIPTOR_IMAGES_obj in scope:
                                        ITEMS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_DESCRIPTOR_IMAGES_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_DESCRIPTOR_IMAGES",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_DESCRIPTOR_IMAGES**: $.message.catalog['bpp/providers'][*].items[*].descriptor.images[*] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_DESCRIPTOR_IMAGES",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT_obj in scope:
                                        ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT_obj, "$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit")
                                        var_enum = ["unit","dozen","gram","kilogram","tonne","litre","millilitre"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT**: every element of $.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit must be in ["unit", "dozen", "gram", "kilogram", "tonne", "litre", "millilitre"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE_obj in scope:
                                        ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE_obj, "$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE**: $.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_QUANTITY_AVAILABLE_COUNT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_QUANTITY_AVAILABLE_COUNT_obj in scope:
                                        ITEMS_QUANTITY_AVAILABLE_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_QUANTITY_AVAILABLE_COUNT_obj, "$.message.catalog['bpp/providers'][*].items[*].quantity.available.count")
                                        var_enum = ["99","0"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del ITEMS_QUANTITY_AVAILABLE_COUNT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_QUANTITY_AVAILABLE_COUNT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_QUANTITY_AVAILABLE_COUNT**: every element of $.message.catalog['bpp/providers'][*].items[*].quantity.available.count must be in ["99", "0"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_AVAILABLE_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del ITEMS_QUANTITY_AVAILABLE_COUNT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_QUANTITY_AVAILABLE_COUNT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_AVAILABLE_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def ITEMS_QUANTITY_MAXIMUM_COUNT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_QUANTITY_MAXIMUM_COUNT_obj in scope:
                                        ITEMS_QUANTITY_MAXIMUM_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_QUANTITY_MAXIMUM_COUNT_obj, "$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_QUANTITY_MAXIMUM_COUNT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_QUANTITY_MAXIMUM_COUNT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_QUANTITY_MAXIMUM_COUNT**: $.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_MAXIMUM_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_QUANTITY_MAXIMUM_COUNT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_QUANTITY_MAXIMUM_COUNT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_QUANTITY_MAXIMUM_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_PRICE_CURRENCY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_PRICE_CURRENCY_obj in scope:
                                        ITEMS_PRICE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_PRICE_CURRENCY_obj, "$.message.catalog['bpp/providers'][*].items[*].price.currency")
                                        var_enum = ["INR"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del ITEMS_PRICE_CURRENCY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_PRICE_CURRENCY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_PRICE_CURRENCY**: every element of $.message.catalog['bpp/providers'][*].items[*].price.currency must be in ["INR"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_PRICE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","var_enum":["INR"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del ITEMS_PRICE_CURRENCY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_PRICE_CURRENCY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_PRICE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","var_enum":["INR"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def ITEMS_PRICE_VALUE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_PRICE_VALUE_obj in scope:
                                        ITEMS_PRICE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_PRICE_VALUE_obj, "$.message.catalog['bpp/providers'][*].items[*].price.value")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_PRICE_VALUE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_PRICE_VALUE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_PRICE_VALUE**: $.message.catalog['bpp/providers'][*].items[*].price.value must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_PRICE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_PRICE_VALUE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_PRICE_VALUE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_PRICE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_PRICE_MAXIMUM_VALUE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_PRICE_MAXIMUM_VALUE_obj in scope:
                                        ITEMS_PRICE_MAXIMUM_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_PRICE_MAXIMUM_VALUE_obj, "$.message.catalog['bpp/providers'][*].items[*].price.maximum_value")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_PRICE_MAXIMUM_VALUE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_PRICE_MAXIMUM_VALUE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_PRICE_MAXIMUM_VALUE**: $.message.catalog['bpp/providers'][*].items[*].price.maximum_value must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_PRICE_MAXIMUM_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.maximum_value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_PRICE_MAXIMUM_VALUE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_PRICE_MAXIMUM_VALUE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_PRICE_MAXIMUM_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.maximum_value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_CATEGORY_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_CATEGORY_ID_obj in scope:
                                        ITEMS_CATEGORY_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_CATEGORY_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        valid = ["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"]

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del ITEMS_CATEGORY_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_CATEGORY_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_CATEGORY_ID**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks", "Gift Voucher"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","valid":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del ITEMS_CATEGORY_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_CATEGORY_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","valid":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def ITEMS_FULFILLMENT_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_FULFILLMENT_ID_obj in scope:
                                        ITEMS_FULFILLMENT_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_FULFILLMENT_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].fulfillment_id")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_FULFILLMENT_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_FULFILLMENT_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_FULFILLMENT_ID**: $.message.catalog['bpp/providers'][*].items[*].fulfillment_id must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_FULFILLMENT_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_FULFILLMENT_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_LOCATION_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_LOCATION_ID_obj in scope:
                                        ITEMS_LOCATION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_LOCATION_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].location_id")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_LOCATION_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_LOCATION_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_LOCATION_ID**: $.message.catalog['bpp/providers'][*].items[*].location_id must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].location_id","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_LOCATION_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_LOCATION_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].location_id","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_RETURNABLE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_RETURNABLE_obj in scope:
                                        ITEMS_RETURNABLE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_RETURNABLE_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_RETURNABLE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_RETURNABLE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_RETURNABLE**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable'] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_RETURNABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_RETURNABLE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_RETURNABLE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_RETURNABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_CANCELLABLE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_CANCELLABLE_obj in scope:
                                        ITEMS_CANCELLABLE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_CANCELLABLE_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_CANCELLABLE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_CANCELLABLE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_CANCELLABLE**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable'] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_CANCELLABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_CANCELLABLE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_CANCELLABLE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_CANCELLABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_SELLER_PICKUP_RETURN(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_SELLER_PICKUP_RETURN_obj in scope:
                                        ITEMS_SELLER_PICKUP_RETURN_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_SELLER_PICKUP_RETURN_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_SELLER_PICKUP_RETURN_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_SELLER_PICKUP_RETURN",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_SELLER_PICKUP_RETURN**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return'] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_SELLER_PICKUP_RETURN","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_SELLER_PICKUP_RETURN_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_SELLER_PICKUP_RETURN",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_SELLER_PICKUP_RETURN","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_TIME_TO_SHIP(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TIME_TO_SHIP_obj in scope:
                                        ITEMS_TIME_TO_SHIP_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_TIME_TO_SHIP_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_TIME_TO_SHIP_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_TIME_TO_SHIP",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_TIME_TO_SHIP**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship'] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_TIME_TO_SHIP","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_TIME_TO_SHIP_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_TIME_TO_SHIP",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_TIME_TO_SHIP","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_AVAILABLE_ON_COD(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_AVAILABLE_ON_COD_obj in scope:
                                        ITEMS_AVAILABLE_ON_COD_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_AVAILABLE_ON_COD_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_AVAILABLE_ON_COD_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_AVAILABLE_ON_COD",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_AVAILABLE_ON_COD**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod'] must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_AVAILABLE_ON_COD","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_AVAILABLE_ON_COD_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_AVAILABLE_ON_COD",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_AVAILABLE_ON_COD","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO_obj in scope:
                                        ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO_obj in scope:
                                        ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO_obj in scope:
                                        ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO_obj in scope:
                                        ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO_obj in scope:
                                        ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Bakery, Cakes & Dairy", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Tinned and Processed Food", "Energy and Soft Drinks", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY_obj in scope:
                                        ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS_obj in scope:
                                        ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME_obj in scope:
                                        ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_CONTINUE_":"!(category all in applicable_categories)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_CONTINUE_":"!(category all in applicable_categories)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT_obj in scope:
                                        ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT_obj, "$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import")
                                        category = payload_utils["get_json_path"](ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                                        applicable_categories = ["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"]

                                        skip_check = not (validation_utils["all_in"](category, applicable_categories))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT**: $.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import must be present in the payload

                                	> Note: **Condition ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Cleaning & Household", "Bakery, Cakes & Dairy", "Pet Care", "Stationery", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def ITEMS_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TAGS_obj in scope:
                                        ITEMS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_BPP_ITEMS_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_BPP_ITEMS_VALID_TAGS_obj in scope:
                                                TAGS_BPP_ITEMS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_BPP_ITEMS_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[*].code")
                                                valid = ["origin","veg_nonveg","image","timing","np_fees"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, valid)

                                                if not validate:
                                                    del TAGS_BPP_ITEMS_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_BPP_ITEMS_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_BPP_ITEMS_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[*].code must be in ["origin", "veg_nonveg", "image", "timing", "np_fees"]

                                        	> Note: **Condition TAGS_BPP_ITEMS_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_BPP_ITEMS_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_BPP_ITEMS_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"}
                                        """
                                            }}] + sub_results

                                        def TAGS_ITEMS_ORIGIN_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_ITEMS_ORIGIN_VALID_TAGS_obj in scope:
                                                TAGS_ITEMS_ORIGIN_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_ITEMS_ORIGIN_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code")
                                                tag_enum = ["country"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, tag_enum)

                                                if not validate:
                                                    del TAGS_ITEMS_ORIGIN_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_ITEMS_ORIGIN_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_ITEMS_ORIGIN_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code must be in ["country"]

                                        	> Note: **Condition TAGS_ITEMS_ORIGIN_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_ITEMS_ORIGIN_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_ITEMS_ORIGIN_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                            }}] + sub_results

                                        def ITEMS_TAGS_ORIGIN(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ITEMS_TAGS_ORIGIN_obj in scope:
                                                ITEMS_TAGS_ORIGIN_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ITEMS_TAGS_ORIGIN_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value")
                                                reg = ["^[A-Z]{3}$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del ITEMS_TAGS_ORIGIN_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ITEMS_TAGS_ORIGIN",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition ITEMS_TAGS_ORIGIN**: all elements of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value must follow every regex in ["^[A-Z]{3}$"]

                                        	> Note: **Condition ITEMS_TAGS_ORIGIN** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del ITEMS_TAGS_ORIGIN_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ITEMS_TAGS_ORIGIN",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def ITEMS_TAGS_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ITEMS_TAGS_TYPE_obj in scope:
                                                ITEMS_TAGS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ITEMS_TAGS_TYPE_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value")
                                                var_enum = ["back_image"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del ITEMS_TAGS_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ITEMS_TAGS_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition ITEMS_TAGS_TYPE**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value must be in ["back_image"]

                                        	> Note: **Condition ITEMS_TAGS_TYPE** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del ITEMS_TAGS_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ITEMS_TAGS_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def ITEMS_TAGS_TYPE_VALID_URL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ITEMS_TAGS_TYPE_VALID_URL_obj in scope:
                                                ITEMS_TAGS_TYPE_VALID_URL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ITEMS_TAGS_TYPE_VALID_URL_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value")
                                                reg = ["^(https?:\\/\\/)?(www\\.)?[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(\\/[^\\s]*)?$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del ITEMS_TAGS_TYPE_VALID_URL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ITEMS_TAGS_TYPE_VALID_URL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition ITEMS_TAGS_TYPE_VALID_URL**: all elements of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value must follow every regex in ["^(https?:\\/\\/)?(www\\.)?[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(\/[^\\s]*)?$"]

                                        	> Note: **Condition ITEMS_TAGS_TYPE_VALID_URL** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del ITEMS_TAGS_TYPE_VALID_URL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ITEMS_TAGS_TYPE_VALID_URL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def TAGS_VEG_NONVEG(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_VEG_NONVEG_obj in scope:
                                                TAGS_VEG_NONVEG_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_VEG_NONVEG_CODES(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_VEG_NONVEG_CODES_obj in scope:
                                                        TAGS_VEG_NONVEG_CODES_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_VEG_NONVEG_CODES_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code")
                                                        var_enum = ["veg","non_veg","egg"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_VEG_NONVEG_CODES_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_VEG_NONVEG_CODES",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_VEG_NONVEG_CODES**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code must be in ["veg", "non_veg", "egg"]

                                                	> Note: **Condition TAGS_VEG_NONVEG_CODES** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_VEG_NONVEG_CODES_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_VEG_NONVEG_CODES",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_VEG_NONVEG_VALUES(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_VEG_NONVEG_VALUES_obj in scope:
                                                        TAGS_VEG_NONVEG_VALUES_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_VEG_NONVEG_VALUES_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value")
                                                        var_enum = ["yes"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_VEG_NONVEG_VALUES_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_VEG_NONVEG_VALUES",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_VEG_NONVEG_VALUES**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value must be in ["yes"]

                                                	> Note: **Condition TAGS_VEG_NONVEG_VALUES** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_VEG_NONVEG_VALUES_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_VEG_NONVEG_VALUES",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_VEG_NONVEG_CODES,
                                                    TAGS_VEG_NONVEG_VALUES,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_VEG_NONVEG_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_VEG_NONVEG",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_VEG_NONVEG","_RETURN_":[{"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_BPP_ITEMS_VALID_TAGS,
                                            TAGS_ITEMS_ORIGIN_VALID_TAGS,
                                            ITEMS_TAGS_ORIGIN,
                                            ITEMS_TAGS_TYPE,
                                            ITEMS_TAGS_TYPE_VALID_URL,
                                            TAGS_VEG_NONVEG,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del ITEMS_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"TAGS_VEG_NONVEG","_RETURN_":[{"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}]}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    ITEMS_ID,
                                    ITEMS_RATING,
                                    ITEMS_TIME_LABEL,
                                    ITEMS_TIME_TIMESTAMP,
                                    ITEMS_DESCRIPTOR_NAME,
                                    ITEMS_DESCRIPTOR_SYMBOL,
                                    ITEMS_DESCRIPTOR_SHORT_DESC,
                                    ITEMS_DESCRIPTOR_CODE,
                                    ITEMS_DESCRIPTOR_IMAGES,
                                    ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT,
                                    ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE,
                                    ITEMS_QUANTITY_AVAILABLE_COUNT,
                                    ITEMS_QUANTITY_MAXIMUM_COUNT,
                                    ITEMS_PRICE_CURRENCY,
                                    ITEMS_PRICE_VALUE,
                                    ITEMS_PRICE_MAXIMUM_VALUE,
                                    ITEMS_CATEGORY_ID,
                                    ITEMS_FULFILLMENT_ID,
                                    ITEMS_LOCATION_ID,
                                    ITEMS_RETURNABLE,
                                    ITEMS_CANCELLABLE,
                                    ITEMS_SELLER_PICKUP_RETURN,
                                    ITEMS_TIME_TO_SHIP,
                                    ITEMS_AVAILABLE_ON_COD,
                                    ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO,
                                    ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO,
                                    ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO,
                                    ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO,
                                    ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO,
                                    ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY,
                                    ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS,
                                    ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME,
                                    ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT,
                                    ITEMS_TAGS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_ITEMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_ITEMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RATING","attr":"$.message.catalog['bpp/providers'][*].items[*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"ITEMS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].items[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].items[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.code","reg":["^(1|5):"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_AVAILABLE_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_MAXIMUM_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","var_enum":["INR"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_PRICE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_MAXIMUM_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.maximum_value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","valid":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RETURNABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CANCELLABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_SELLER_PICKUP_RETURN","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TIME_TO_SHIP","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_AVAILABLE_ON_COD","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_CONTINUE_":"!(category all in applicable_categories)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"TAGS_VEG_NONVEG","_RETURN_":[{"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}]}]}]}
                        """
                            }}] + sub_results

                        def PROVIDERS_OFFERS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_OFFERS_obj in scope:
                                PROVIDERS_OFFERS_obj["_EXTERNAL"] = input_data["external_data"]

                                def OFFERS_DESCRIPTOR_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for OFFERS_DESCRIPTOR_CODE_obj in scope:
                                        OFFERS_DESCRIPTOR_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](OFFERS_DESCRIPTOR_CODE_obj, "$.message.catalog['bpp/providers'][*].offers[*].descriptor.code")
                                        var_enum = ["discount","buyXgetY","freebie","slab","combo","delivery"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del OFFERS_DESCRIPTOR_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "OFFERS_DESCRIPTOR_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition OFFERS_DESCRIPTOR_CODE**: every element of $.message.catalog['bpp/providers'][*].offers[*].descriptor.code must be in ["discount", "buyXgetY", "freebie", "slab", "combo", "delivery"]

                                	> Note: **Condition OFFERS_DESCRIPTOR_CODE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].descriptor.code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"OFFERS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo","delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del OFFERS_DESCRIPTOR_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "OFFERS_DESCRIPTOR_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"OFFERS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo","delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def BPP_PROVIDERS_OFFERS_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BPP_PROVIDERS_OFFERS_TAGS_obj in scope:
                                        BPP_PROVIDERS_OFFERS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_OFFERS_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_OFFERS_VALID_TAGS_obj in scope:
                                                TAGS_OFFERS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_OFFERS_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[*].code")
                                                valid = ["qualifier","benefit","meta","finance_terms"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, valid)

                                                if not validate:
                                                    del TAGS_OFFERS_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_OFFERS_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_OFFERS_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[*].code must be in ["qualifier", "benefit", "meta", "finance_terms"]

                                        	> Note: **Condition TAGS_OFFERS_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_OFFERS_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_OFFERS_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"}
                                        """
                                            }}] + sub_results

                                        def TAGS_QUALIFIER(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_QUALIFIER_obj in scope:
                                                TAGS_QUALIFIER_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_QUALIFIER_VALID_TAGS(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_QUALIFIER_VALID_TAGS_obj in scope:
                                                        TAGS_QUALIFIER_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_QUALIFIER_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code")
                                                        tag_enum = ["min_value","item_count","item_count_upper"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_QUALIFIER_VALID_TAGS_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_QUALIFIER_VALID_TAGS",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_QUALIFIER_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code must be in ["min_value", "item_count", "item_count_upper"]

                                                	> Note: **Condition TAGS_QUALIFIER_VALID_TAGS** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_QUALIFIER_VALID_TAGS_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_QUALIFIER_VALID_TAGS",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_QUALIFIER_VALID_TAGS,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_QUALIFIER_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_QUALIFIER",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_QUALIFIER","_RETURN_":[{"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}]}
                                        """
                                            }}] + sub_results

                                        def TAGS_BENEFIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_BENEFIT_obj in scope:
                                                TAGS_BENEFIT_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_BENEFIT_VALID_TAGS(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_BENEFIT_VALID_TAGS_obj in scope:
                                                        TAGS_BENEFIT_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_BENEFIT_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code")
                                                        tag_enum = ["value_type","value","value_cap","item_count","item_id","item_value"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_BENEFIT_VALID_TAGS_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_BENEFIT_VALID_TAGS",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_BENEFIT_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code must be in ["value_type", "value", "value_cap", "item_count", "item_id", "item_value"]

                                                	> Note: **Condition TAGS_BENEFIT_VALID_TAGS** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_BENEFIT_VALID_TAGS_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_BENEFIT_VALID_TAGS",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_BENEFIT_VALUE_TYPE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_BENEFIT_VALUE_TYPE_obj in scope:
                                                        TAGS_BENEFIT_VALUE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_BENEFIT_VALUE_TYPE_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value")
                                                        var_enum = ["percent","amount"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_BENEFIT_VALUE_TYPE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_BENEFIT_VALUE_TYPE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_BENEFIT_VALUE_TYPE**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value must be in ["percent", "amount"]

                                                	> Note: **Condition TAGS_BENEFIT_VALUE_TYPE** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_BENEFIT_VALUE_TYPE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_BENEFIT_VALUE_TYPE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_BENEFIT_VALID_TAGS,
                                                    TAGS_BENEFIT_VALUE_TYPE,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_BENEFIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_BENEFIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_BENEFIT","_RETURN_":[{"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}
                                        """
                                            }}] + sub_results

                                        def TAGS_META(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_META_obj in scope:
                                                TAGS_META_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_META_VALID_TAGS(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_META_VALID_TAGS_obj in scope:
                                                        TAGS_META_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_META_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code")
                                                        tag_enum = ["additive","auto"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_META_VALID_TAGS_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_META_VALID_TAGS",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_META_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code must be in ["additive", "auto"]

                                                	> Note: **Condition TAGS_META_VALID_TAGS** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_META_VALID_TAGS_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_META_VALID_TAGS",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_META_ADDITIVE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_META_ADDITIVE_obj in scope:
                                                        TAGS_META_ADDITIVE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_META_ADDITIVE_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value")
                                                        var_enum = ["yes","no"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_META_ADDITIVE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_META_ADDITIVE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_META_ADDITIVE**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value must be in ["yes", "no"]

                                                	> Note: **Condition TAGS_META_ADDITIVE** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_META_ADDITIVE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_META_ADDITIVE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                def TAGS_META_AUTO(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_META_AUTO_obj in scope:
                                                        TAGS_META_AUTO_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_META_AUTO_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value")
                                                        var_enum = ["yes","no"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del TAGS_META_AUTO_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_META_AUTO",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_META_AUTO**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value must be in ["yes", "no"]

                                                	> Note: **Condition TAGS_META_AUTO** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_META_AUTO_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_META_AUTO",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_META_VALID_TAGS,
                                                    TAGS_META_ADDITIVE,
                                                    TAGS_META_AUTO,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_META_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_META",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_META","_RETURN_":[{"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}
                                        """
                                            }}] + sub_results

                                        def TAGS_FINANCE_TERMS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_FINANCE_TERMS_obj in scope:
                                                TAGS_FINANCE_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                                def TAGS_FINANCE_TERMS_VALID_TAGS(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for TAGS_FINANCE_TERMS_VALID_TAGS_obj in scope:
                                                        TAGS_FINANCE_TERMS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_TERMS_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code")
                                                        tag_enum = ["subvention_type","subvention_amount"]

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["all_in"](attr, tag_enum)

                                                        if not validate:
                                                            del TAGS_FINANCE_TERMS_VALID_TAGS_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "TAGS_FINANCE_TERMS_VALID_TAGS",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition TAGS_FINANCE_TERMS_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code must be in ["subvention_type", "subvention_amount"]

                                                	> Note: **Condition TAGS_FINANCE_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
                                                	>
                                                	> - **condition B**: $.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code must **not** be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del TAGS_FINANCE_TERMS_VALID_TAGS_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "TAGS_FINANCE_TERMS_VALID_TAGS",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    TAGS_FINANCE_TERMS_VALID_TAGS,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del TAGS_FINANCE_TERMS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_FINANCE_TERMS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_OFFERS_VALID_TAGS,
                                            TAGS_QUALIFIER,
                                            TAGS_BENEFIT,
                                            TAGS_META,
                                            TAGS_FINANCE_TERMS,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del BPP_PROVIDERS_OFFERS_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BPP_PROVIDERS_OFFERS_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BPP_PROVIDERS_OFFERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_QUALIFIER","_RETURN_":[{"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_BENEFIT","_RETURN_":[{"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_META","_RETURN_":[{"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}]}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    OFFERS_DESCRIPTOR_CODE,
                                    BPP_PROVIDERS_OFFERS_TAGS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_OFFERS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_OFFERS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo","delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BPP_PROVIDERS_OFFERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_QUALIFIER","_RETURN_":[{"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_BENEFIT","_RETURN_":[{"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_META","_RETURN_":[{"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}]}]}]}
                        """
                            }}] + sub_results

                        def PROVIDERS_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PROVIDERS_TAGS_obj in scope:
                                PROVIDERS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_PROVIDERS_VALID_TIMING_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_PROVIDERS_VALID_TIMING_TAGS_obj in scope:
                                        TAGS_PROVIDERS_VALID_TIMING_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_PROVIDERS_VALID_TIMING_TAGS_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_PROVIDERS_VALID_TIMING_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_PROVIDERS_VALID_TIMING_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_PROVIDERS_VALID_TIMING_TAGS**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value must be present in the payload

                                	> Note: **Condition TAGS_PROVIDERS_VALID_TIMING_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_VALID_TIMING_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_PROVIDERS_VALID_TIMING_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_PROVIDERS_VALID_TIMING_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_VALID_TIMING_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_PROVIDERS_SERVICEABILITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_PROVIDERS_SERVICEABILITY_obj in scope:
                                        TAGS_PROVIDERS_SERVICEABILITY_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_PROVIDER_SERVICABILITY_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_SERVICABILITY_VALID_TAGS_obj in scope:
                                                TAGS_PROVIDER_SERVICABILITY_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDER_SERVICABILITY_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code")
                                                tag_enum = ["location","category","type","val","day_from","day_to","time_from","time_to","unit"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, tag_enum)

                                                if not validate:
                                                    del TAGS_PROVIDER_SERVICABILITY_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_SERVICABILITY_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDER_SERVICABILITY_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code must be in ["location", "category", "type", "val", "day_from", "day_to", "time_from", "time_to", "unit"]

                                        	> Note: **Condition TAGS_PROVIDER_SERVICABILITY_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDER_SERVICABILITY_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_SERVICABILITY_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDERS_SERVICEABILITY_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDERS_SERVICEABILITY_TYPE_obj in scope:
                                                TAGS_PROVIDERS_SERVICEABILITY_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDERS_SERVICEABILITY_TYPE_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value")
                                                var_enum = ["10","11","12","13"]

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_PROVIDERS_SERVICEABILITY_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDERS_SERVICEABILITY_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDERS_SERVICEABILITY_TYPE**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value must be in ["10", "11", "12", "13"]""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDERS_SERVICEABILITY_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDERS_SERVICEABILITY_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDERS_SERVICEABILITY_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDERS_SERVICEABILITY_UNIT_obj in scope:
                                                TAGS_PROVIDERS_SERVICEABILITY_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDERS_SERVICEABILITY_UNIT_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value")
                                                var_enum = ["km","geojson","country","pincode"]

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_PROVIDERS_SERVICEABILITY_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDERS_SERVICEABILITY_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDERS_SERVICEABILITY_UNIT**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value must be in ["km", "geojson", "country", "pincode"]""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDERS_SERVICEABILITY_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDERS_SERVICEABILITY_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_PROVIDER_SERVICABILITY_VALID_TAGS,
                                            TAGS_PROVIDERS_SERVICEABILITY_TYPE,
                                            TAGS_PROVIDERS_SERVICEABILITY_UNIT,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_PROVIDERS_SERVICEABILITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_PROVIDERS_SERVICEABILITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                def TAGS_PROVIDERS_ORDER_VALUE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_PROVIDERS_ORDER_VALUE_obj in scope:
                                        TAGS_PROVIDERS_ORDER_VALUE_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS_obj in scope:
                                                TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code")
                                                tag_enum = ["min_value"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, tag_enum)

                                                if not validate:
                                                    del TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code must be in ["min_value"]

                                        	> Note: **Condition TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE_obj in scope:
                                                TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value must be present in the payload

                                        	> Note: **Condition TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS,
                                            TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_PROVIDERS_ORDER_VALUE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_PROVIDERS_ORDER_VALUE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_PROVIDERS_CATALOG_LINK(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_PROVIDERS_CATALOG_LINK_obj in scope:
                                        TAGS_PROVIDERS_CATALOG_LINK_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_PROVIDERS_CATALOG_LINK_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDERS_CATALOG_LINK_TYPE_obj in scope:
                                                TAGS_PROVIDERS_CATALOG_LINK_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDERS_CATALOG_LINK_TYPE_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value")
                                                var_enum = ["link","inline"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_PROVIDERS_CATALOG_LINK_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDERS_CATALOG_LINK_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDERS_CATALOG_LINK_TYPE**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value must be in ["link", "inline"]

                                        	> Note: **Condition TAGS_PROVIDERS_CATALOG_LINK_TYPE** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDERS_CATALOG_LINK_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDERS_CATALOG_LINK_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_PROVIDERS_CATALOG_LINK_TYPE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_PROVIDERS_CATALOG_LINK_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_PROVIDERS_CATALOG_LINK",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                def TAGS_PROVIDERS_TIMING(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_PROVIDERS_TIMING_obj in scope:
                                        TAGS_PROVIDERS_TIMING_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_PROVIDER_TIMING_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_TIMING_VALID_TAGS_obj in scope:
                                                TAGS_PROVIDER_TIMING_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDER_TIMING_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code")
                                                tag_enum = ["type","location","day_from","day_to","time_from","time_to"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, tag_enum)

                                                if not validate:
                                                    del TAGS_PROVIDER_TIMING_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_TIMING_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDER_TIMING_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code must be in ["type", "location", "day_from", "day_to", "time_from", "time_to"]

                                        	> Note: **Condition TAGS_PROVIDER_TIMING_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDER_TIMING_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_TIMING_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_PROVIDER_TIMING_VALID_TAGS,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_PROVIDERS_TIMING_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_PROVIDERS_TIMING",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_TIMING","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}]}
                                """
                                    }}] + sub_results

                                def TAGS_PROVIDERS_NP_FEES(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_PROVIDERS_NP_FEES_obj in scope:
                                        TAGS_PROVIDERS_NP_FEES_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TAGS_PROVIDER_NP_FEES_VALID_TAGS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDER_NP_FEES_VALID_TAGS_obj in scope:
                                                TAGS_PROVIDER_NP_FEES_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDER_NP_FEES_VALID_TAGS_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code")
                                                tag_enum = ["channel_margin_type","channel_margin_value"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, tag_enum)

                                                if not validate:
                                                    del TAGS_PROVIDER_NP_FEES_VALID_TAGS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDER_NP_FEES_VALID_TAGS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDER_NP_FEES_VALID_TAGS**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code must be in ["channel_margin_type", "channel_margin_value"]

                                        	> Note: **Condition TAGS_PROVIDER_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDER_NP_FEES_VALID_TAGS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDER_NP_FEES_VALID_TAGS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"}
                                        """
                                            }}] + sub_results

                                        def TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE_obj in scope:
                                                TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE_obj, "$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value")
                                                var_enum = ["percent","amount"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]

                                        	> Note: **Condition TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TAGS_PROVIDER_NP_FEES_VALID_TAGS,
                                            TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_PROVIDERS_NP_FEES_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_PROVIDERS_NP_FEES",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_PROVIDERS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_PROVIDERS_VALID_TIMING_TAGS,
                                    TAGS_PROVIDERS_SERVICEABILITY,
                                    TAGS_PROVIDERS_ORDER_VALUE,
                                    TAGS_PROVIDERS_CATALOG_LINK,
                                    TAGS_PROVIDERS_TIMING,
                                    TAGS_PROVIDERS_NP_FEES,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PROVIDERS_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PROVIDERS_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PROVIDERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_VALID_TIMING_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_TIMING","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_PROVIDERS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            PROVIDERS_ID,
                            PROVIDERS_RATING,
                            PROVIDERS_TIME_LABEL,
                            PROVIDERS_TIME_TIMESTAMP,
                            PROVIDERS_TAGS_VALID_ENUMS,
                            PROVIDERS_FULFILLMENTS,
                            PROVIDERS_DESCRIPTOR,
                            PROVIDERS_TTL,
                            PROVIDERS_LOCATIONS,
                            PROVIDERS_CATEGORIES,
                            PROVIDERS_ITEMS,
                            PROVIDERS_OFFERS,
                            PROVIDERS_TAGS,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del CATALOG_BPP_PROVIDERS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "CATALOG_BPP_PROVIDERS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"CATALOG_BPP_PROVIDERS","_RETURN_":[{"_NAME_":"PROVIDERS_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_RATING","attr":"$.message.catalog['bpp/providers'][*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"PROVIDERS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PROVIDERS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"PROVIDERS_TAGS_VALID_ENUMS","attr":"$.message.catalog['bpp/providers'][*].tags[*].code","var_enum":["timing","close_timing","serviceability","order_value","np_fees"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PROVIDERS_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_CONTACT_PHONE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone","phone":["^\\\\d{10,11}$"],"_RETURN_":"attr follow regex phone"},{"_NAME_":"FULFILLMENTS_CONTACT_EMAIL","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email","email":["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"],"_RETURN_":"attr follow regex email"}]},{"_NAME_":"PROVIDERS_DESCRIPTOR","_RETURN_":[{"_NAME_":"PROVIDERS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].descriptor.images[*]","_RETURN_":"attr are present"}]},{"_NAME_":"PROVIDERS_TTL","attr":"$.message.catalog['bpp/providers'][*].ttl","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_LOCATIONS","_RETURN_":[{"_NAME_":"LOCATIONS_ID","attr":"$.message.catalog['bpp/providers'][*].locations[*].id","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LOCATIONS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]","time_reg":["^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE_TIMES","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","_CONTINUE_":"!(attr are present)","time_reg":["^(?:[01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_DAYS","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.days","_CONTINUE_":"!(attr are present)","days_reg":["^(?!.*\\\\b([1-7]),.*\\\\b\\\\1\\\\b)([1-7](,[1-7]){0,6})$"],"_RETURN_":"attr follow regex days_reg"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY_RANGE","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","times":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","range":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","_RETURN_":"(frequency are present && times are present) || range are present"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","_CONTINUE_":"!(frequency are present)","reg":["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"],"_RETURN_":"frequency follow regex reg"},{"_NAME_":"LOCATIONS_GPS","attr":"$.message.catalog['bpp/providers'][*].locations[*].gps","reg":["^\\\\d{2}\\\\.\\\\d{4,}\\\\s*,\\\\s*\\\\d{2}\\\\.\\\\d{4,}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RANGE_START_AND_END","start":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","end":"$.message.catalog['bpp/providers'][*].locations[*].time.range.end","reg":["^([01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"start follow regex reg && end follow regex reg"},{"_NAME_":"LOCATIONS_ADDRESS_LOCALITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.locality","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STREET","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.street","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_CITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.city","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_AREA_CODE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.area_code","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STATE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.state","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_CIRCLE_RADIUS_UNIT","attr":"$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit","var_enum":["km"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"PROVIDERS_CATEGORIES","_RETURN_":[{"_NAME_":"CATEGORIES_ID","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","reg":["^[a-zA-Z0-9]{1,12}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"CATEGORIES_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].categories[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"BPP_PROVIDER_CATEGORIES_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_ATTR","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}]}]}]},{"_NAME_":"PROVIDERS_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RATING","attr":"$.message.catalog['bpp/providers'][*].items[*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"ITEMS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].items[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].items[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.code","reg":["^(1|5):"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_AVAILABLE_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_MAXIMUM_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","var_enum":["INR"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_PRICE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_MAXIMUM_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.maximum_value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","valid":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RETURNABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CANCELLABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_SELLER_PICKUP_RETURN","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TIME_TO_SHIP","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_AVAILABLE_ON_COD","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_CONTINUE_":"!(category all in applicable_categories)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"TAGS_VEG_NONVEG","_RETURN_":[{"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"PROVIDERS_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo","delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BPP_PROVIDERS_OFFERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_QUALIFIER","_RETURN_":[{"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_BENEFIT","_RETURN_":[{"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_META","_RETURN_":[{"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}]}]}]},{"_NAME_":"PROVIDERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_VALID_TIMING_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_TIMING","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_PROVIDERS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]}]}
                """
                    }}] + sub_results

                def CATALOG_BPP_FULFILLMENTS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for CATALOG_BPP_FULFILLMENTS_obj in scope:
                        CATALOG_BPP_FULFILLMENTS_obj["_EXTERNAL"] = input_data["external_data"]

                        def BPP_FULFILLMENTS_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BPP_FULFILLMENTS_TYPE_obj in scope:
                                BPP_FULFILLMENTS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BPP_FULFILLMENTS_TYPE_obj, "$.message.catalog['bpp/fulfillments'][*].type")
                                var_enum = ["Delivery","Self-Pickup","Buyer-Delivery"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del BPP_FULFILLMENTS_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BPP_FULFILLMENTS_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BPP_FULFILLMENTS_TYPE**: every element of $.message.catalog['bpp/fulfillments'][*].type must be in ["Delivery", "Self-Pickup", "Buyer-Delivery"]

                        	> Note: **Condition BPP_FULFILLMENTS_TYPE** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.catalog['bpp/fulfillments'][*].type must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BPP_FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/fulfillments'][*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del BPP_FULFILLMENTS_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BPP_FULFILLMENTS_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BPP_FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/fulfillments'][*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        test_functions = [
                            BPP_FULFILLMENTS_TYPE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del CATALOG_BPP_FULFILLMENTS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "CATALOG_BPP_FULFILLMENTS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"CATALOG_BPP_FULFILLMENTS","_RETURN_":[{"_NAME_":"BPP_FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/fulfillments'][*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}
                """
                    }}] + sub_results

                test_functions = [
                    CATALOG_BPP_DESCRIPTOR,
                    CATALOG_BPP_PROVIDERS,
                    CATALOG_BPP_FULFILLMENTS,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del ON_SEARCH_CATALOG_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_SEARCH_CATALOG",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_SEARCH_CATALOG","_RETURN_":[{"_NAME_":"CATALOG_BPP_DESCRIPTOR","_RETURN_":[{"_NAME_":"BPP_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/descriptor'].symbol","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/descriptor'].short_desc","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/descriptor'].long_desc","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/descriptor'].images[*]","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[*].code","valid":["bpp_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_ENUMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code","valid":["np_type","accept_bap_terms","collect_payment"],"_RETURN_":"attr all in valid"},{"_NAME_":"BPP_DESCRIPTOR_TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"CATALOG_BPP_PROVIDERS","_RETURN_":[{"_NAME_":"PROVIDERS_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_RATING","attr":"$.message.catalog['bpp/providers'][*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"PROVIDERS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PROVIDERS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"PROVIDERS_TAGS_VALID_ENUMS","attr":"$.message.catalog['bpp/providers'][*].tags[*].code","var_enum":["timing","close_timing","serviceability","order_value","np_fees"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PROVIDERS_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_CONTACT_PHONE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone","phone":["^\\\\d{10,11}$"],"_RETURN_":"attr follow regex phone"},{"_NAME_":"FULFILLMENTS_CONTACT_EMAIL","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email","email":["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"],"_RETURN_":"attr follow regex email"}]},{"_NAME_":"PROVIDERS_DESCRIPTOR","_RETURN_":[{"_NAME_":"PROVIDERS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].descriptor.images[*]","_RETURN_":"attr are present"}]},{"_NAME_":"PROVIDERS_TTL","attr":"$.message.catalog['bpp/providers'][*].ttl","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_LOCATIONS","_RETURN_":[{"_NAME_":"LOCATIONS_ID","attr":"$.message.catalog['bpp/providers'][*].locations[*].id","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LOCATIONS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]","time_reg":["^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE_TIMES","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","_CONTINUE_":"!(attr are present)","time_reg":["^(?:[01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_DAYS","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.days","_CONTINUE_":"!(attr are present)","days_reg":["^(?!.*\\\\b([1-7]),.*\\\\b\\\\1\\\\b)([1-7](,[1-7]){0,6})$"],"_RETURN_":"attr follow regex days_reg"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY_RANGE","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","times":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","range":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","_RETURN_":"(frequency are present && times are present) || range are present"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","_CONTINUE_":"!(frequency are present)","reg":["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"],"_RETURN_":"frequency follow regex reg"},{"_NAME_":"LOCATIONS_GPS","attr":"$.message.catalog['bpp/providers'][*].locations[*].gps","reg":["^\\\\d{2}\\\\.\\\\d{4,}\\\\s*,\\\\s*\\\\d{2}\\\\.\\\\d{4,}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RANGE_START_AND_END","start":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","end":"$.message.catalog['bpp/providers'][*].locations[*].time.range.end","reg":["^([01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"start follow regex reg && end follow regex reg"},{"_NAME_":"LOCATIONS_ADDRESS_LOCALITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.locality","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STREET","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.street","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_CITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.city","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_AREA_CODE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.area_code","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STATE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.state","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_CIRCLE_RADIUS_UNIT","attr":"$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit","var_enum":["km"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"PROVIDERS_CATEGORIES","_RETURN_":[{"_NAME_":"CATEGORIES_ID","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","reg":["^[a-zA-Z0-9]{1,12}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"CATEGORIES_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].categories[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"BPP_PROVIDER_CATEGORIES_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_ATTR","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}]}]}]},{"_NAME_":"PROVIDERS_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RATING","attr":"$.message.catalog['bpp/providers'][*].items[*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"ITEMS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].items[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].items[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.code","reg":["^(1|5):"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_AVAILABLE_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_MAXIMUM_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","var_enum":["INR"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_PRICE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_MAXIMUM_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.maximum_value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","valid":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RETURNABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CANCELLABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_SELLER_PICKUP_RETURN","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TIME_TO_SHIP","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_AVAILABLE_ON_COD","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_CONTINUE_":"!(category all in applicable_categories)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"TAGS_VEG_NONVEG","_RETURN_":[{"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"PROVIDERS_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo","delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BPP_PROVIDERS_OFFERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_QUALIFIER","_RETURN_":[{"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_BENEFIT","_RETURN_":[{"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_META","_RETURN_":[{"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}]}]}]},{"_NAME_":"PROVIDERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_VALID_TIMING_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_TIMING","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_PROVIDERS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"CATALOG_BPP_FULFILLMENTS","_RETURN_":[{"_NAME_":"BPP_FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/fulfillments'][*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}]}
        """
            }}] + sub_results

        test_functions = [
            ON_SEARCH_CONTEXT,
            ON_SEARCH_CATALOG,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_search_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_search_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_search_validations","_RETURN_":[{"_NAME_":"ON_SEARCH_CONTEXT","_DESCRIPTION_":"Validate on_search context","action":["on_search"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_search"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_search"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_search"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_search"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_search"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_search"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_search"]}]}]},{"_NAME_":"ON_SEARCH_CATALOG","_RETURN_":[{"_NAME_":"CATALOG_BPP_DESCRIPTOR","_RETURN_":[{"_NAME_":"BPP_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/descriptor'].symbol","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/descriptor'].short_desc","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/descriptor'].long_desc","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/descriptor'].images[*]","_RETURN_":"attr are present"},{"_NAME_":"BPP_DESCRIPTOR_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[*].code","valid":["bpp_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_DESCRIPTORS_VALID_ENUMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code","valid":["np_type","accept_bap_terms","collect_payment"],"_RETURN_":"attr all in valid"},{"_NAME_":"BPP_DESCRIPTOR_TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","var_enum":["ISN","MSN"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_COLLECT_PAYMENT","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='collect_payment')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","var_enum":["true","false"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"CATALOG_BPP_PROVIDERS","_RETURN_":[{"_NAME_":"PROVIDERS_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_RATING","attr":"$.message.catalog['bpp/providers'][*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"PROVIDERS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PROVIDERS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"PROVIDERS_TAGS_VALID_ENUMS","attr":"$.message.catalog['bpp/providers'][*].tags[*].code","var_enum":["timing","close_timing","serviceability","order_value","np_fees"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PROVIDERS_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_CONTACT_PHONE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.phone","phone":["^\\\\d{10,11}$"],"_RETURN_":"attr follow regex phone"},{"_NAME_":"FULFILLMENTS_CONTACT_EMAIL","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].contact.email","email":["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"],"_RETURN_":"attr follow regex email"}]},{"_NAME_":"PROVIDERS_DESCRIPTOR","_RETURN_":[{"_NAME_":"PROVIDERS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].descriptor.images[*]","_RETURN_":"attr are present"}]},{"_NAME_":"PROVIDERS_TTL","attr":"$.message.catalog['bpp/providers'][*].ttl","_RETURN_":"attr are present"},{"_NAME_":"PROVIDERS_LOCATIONS","_RETURN_":[{"_NAME_":"LOCATIONS_ID","attr":"$.message.catalog['bpp/providers'][*].locations[*].id","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LOCATIONS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.timestamp","time_reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.holidays[*]","time_reg":["^\\\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\\\d|3[01])$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_SCHEDULE_TIMES","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","_CONTINUE_":"!(attr are present)","time_reg":["^(?:[01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"attr follow regex time_reg"},{"_NAME_":"LOCATIONS_TIME_DAYS","attr":"$.message.catalog['bpp/providers'][*].locations[*].time.days","_CONTINUE_":"!(attr are present)","days_reg":["^(?!.*\\\\b([1-7]),.*\\\\b\\\\1\\\\b)([1-7](,[1-7]){0,6})$"],"_RETURN_":"attr follow regex days_reg"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY_RANGE","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","times":"$.message.catalog['bpp/providers'][*].locations[*].time.schedule.times[*]","range":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","_RETURN_":"(frequency are present && times are present) || range are present"},{"_NAME_":"LOCATIONS_TIME_FREQUENCY","frequency":"$.message.catalog['bpp/providers'][*].locations[*].time.frequency","_CONTINUE_":"!(frequency are present)","reg":["^P(?=\\d|T)(?:(\\d+)Y)?(?:(\\d+)M)?(?:(\\d+)W)?(?:(\\d+)D)?(?:T(?=\\d)(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)S)?)?$"],"_RETURN_":"frequency follow regex reg"},{"_NAME_":"LOCATIONS_GPS","attr":"$.message.catalog['bpp/providers'][*].locations[*].gps","reg":["^\\\\d{2}\\\\.\\\\d{4,}\\\\s*,\\\\s*\\\\d{2}\\\\.\\\\d{4,}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RANGE_START_AND_END","start":"$.message.catalog['bpp/providers'][*].locations[*].time.range.start","end":"$.message.catalog['bpp/providers'][*].locations[*].time.range.end","reg":["^([01]\\\\d|2[0-3])[0-5]\\\\d$"],"_RETURN_":"start follow regex reg && end follow regex reg"},{"_NAME_":"LOCATIONS_ADDRESS_LOCALITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.locality","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STREET","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.street","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_CITY","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.city","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_AREA_CODE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.area_code","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_ADDRESS_STATE","attr":"$.message.catalog['bpp/providers'][*].locations[*].address.state","_RETURN_":"attr are present"},{"_NAME_":"LOCATIONS_CIRCLE_RADIUS_UNIT","attr":"$.message.catalog['bpp/providers'][*].locations[*].circle.radius.unit","var_enum":["km"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"PROVIDERS_CATEGORIES","_RETURN_":[{"_NAME_":"CATEGORIES_ID","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","reg":["^[a-zA-Z0-9]{1,12}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"CATEGORIES_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].categories[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"BPP_PROVIDER_CATEGORIES_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[*].code","tag_enum":["type","attr","np_fees"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[*].code","tag_enum":["type","attr"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_1","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_TAGS_2","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["variant_group","category"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDER_CATEGORY_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDER_CATEGORY_ATTR","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_CATEGORY_TYPE_ATTR","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].categories[*].tags[?(@.code=='attr')].list[*].code","tag_enum":["name","seq"],"_RETURN_":"attr all in tag_enum"}]}]}]},{"_NAME_":"PROVIDERS_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RATING","attr":"$.message.catalog['bpp/providers'][*].items[*].rating","_CONTINUE_":"!(attr are present)","rating_reg":["^(?:[1-4](?:\\\\.\\\\d+)?|5(?:\\\\.0+)?|\\\\s*)$"],"_RETURN_":"attr follow regex rating_reg"},{"_NAME_":"ITEMS_TIME_LABEL","attr":"$.message.catalog['bpp/providers'][*].items[*].time.label","var_enum":["enable","disable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TIME_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].items[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SYMBOL","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.symbol","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.code","reg":["^(1|5):"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_DESCRIPTOR_IMAGES","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_UNIT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.unit","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_UNITIZED_MEASURE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.unitized.measure.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_AVAILABLE_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_QUANTITY_MAXIMUM_COUNT","attr":"$.message.catalog['bpp/providers'][*].items[*].quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","var_enum":["INR"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_PRICE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PRICE_MAXIMUM_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.maximum_value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","valid":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_RETURNABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/returnable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_CANCELLABLE","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/cancellable']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_SELLER_PICKUP_RETURN","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/seller_pickup_return']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TIME_TO_SHIP","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/time_to_ship']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_AVAILABLE_ON_COD","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/available_on_cod']","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_ADDITIVES_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].additives_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_BRAND_OWNER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].brand_owner_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_IMPORTER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].importer_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_NUTRITIONAL_INFO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].nutritional_info","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PREPACKAGED_FOOD_OTHER_FSSAI_LICENSE_NO","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_prepackaged_food'].other_FSSAI_license_no","_RETURN_":"attr are present","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Bakery, Cakes & Dairy","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Tinned and Processed Food","Energy and Soft Drinks","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Snacks"]},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_COMMON_OR_GENERIC_NAME_OF_COMMODITY","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].common_or_generic_name_of_commodity","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_ADDRESS","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_address","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MANUFACTURER_OR_PACKER_NAME","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].manufacturer_or_packer_name","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_CONTINUE_":"!(category all in applicable_categories)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_STATUTORY_REQS_PACKAGED_COMMODITIES_MONTH_YEAR_OF_MANUFACTURE_PACKING_IMPORT","attr":"$.message.catalog['bpp/providers'][*].items[*]['@ondc/org/statutory_reqs_packaged_commodities'].month_year_of_manufacture_packing_import","category":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(category all in applicable_categories)","applicable_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Cleaning & Household","Bakery, Cakes & Dairy","Pet Care","Stationery","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks"],"_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_ITEMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","valid":["origin","veg_nonveg","image","timing","np_fees"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_ITEMS_ORIGIN_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[*].code","tag_enum":["country"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"ITEMS_TAGS_ORIGIN","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='origin')].list[?(@.code=='country')].value","reg":["^[A-Z]{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"ITEMS_TAGS_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='type')].value","var_enum":["back_image"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_TYPE_VALID_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='image')].list[?(@.code=='url')].value","reg":["^(https?:\\\\/\\\\/)?(www\\\\.)?[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}(\\/[^\\\\s]*)?$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"TAGS_VEG_NONVEG","_RETURN_":[{"_NAME_":"TAGS_VEG_NONVEG_CODES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].code","var_enum":["veg","non_veg","egg"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_VEG_NONVEG_VALUES","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='veg_nonveg')].list[*].value","var_enum":["yes"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"PROVIDERS_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","attr":"$.message.catalog['bpp/providers'][*].offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo","delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BPP_PROVIDERS_OFFERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_OFFERS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[*].code","valid":["qualifier","benefit","meta","finance_terms"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_QUALIFIER","_RETURN_":[{"_NAME_":"TAGS_QUALIFIER_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='qualifier')].list[*].code","tag_enum":["min_value","item_count","item_count_upper"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_BENEFIT","_RETURN_":[{"_NAME_":"TAGS_BENEFIT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[*].code","tag_enum":["value_type","value","value_cap","item_count","item_id","item_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_BENEFIT_VALUE_TYPE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='benefit')].list[?(@.code=='value_type')].value","var_enum":["percent","amount"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_META","_RETURN_":[{"_NAME_":"TAGS_META_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[*].code","tag_enum":["additive","auto"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_META_ADDITIVE","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_META_AUTO","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='meta')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].offers[*].tags[?(@.code=='finance_terms')].list[*].code","tag_enum":["subvention_type","subvention_amount"],"_RETURN_":"attr all in tag_enum"}]}]}]},{"_NAME_":"PROVIDERS_TAGS","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_VALID_TIMING_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_SERVICABILITY_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[*].code","tag_enum":["location","category","type","val","day_from","day_to","time_from","time_to","unit"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_TYPE","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='type')].value","var_enum":["10","11","12","13"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_PROVIDERS_SERVICEABILITY_UNIT","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='serviceability')].list[?(@.code=='unit')].value","var_enum":["km","geojson","country","pincode"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_ORDER_VALUE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[*].code","tag_enum":["min_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_ORDER_VALUE_MIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='order_value')].list[?(@.code=='min_value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK","_RETURN_":[{"_NAME_":"TAGS_PROVIDERS_CATALOG_LINK_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='catalog_link')].list[?(@.code=='type')].value","var_enum":["link","inline"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_PROVIDERS_TIMING","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_TIMING_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='timing')].list[*].code","tag_enum":["type","location","day_from","day_to","time_from","time_to"],"_RETURN_":"attr all in tag_enum"}]},{"_NAME_":"TAGS_PROVIDERS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_PROVIDER_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[*].code","tag_enum":["channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in tag_enum"},{"_NAME_":"TAGS_PROVIDERS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]}]},{"_NAME_":"CATALOG_BPP_FULFILLMENTS","_RETURN_":[{"_NAME_":"BPP_FULFILLMENTS_TYPE","attr":"$.message.catalog['bpp/fulfillments'][*].type","var_enum":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}]}]}
"""
    }}] + sub_results

def on_search(input_data):
    total_results = on_search_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "on_search_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
