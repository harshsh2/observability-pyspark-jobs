from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_select_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_select_validations_obj in scope:
        on_select_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def ON_SELECT_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_SELECT_CONTEXT_obj in scope:
                ON_SELECT_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["on_select"]

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
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_DOMAIN_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_DOMAIN",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_DOMAIN**

                        - $.context.domain must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_ACTION**

                        - $.context.action must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_COUNTRY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_COUNTRY**

                        - $.context.country must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_CITY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_CITY**

                        - $.context.city must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_select"]}
                        """
                                        }
                                    }]

                                # del CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CONTEXT_REQUIRED_CITY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_VERSION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_VERSION**

                        - $.context.core_version must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_BAP_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_BAP_ID**

                        - $.context.bap_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_BAP_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_BAP_URI**

                        - $.context.bap_uri must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BPP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BPP_ID_obj in scope:
                                CONTEXT_REQUIRED_BPP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                search = ["search"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BPP_ID_obj, "$.context.bap_id")
                                action = ["on_select"]

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
                                        "description": r"""#### **CONTEXT_REQUIRED_BPP_ID**

                        - $.context.bap_id must be present in the payload

                        > **Skip if:**
                        >
                        >     - ["on_select"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BPP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BPP_URI_obj in scope:
                                CONTEXT_REQUIRED_BPP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                search = ["search"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BPP_URI_obj, "$.context.bap_uri")
                                action = ["on_select"]

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
                                        "description": r"""#### **CONTEXT_REQUIRED_BPP_URI**

                        - $.context.bap_uri must be present in the payload

                        > **Skip if:**
                        >
                        >     - ["on_select"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_TRANSACTION_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_TRANSACTION_ID**

                        - $.context.transaction_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_MESSAGE_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_MESSAGE_ID**

                        - $.context.message_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                action = ["on_select"]

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REQUIRED_TIMESTAMP",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REQUIRED_TIMESTAMP**

                        - $.context.timestamp must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_select"]}
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
                                action = ["on_select"]

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
                                        "description": r"""#### **CONTEXT_REQUIRED_TTL**

                        - $.context.ttl must be present in the payload

                        > **Skip if:**
                        >
                        >     - all elements of ["on_select"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_select"]}
                        """
                            }}] + sub_results

                        test_functions = [
                            CONTEXT_REQUIRED_DOMAIN,
                            CONTEXT_REQUIRED_ACTION,
                            CONTEXT_REQUIRED_COUNTRY,
                            CONTEXT_REQUIRED_CITY,
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_select"]}]}
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
                                domain = ["ONDC:RET11"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_DOMAIN_obj, "$.context.domain")
                                action = ["on_select"]

                                validate = validation_utils["equal_to"](attr, domain)

                                if not validate:
                                    del CONTEXT_ENUM_DOMAIN_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_DOMAIN",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_DOMAIN**

                        - $.context.domain must equal ["ONDC:RET11"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["on_select"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["on_select"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_VERSION_obj in scope:
                                CONTEXT_ENUM_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                version = ["1.2.0","1.2.5"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_VERSION_obj, "$.context.core_version")
                                action = ["on_select"]

                                validate = validation_utils["all_in"](attr, version)

                                if not validate:
                                    del CONTEXT_ENUM_VERSION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_VERSION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_VERSION**

                        - All elements of $.context.core_version must be in ["1.2.0", "1.2.5"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_select"]}
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
                                action = ["on_select"]

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del CONTEXT_REG_BAP_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_REG_BAP_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_REG_BAP_URI**

                        - All elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_select"]}
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
                                action = ["on_select"]

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
                                        "description": r"""#### **CONTEXT_REG_BPP_URI**

                        - All elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]

                        > **Skip if:**
                        >
                        >     - ["on_select"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_select"]}
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
                                optional_vars = ["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"]
                                action = ["on_select"]

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
                                        "description": r"""#### **CONTEXT_REG_TTL**

                        - All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

                        > **Skip if:**
                        >
                        >     - all elements of ["on_select"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_select"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_select"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_select"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_select"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_select"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_select"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_select"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_select"]}]}
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

                # del ON_SELECT_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_SELECT_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_SELECT_CONTEXT","_DESCRIPTION_":"Validate on_select context","action":["on_select"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_select"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_select"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_select"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_select"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_select"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_select"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_select"]}]}]}
        """
            }}] + sub_results

        def ON_SELECT_ORDER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_SELECT_ORDER_obj in scope:
                ON_SELECT_ORDER_obj["_EXTERNAL"] = input_data["external_data"]

                def ORDER_PROVIDER(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PROVIDER_obj in scope:
                        ORDER_PROVIDER_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ORDER_PROVIDER_obj, "$.message.order.provider.id")

                        validate = validation_utils["are_present"](attr)

                        if not validate:
                            del ORDER_PROVIDER_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ORDER_PROVIDER",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ORDER_PROVIDER**

                - $.message.order.provider.id must be present in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ORDER_PROVIDER","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
                """
                                }
                            }]

                        # del ORDER_PROVIDER_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_PROVIDER",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_PROVIDER","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
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
                                        "description": r"""#### **ITEMS_ID**

                        - $.message.order.items[*].id must be present in the payload""",
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
                                        "description": r"""#### **ITEMS_FULFILLMENT_ID**

                        - $.message.order.items[*].fulfillment_id must be present in the payload""",
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

                        def ITEMS_PARENT_ITEM_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_PARENT_ITEM_ID_obj in scope:
                                ITEMS_PARENT_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_PARENT_ITEM_ID_obj, "$.message.order.items[*].parent_item_id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_PARENT_ITEM_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_PARENT_ITEM_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ITEMS_PARENT_ITEM_ID**

                        - $.message.order.items[*].parent_item_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ITEMS_PARENT_ITEM_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_PARENT_ITEM_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ITEMS_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_obj in scope:
                                ITEMS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def ITEMS_TAGS_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TAGS_TYPE_obj in scope:
                                        ITEMS_TAGS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_TAGS_TYPE_obj, "$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value")
                                        var_enum = ["item","customization"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del ITEMS_TAGS_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_TAGS_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **ITEMS_TAGS_TYPE**

                                - All elements of $.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value must be in ["item", "customization"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"}
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
                                {"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def ITEMS_TAGS_PARENT_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ITEMS_TAGS_PARENT_ID_obj in scope:
                                        ITEMS_TAGS_PARENT_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ITEMS_TAGS_PARENT_ID_obj, "$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ITEMS_TAGS_PARENT_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ITEMS_TAGS_PARENT_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **ITEMS_TAGS_PARENT_ID**

                                - $.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ITEMS_TAGS_PARENT_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ITEMS_TAGS_PARENT_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    ITEMS_TAGS_TYPE,
                                    ITEMS_TAGS_PARENT_ID,
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
                        {"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            ITEMS_ID,
                            ITEMS_FULFILLMENT_ID,
                            ITEMS_PARENT_ITEM_ID,
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
                {"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}
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
                                        "description": r"""#### **FULFILLMENTS_ID**

                        - $.message.order.fulfillments[*].id must be present in the payload""",
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

                        def FULFILLMENTS_PROVIDER_NAME(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_PROVIDER_NAME_obj in scope:
                                FULFILLMENTS_PROVIDER_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_PROVIDER_NAME_obj, "$.message.order.fulfillments[*]['@ondc/org/provider_name']")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_PROVIDER_NAME_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_PROVIDER_NAME",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_PROVIDER_NAME**

                        - $.message.order.fulfillments[*]['@ondc/org/provider_name'] must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_PROVIDER_NAME","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_PROVIDER_NAME_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_PROVIDER_NAME",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_PROVIDER_NAME","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TRACKING(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TRACKING_obj in scope:
                                FULFILLMENTS_TRACKING_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_TRACKING_obj, "$.message.order.fulfillments[*].tracking")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_TRACKING_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_TRACKING",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_TRACKING**

                        - $.message.order.fulfillments[*].tracking must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_TRACKING_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_TRACKING",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_CATEGORY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_CATEGORY_obj in scope:
                                FULFILLMENTS_CATEGORY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_CATEGORY_obj, "$.message.order.fulfillments[*]['@ondc/org/category']")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_CATEGORY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_CATEGORY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_CATEGORY**

                        - $.message.order.fulfillments[*]['@ondc/org/category'] must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_CATEGORY","attr":"$.message.order.fulfillments[*]['@ondc/org/category']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_CATEGORY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_CATEGORY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_CATEGORY","attr":"$.message.order.fulfillments[*]['@ondc/org/category']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TAT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TAT_obj in scope:
                                FULFILLMENTS_TAT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_TAT_obj, "$.message.order.fulfillments[*]['@ondc/org/TAT']")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_TAT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_TAT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_TAT**

                        - $.message.order.fulfillments[*]['@ondc/org/TAT'] must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TAT","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_TAT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_TAT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TAT","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_STATE_CODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_STATE_CODE_obj in scope:
                                FULFILLMENTS_STATE_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_STATE_CODE_obj, "$.message.order.fulfillments[*].state.descriptor.code")
                                var_enum = ["Serviceable","Non-serviceable"]

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del FULFILLMENTS_STATE_CODE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_STATE_CODE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_STATE_CODE**

                        - All elements of $.message.order.fulfillments[*].state.descriptor.code must be in ["Serviceable", "Non-serviceable"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_STATE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Serviceable","Non-serviceable"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_STATE_CODE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_STATE_CODE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_STATE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Serviceable","Non-serviceable"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TAGS_ORDER_DETAILS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TAGS_ORDER_DETAILS_obj in scope:
                                FULFILLMENTS_TAGS_ORDER_DETAILS_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT**

                                - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE**

                                - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT**

                                - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH**

                                - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH**

                                - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT_obj in scope:
                                        FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT**

                                - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT,
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE,
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT,
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH,
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH,
                                    FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT,
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
                        {"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILLMENTS_ID,
                            FULFILLMENTS_PROVIDER_NAME,
                            FULFILLMENTS_TRACKING,
                            FULFILLMENTS_CATEGORY,
                            FULFILLMENTS_TAT,
                            FULFILLMENTS_STATE_CODE,
                            FULFILLMENTS_TAGS_ORDER_DETAILS,
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
                {"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_PROVIDER_NAME","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_CATEGORY","attr":"$.message.order.fulfillments[*]['@ondc/org/category']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAT","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_STATE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Serviceable","Non-serviceable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]}
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
                                        "description": r"""#### **QUOTE_PRICE_CURRENCY**

                        - $.message.order.quote.price.currency must be present in the payload""",
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
                                        "description": r"""#### **QUOTE_PRICE_VALUE**

                        - $.message.order.quote.price.value must be present in the payload""",
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
                                                        "description": r"""#### **BREAKUP_ITEM_ID**

                                        - $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload""",
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
                                                        "description": r"""#### **BREAKUP_ITEM_QUANTITY_COUNT**

                                        - $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count is not in the payload""",
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
                                                        "description": r"""#### **BREAKUP_ITEM_TITLE**

                                        - $.message.order.quote.breakup[*].title must be present in the payload""",
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
                                                        "description": r"""#### **BREAKUP_ITEM_TITLE_TYPE**

                                        - All elements of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["item", "delivery", "packing", "tax", "misc", "discount", "offer"]""",
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
                                                        "description": r"""#### **BREAKUP_ITEM_PRICE_CURRENCY**

                                        - $.message.order.quote.breakup[*].price.currency must be present in the payload""",
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
                                                        "description": r"""#### **BREAKUP_ITEM_PRICE_VALUE**

                                        - $.message.order.quote.breakup[*].price.value must be present in the payload""",
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

                                        def BREAKUP_ITEM_TTL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_TTL_obj in scope:
                                                BREAKUP_ITEM_TTL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_TTL_obj, "$.message.order.quote.breakup[*].ttl")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del BREAKUP_ITEM_TTL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_TTL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **BREAKUP_ITEM_TTL**

                                        - $.message.order.quote.breakup[*].ttl must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.quote.breakup[*].ttl is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del BREAKUP_ITEM_TTL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "BREAKUP_ITEM_TTL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def BREAKUP_ITEM_ITEM(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for BREAKUP_ITEM_ITEM_obj in scope:
                                                BREAKUP_ITEM_ITEM_obj["_EXTERNAL"] = input_data["external_data"]

                                                def BREAKUP_ITEM_ITEM_PARENT_ITEM_ID(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for BREAKUP_ITEM_ITEM_PARENT_ITEM_ID_obj in scope:
                                                        BREAKUP_ITEM_ITEM_PARENT_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_PARENT_ITEM_ID_obj, "$.message.order.quote.breakup[*].item.parent_item_id")

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del BREAKUP_ITEM_ITEM_PARENT_ITEM_ID_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_PARENT_ITEM_ID",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_PARENT_ITEM_ID**

                                                - $.message.order.quote.breakup[*].item.parent_item_id must be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del BREAKUP_ITEM_ITEM_PARENT_ITEM_ID_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ITEM_PARENT_ITEM_ID",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT_obj in scope:
                                                        BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT_obj, "$.message.order.quote.breakup[*].item.quantity.available.count")
                                                        var_enum = ["99","0"]

                                                        validate = validation_utils["all_in"](attr, var_enum)

                                                        if not validate:
                                                            del BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT**

                                                - All elements of $.message.order.quote.breakup[*].item.quantity.available.count must be in ["99", "0"]""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                                }
                                                            }]

                                                        # del BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"}
                                                """
                                                    }}] + sub_results

                                                def BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT_obj in scope:
                                                        BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT_obj, "$.message.order.quote.breakup[*].item.quantity.maximum.count")

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT**

                                                - $.message.order.quote.breakup[*].item.quantity.maximum.count must be present in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

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
                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_PRICE_CURRENCY**

                                                - $.message.order.quote.breakup[*].item.price.currency must be present in the payload""",
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
                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_PRICE_VALUE**

                                                - $.message.order.quote.breakup[*].item.price.value must be present in the payload""",
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

                                                        def BREAKUP_ITEM_ITEM_TAGS_TYPE(input_data):
                                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                            sub_results = []
                                                            valid = True

                                                            for BREAKUP_ITEM_ITEM_TAGS_TYPE_obj in scope:
                                                                BREAKUP_ITEM_ITEM_TAGS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value")
                                                                var_enum = ["item","customization"]

                                                                validate = validation_utils["all_in"](attr, var_enum)

                                                                if not validate:
                                                                    del BREAKUP_ITEM_ITEM_TAGS_TYPE_obj["_EXTERNAL"]
                                                                    return [{
                                                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TYPE",
                                                                        "valid": False,
                                                                        "code": 30000,
                                                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TYPE**

                                                        - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value must be in ["item", "customization"]""",
                                                                        "_debug_info": {
                                                                            "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"}
                                                        """
                                                                        }
                                                                    }]

                                                                # del BREAKUP_ITEM_ITEM_TAGS_TYPE_obj["_EXTERNAL"]

                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TYPE",
                                                                "valid": valid,
                                                                "code": 200 if valid else 30000, 
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"}
                                                        """
                                                            }}] + sub_results

                                                        def BREAKUP_ITEM_ITEM_TAGS_PARENT_ID(input_data):
                                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                            sub_results = []
                                                            valid = True

                                                            for BREAKUP_ITEM_ITEM_TAGS_PARENT_ID_obj in scope:
                                                                BREAKUP_ITEM_ITEM_TAGS_PARENT_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_PARENT_ID_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value")

                                                                skip_check = not (validation_utils["are_present"](attr))
                                                                if skip_check:
                                                                    continue

                                                                validate = validation_utils["are_present"](attr)

                                                                if not validate:
                                                                    del BREAKUP_ITEM_ITEM_TAGS_PARENT_ID_obj["_EXTERNAL"]
                                                                    return [{
                                                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_PARENT_ID",
                                                                        "valid": False,
                                                                        "code": 30000,
                                                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_PARENT_ID**

                                                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value must be present in the payload

                                                        > **Skip if:**
                                                        >
                                                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value is not in the payload""",
                                                                        "_debug_info": {
                                                                            "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                                        """
                                                                        }
                                                                    }]

                                                                # del BREAKUP_ITEM_ITEM_TAGS_PARENT_ID_obj["_EXTERNAL"]

                                                            return [{
                                                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_PARENT_ID",
                                                                "valid": valid,
                                                                "code": 200 if valid else 30000, 
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE**

                                                                - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value must be in ["fulfillment", "order", "item"]

                                                                > **Skip if:**
                                                                >
                                                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value is not in the payload""",
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
                                                                                "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE**

                                                                - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value must be in ["delivery", "packaging", "misc"]

                                                                > **Skip if:**
                                                                >
                                                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value is not in the payload""",
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
                                                            BREAKUP_ITEM_ITEM_TAGS_TYPE,
                                                            BREAKUP_ITEM_ITEM_TAGS_PARENT_ID,
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
                                                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    BREAKUP_ITEM_ITEM_PARENT_ITEM_ID,
                                                    BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT,
                                                    BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT,
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
                                        {"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            BREAKUP_ITEM_ID,
                                            BREAKUP_ITEM_QUANTITY_COUNT,
                                            BREAKUP_ITEM_TITLE,
                                            BREAKUP_ITEM_TITLE_TYPE,
                                            BREAKUP_ITEM_PRICE_CURRENCY,
                                            BREAKUP_ITEM_PRICE_VALUE,
                                            BREAKUP_ITEM_TTL,
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
                                {"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}
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
                        {"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            QUOTE_PRICE_CURRENCY,
                            QUOTE_PRICE_VALUE,
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
                {"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]}
                """
                    }}] + sub_results

                def BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_obj in scope:
                        BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_obj["_EXTERNAL"] = input_data["external_data"]

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID**

                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value")
                                var_enum = ["percent"]

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
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE**

                        - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value must be in ["percent"]

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"}
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
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE**

                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE,
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
                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_obj in scope:
                        BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_obj["_EXTERNAL"] = input_data["external_data"]

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID**

                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value")
                                var_enum = ["delivery","discount"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE**

                        - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value must be in ["delivery", "discount"]

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value","var_enum":["delivery","discount"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value","var_enum":["delivery","discount"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value")
                                var_enum = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO**

                        - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value")
                                var_enum = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE**

                        - All elements of $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID**

                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE**

                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT_obj in scope:
                                BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT**

                        - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE,
                            BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_obj["_EXTERNAL"]

                    return [{
                        "test_name": "BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value","var_enum":["delivery","discount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ERROR(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ERROR_obj in scope:
                        ERROR_obj["_EXTERNAL"] = input_data["external_data"]

                        def ERROR_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ERROR_TYPE_obj in scope:
                                ERROR_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ERROR_TYPE_obj, "$.error.type")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ERROR_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ERROR_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ERROR_TYPE**

                        - $.error.type must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.error.type is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ERROR_TYPE","attr":"$.error.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ERROR_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ERROR_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ERROR_TYPE","attr":"$.error.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ERROR_CODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ERROR_CODE_obj in scope:
                                ERROR_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ERROR_CODE_obj, "$.error.code")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ERROR_CODE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ERROR_CODE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ERROR_CODE**

                        - $.error.code must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.error.code is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ERROR_CODE","attr":"$.error.code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ERROR_CODE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ERROR_CODE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ERROR_CODE","attr":"$.error.code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ERROR_MESSAGE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ERROR_MESSAGE_obj in scope:
                                ERROR_MESSAGE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ERROR_MESSAGE_obj, "$.error.message")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ERROR_MESSAGE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ERROR_MESSAGE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ERROR_MESSAGE**

                        - $.error.message must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.error.message is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ERROR_MESSAGE","attr":"$.error.message","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ERROR_MESSAGE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ERROR_MESSAGE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ERROR_MESSAGE","attr":"$.error.message","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            ERROR_TYPE,
                            ERROR_CODE,
                            ERROR_MESSAGE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ERROR_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ERROR",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ERROR","_RETURN_":[{"_NAME_":"ERROR_TYPE","attr":"$.error.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ERROR_CODE","attr":"$.error.code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ERROR_MESSAGE","attr":"$.error.message","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_PROVIDER,
                    ORDER_ITEMS,
                    ORDER_FULFILLMENTS,
                    ORDER_QUOTE,
                    BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES,
                    BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER,
                    ERROR,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del ON_SELECT_ORDER_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_SELECT_ORDER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_SELECT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_PROVIDER_NAME","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_CATEGORY","attr":"$.message.order.fulfillments[*]['@ondc/org/category']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAT","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_STATE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Serviceable","Non-serviceable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value","var_enum":["delivery","discount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ERROR","_RETURN_":[{"_NAME_":"ERROR_TYPE","attr":"$.error.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ERROR_CODE","attr":"$.error.code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ERROR_MESSAGE","attr":"$.error.message","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}
        """
            }}] + sub_results

        test_functions = [
            ON_SELECT_CONTEXT,
            ON_SELECT_ORDER,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_select_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_select_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_select_validations","_RETURN_":[{"_NAME_":"ON_SELECT_CONTEXT","_DESCRIPTION_":"Validate on_select context","action":["on_select"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_select"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_select"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_select"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_select"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_select"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_select"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_select"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_select"]}]}]},{"_NAME_":"ON_SELECT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_PROVIDER_NAME","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_CATEGORY","attr":"$.message.order.fulfillments[*]['@ondc/org/category']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAT","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_STATE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Serviceable","Non-serviceable"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='type')].value","var_enum":["delivery","discount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_AUTO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='auto')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ADDITIVE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='additive')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_value')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_OFFER_ITEM_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='offer')].list[?(@.code=='item_count')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ERROR","_RETURN_":[{"_NAME_":"ERROR_TYPE","attr":"$.error.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ERROR_CODE","attr":"$.error.code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ERROR_MESSAGE","attr":"$.error.message","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}]}
"""
    }}] + sub_results

def on_select(input_data):
    total_results = on_select_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "on_select_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
