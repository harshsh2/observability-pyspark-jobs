from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_init_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_init_validations_obj in scope:
        on_init_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def ON_INIT_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_INIT_CONTEXT_obj in scope:
                ON_INIT_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["on_init"]

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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]}
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
                                action = ["on_init"]

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
                        {"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                        {"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]}
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
                                action = ["on_init"]

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
                        	> - **condition B**: ["on_init"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]}
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
                                action = ["on_init"]

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
                        	> - **condition B**: ["on_init"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]}
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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                                action = ["on_init"]

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
                        	> - **condition B**: every element of ["on_init"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}]}
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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["on_init"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition CONTEXT_ENUM_ACTION**: $.context.action must be equal to ["on_init"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]}
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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]}
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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                                action = ["on_init"]

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
                        	> - **condition B**: ["on_init"] must be equal to ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]}
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
                                action = ["on_init"]

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
                        	> - **condition B**: every element of ["on_init"] must be in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}]}
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

                # del ON_INIT_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_INIT_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_INIT_CONTEXT","_DESCRIPTION_":"Validate on_init context","action":["on_init"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}]}]}
        """
            }}] + sub_results

        def ON_INIT_ORDER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_INIT_ORDER_obj in scope:
                ON_INIT_ORDER_obj["_EXTERNAL"] = input_data["external_data"]

                def ORDER_PROVIDER(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PROVIDER_obj in scope:
                        ORDER_PROVIDER_obj["_EXTERNAL"] = input_data["external_data"]

                        def ORDER_PROVIDER_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ORDER_PROVIDER_ID_obj in scope:
                                ORDER_PROVIDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ORDER_PROVIDER_ID_obj, "$.message.order.provider.id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ORDER_PROVIDER_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ORDER_PROVIDER_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ORDER_PROVIDER_ID**: $.message.order.provider.id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ORDER_PROVIDER_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ORDER_PROVIDER_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ORDER_PROVIDER_LOCATIONS_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ORDER_PROVIDER_LOCATIONS_ID_obj in scope:
                                ORDER_PROVIDER_LOCATIONS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ORDER_PROVIDER_LOCATIONS_ID_obj, "$.message.order.provider.locations[*].id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ORDER_PROVIDER_LOCATIONS_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ORDER_PROVIDER_LOCATIONS_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ORDER_PROVIDER_LOCATIONS_ID**: $.message.order.provider.locations[*].id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ORDER_PROVIDER_LOCATIONS_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ORDER_PROVIDER_LOCATIONS_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            ORDER_PROVIDER_ID,
                            ORDER_PROVIDER_LOCATIONS_ID,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_PROVIDER_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_PROVIDER",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_ITEMS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_ITEMS_obj in scope:
                        ORDER_ITEMS_obj["_EXTERNAL"] = input_data["external_data"]

                        def ITEMS_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_ID_obj in scope:
                                ITEMS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_ID_obj, "$.message.order.items[*].id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_ID**: $.message.order.items[*].id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"}
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
                        {"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ITEMS_FULFILLMENT_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_FULFILLMENT_ID_obj in scope:
                                ITEMS_FULFILLMENT_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_FULFILLMENT_ID_obj, "$.message.order.items[*].fulfillment_id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_FULFILLMENT_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_FULFILLMENT_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_FULFILLMENT_ID**: $.message.order.items[*].fulfillment_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"}
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
                        {"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ITEMS_LOCATION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_LOCATION_ID_obj in scope:
                                ITEMS_LOCATION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_LOCATION_ID_obj, "$.message.order.items[*].location_id")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_LOCATION_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_LOCATION_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_LOCATION_ID**: $.message.order.items[*].location_id must be present in the payload

                        	> Note: **Condition ITEMS_LOCATION_ID** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.items[*].location_id must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                        {"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ITEMS_QUANTITY_COUNT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_QUANTITY_COUNT_obj in scope:
                                ITEMS_QUANTITY_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_QUANTITY_COUNT_obj, "$.message.order.items[*].quantity.count")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_QUANTITY_COUNT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_QUANTITY_COUNT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_QUANTITY_COUNT**: $.message.order.items[*].quantity.count must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ITEMS_QUANTITY_COUNT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_QUANTITY_COUNT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ITEMS_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_obj in scope:
                                ITEMS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def ITEMS_TAGS_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TAGS_VALID_TAGS_obj in scope:
                                        ITEMS_TAGS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_TAGS_VALID_TAGS_obj, "$.message.order.items[*].tags[*].code")
                                        valid = ["np_fees"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del ITEMS_TAGS_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_TAGS_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees"]

                                	> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del ITEMS_TAGS_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_TAGS_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    ITEMS_TAGS_VALID_TAGS,
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
                        {"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees"],"_RETURN_":"attr all in valid"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            ITEMS_ID,
                            ITEMS_FULFILLMENT_ID,
                            ITEMS_LOCATION_ID,
                            ITEMS_QUANTITY_COUNT,
                            ITEMS_TAGS,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_ITEMS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_ITEMS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees"],"_RETURN_":"attr all in valid"}]}]}
                """
                    }}] + sub_results

                def ORDER_ITEMS_ADDITIONAL_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_ITEMS_ADDITIONAL_TAGS_obj in scope:
                        ORDER_ITEMS_ADDITIONAL_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def ITEMS_TAGS_VALID_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_VALID_TAGS_obj in scope:
                                ITEMS_TAGS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_TAGS_VALID_TAGS_obj, "$.message.order.items[*].tags[*].code")
                                valid = ["np_fees","rto_action"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, valid)

                                if not validate:
                                    del ITEMS_TAGS_VALID_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_TAGS_VALID_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_TAGS_VALID_TAGS**: every element of $.message.order.items[*].tags[*].code must be in ["np_fees", "rto_action"]

                        	> Note: **Condition ITEMS_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees","rto_action"],"_RETURN_":"attr all in valid"}
                        """
                                        }
                                    }]

                                # del ITEMS_TAGS_VALID_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_TAGS_VALID_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees","rto_action"],"_RETURN_":"attr all in valid"}
                        """
                            }}] + sub_results

                        def ITEMS_TAGS_NP_FEES_VALID_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_NP_FEES_VALID_TAGS_obj in scope:
                                ITEMS_TAGS_NP_FEES_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_TAGS_NP_FEES_VALID_TAGS_obj, "$.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code")
                                valid = ["id"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, valid)

                                if not validate:
                                    del ITEMS_TAGS_NP_FEES_VALID_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_TAGS_NP_FEES_VALID_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_TAGS_NP_FEES_VALID_TAGS**: every element of $.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code must be in ["id"]

                        	> Note: **Condition ITEMS_TAGS_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code","valid":["id"],"_RETURN_":"attr all in valid"}
                        """
                                        }
                                    }]

                                # del ITEMS_TAGS_NP_FEES_VALID_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_TAGS_NP_FEES_VALID_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code","valid":["id"],"_RETURN_":"attr all in valid"}
                        """
                            }}] + sub_results

                        def ITEMS_TAGS_RTO_ACTION_VALID_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_RTO_ACTION_VALID_TAGS_obj in scope:
                                ITEMS_TAGS_RTO_ACTION_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_TAGS_RTO_ACTION_VALID_TAGS_obj, "$.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code")
                                valid = ["return_to_origin"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, valid)

                                if not validate:
                                    del ITEMS_TAGS_RTO_ACTION_VALID_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_TAGS_RTO_ACTION_VALID_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_TAGS_RTO_ACTION_VALID_TAGS**: every element of $.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code must be in ["return_to_origin"]

                        	> Note: **Condition ITEMS_TAGS_RTO_ACTION_VALID_TAGS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_RTO_ACTION_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code","valid":["return_to_origin"],"_RETURN_":"attr all in valid"}
                        """
                                        }
                                    }]

                                # del ITEMS_TAGS_RTO_ACTION_VALID_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_TAGS_RTO_ACTION_VALID_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_RTO_ACTION_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code","valid":["return_to_origin"],"_RETURN_":"attr all in valid"}
                        """
                            }}] + sub_results

                        def ITEMS_TAGS_RTO_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_RTO_ACTION_obj in scope:
                                ITEMS_TAGS_RTO_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_TAGS_RTO_ACTION_obj, "$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value")
                                var_enum = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del ITEMS_TAGS_RTO_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_TAGS_RTO_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition ITEMS_TAGS_RTO_ACTION**: every element of $.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must be in ["yes", "no"]

                        	> Note: **Condition ITEMS_TAGS_RTO_ACTION** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del ITEMS_TAGS_RTO_ACTION_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_TAGS_RTO_ACTION",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        test_functions = [
                            ITEMS_TAGS_VALID_TAGS,
                            ITEMS_TAGS_NP_FEES_VALID_TAGS,
                            ITEMS_TAGS_RTO_ACTION_VALID_TAGS,
                            ITEMS_TAGS_RTO_ACTION,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_ITEMS_ADDITIONAL_TAGS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_ITEMS_ADDITIONAL_TAGS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_ITEMS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees","rto_action"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code","valid":["id"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code","valid":["return_to_origin"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]}
                """
                    }}] + sub_results

                def ORDER_BILLING(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_BILLING_obj in scope:
                        ORDER_BILLING_obj["_EXTERNAL"] = input_data["external_data"]

                        def BILLING_ADDRESS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BILLING_ADDRESS_obj in scope:
                                BILLING_ADDRESS_obj["_EXTERNAL"] = input_data["external_data"]

                                def BILLING_ADDRESS_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_NAME_obj in scope:
                                        BILLING_ADDRESS_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_NAME_obj, "$.message.order.billing.address.name")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_NAME**: $.message.order.billing.address.name must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BILLING_ADDRESS_BUILDING(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_BUILDING_obj in scope:
                                        BILLING_ADDRESS_BUILDING_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_BUILDING_obj, "$.message.order.billing.address.building")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_BUILDING_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_BUILDING",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_BUILDING**: $.message.order.billing.address.building must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_BUILDING_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_BUILDING",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BILLING_ADDRESS_LOCALITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_LOCALITY_obj in scope:
                                        BILLING_ADDRESS_LOCALITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_LOCALITY_obj, "$.message.order.billing.address.locality")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_LOCALITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_LOCALITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_LOCALITY**: $.message.order.billing.address.locality must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_LOCALITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_LOCALITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BILLING_ADDRESS_CITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_CITY_obj in scope:
                                        BILLING_ADDRESS_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_CITY_obj, "$.message.order.billing.address.city")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_CITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_CITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_CITY**: $.message.order.billing.address.city must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_CITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_CITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BILLING_ADDRESS_STATE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_STATE_obj in scope:
                                        BILLING_ADDRESS_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_STATE_obj, "$.message.order.billing.address.state")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_STATE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_STATE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_STATE**: $.message.order.billing.address.state must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_STATE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_STATE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BILLING_ADDRESS_COUNTRY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_COUNTRY_obj in scope:
                                        BILLING_ADDRESS_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_COUNTRY_obj, "$.message.order.billing.address.country")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_COUNTRY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_COUNTRY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_COUNTRY**: $.message.order.billing.address.country must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_COUNTRY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_COUNTRY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def BILLING_ADDRESS_AREA_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BILLING_ADDRESS_AREA_CODE_obj in scope:
                                        BILLING_ADDRESS_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BILLING_ADDRESS_AREA_CODE_obj, "$.message.order.billing.address.area_code")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del BILLING_ADDRESS_AREA_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BILLING_ADDRESS_AREA_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BILLING_ADDRESS_AREA_CODE**: $.message.order.billing.address.area_code must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del BILLING_ADDRESS_AREA_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BILLING_ADDRESS_AREA_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    BILLING_ADDRESS_NAME,
                                    BILLING_ADDRESS_BUILDING,
                                    BILLING_ADDRESS_LOCALITY,
                                    BILLING_ADDRESS_CITY,
                                    BILLING_ADDRESS_STATE,
                                    BILLING_ADDRESS_COUNTRY,
                                    BILLING_ADDRESS_AREA_CODE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del BILLING_ADDRESS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BILLING_ADDRESS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def BILLING_PHONE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BILLING_PHONE_obj in scope:
                                BILLING_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BILLING_PHONE_obj, "$.message.order.billing.phone")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BILLING_PHONE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BILLING_PHONE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BILLING_PHONE**: $.message.order.billing.phone must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BILLING_PHONE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BILLING_PHONE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BILLING_NAME(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BILLING_NAME_obj in scope:
                                BILLING_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BILLING_NAME_obj, "$.message.order.billing.name")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BILLING_NAME_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BILLING_NAME",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BILLING_NAME**: $.message.order.billing.name must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BILLING_NAME_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BILLING_NAME",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BILLING_CREATED_AT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BILLING_CREATED_AT_obj in scope:
                                BILLING_CREATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BILLING_CREATED_AT_obj, "$.message.order.billing.created_at")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BILLING_CREATED_AT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BILLING_CREATED_AT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BILLING_CREATED_AT**: $.message.order.billing.created_at must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BILLING_CREATED_AT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BILLING_CREATED_AT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BILLING_UPDATED_AT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BILLING_UPDATED_AT_obj in scope:
                                BILLING_UPDATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BILLING_UPDATED_AT_obj, "$.message.order.billing.updated_at")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BILLING_UPDATED_AT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BILLING_UPDATED_AT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition BILLING_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BILLING_UPDATED_AT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BILLING_UPDATED_AT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            BILLING_ADDRESS,
                            BILLING_PHONE,
                            BILLING_NAME,
                            BILLING_CREATED_AT,
                            BILLING_UPDATED_AT,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_BILLING_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_BILLING",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_FULFILLMENTS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_FULFILLMENTS_obj in scope:
                        ORDER_FULFILLMENTS_obj["_EXTERNAL"] = input_data["external_data"]

                        def FULFILLMENTS_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_ID_obj in scope:
                                FULFILLMENTS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_ID_obj, "$.message.order.fulfillments[*].id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition FULFILLMENTS_ID**: $.message.order.fulfillments[*].id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"}
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
                        {"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TYPE_obj in scope:
                                FULFILLMENTS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_TYPE_obj, "$.message.order.fulfillments[*].type")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition FULFILLMENTS_TYPE**: $.message.order.fulfillments[*].type must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"}
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
                        {"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_END_LOCATION_GPS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_END_LOCATION_GPS_obj in scope:
                                FULFILLMENTS_END_LOCATION_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_GPS_obj, "$.message.order.fulfillments[*].end.location.gps")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_END_LOCATION_GPS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_GPS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition FULFILLMENTS_END_LOCATION_GPS**: $.message.order.fulfillments[*].end.location.gps must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_END_LOCATION_GPS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_END_LOCATION_GPS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_END_LOCATION_ADDRESS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_END_LOCATION_ADDRESS_obj in scope:
                                FULFILLMENTS_END_LOCATION_ADDRESS_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_END_LOCATION_ADDRESS_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_NAME_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_NAME_obj, "$.message.order.fulfillments[*].end.location.address.name")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_NAME**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj, "$.message.order.fulfillments[*].end.location.address.building")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj, "$.message.order.fulfillments[*].end.location.address.locality")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_LOCATION_ADDRESS_CITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj, "$.message.order.fulfillments[*].end.location.address.city")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_CITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_CITY**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_CITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_LOCATION_ADDRESS_STATE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj, "$.message.order.fulfillments[*].end.location.address.state")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_STATE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_STATE**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_STATE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj, "$.message.order.fulfillments[*].end.location.address.country")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj in scope:
                                        FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj, "$.message.order.fulfillments[*].end.location.address.area_code")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_END_LOCATION_ADDRESS_NAME,
                                    FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING,
                                    FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY,
                                    FULFILLMENTS_END_LOCATION_ADDRESS_CITY,
                                    FULFILLMENTS_END_LOCATION_ADDRESS_STATE,
                                    FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY,
                                    FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_END_LOCATION_ADDRESS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_END_CONTACT_PHONE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_END_CONTACT_PHONE_obj in scope:
                                FULFILLMENTS_END_CONTACT_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_CONTACT_PHONE_obj, "$.message.order.fulfillments[*].end.contact.phone")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_END_CONTACT_PHONE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_END_CONTACT_PHONE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition FULFILLMENTS_END_CONTACT_PHONE**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_END_CONTACT_PHONE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_END_CONTACT_PHONE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILLMENTS_ID,
                            FULFILLMENTS_TYPE,
                            FULFILLMENTS_END_LOCATION_GPS,
                            FULFILLMENTS_END_LOCATION_ADDRESS,
                            FULFILLMENTS_END_CONTACT_PHONE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_FULFILLMENTS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_FULFILLMENTS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_FULFILLMENTS_ADDITIONAL_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_FULFILLMENTS_ADDITIONAL_TAGS_obj in scope:
                        ORDER_FULFILLMENTS_ADDITIONAL_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def FULFILLMENTS_TAGS_ORDER_DETAILS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TAGS_ORDER_DETAILS_obj in scope:
                                FULFILLMENTS_TAGS_ORDER_DETAILS_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_TAGS_ORDER_VALID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_VALID_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_VALID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_VALID_obj, "$.message.order.fulfillments[*].tags[*].code")
                                        valid = ["order_details"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_VALID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_VALID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_TAGS_ORDER_VALID**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["order_details"]

                                	> Note: **Condition FULFILLMENTS_TAGS_ORDER_VALID** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_VALID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[*].code","valid":["order_details"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_VALID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_VALID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_VALID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[*].code","valid":["order_details"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code")
                                        valid = ["weight_unit","weight_value","dim_unit","length","breadth","height"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS**: every element of $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must be in ["weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]

                                	> Note: **Condition FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code","valid":["weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code","valid":["weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_TAGS_ORDER_VALID,
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_TAGS_ORDER_DETAILS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_VALID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[*].code","valid":["order_details"],"_RETURN_":"attr all in valid"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code","valid":["weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"attr all in valid"}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TAGS_RTO_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TAGS_RTO_ACTION_obj in scope:
                                FULFILLMENTS_TAGS_RTO_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_RTO_ACTION_obj, "$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value")
                                var_enum = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del FULFILLMENTS_TAGS_RTO_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_RTO_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition FULFILLMENTS_TAGS_RTO_ACTION**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must be in ["yes", "no"]

                        	> Note: **Condition FULFILLMENTS_TAGS_RTO_ACTION** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_TAGS_RTO_ACTION_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_TAGS_RTO_ACTION",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILLMENTS_TAGS_ORDER_DETAILS,
                            FULFILLMENTS_TAGS_RTO_ACTION,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_FULFILLMENTS_ADDITIONAL_TAGS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_FULFILLMENTS_ADDITIONAL_TAGS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_VALID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[*].code","valid":["order_details"],"_RETURN_":"attr all in valid"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code","valid":["weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]}
                """
                    }}] + sub_results

                def ORDER_QUOTE(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_QUOTE_obj in scope:
                        ORDER_QUOTE_obj["_EXTERNAL"] = input_data["external_data"]

                        def QUOTE_PRICE_CURRENCY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for QUOTE_PRICE_CURRENCY_obj in scope:
                                QUOTE_PRICE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](QUOTE_PRICE_CURRENCY_obj, "$.message.order.quote.price.currency")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del QUOTE_PRICE_CURRENCY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "QUOTE_PRICE_CURRENCY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition QUOTE_PRICE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del QUOTE_PRICE_CURRENCY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "QUOTE_PRICE_CURRENCY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def QUOTE_PRICE_VALUE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for QUOTE_PRICE_VALUE_obj in scope:
                                QUOTE_PRICE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](QUOTE_PRICE_VALUE_obj, "$.message.order.quote.price.value")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del QUOTE_PRICE_VALUE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "QUOTE_PRICE_VALUE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition QUOTE_PRICE_VALUE**: $.message.order.quote.price.value must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del QUOTE_PRICE_VALUE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "QUOTE_PRICE_VALUE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def QUOTE_TTL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for QUOTE_TTL_obj in scope:
                                QUOTE_TTL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](QUOTE_TTL_obj, "$.message.order.quote.ttl")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del QUOTE_TTL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "QUOTE_TTL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition QUOTE_TTL**: $.message.order.quote.ttl must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del QUOTE_TTL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "QUOTE_TTL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def QUOTE_BREAKUP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for QUOTE_BREAKUP_obj in scope:
                                QUOTE_BREAKUP_obj["_EXTERNAL"] = input_data["external_data"]

                                def BREAKUP_ITEM(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BREAKUP_ITEM_obj in scope:
                                        BREAKUP_ITEM_obj["_EXTERNAL"] = input_data["external_data"]

                                        def BREAKUP_ITEM_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_ID_obj in scope:
                                                BREAKUP_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ID_obj, "$.message.order.quote.breakup[*]['@ondc/org/item_id']")

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del BREAKUP_ITEM_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition BREAKUP_ITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_QUANTITY_COUNT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_QUANTITY_COUNT_obj in scope:
                                                BREAKUP_ITEM_QUANTITY_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_QUANTITY_COUNT_obj, "$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del BREAKUP_ITEM_QUANTITY_COUNT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_QUANTITY_COUNT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition BREAKUP_ITEM_QUANTITY_COUNT**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload

                                        	> Note: **Condition BREAKUP_ITEM_QUANTITY_COUNT** can be skipped if the following conditions are met:
                                        	>
                                        	> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must **not** be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_QUANTITY_COUNT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_QUANTITY_COUNT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_TITLE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_TITLE_obj in scope:
                                                BREAKUP_ITEM_TITLE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_TITLE_obj, "$.message.order.quote.breakup[*].title")

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del BREAKUP_ITEM_TITLE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_TITLE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition BREAKUP_ITEM_TITLE**: $.message.order.quote.breakup[*].title must be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_TITLE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_TITLE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_TITLE_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_TITLE_TYPE_obj in scope:
                                                BREAKUP_ITEM_TITLE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_TITLE_TYPE_obj, "$.message.order.quote.breakup[*]['@ondc/org/title_type']")
                                                var_enum = ["item","delivery","packing","tax","misc","discount","offer"]

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del BREAKUP_ITEM_TITLE_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_TITLE_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition BREAKUP_ITEM_TITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_TITLE_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_TITLE_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_PRICE_CURRENCY(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_PRICE_CURRENCY_obj in scope:
                                                BREAKUP_ITEM_PRICE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_PRICE_CURRENCY_obj, "$.message.order.quote.breakup[*].price.currency")

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del BREAKUP_ITEM_PRICE_CURRENCY_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_PRICE_CURRENCY",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition BREAKUP_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].price.currency must be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_PRICE_CURRENCY_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_PRICE_CURRENCY",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_PRICE_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_PRICE_VALUE_obj in scope:
                                                BREAKUP_ITEM_PRICE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_PRICE_VALUE_obj, "$.message.order.quote.breakup[*].price.value")

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del BREAKUP_ITEM_PRICE_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_PRICE_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""- **condition BREAKUP_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].price.value must be present in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_PRICE_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_PRICE_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_ITEM(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_ITEM_obj in scope:
                                                BREAKUP_ITEM_ITEM_obj["_EXTERNAL"] = input_data["external_data"]

                                                def BREAKUP_ITEM_ITEM_PRICE_CURRENCY(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for BREAKUP_ITEM_ITEM_PRICE_CURRENCY_obj in scope:
                                                        BREAKUP_ITEM_ITEM_PRICE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_PRICE_CURRENCY_obj, "$.message.order.quote.breakup[*].item.price.currency")

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del BREAKUP_ITEM_ITEM_PRICE_CURRENCY_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_PRICE_CURRENCY",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition BREAKUP_ITEM_ITEM_PRICE_CURRENCY**: $.message.order.quote.breakup[*].item.price.currency must be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del BREAKUP_ITEM_ITEM_PRICE_CURRENCY_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ITEM_PRICE_CURRENCY",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def BREAKUP_ITEM_ITEM_PRICE_VALUE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for BREAKUP_ITEM_ITEM_PRICE_VALUE_obj in scope:
                                                        BREAKUP_ITEM_ITEM_PRICE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_PRICE_VALUE_obj, "$.message.order.quote.breakup[*].item.price.value")

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del BREAKUP_ITEM_ITEM_PRICE_VALUE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_PRICE_VALUE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""- **condition BREAKUP_ITEM_ITEM_PRICE_VALUE**: $.message.order.quote.breakup[*].item.price.value must be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del BREAKUP_ITEM_ITEM_PRICE_VALUE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ITEM_PRICE_VALUE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def BREAKUP_ITEM_ITEM_TAGS(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for BREAKUP_ITEM_ITEM_TAGS_obj in scope:
                                                        BREAKUP_ITEM_ITEM_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                                        def BREAKUP_ITEM_VALID_TAGS(input_data):
                                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                            sub_results = []
                                                            valid = True

                                                            for BREAKUP_ITEM_VALID_TAGS_obj in scope:
                                                                BREAKUP_ITEM_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_VALID_TAGS_obj, "$.message.order.quote.breakup[*].item.tags[*].code")
                                                                valid = ["quote","np_fees","offer"]

                                                                skip_check = not (validation_utils["are_present"](attr))
                                                                if skip_check:
                                                                    continue

                                                                validate = validation_utils["all_in"](attr, valid)

                                                                if not validate:
                                                                    del BREAKUP_ITEM_VALID_TAGS_obj["_EXTERNAL"]
                                                                    return [{
                                                                        "test_name": "BREAKUP_ITEM_VALID_TAGS",
                                                                        "valid": False,
                                                                        "code": 30000,
                                                                        "description": r"""- **condition BREAKUP_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["quote", "np_fees", "offer"]

                                                        	> Note: **Condition BREAKUP_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
                                                        	>
                                                        	> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload""",
                                                                        "_debug_info": {
                                                                            "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"}
                                                        """
                                                                        }
                                                                    }]

                                                                # del BREAKUP_ITEM_VALID_TAGS_obj["_EXTERNAL"]

                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_VALID_TAGS",
                                                                "valid": valid,
                                                                "code": 200 if valid else 30000, 
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"}
                                                        """
                                                            }}] + sub_results

                                                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE(input_data):
                                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                            sub_results = []
                                                            valid = True

                                                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_obj in scope:
                                                                BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_obj["_EXTERNAL"] = input_data["external_data"]

                                                                def BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE(input_data):
                                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                                    sub_results = []
                                                                    valid = True

                                                                    for BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE_obj in scope:
                                                                        BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value")
                                                                        var_enum = ["fulfillment","order","item"]

                                                                        skip_check = not (validation_utils["are_present"](attr))
                                                                        if skip_check:
                                                                            continue

                                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                                        if not validate:
                                                                            del BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE_obj["_EXTERNAL"]
                                                                            return [{
                                                                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE",
                                                                                "valid": False,
                                                                                "code": 30000,
                                                                                "description": r"""- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]

                                                                	> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE** can be skipped if the following conditions are met:
                                                                	>
                                                                	> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must **not** be present in the payload""",
                                                                                "_debug_info": {
                                                                                    "fed_config": r"""
                                                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                                """
                                                                                }
                                                                            }]

                                                                        # del BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE_obj["_EXTERNAL"]

                                                                    return [{
                                                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE",
                                                                        "valid": valid,
                                                                        "code": 200 if valid else 30000, 
                                                                        "_debug_info": {
                                                                            "fed_config": r"""
                                                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                                                                """
                                                                    }}] + sub_results

                                                                def BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE(input_data):
                                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                                    sub_results = []
                                                                    valid = True

                                                                    for BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE_obj in scope:
                                                                        BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value")
                                                                        var_enum = ["delivery","packaging","misc"]

                                                                        skip_check = not (validation_utils["are_present"](attr))
                                                                        if skip_check:
                                                                            continue

                                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                                        if not validate:
                                                                            del BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE_obj["_EXTERNAL"]
                                                                            return [{
                                                                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE",
                                                                                "valid": False,
                                                                                "code": 30000,
                                                                                "description": r"""- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]

                                                                	> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE** can be skipped if the following conditions are met:
                                                                	>
                                                                	> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must **not** be present in the payload""",
                                                                                "_debug_info": {
                                                                                    "fed_config": r"""
                                                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}
                                                                """
                                                                                }
                                                                            }]

                                                                        # del BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE_obj["_EXTERNAL"]

                                                                    return [{
                                                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE",
                                                                        "valid": valid,
                                                                        "code": 200 if valid else 30000, 
                                                                        "_debug_info": {
                                                                            "fed_config": r"""
                                                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}
                                                                """
                                                                    }}] + sub_results

                                                                test_functions = [
                                                                    BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE,
                                                                    BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE,
                                                                ]

                                                                all_results = []
                                                                for fn in test_functions:
                                                                    sub_result = fn(input_data)
                                                                    all_results.extend(sub_result)

                                                                sub_results = all_results
                                                                valid = all(r["valid"] for r in sub_results)

                                                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_obj["_EXTERNAL"]

                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE",
                                                                "valid": valid,
                                                                "code": 200 if valid else 30000, 
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}
                                                        """
                                                            }}] + sub_results

                                                        test_functions = [
                                                            BREAKUP_ITEM_VALID_TAGS,
                                                            BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE,
                                                        ]

                                                        all_results = []
                                                        for fn in test_functions:
                                                            sub_result = fn(input_data)
                                                            all_results.extend(sub_result)

                                                        sub_results = all_results
                                                        valid = all(r["valid"] for r in sub_results)

                                                        # del BREAKUP_ITEM_ITEM_TAGS_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    BREAKUP_ITEM_ITEM_PRICE_CURRENCY,
                                                    BREAKUP_ITEM_ITEM_PRICE_VALUE,
                                                    BREAKUP_ITEM_ITEM_TAGS,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del BREAKUP_ITEM_ITEM_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_ITEM",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            BREAKUP_ITEM_ID,
                                            BREAKUP_ITEM_QUANTITY_COUNT,
                                            BREAKUP_ITEM_TITLE,
                                            BREAKUP_ITEM_TITLE_TYPE,
                                            BREAKUP_ITEM_PRICE_CURRENCY,
                                            BREAKUP_ITEM_PRICE_VALUE,
                                            BREAKUP_ITEM_ITEM,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del BREAKUP_ITEM_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BREAKUP_ITEM",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    BREAKUP_ITEM,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del QUOTE_BREAKUP_obj["_EXTERNAL"]

                            return [{
                                "test_name": "QUOTE_BREAKUP",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            QUOTE_PRICE_CURRENCY,
                            QUOTE_PRICE_VALUE,
                            QUOTE_TTL,
                            QUOTE_BREAKUP,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_QUOTE_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_QUOTE",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]}
                """
                    }}] + sub_results

                def ORDER_QUOTE_ADDITIONAL_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_QUOTE_ADDITIONAL_TAGS_obj in scope:
                        ORDER_QUOTE_ADDITIONAL_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_ITEM_VALID_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_ITEM_VALID_TAGS_obj in scope:
                                TAGS_ITEM_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_ITEM_VALID_TAGS_obj, "$.message.order.quote.breakup[*].item.tags[*].code")
                                valid = ["finance_terms","np_fees","quote"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, valid)

                                if not validate:
                                    del TAGS_ITEM_VALID_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_ITEM_VALID_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition TAGS_ITEM_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[*].code must be in ["finance_terms", "np_fees", "quote"]

                        	> Note: **Condition TAGS_ITEM_VALID_TAGS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.quote.breakup[*].item.tags[*].code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["finance_terms","np_fees","quote"],"_RETURN_":"attr all in valid"}
                        """
                                        }
                                    }]

                                # del TAGS_ITEM_VALID_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_ITEM_VALID_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["finance_terms","np_fees","quote"],"_RETURN_":"attr all in valid"}
                        """
                            }}] + sub_results

                        def TAGS_FINANCE_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_FINANCE_TERMS_obj in scope:
                                TAGS_FINANCE_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS_obj in scope:
                                        TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code")
                                        valid = ["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must be in ["subvention_type", "subvention_amount", "provider_tax_number", "bank_account_no", "ifsc_code"]

                                	> Note: **Condition TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code","valid":["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code","valid":["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS,
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
                        {"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code","valid":["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"],"_RETURN_":"attr all in valid"}]}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_NP_FEES_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_NP_FEES_VALID_TAGS_obj in scope:
                                        TAGS_NP_FEES_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_NP_FEES_VALID_TAGS_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code")
                                        valid = ["id","channel_margin_type","channel_margin_value"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_NP_FEES_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_NP_FEES_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_NP_FEES_VALID_TAGS**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must be in ["id", "channel_margin_type", "channel_margin_value"]

                                	> Note: **Condition TAGS_NP_FEES_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code","valid":["id","channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_NP_FEES_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_NP_FEES_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code","valid":["id","channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj in scope:
                                        BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value")
                                        var_enum = ["percent","amount"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE**: every element of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent", "amount"]

                                	> Note: **Condition BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_NP_FEES_VALID_TAGS,
                                    BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code","valid":["id","channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_ITEM_VALID_TAGS,
                            TAGS_FINANCE_TERMS,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_QUOTE_ADDITIONAL_TAGS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_QUOTE_ADDITIONAL_TAGS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_QUOTE_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"TAGS_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["finance_terms","np_fees","quote"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code","valid":["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code","valid":["id","channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]}
                """
                    }}] + sub_results

                def ORDER_PAYMENT(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PAYMENT_obj in scope:
                        ORDER_PAYMENT_obj["_EXTERNAL"] = input_data["external_data"]

                        def PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE_obj in scope:
                                PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE_obj, "$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']")
                                var_enum = ["percent","amount"]

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**: every element of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT_obj in scope:
                                PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT_obj, "$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']")
                                reg = ["^(\\d*.?\\d{1,2})$"]

                                validate = (validation_utils["are_present"](attr)) and (validation_utils["follow_regex"](attr, reg))

                                if not validate:
                                    del PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**: all of the following sub conditions must be met:

                          - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.1**: $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
                          - **condition PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT.2**: all elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"}
                        """
                                        }
                                    }]

                                # del PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"}
                        """
                            }}] + sub_results

                        def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_obj in scope:
                                PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_obj["_EXTERNAL"] = input_data["external_data"]

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload

                                	> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload

                                	> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type")
                                        var_enum = ["upi","neft","rtgs"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]

                                	> Note: **Condition PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","_CONTINUE_":"!(attr are present)","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","_CONTINUE_":"!(attr are present)","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","_CONTINUE_":"!(attr are present)","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE,
                            PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT,
                            PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_PAYMENT_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_PAYMENT",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","_CONTINUE_":"!(attr are present)","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}]}]}
                """
                    }}] + sub_results

                def ORDER_PAYMENT_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PAYMENT_TAGS_obj in scope:
                        ORDER_PAYMENT_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def PAYMENT_TAGS_VALID_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_TAGS_VALID_TAGS_obj in scope:
                                PAYMENT_TAGS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_TAGS_VALID_TAGS_obj, "$.message.order.payment.tags[*].code")
                                valid = ["bpp_terms","bpp_collect"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, valid)

                                if not validate:
                                    del PAYMENT_TAGS_VALID_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_TAGS_VALID_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""- **condition PAYMENT_TAGS_VALID_TAGS**: every element of $.message.order.payment.tags[*].code must be in ["bpp_terms", "bpp_collect"]

                        	> Note: **Condition PAYMENT_TAGS_VALID_TAGS** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.payment.tags[*].code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[*].code","valid":["bpp_terms","bpp_collect"],"_RETURN_":"attr all in valid"}
                        """
                                        }
                                    }]

                                # del PAYMENT_TAGS_VALID_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_TAGS_VALID_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[*].code","valid":["bpp_terms","bpp_collect"],"_RETURN_":"attr all in valid"}
                        """
                            }}] + sub_results

                        def TAGS_BPP_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BPP_TERMS_obj in scope:
                                TAGS_BPP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_BPP_TERMS_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_VALID_TAGS_obj in scope:
                                        TAGS_BPP_TERMS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_VALID_TAGS_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code")
                                        valid = ["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_BPP_TERMS_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must be in ["max_liability_cap", "max_liability", "mandatory_arbitration", "court_jurisdiction", "delay_interest", "np_type", "tax_number", "provider_tax_number", "accept_bap_terms"]

                                	> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_BPP_TERMS_VALID_TAGS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del TAGS_BPP_TERMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BPP_TERMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]}
                        """
                            }}] + sub_results

                        def TAGS_BPP_COLLECT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BPP_COLLECT_obj in scope:
                                TAGS_BPP_COLLECT_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_BPP_COLLECT_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_COLLECT_VALID_TAGS_obj in scope:
                                        TAGS_BPP_COLLECT_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_COLLECT_VALID_TAGS_obj, "$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code")
                                        valid = ["success","error"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_BPP_COLLECT_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_COLLECT_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_COLLECT_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code must be in ["success", "error"]

                                	> Note: **Condition TAGS_BPP_COLLECT_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_COLLECT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code","valid":["success","error"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_COLLECT_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_COLLECT_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_COLLECT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code","valid":["success","error"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_COLLECT_SUCCESS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_COLLECT_SUCCESS_obj in scope:
                                        TAGS_BPP_COLLECT_SUCCESS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_COLLECT_SUCCESS_obj, "$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value")
                                        var_enum = ["Y","N"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del TAGS_BPP_COLLECT_SUCCESS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_COLLECT_SUCCESS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_COLLECT_SUCCESS**: every element of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value must be in ["Y", "N"]

                                	> Note: **Condition TAGS_BPP_COLLECT_SUCCESS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_COLLECT_SUCCESS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_COLLECT_SUCCESS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_COLLECT_ERROR(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_COLLECT_ERROR_obj in scope:
                                        TAGS_BPP_COLLECT_ERROR_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_COLLECT_ERROR_obj, "$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value")
                                        var_enum = ["Y","N"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del TAGS_BPP_COLLECT_ERROR_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_COLLECT_ERROR",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_COLLECT_ERROR**: every element of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value must be in ["Y", "N"]

                                	> Note: **Condition TAGS_BPP_COLLECT_ERROR** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_COLLECT_ERROR_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_COLLECT_ERROR",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_BPP_COLLECT_VALID_TAGS,
                                    TAGS_BPP_COLLECT_SUCCESS,
                                    TAGS_BPP_COLLECT_ERROR,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del TAGS_BPP_COLLECT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BPP_COLLECT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code","valid":["success","error"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            PAYMENT_TAGS_VALID_TAGS,
                            TAGS_BPP_TERMS,
                            TAGS_BPP_COLLECT,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_PAYMENT_TAGS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_PAYMENT_TAGS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_PAYMENT_TAGS","_RETURN_":[{"_NAME_":"PAYMENT_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[*].code","valid":["bpp_terms","bpp_collect"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code","valid":["success","error"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}]}
                """
                    }}] + sub_results

                def ORDER_OFFERS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_OFFERS_obj in scope:
                        ORDER_OFFERS_obj["_EXTERNAL"] = input_data["external_data"]

                        def OFFERS_DESCRIPTOR_CODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_DESCRIPTOR_CODE_obj in scope:
                                OFFERS_DESCRIPTOR_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_DESCRIPTOR_CODE_obj, "$.message.order.offers[*].descriptor.code")
                                var_enum = ["discount","buyXgetY","freebie","slab","combo"]

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
                                        "description": r"""- **condition OFFERS_DESCRIPTOR_CODE**: every element of $.message.order.offers[*].descriptor.code must be in ["discount", "buyXgetY", "freebie", "slab", "combo"]

                        	> Note: **Condition OFFERS_DESCRIPTOR_CODE** can be skipped if the following conditions are met:
                        	>
                        	> - **condition B**: $.message.order.offers[*].descriptor.code must **not** be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"}
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
                        {"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        test_functions = [
                            OFFERS_DESCRIPTOR_CODE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_OFFERS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_OFFERS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"}]}
                """
                    }}] + sub_results

                def ORDER_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_TAGS_obj in scope:
                        ORDER_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BAP_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_TERMS_obj in scope:
                                TAGS_BAP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_BPP_TERMS_VALID_TAGS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_VALID_TAGS_obj in scope:
                                        TAGS_BPP_TERMS_VALID_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_VALID_TAGS_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code")
                                        valid = ["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, valid)

                                        if not validate:
                                            del TAGS_BPP_TERMS_VALID_TAGS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_VALID_TAGS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""- **condition TAGS_BPP_TERMS_VALID_TAGS**: every element of $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must be in ["max_liability_cap", "max_liability", "mandatory_arbitration", "court_jurisdiction", "delay_interest", "np_type", "tax_number", "provider_tax_number", "accept_bap_terms"]

                                	> Note: **Condition TAGS_BPP_TERMS_VALID_TAGS** can be skipped if the following conditions are met:
                                	>
                                	> - **condition B**: $.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code must **not** be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_VALID_TAGS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_VALID_TAGS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_BPP_TERMS_VALID_TAGS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del TAGS_BAP_TERMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_TERMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_BAP_TERMS,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_TAGS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_TAGS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]}]}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_PROVIDER,
                    ORDER_ITEMS,
                    ORDER_ITEMS_ADDITIONAL_TAGS,
                    ORDER_BILLING,
                    ORDER_FULFILLMENTS,
                    ORDER_FULFILLMENTS_ADDITIONAL_TAGS,
                    ORDER_QUOTE,
                    ORDER_QUOTE_ADDITIONAL_TAGS,
                    ORDER_PAYMENT,
                    ORDER_PAYMENT_TAGS,
                    ORDER_OFFERS,
                    ORDER_TAGS,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del ON_INIT_ORDER_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_INIT_ORDER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_INIT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees"],"_RETURN_":"attr all in valid"}]}]},{"_NAME_":"ORDER_ITEMS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees","rto_action"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code","valid":["id"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code","valid":["return_to_origin"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_VALID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[*].code","valid":["order_details"],"_RETURN_":"attr all in valid"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code","valid":["weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"TAGS_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["finance_terms","np_fees","quote"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code","valid":["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code","valid":["id","channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","_CONTINUE_":"!(attr are present)","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_PAYMENT_TAGS","_RETURN_":[{"_NAME_":"PAYMENT_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[*].code","valid":["bpp_terms","bpp_collect"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code","valid":["success","error"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]}]}]}
        """
            }}] + sub_results

        test_functions = [
            ON_INIT_CONTEXT,
            ON_INIT_ORDER,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_init_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_init_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_init_validations","_RETURN_":[{"_NAME_":"ON_INIT_CONTEXT","_DESCRIPTION_":"Validate on_init context","action":["on_init"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"REQUIRED_CONTEXT_CODE_14","attr":"$.context.city","reg":["^(std:\\\\d{3,5}|\\\\*)$"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bpp_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bpp_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET10"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}]}]},{"_NAME_":"ON_INIT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees"],"_RETURN_":"attr all in valid"}]}]},{"_NAME_":"ORDER_ITEMS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[*].code","valid":["np_fees","rto_action"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[*].code","valid":["id"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[*].code","valid":["return_to_origin"],"_RETURN_":"attr all in valid"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_VALID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[*].code","valid":["order_details"],"_RETURN_":"attr all in valid"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[*].code","valid":["weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["quote","np_fees","offer"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"TAGS_ITEM_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[*].code","valid":["finance_terms","np_fees","quote"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[*].code","valid":["subvention_type","subvention_amount","provider_tax_number","bank_account_no","ifsc_code"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"TAGS_NP_FEES_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[*].code","valid":["id","channel_margin_type","channel_margin_value"],"_RETURN_":"attr all in valid"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","_CONTINUE_":"!(attr are present)","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_PAYMENT_TAGS","_RETURN_":[{"_NAME_":"PAYMENT_TAGS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[*].code","valid":["bpp_terms","bpp_collect"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]},{"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[*].code","valid":["success","error"],"_RETURN_":"attr all in valid"},{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_VALID_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[*].code","valid":["max_liability_cap","max_liability","mandatory_arbitration","court_jurisdiction","delay_interest","np_type","tax_number","provider_tax_number","accept_bap_terms"],"_RETURN_":"attr all in valid"}]}]}]}]}
"""
    }}] + sub_results

def on_init(input_data):
    total_results = on_init_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "on_init_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
