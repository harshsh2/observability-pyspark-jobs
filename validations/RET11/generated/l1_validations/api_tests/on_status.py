from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_status_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_status_validations_obj in scope:
        on_status_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def ON_STATUS_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_STATUS_CONTEXT_obj in scope:
                ON_STATUS_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["on_status"]

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
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]}
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
                                action = ["on_status"]

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
                        >     - ["on_status"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_status"]}
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
                                action = ["on_status"]

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
                        >     - ["on_status"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_status"]}
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
                                action = ["on_status"]

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
                        >     - all elements of ["on_status"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_status"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_status"]}]}
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
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_status"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["on_status"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_status"]}
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
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_status"]}
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
                                action = ["on_status"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_status"]}
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
                                action = ["on_status"]

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
                        >     - ["on_status"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_status"]}
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
                                action = ["on_status"]

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
                        >     - all elements of ["on_status"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_status"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_status"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_status"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_status"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_status"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_status"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_status"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_status"]}]}
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

                # del ON_STATUS_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_STATUS_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_STATUS_CONTEXT","_DESCRIPTION_":"Validate on_status context","action":["on_status"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_status"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_status"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_status"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_status"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_status"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_status"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_status"]}]}]}
        """
            }}] + sub_results

        def ON_STATUS_ORDER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for ON_STATUS_ORDER_obj in scope:
                ON_STATUS_ORDER_obj["_EXTERNAL"] = input_data["external_data"]

                def ORDER_ID(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_ID_obj in scope:
                        ORDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ORDER_ID_obj, "$.message.order.id")
                        pattern = ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]

                        validate = (validation_utils["are_present"](attr)) and (validation_utils["follow_regex"](attr, pattern))

                        if not validate:
                            del ORDER_ID_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ORDER_ID",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ORDER_ID**

                **All of the following must be true:**
                  - $.message.order.id must be present in the payload
                  - All elements of $.message.order.id must follow every regex in ["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"]""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ORDER_ID","attr":"$.message.order.id","pattern":["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"],"_RETURN_":"attr are present && attr follow regex pattern"}
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
                {"_NAME_":"ORDER_ID","attr":"$.message.order.id","pattern":["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"],"_RETURN_":"attr are present && attr follow regex pattern"}
                """
                    }}] + sub_results

                def ORDER_STATE(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_STATE_obj in scope:
                        ORDER_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ORDER_STATE_obj, "$.message.order.state")
                        var_enum = ["Created","Accepted","In-progress","Completed","Cancelled"]

                        validate = validation_utils["all_in"](attr, var_enum)

                        if not validate:
                            del ORDER_STATE_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ORDER_STATE",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ORDER_STATE**

                - All elements of $.message.order.state must be in ["Created", "Accepted", "In-progress", "Completed", "Cancelled"]""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ORDER_STATE","attr":"$.message.order.state","var_enum":["Created","Accepted","In-progress","Completed","Cancelled"],"_RETURN_":"attr all in var_enum"}
                """
                                }
                            }]

                        # del ORDER_STATE_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_STATE",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_STATE","attr":"$.message.order.state","var_enum":["Created","Accepted","In-progress","Completed","Cancelled"],"_RETURN_":"attr all in var_enum"}
                """
                    }}] + sub_results

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
                                        "description": r"""#### **ORDER_PROVIDER_ID**

                        - $.message.order.provider.id must be present in the payload""",
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
                                        "description": r"""#### **ORDER_PROVIDER_LOCATIONS_ID**

                        - $.message.order.provider.locations[*].id must be present in the payload""",
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

                def ORDER_CANCELLATION(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_CANCELLATION_obj in scope:
                        ORDER_CANCELLATION_obj["_EXTERNAL"] = input_data["external_data"]

                        def CANCELLATION_CANCELLED_BY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CANCELLATION_CANCELLED_BY_obj in scope:
                                CANCELLATION_CANCELLED_BY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CANCELLATION_CANCELLED_BY_obj, "$.message.order.cancellation.cancelled_by")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del CANCELLATION_CANCELLED_BY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CANCELLATION_CANCELLED_BY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CANCELLATION_CANCELLED_BY**

                        - $.message.order.cancellation.cancelled_by must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.cancellation.cancelled_by is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CANCELLATION_CANCELLED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.cancelled_by","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del CANCELLATION_CANCELLED_BY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CANCELLATION_CANCELLED_BY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CANCELLATION_CANCELLED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.cancelled_by","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def CANCELLATION_REASON(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CANCELLATION_REASON_obj in scope:
                                CANCELLATION_REASON_obj["_EXTERNAL"] = input_data["external_data"]

                                def CANCELLATION_REASON_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for CANCELLATION_REASON_ID_obj in scope:
                                        CANCELLATION_REASON_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](CANCELLATION_REASON_ID_obj, "$.message.order.cancellation.reason.id")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del CANCELLATION_REASON_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "CANCELLATION_REASON_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **CANCELLATION_REASON_ID**

                                - $.message.order.cancellation.reason.id must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.cancellation.reason.id is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"CANCELLATION_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.id","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del CANCELLATION_REASON_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "CANCELLATION_REASON_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"CANCELLATION_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.id","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def CANCELLATION_REASON_STATE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for CANCELLATION_REASON_STATE_obj in scope:
                                        CANCELLATION_REASON_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](CANCELLATION_REASON_STATE_obj, "$.message.order.cancellation.reason.state")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del CANCELLATION_REASON_STATE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "CANCELLATION_REASON_STATE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **CANCELLATION_REASON_STATE**

                                - $.message.order.cancellation.reason.state must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.cancellation.reason.state is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"CANCELLATION_REASON_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.state","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del CANCELLATION_REASON_STATE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "CANCELLATION_REASON_STATE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"CANCELLATION_REASON_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.state","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    CANCELLATION_REASON_ID,
                                    CANCELLATION_REASON_STATE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del CANCELLATION_REASON_obj["_EXTERNAL"]

                            return [{
                                "test_name": "CANCELLATION_REASON",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"CANCELLATION_REASON","_RETURN_":[{"_NAME_":"CANCELLATION_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.id","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.state","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            CANCELLATION_CANCELLED_BY,
                            CANCELLATION_REASON,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_CANCELLATION_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_CANCELLATION",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_CANCELLATION","_RETURN_":[{"_NAME_":"CANCELLATION_CANCELLED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.cancelled_by","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON","_RETURN_":[{"_NAME_":"CANCELLATION_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.id","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.state","_RETURN_":"attr are present"}]}]}
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

                        def ITEMS_PARENT_ITEM_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_PARENT_ITEM_ID_obj in scope:
                                ITEMS_PARENT_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_PARENT_ITEM_ID_obj, "$.message.order.items[*].parent_item_id")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_PARENT_ITEM_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_PARENT_ITEM_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ITEMS_PARENT_ITEM_ID**

                        - $.message.order.items[*].parent_item_id must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.items[*].parent_item_id is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                        {"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                                        "description": r"""#### **ITEMS_QUANTITY_COUNT**

                        - $.message.order.items[*].quantity.count must be present in the payload""",
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
                                {"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
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
                                {"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
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
                        {"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def ITEMS_TAGS_NP_FEES(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_TAGS_NP_FEES_obj in scope:
                                ITEMS_TAGS_NP_FEES_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_TAGS_NP_FEES_obj, "$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_TAGS_NP_FEES_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_TAGS_NP_FEES",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ITEMS_TAGS_NP_FEES**

                        - $.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ITEMS_TAGS_NP_FEES_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_TAGS_NP_FEES",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            ITEMS_ID,
                            ITEMS_PARENT_ITEM_ID,
                            ITEMS_FULFILLMENT_ID,
                            ITEMS_QUANTITY_COUNT,
                            ITEMS_TAGS,
                            ITEMS_TAGS_NP_FEES,
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
                {"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_BILLING(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_BILLING_obj in scope:
                        ORDER_BILLING_obj["_EXTERNAL"] = input_data["external_data"]

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
                                        "description": r"""#### **BILLING_NAME**

                        - $.message.order.billing.name must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_NAME**

                                - $.message.order.billing.address.name must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_BUILDING**

                                - $.message.order.billing.address.building must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_LOCALITY**

                                - $.message.order.billing.address.locality must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_CITY**

                                - $.message.order.billing.address.city must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_STATE**

                                - $.message.order.billing.address.state must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_COUNTRY**

                                - $.message.order.billing.address.country must be present in the payload""",
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
                                                "description": r"""#### **BILLING_ADDRESS_AREA_CODE**

                                - $.message.order.billing.address.area_code must be present in the payload""",
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
                                        "description": r"""#### **BILLING_PHONE**

                        - $.message.order.billing.phone must be present in the payload""",
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

                        def BILLING_EMAIL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for BILLING_EMAIL_obj in scope:
                                BILLING_EMAIL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](BILLING_EMAIL_obj, "$.message.order.billing.email")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del BILLING_EMAIL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "BILLING_EMAIL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **BILLING_EMAIL**

                        - $.message.order.billing.email must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.billing.email is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del BILLING_EMAIL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "BILLING_EMAIL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                                        "description": r"""#### **BILLING_CREATED_AT**

                        - $.message.order.billing.created_at must be present in the payload""",
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
                                        "description": r"""#### **BILLING_UPDATED_AT**

                        - $.message.order.billing.updated_at must be present in the payload""",
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
                            BILLING_NAME,
                            BILLING_ADDRESS,
                            BILLING_PHONE,
                            BILLING_EMAIL,
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
                {"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]}
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

                        def FULFILLMENTS_STATE_DESCRIPTOR_CODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_STATE_DESCRIPTOR_CODE_obj in scope:
                                FULFILLMENTS_STATE_DESCRIPTOR_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_STATE_DESCRIPTOR_CODE_obj, "$.message.order.fulfillments[*].state.descriptor.code")
                                var_enum = ["Pending","Packed","Agent-assigned","At-pickup","At-delivery","Order-picked-up","Out-for-delivery","Order-delivered","Cancelled","RTO-Initiated","RTO-Disposed","RTO-Delivered"]

                                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                if not validate:
                                    del FULFILLMENTS_STATE_DESCRIPTOR_CODE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_STATE_DESCRIPTOR_CODE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_STATE_DESCRIPTOR_CODE**

                        **All of the following must be true:**
                          - $.message.order.fulfillments[*].state.descriptor.code must be present in the payload
                          - All elements of $.message.order.fulfillments[*].state.descriptor.code must be in ["Pending", "Packed", "Agent-assigned", "At-pickup", "At-delivery", "Order-picked-up", "Out-for-delivery", "Order-delivered", "Cancelled", "RTO-Initiated", "RTO-Disposed", "RTO-Delivered"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_STATE_DESCRIPTOR_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Pending","Packed","Agent-assigned","At-pickup","At-delivery","Order-picked-up","Out-for-delivery","Order-delivered","Cancelled","RTO-Initiated","RTO-Disposed","RTO-Delivered"],"_RETURN_":"attr are present && attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_STATE_DESCRIPTOR_CODE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_STATE_DESCRIPTOR_CODE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_STATE_DESCRIPTOR_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Pending","Packed","Agent-assigned","At-pickup","At-delivery","Order-picked-up","Out-for-delivery","Order-delivered","Cancelled","RTO-Initiated","RTO-Disposed","RTO-Delivered"],"_RETURN_":"attr are present && attr all in var_enum"}
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
                                        "description": r"""#### **FULFILLMENTS_TYPE**

                        - $.message.order.fulfillments[*].type must be present in the payload""",
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

                        def FULFILLMENTS_ONDC_ORG_PROVIDER_NAME(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_ONDC_ORG_PROVIDER_NAME_obj in scope:
                                FULFILLMENTS_ONDC_ORG_PROVIDER_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_ONDC_ORG_PROVIDER_NAME_obj, "$.message.order.fulfillments[*]['@ondc/org/provider_name']")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_ONDC_ORG_PROVIDER_NAME_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_ONDC_ORG_PROVIDER_NAME",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_ONDC_ORG_PROVIDER_NAME**

                        - $.message.order.fulfillments[*]['@ondc/org/provider_name'] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.fulfillments[*]['@ondc/org/provider_name'] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_ONDC_ORG_PROVIDER_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_ONDC_ORG_PROVIDER_NAME_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_ONDC_ORG_PROVIDER_NAME",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_ONDC_ORG_PROVIDER_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TRACKING(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TRACKING_obj in scope:
                                FULFILLMENTS_TRACKING_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_TRACKING_obj, "$.message.order.fulfillments[*].tracking")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_TRACKING_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_TRACKING",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_TRACKING**

                        - $.message.order.fulfillments[*].tracking must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.fulfillments[*].tracking is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TRACKING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}
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
                        {"_NAME_":"FULFILLMENTS_TRACKING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_ONDC_ORG_TAT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_ONDC_ORG_TAT_obj in scope:
                                FULFILLMENTS_ONDC_ORG_TAT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENTS_ONDC_ORG_TAT_obj, "$.message.order.fulfillments[*]['@ondc/org/TAT']")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENTS_ONDC_ORG_TAT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENTS_ONDC_ORG_TAT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENTS_ONDC_ORG_TAT**

                        - $.message.order.fulfillments[*]['@ondc/org/TAT'] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.fulfillments[*]['@ondc/org/TAT'] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_ONDC_ORG_TAT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENTS_ONDC_ORG_TAT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_ONDC_ORG_TAT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_ONDC_ORG_TAT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_START(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_START_obj in scope:
                                FULFILLMENTS_START_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_START_LOCATION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_START_LOCATION_obj in scope:
                                        FULFILLMENTS_START_LOCATION_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME_obj in scope:
                                                FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME_obj, "$.message.order.fulfillments[*].start.location.descriptor.name")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME**

                                        - $.message.order.fulfillments[*].start.location.descriptor.name must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.location.descriptor.name is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_LOCATION_GPS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_LOCATION_GPS_obj in scope:
                                                FULFILLMENTS_START_LOCATION_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_LOCATION_GPS_obj, "$.message.order.fulfillments[*].start.location.gps")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_LOCATION_GPS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_LOCATION_GPS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_LOCATION_GPS**

                                        - $.message.order.fulfillments[*].start.location.gps must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.location.gps is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_LOCATION_GPS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_LOCATION_GPS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_LOCATION_ADDRESS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_LOCATION_ADDRESS_obj in scope:
                                                FULFILLMENTS_START_LOCATION_ADDRESS_obj["_EXTERNAL"] = input_data["external_data"]

                                                def FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY_obj in scope:
                                                        FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY_obj, "$.message.order.fulfillments[*].start.location.address.locality")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY**

                                                - $.message.order.fulfillments[*].start.location.address.locality must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].start.location.address.locality is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_START_LOCATION_ADDRESS_CITY(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_START_LOCATION_ADDRESS_CITY_obj in scope:
                                                        FULFILLMENTS_START_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_START_LOCATION_ADDRESS_CITY_obj, "$.message.order.fulfillments[*].start.location.address.city")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_START_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_CITY",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_START_LOCATION_ADDRESS_CITY**

                                                - $.message.order.fulfillments[*].start.location.address.city must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].start.location.address.city is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del FULFILLMENTS_START_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_CITY",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE_obj in scope:
                                                        FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE_obj, "$.message.order.fulfillments[*].start.location.address.area_code")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE**

                                                - $.message.order.fulfillments[*].start.location.address.area_code must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].start.location.address.area_code is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_START_LOCATION_ADDRESS_STATE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_START_LOCATION_ADDRESS_STATE_obj in scope:
                                                        FULFILLMENTS_START_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_START_LOCATION_ADDRESS_STATE_obj, "$.message.order.fulfillments[*].start.location.address.state")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_START_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_STATE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_START_LOCATION_ADDRESS_STATE**

                                                - $.message.order.fulfillments[*].start.location.address.state must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].start.location.address.state is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}
                                                """
                                                                }
                                                            }]

                                                        # del FULFILLMENTS_START_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"]

                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS_STATE",
                                                        "valid": valid,
                                                        "code": 200 if valid else 30000, 
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY,
                                                    FULFILLMENTS_START_LOCATION_ADDRESS_CITY,
                                                    FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE,
                                                    FULFILLMENTS_START_LOCATION_ADDRESS_STATE,
                                                ]

                                                all_results = []
                                                for fn in test_functions:
                                                    sub_result = fn(input_data)
                                                    all_results.extend(sub_result)

                                                sub_results = all_results
                                                valid = all(r["valid"] for r in sub_results)

                                                # del FULFILLMENTS_START_LOCATION_ADDRESS_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_LOCATION_ADDRESS",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME,
                                            FULFILLMENTS_START_LOCATION_GPS,
                                            FULFILLMENTS_START_LOCATION_ADDRESS,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_START_LOCATION_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_START_LOCATION",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_START_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}]}]}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_START_TIME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_START_TIME_obj in scope:
                                        FULFILLMENTS_START_TIME_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_START_TIME_RANGE_START(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_TIME_RANGE_START_obj in scope:
                                                FULFILLMENTS_START_TIME_RANGE_START_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_TIME_RANGE_START_obj, "$.message.order.fulfillments[*].start.time.range.start")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_TIME_RANGE_START_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_TIME_RANGE_START",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_TIME_RANGE_START**

                                        - $.message.order.fulfillments[*].start.time.range.start must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.time.range.start is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_TIME_RANGE_START_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_TIME_RANGE_START",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_TIME_RANGE_END(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_TIME_RANGE_END_obj in scope:
                                                FULFILLMENTS_START_TIME_RANGE_END_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_TIME_RANGE_END_obj, "$.message.order.fulfillments[*].start.time.range.end")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_TIME_RANGE_END_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_TIME_RANGE_END",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_TIME_RANGE_END**

                                        - $.message.order.fulfillments[*].start.time.range.end must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.time.range.end is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_TIME_RANGE_END_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_TIME_RANGE_END",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_TIME_TIMESTAMP(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_TIME_TIMESTAMP_obj in scope:
                                                FULFILLMENTS_START_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_TIME_TIMESTAMP_obj, "$.message.order.fulfillments[*].start.time.timestamp")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_TIME_TIMESTAMP",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_TIME_TIMESTAMP**

                                        - $.message.order.fulfillments[*].start.time.timestamp must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.time.timestamp is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_TIME_TIMESTAMP_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_TIME_TIMESTAMP",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_START_TIME_RANGE_START,
                                            FULFILLMENTS_START_TIME_RANGE_END,
                                            FULFILLMENTS_START_TIME_TIMESTAMP,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_START_TIME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_START_TIME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_START_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_START_INSTRUCTIONS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_START_INSTRUCTIONS_obj in scope:
                                        FULFILLMENTS_START_INSTRUCTIONS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_START_INSTRUCTIONS_CODE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_INSTRUCTIONS_CODE_obj in scope:
                                                FULFILLMENTS_START_INSTRUCTIONS_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_INSTRUCTIONS_CODE_obj, "$.message.order.fulfillments[*].start.instructions.code")
                                                var_enum = ["1","2","3","4"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                                if not validate:
                                                    del FULFILLMENTS_START_INSTRUCTIONS_CODE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_INSTRUCTIONS_CODE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_INSTRUCTIONS_CODE**

                                        **All of the following must be true:**
                                          - $.message.order.fulfillments[*].start.instructions.code must be present in the payload
                                          - All elements of $.message.order.fulfillments[*].start.instructions.code must be in ["1", "2", "3", "4"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.instructions.code is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_INSTRUCTIONS_CODE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_INSTRUCTIONS_CODE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_INSTRUCTIONS_NAME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_INSTRUCTIONS_NAME_obj in scope:
                                                FULFILLMENTS_START_INSTRUCTIONS_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_INSTRUCTIONS_NAME_obj, "$.message.order.fulfillments[*].start.instructions.name")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_INSTRUCTIONS_NAME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_INSTRUCTIONS_NAME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_INSTRUCTIONS_NAME**

                                        - $.message.order.fulfillments[*].start.instructions.name must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.instructions.name is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_INSTRUCTIONS_NAME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_INSTRUCTIONS_NAME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC_obj in scope:
                                                FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC_obj, "$.message.order.fulfillments[*].start.instructions.short_desc")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC**

                                        - $.message.order.fulfillments[*].start.instructions.short_desc must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.instructions.short_desc is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC_obj in scope:
                                                FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC_obj, "$.message.order.fulfillments[*].start.instructions.long_desc")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC**

                                        - $.message.order.fulfillments[*].start.instructions.long_desc must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.instructions.long_desc is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj in scope:
                                                FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj, "$.message.order.fulfillments[*].start.instructions.additional_desc.content_type")
                                                var_enum = ["text/plain","text/html"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE**

                                        - All elements of $.message.order.fulfillments[*].start.instructions.additional_desc.content_type must be in ["text/plain", "text/html"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.instructions.additional_desc.content_type is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_START_INSTRUCTIONS_CODE,
                                            FULFILLMENTS_START_INSTRUCTIONS_NAME,
                                            FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC,
                                            FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC,
                                            FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_START_INSTRUCTIONS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_START_INSTRUCTIONS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_START_CONTACT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_START_CONTACT_obj in scope:
                                        FULFILLMENTS_START_CONTACT_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_START_CONTACT_PHONE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_CONTACT_PHONE_obj in scope:
                                                FULFILLMENTS_START_CONTACT_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_CONTACT_PHONE_obj, "$.message.order.fulfillments[*].start.contact.phone")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_CONTACT_PHONE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_CONTACT_PHONE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_CONTACT_PHONE**

                                        - $.message.order.fulfillments[*].start.contact.phone must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.contact.phone is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_CONTACT_PHONE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_CONTACT_PHONE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_START_CONTACT_EMAIL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_START_CONTACT_EMAIL_obj in scope:
                                                FULFILLMENTS_START_CONTACT_EMAIL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_START_CONTACT_EMAIL_obj, "$.message.order.fulfillments[*].start.contact.email")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_START_CONTACT_EMAIL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_START_CONTACT_EMAIL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_START_CONTACT_EMAIL**

                                        - $.message.order.fulfillments[*].start.contact.email must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].start.contact.email is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_START_CONTACT_EMAIL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_START_CONTACT_EMAIL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_START_CONTACT_PHONE,
                                            FULFILLMENTS_START_CONTACT_EMAIL,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_START_CONTACT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_START_CONTACT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_START_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_START_LOCATION,
                                    FULFILLMENTS_START_TIME,
                                    FULFILLMENTS_START_INSTRUCTIONS,
                                    FULFILLMENTS_START_CONTACT,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_START_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_START",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_START","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_START_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"FULFILLMENTS_START_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}]}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_END(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_END_obj in scope:
                                FULFILLMENTS_END_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_END_LOCATION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_LOCATION_obj in scope:
                                        FULFILLMENTS_END_LOCATION_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_END_LOCATION_GPS(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_LOCATION_GPS_obj in scope:
                                                FULFILLMENTS_END_LOCATION_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_GPS_obj, "$.message.order.fulfillments[*].end.location.gps")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_LOCATION_GPS_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_LOCATION_GPS",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_LOCATION_GPS**

                                        - $.message.order.fulfillments[*].end.location.gps must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.location.gps is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"}
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
                                        {"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"}
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

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_NAME_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_NAME",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_NAME**

                                                - $.message.order.fulfillments[*].end.location.address.name must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.name is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj in scope:
                                                        FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj, "$.message.order.fulfillments[*].end.location.address.building")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING**

                                                - $.message.order.fulfillments[*].end.location.address.building must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.building is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj in scope:
                                                        FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj, "$.message.order.fulfillments[*].end.location.address.locality")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY**

                                                - $.message.order.fulfillments[*].end.location.address.locality must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.locality is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj in scope:
                                                        FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj, "$.message.order.fulfillments[*].end.location.address.country")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY**

                                                - $.message.order.fulfillments[*].end.location.address.country must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.country is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_END_LOCATION_ADDRESS_CITY(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj in scope:
                                                        FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj, "$.message.order.fulfillments[*].end.location.address.city")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_CITY_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_CITY",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_CITY**

                                                - $.message.order.fulfillments[*].end.location.address.city must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.city is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj in scope:
                                                        FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj, "$.message.order.fulfillments[*].end.location.address.area_code")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE**

                                                - $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.area_code is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                def FULFILLMENTS_END_LOCATION_ADDRESS_STATE(input_data):
                                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                                    sub_results = []
                                                    valid = True

                                                    for FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj in scope:
                                                        FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj, "$.message.order.fulfillments[*].end.location.address.state")

                                                        skip_check = not (validation_utils["are_present"](attr))
                                                        if skip_check:
                                                            continue

                                                        validate = validation_utils["are_present"](attr)

                                                        if not validate:
                                                            del FULFILLMENTS_END_LOCATION_ADDRESS_STATE_obj["_EXTERNAL"]
                                                            return [{
                                                                "test_name": "FULFILLMENTS_END_LOCATION_ADDRESS_STATE",
                                                                "valid": False,
                                                                "code": 30000,
                                                                "description": r"""#### **FULFILLMENTS_END_LOCATION_ADDRESS_STATE**

                                                - $.message.order.fulfillments[*].end.location.address.state must be present in the payload

                                                > **Skip if:**
                                                >
                                                >     - $.message.order.fulfillments[*].end.location.address.state is not in the payload""",
                                                                "_debug_info": {
                                                                    "fed_config": r"""
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}
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
                                                {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}
                                                """
                                                    }}] + sub_results

                                                test_functions = [
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_NAME,
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING,
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY,
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY,
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_CITY,
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE,
                                                    FULFILLMENTS_END_LOCATION_ADDRESS_STATE,
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
                                        {"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}]}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_END_LOCATION_GPS,
                                            FULFILLMENTS_END_LOCATION_ADDRESS,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_END_LOCATION_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_LOCATION",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}]}]}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_TIME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_TIME_obj in scope:
                                        FULFILLMENTS_END_TIME_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_END_TIME_RANGE_START(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_TIME_RANGE_START_obj in scope:
                                                FULFILLMENTS_END_TIME_RANGE_START_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_TIME_RANGE_START_obj, "$.message.order.fulfillments[*].end.time.range.start")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_TIME_RANGE_START_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_TIME_RANGE_START",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_TIME_RANGE_START**

                                        - $.message.order.fulfillments[*].end.time.range.start must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.time.range.start is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_TIME_RANGE_START_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_TIME_RANGE_START",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_END_TIME_RANGE_END(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_TIME_RANGE_END_obj in scope:
                                                FULFILLMENTS_END_TIME_RANGE_END_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_TIME_RANGE_END_obj, "$.message.order.fulfillments[*].end.time.range.end")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_TIME_RANGE_END_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_TIME_RANGE_END",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_TIME_RANGE_END**

                                        - $.message.order.fulfillments[*].end.time.range.end must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.time.range.end is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_TIME_RANGE_END_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_TIME_RANGE_END",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_END_TIME_TIMESTAMP(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_TIME_TIMESTAMP_obj in scope:
                                                FULFILLMENTS_END_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_TIME_TIMESTAMP_obj, "$.message.order.fulfillments[*].end.time.timestamp")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_TIME_TIMESTAMP",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_TIME_TIMESTAMP**

                                        - $.message.order.fulfillments[*].end.time.timestamp must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.time.timestamp is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_TIME_TIMESTAMP_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_TIME_TIMESTAMP",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_END_TIME_RANGE_START,
                                            FULFILLMENTS_END_TIME_RANGE_END,
                                            FULFILLMENTS_END_TIME_TIMESTAMP,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_END_TIME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_TIME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_INSTRUCTIONS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_INSTRUCTIONS_obj in scope:
                                        FULFILLMENTS_END_INSTRUCTIONS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_END_INSTRUCTIONS_CODE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_INSTRUCTIONS_CODE_obj in scope:
                                                FULFILLMENTS_END_INSTRUCTIONS_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_INSTRUCTIONS_CODE_obj, "$.message.order.fulfillments[*].end.instructions.code")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_INSTRUCTIONS_CODE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_INSTRUCTIONS_CODE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_INSTRUCTIONS_CODE**

                                        - $.message.order.fulfillments[*].end.instructions.code must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.instructions.code is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_INSTRUCTIONS_CODE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_INSTRUCTIONS_CODE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_END_INSTRUCTIONS_NAME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_INSTRUCTIONS_NAME_obj in scope:
                                                FULFILLMENTS_END_INSTRUCTIONS_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_INSTRUCTIONS_NAME_obj, "$.message.order.fulfillments[*].end.instructions.name")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_INSTRUCTIONS_NAME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_INSTRUCTIONS_NAME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_INSTRUCTIONS_NAME**

                                        - $.message.order.fulfillments[*].end.instructions.name must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.instructions.name is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_INSTRUCTIONS_NAME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_INSTRUCTIONS_NAME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC_obj in scope:
                                                FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC_obj, "$.message.order.fulfillments[*].end.instructions.short_desc")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC**

                                        - $.message.order.fulfillments[*].end.instructions.short_desc must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.instructions.short_desc is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC_obj in scope:
                                                FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC_obj, "$.message.order.fulfillments[*].end.instructions.long_desc")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC**

                                        - $.message.order.fulfillments[*].end.instructions.long_desc must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.instructions.long_desc is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_END_INSTRUCTIONS_CODE,
                                            FULFILLMENTS_END_INSTRUCTIONS_NAME,
                                            FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC,
                                            FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_END_INSTRUCTIONS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_INSTRUCTIONS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_END_CONTACT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_CONTACT_obj in scope:
                                        FULFILLMENTS_END_CONTACT_obj["_EXTERNAL"] = input_data["external_data"]

                                        def FULFILLMENTS_END_CONTACT_PHONE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_CONTACT_PHONE_obj in scope:
                                                FULFILLMENTS_END_CONTACT_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_CONTACT_PHONE_obj, "$.message.order.fulfillments[*].end.contact.phone")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_CONTACT_PHONE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_CONTACT_PHONE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_CONTACT_PHONE**

                                        - $.message.order.fulfillments[*].end.contact.phone must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.contact.phone is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}
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
                                        {"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def FULFILLMENTS_END_CONTACT_EMAIL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for FULFILLMENTS_END_CONTACT_EMAIL_obj in scope:
                                                FULFILLMENTS_END_CONTACT_EMAIL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](FULFILLMENTS_END_CONTACT_EMAIL_obj, "$.message.order.fulfillments[*].end.contact.email")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del FULFILLMENTS_END_CONTACT_EMAIL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "FULFILLMENTS_END_CONTACT_EMAIL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **FULFILLMENTS_END_CONTACT_EMAIL**

                                        - $.message.order.fulfillments[*].end.contact.email must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].end.contact.email is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del FULFILLMENTS_END_CONTACT_EMAIL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "FULFILLMENTS_END_CONTACT_EMAIL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            FULFILLMENTS_END_CONTACT_PHONE,
                                            FULFILLMENTS_END_CONTACT_EMAIL,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del FULFILLMENTS_END_CONTACT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_CONTACT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_END_LOCATION,
                                    FULFILLMENTS_END_TIME,
                                    FULFILLMENTS_END_INSTRUCTIONS,
                                    FULFILLMENTS_END_CONTACT,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_END_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_END",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}]}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_AGENT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_AGENT_obj in scope:
                                FULFILLMENTS_AGENT_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_AGENT_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_AGENT_NAME_obj in scope:
                                        FULFILLMENTS_AGENT_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_AGENT_NAME_obj, "$.message.order.fulfillments[*].agent.name")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_AGENT_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_AGENT_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_AGENT_NAME**

                                - $.message.order.fulfillments[*].agent.name must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].agent.name is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_AGENT_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_AGENT_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_AGENT_PHONE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_AGENT_PHONE_obj in scope:
                                        FULFILLMENTS_AGENT_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_AGENT_PHONE_obj, "$.message.order.fulfillments[*].agent.phone")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_AGENT_PHONE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_AGENT_PHONE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_AGENT_PHONE**

                                - $.message.order.fulfillments[*].agent.phone must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].agent.phone is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.phone","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_AGENT_PHONE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_AGENT_PHONE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.phone","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_AGENT_NAME,
                                    FULFILLMENTS_AGENT_PHONE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_AGENT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_AGENT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_AGENT","_RETURN_":[{"_NAME_":"FULFILLMENTS_AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.phone","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_VEHICLE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_VEHICLE_obj in scope:
                                FULFILLMENTS_VEHICLE_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_VEHICLE_CATEGORY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_VEHICLE_CATEGORY_obj in scope:
                                        FULFILLMENTS_VEHICLE_CATEGORY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_VEHICLE_CATEGORY_obj, "$.message.order.fulfillments[*].vehicle.category")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_VEHICLE_CATEGORY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_VEHICLE_CATEGORY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_VEHICLE_CATEGORY**

                                - $.message.order.fulfillments[*].vehicle.category must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].vehicle.category is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_VEHICLE_CATEGORY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.category","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_VEHICLE_CATEGORY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_VEHICLE_CATEGORY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_VEHICLE_CATEGORY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.category","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_VEHICLE_SIZE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_VEHICLE_SIZE_obj in scope:
                                        FULFILLMENTS_VEHICLE_SIZE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_VEHICLE_SIZE_obj, "$.message.order.fulfillments[*].vehicle.size")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_VEHICLE_SIZE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_VEHICLE_SIZE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_VEHICLE_SIZE**

                                - $.message.order.fulfillments[*].vehicle.size must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].vehicle.size is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_VEHICLE_SIZE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.size","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_VEHICLE_SIZE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_VEHICLE_SIZE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_VEHICLE_SIZE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.size","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def FULFILLMENTS_VEHICLE_REGISTRATION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_VEHICLE_REGISTRATION_obj in scope:
                                        FULFILLMENTS_VEHICLE_REGISTRATION_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_VEHICLE_REGISTRATION_obj, "$.message.order.fulfillments[*].vehicle.registration")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_VEHICLE_REGISTRATION_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_VEHICLE_REGISTRATION",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_VEHICLE_REGISTRATION**

                                - $.message.order.fulfillments[*].vehicle.registration must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].vehicle.registration is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_VEHICLE_REGISTRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.registration","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_VEHICLE_REGISTRATION_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_VEHICLE_REGISTRATION",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_VEHICLE_REGISTRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.registration","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_VEHICLE_CATEGORY,
                                    FULFILLMENTS_VEHICLE_SIZE,
                                    FULFILLMENTS_VEHICLE_REGISTRATION,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_VEHICLE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_VEHICLE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_VEHICLE","_RETURN_":[{"_NAME_":"FULFILLMENTS_VEHICLE_CATEGORY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.category","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_SIZE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.size","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_REGISTRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.registration","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TAGS_obj in scope:
                                FULFILLMENTS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_STATE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_STATE_obj in scope:
                                        TAGS_STATE_obj["_EXTERNAL"] = input_data["external_data"]

                                        def STATE_READY_TO_SHIP(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for STATE_READY_TO_SHIP_obj in scope:
                                                STATE_READY_TO_SHIP_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](STATE_READY_TO_SHIP_obj, "$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del STATE_READY_TO_SHIP_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "STATE_READY_TO_SHIP",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **STATE_READY_TO_SHIP**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del STATE_READY_TO_SHIP_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "STATE_READY_TO_SHIP",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            STATE_READY_TO_SHIP,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_STATE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_STATE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_STATE","_RETURN_":[{"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_ROUTING(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_ROUTING_obj in scope:
                                        TAGS_ROUTING_obj["_EXTERNAL"] = input_data["external_data"]

                                        def ROUTING_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ROUTING_TYPE_obj in scope:
                                                ROUTING_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ROUTING_TYPE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ROUTING_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ROUTING_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ROUTING_TYPE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ROUTING_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ROUTING_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            ROUTING_TYPE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_ROUTING_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_ROUTING",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_ROUTING","_RETURN_":[{"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_TRACKING(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_TRACKING_obj in scope:
                                        TAGS_TRACKING_obj["_EXTERNAL"] = input_data["external_data"]

                                        def TRACKING_GPS_ENABLED(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TRACKING_GPS_ENABLED_obj in scope:
                                                TRACKING_GPS_ENABLED_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TRACKING_GPS_ENABLED_obj, "$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del TRACKING_GPS_ENABLED_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TRACKING_GPS_ENABLED",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **TRACKING_GPS_ENABLED**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del TRACKING_GPS_ENABLED_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TRACKING_GPS_ENABLED",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def TRACKING_URL_ENABLED(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TRACKING_URL_ENABLED_obj in scope:
                                                TRACKING_URL_ENABLED_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TRACKING_URL_ENABLED_obj, "$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del TRACKING_URL_ENABLED_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TRACKING_URL_ENABLED",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **TRACKING_URL_ENABLED**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del TRACKING_URL_ENABLED_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TRACKING_URL_ENABLED",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def TRACKING_URL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for TRACKING_URL_obj in scope:
                                                TRACKING_URL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](TRACKING_URL_obj, "$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value")
                                                reg = ["^https?://.*$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del TRACKING_URL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "TRACKING_URL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **TRACKING_URL**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del TRACKING_URL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "TRACKING_URL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            TRACKING_GPS_ENABLED,
                                            TRACKING_URL_ENABLED,
                                            TRACKING_URL,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_TRACKING_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_TRACKING",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]}
                                """
                                    }}] + sub_results

                                def TAGS_FULFILLMENT_DELAY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FULFILLMENT_DELAY_obj in scope:
                                        TAGS_FULFILLMENT_DELAY_obj["_EXTERNAL"] = input_data["external_data"]

                                        def DELAY_STATE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_STATE_obj in scope:
                                                DELAY_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_STATE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value")
                                                var_enum = ["Order-picked-up","Order-delivered"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del DELAY_STATE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DELAY_STATE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DELAY_STATE**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del DELAY_STATE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DELAY_STATE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def DELAY_REASON_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_REASON_ID_obj in scope:
                                                DELAY_REASON_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_REASON_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DELAY_REASON_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DELAY_REASON_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DELAY_REASON_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DELAY_REASON_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DELAY_REASON_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def DELAY_TIMESTAMP(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_TIMESTAMP_obj in scope:
                                                DELAY_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_TIMESTAMP_obj, "$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del DELAY_TIMESTAMP_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DELAY_TIMESTAMP",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DELAY_TIMESTAMP**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value must follow every regex in ["^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del DELAY_TIMESTAMP_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DELAY_TIMESTAMP",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            DELAY_STATE,
                                            DELAY_REASON_ID,
                                            DELAY_TIMESTAMP,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_FULFILLMENT_DELAY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FULFILLMENT_DELAY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}]}
                                """
                                    }}] + sub_results

                                def TAGS_ORDER_DETAILS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_ORDER_DETAILS_obj in scope:
                                        TAGS_ORDER_DETAILS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def ORDER_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_ID_obj in scope:
                                                ORDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value")

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
                                                        "description": r"""#### **ORDER_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
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
                                        {"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def ORDER_WEIGHT_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_WEIGHT_UNIT_obj in scope:
                                                ORDER_WEIGHT_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_WEIGHT_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ORDER_WEIGHT_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ORDER_WEIGHT_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ORDER_WEIGHT_UNIT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ORDER_WEIGHT_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ORDER_WEIGHT_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def ORDER_WEIGHT_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_WEIGHT_VALUE_obj in scope:
                                                ORDER_WEIGHT_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_WEIGHT_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ORDER_WEIGHT_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ORDER_WEIGHT_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ORDER_WEIGHT_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ORDER_WEIGHT_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ORDER_WEIGHT_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def ORDER_DIM_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_DIM_UNIT_obj in scope:
                                                ORDER_DIM_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_DIM_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ORDER_DIM_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ORDER_DIM_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ORDER_DIM_UNIT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ORDER_DIM_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ORDER_DIM_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def ORDER_LENGTH(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_LENGTH_obj in scope:
                                                ORDER_LENGTH_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_LENGTH_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ORDER_LENGTH_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ORDER_LENGTH",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ORDER_LENGTH**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ORDER_LENGTH_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ORDER_LENGTH",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def ORDER_BREADTH(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_BREADTH_obj in scope:
                                                ORDER_BREADTH_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_BREADTH_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ORDER_BREADTH_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ORDER_BREADTH",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ORDER_BREADTH**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ORDER_BREADTH_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ORDER_BREADTH",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def ORDER_HEIGHT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for ORDER_HEIGHT_obj in scope:
                                                ORDER_HEIGHT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](ORDER_HEIGHT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del ORDER_HEIGHT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "ORDER_HEIGHT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **ORDER_HEIGHT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del ORDER_HEIGHT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "ORDER_HEIGHT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            ORDER_ID,
                                            ORDER_WEIGHT_UNIT,
                                            ORDER_WEIGHT_VALUE,
                                            ORDER_DIM_UNIT,
                                            ORDER_LENGTH,
                                            ORDER_BREADTH,
                                            ORDER_HEIGHT,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_ORDER_DETAILS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_ORDER_DETAILS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_STATE,
                                    TAGS_ROUTING,
                                    TAGS_TRACKING,
                                    TAGS_FULFILLMENT_DELAY,
                                    TAGS_ORDER_DETAILS,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del FULFILLMENTS_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENTS_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_STATE","_RETURN_":[{"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_ROUTING","_RETURN_":[{"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILLMENTS_ID,
                            FULFILLMENTS_STATE_DESCRIPTOR_CODE,
                            FULFILLMENTS_TYPE,
                            FULFILLMENTS_ONDC_ORG_PROVIDER_NAME,
                            FULFILLMENTS_TRACKING,
                            FULFILLMENTS_ONDC_ORG_TAT,
                            FULFILLMENTS_START,
                            FULFILLMENTS_END,
                            FULFILLMENTS_AGENT,
                            FULFILLMENTS_VEHICLE,
                            FULFILLMENTS_TAGS,
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
                {"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_STATE_DESCRIPTOR_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Pending","Packed","Agent-assigned","At-pickup","At-delivery","Order-picked-up","Out-for-delivery","Order-delivered","Cancelled","RTO-Initiated","RTO-Disposed","RTO-Delivered"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_ONDC_ORG_PROVIDER_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TRACKING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_ONDC_ORG_TAT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_START_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"FULFILLMENTS_START_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_AGENT","_RETURN_":[{"_NAME_":"FULFILLMENTS_AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.phone","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_VEHICLE","_RETURN_":[{"_NAME_":"FULFILLMENTS_VEHICLE_CATEGORY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.category","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_SIZE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.size","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_REGISTRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.registration","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_STATE","_RETURN_":[{"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_ROUTING","_RETURN_":[{"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]}]}
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

                def ORDER_QUOTE_ADDITIONAL_PROPERTIES(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_QUOTE_ADDITIONAL_PROPERTIES_obj in scope:
                        ORDER_QUOTE_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"] = input_data["external_data"]

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
                                        "description": r"""#### **QUOTE_TTL**

                        - $.message.order.quote.ttl must be present in the payload""",
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

                        test_functions = [
                            QUOTE_TTL,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_QUOTE_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_QUOTE_ADDITIONAL_PROPERTIES",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_QUOTE_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}]}
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
                                        "description": r"""#### **PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE**

                        - All elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]""",
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
                                        "description": r"""#### **PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT**

                        **All of the following must be true:**
                          - $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload
                          - All elements of $.message.order.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]""",
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

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"}
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
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"}
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
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"}
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

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**

                                - All elements of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}
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
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].upi_address")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].upi_address must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].upi_address is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].bank_name")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].bank_name must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].bank_name is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].branch_name")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].branch_name must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].branch_name is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME,
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
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}]}
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
                {"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}]}]}
                """
                    }}] + sub_results

                def ORDER_PAYMENT_ADDITIONAL_PROPERTIES(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PAYMENT_ADDITIONAL_PROPERTIES_obj in scope:
                        ORDER_PAYMENT_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"] = input_data["external_data"]

                        def PAYMENT_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_URI_obj in scope:
                                PAYMENT_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_URI_obj, "$.message.order.payment.uri")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PAYMENT_URI_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_URI",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_URI**

                        - $.message.order.payment.uri must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.payment.uri is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_URI","attr":"$.message.order.payment.uri","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PAYMENT_URI_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_URI",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_URI","attr":"$.message.order.payment.uri","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PAYMENT_TL_METHOD(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_TL_METHOD_obj in scope:
                                PAYMENT_TL_METHOD_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_TL_METHOD_obj, "$.message.order.payment.tl_method")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PAYMENT_TL_METHOD_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_TL_METHOD",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_TL_METHOD**

                        - $.message.order.payment.tl_method must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.payment.tl_method is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_TL_METHOD","attr":"$.message.order.payment.tl_method","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PAYMENT_TL_METHOD_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_TL_METHOD",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_TL_METHOD","attr":"$.message.order.payment.tl_method","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PAYMENT_PARAMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_PARAMS_obj in scope:
                                PAYMENT_PARAMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def PAYMENT_CURRENCY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_CURRENCY_obj in scope:
                                        PAYMENT_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_CURRENCY_obj, "$.message.order.payment.params.currency")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_CURRENCY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_CURRENCY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_CURRENCY**

                                - $.message.order.payment.params.currency must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_CURRENCY","attr":"$.message.order.payment.params.currency","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_CURRENCY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_CURRENCY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_CURRENCY","attr":"$.message.order.payment.params.currency","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_TRANSACTION_ID(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_TRANSACTION_ID_obj in scope:
                                        PAYMENT_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_TRANSACTION_ID_obj, "$.message.order.payment.params.transaction_id")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_TRANSACTION_ID_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_TRANSACTION_ID",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_TRANSACTION_ID**

                                - $.message.order.payment.params.transaction_id must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.params.transaction_id is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_TRANSACTION_ID","attr":"$.message.order.payment.params.transaction_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_TRANSACTION_ID_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_TRANSACTION_ID",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_TRANSACTION_ID","attr":"$.message.order.payment.params.transaction_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_AMOUNT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_AMOUNT_obj in scope:
                                        PAYMENT_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_AMOUNT_obj, "$.message.order.payment.params.amount")

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_AMOUNT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_AMOUNT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_AMOUNT**

                                - $.message.order.payment.params.amount must be present in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_AMOUNT","attr":"$.message.order.payment.params.amount","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_AMOUNT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_AMOUNT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_AMOUNT","attr":"$.message.order.payment.params.amount","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    PAYMENT_CURRENCY,
                                    PAYMENT_TRANSACTION_ID,
                                    PAYMENT_AMOUNT,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PAYMENT_PARAMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_PARAMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_PARAMS","_RETURN_":[{"_NAME_":"PAYMENT_CURRENCY","attr":"$.message.order.payment.params.currency","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TRANSACTION_ID","attr":"$.message.order.payment.params.transaction_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_AMOUNT","attr":"$.message.order.payment.params.amount","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def PAYMENT_STATUS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_STATUS_obj in scope:
                                PAYMENT_STATUS_obj["_EXTERNAL"] = input_data["external_data"]
                                var_enum = ["NOT-PAID","PAID"]
                                attr = payload_utils["get_json_path"](PAYMENT_STATUS_obj, "$.message.order.payment.status")

                                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                if not validate:
                                    del PAYMENT_STATUS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_STATUS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_STATUS**

                        **All of the following must be true:**
                          - $.message.order.payment.status must be present in the payload
                          - All elements of $.message.order.payment.status must be in ["NOT-PAID", "PAID"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_STATUS","var_enum":["NOT-PAID","PAID"],"attr":"$.message.order.payment.status","_RETURN_":"attr are present && attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PAYMENT_STATUS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_STATUS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_STATUS","var_enum":["NOT-PAID","PAID"],"attr":"$.message.order.payment.status","_RETURN_":"attr are present && attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PAYMENT_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_TYPE_obj in scope:
                                PAYMENT_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_TYPE_obj, "$.message.order.payment.type")
                                var_enum = ["ON-ORDER","ON-FULFILLMENT"]

                                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                if not validate:
                                    del PAYMENT_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_TYPE**

                        **All of the following must be true:**
                          - $.message.order.payment.type must be present in the payload
                          - All elements of $.message.order.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_TYPE","attr":"$.message.order.payment.type","var_enum":["ON-ORDER","ON-FULFILLMENT"],"_RETURN_":"attr are present && attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PAYMENT_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_TYPE","attr":"$.message.order.payment.type","var_enum":["ON-ORDER","ON-FULFILLMENT"],"_RETURN_":"attr are present && attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PAYMENT_COLLECTED_BY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_COLLECTED_BY_obj in scope:
                                PAYMENT_COLLECTED_BY_obj["_EXTERNAL"] = input_data["external_data"]
                                var_enum = ["BAP","BPP"]
                                attr = payload_utils["get_json_path"](PAYMENT_COLLECTED_BY_obj, "$.message.order.payment.collected_by")

                                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                if not validate:
                                    del PAYMENT_COLLECTED_BY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_COLLECTED_BY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_COLLECTED_BY**

                        **All of the following must be true:**
                          - $.message.order.payment.collected_by must be present in the payload
                          - All elements of $.message.order.payment.collected_by must be in ["BAP", "BPP"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_COLLECTED_BY","var_enum":["BAP","BPP"],"attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present && attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PAYMENT_COLLECTED_BY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_COLLECTED_BY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_COLLECTED_BY","var_enum":["BAP","BPP"],"attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present && attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW_obj in scope:
                                PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW_obj, "$.message.order.payment['@ondc/org/settlement_window']")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW**

                        - $.message.order.payment['@ondc/org/settlement_window'] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.payment['@ondc/org/settlement_window'] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_window']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_window']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT_obj in scope:
                                PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT_obj, "$.message.order.payment['@ondc/org/withholding_amount']")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT**

                        - $.message.order.payment['@ondc/org/withholding_amount'] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.payment['@ondc/org/withholding_amount'] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/withholding_amount']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/withholding_amount']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PAYMENT_ONDC_ORG_SETTLEMENT_BASIS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_SETTLEMENT_BASIS_obj in scope:
                                PAYMENT_ONDC_ORG_SETTLEMENT_BASIS_obj["_EXTERNAL"] = input_data["external_data"]
                                var_enum = ["shipment","delivery","return_Window_expiry"]
                                attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_BASIS_obj, "$.message.order.payment['@ondc/org/settlement_basis']")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                                if not validate:
                                    del PAYMENT_ONDC_ORG_SETTLEMENT_BASIS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_BASIS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_BASIS**

                        **All of the following must be true:**
                          - $.message.order.payment['@ondc/org/settlement_basis'] must be present in the payload
                          - All elements of $.message.order.payment['@ondc/org/settlement_basis'] must be in ["shipment", "delivery", "return_Window_expiry"]

                        > **Skip if:**
                        >
                        >     - $.message.order.payment['@ondc/org/settlement_basis'] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_BASIS","var_enum":["shipment","delivery","return_Window_expiry"],"_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_basis']","_RETURN_":"attr are present && attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del PAYMENT_ONDC_ORG_SETTLEMENT_BASIS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_BASIS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_BASIS","var_enum":["shipment","delivery","return_Window_expiry"],"_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_basis']","_RETURN_":"attr are present && attr all in var_enum"}
                        """
                            }}] + sub_results

                        def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES_obj in scope:
                                PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"] = input_data["external_data"]

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_status must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_status is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            PAYMENT_URI,
                            PAYMENT_TL_METHOD,
                            PAYMENT_PARAMS,
                            PAYMENT_STATUS,
                            PAYMENT_TYPE,
                            PAYMENT_COLLECTED_BY,
                            PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW,
                            PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT,
                            PAYMENT_ONDC_ORG_SETTLEMENT_BASIS,
                            PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_PAYMENT_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_PAYMENT_ADDITIONAL_PROPERTIES",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_PAYMENT_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_URI","attr":"$.message.order.payment.uri","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TL_METHOD","attr":"$.message.order.payment.tl_method","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_PARAMS","_RETURN_":[{"_NAME_":"PAYMENT_CURRENCY","attr":"$.message.order.payment.params.currency","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TRANSACTION_ID","attr":"$.message.order.payment.params.transaction_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_AMOUNT","attr":"$.message.order.payment.params.amount","_RETURN_":"attr are present"}]},{"_NAME_":"PAYMENT_STATUS","var_enum":["NOT-PAID","PAID"],"attr":"$.message.order.payment.status","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_TYPE","attr":"$.message.order.payment.type","var_enum":["ON-ORDER","ON-FULFILLMENT"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_COLLECTED_BY","var_enum":["BAP","BPP"],"attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_window']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/withholding_amount']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_BASIS","var_enum":["shipment","delivery","return_Window_expiry"],"_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_basis']","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_RETURN_":"attr are present"}]}]}
                """
                    }}] + sub_results

                def ORDER_DOCUMENTS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_DOCUMENTS_obj in scope:
                        ORDER_DOCUMENTS_obj["_EXTERNAL"] = input_data["external_data"]

                        def DOCUMENTS_URL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for DOCUMENTS_URL_obj in scope:
                                DOCUMENTS_URL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](DOCUMENTS_URL_obj, "$.message.order.documents[*].url")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del DOCUMENTS_URL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "DOCUMENTS_URL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **DOCUMENTS_URL**

                        - $.message.order.documents[*].url must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.documents[*].url is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"DOCUMENTS_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].url","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del DOCUMENTS_URL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "DOCUMENTS_URL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"DOCUMENTS_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].url","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def DOCUMENTS_LABEL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for DOCUMENTS_LABEL_obj in scope:
                                DOCUMENTS_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](DOCUMENTS_LABEL_obj, "$.message.order.documents[*].label")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del DOCUMENTS_LABEL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "DOCUMENTS_LABEL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **DOCUMENTS_LABEL**

                        - $.message.order.documents[*].label must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.documents[*].label is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"DOCUMENTS_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].label","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del DOCUMENTS_LABEL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "DOCUMENTS_LABEL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"DOCUMENTS_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].label","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            DOCUMENTS_URL,
                            DOCUMENTS_LABEL,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_DOCUMENTS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_DOCUMENTS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_DOCUMENTS","_RETURN_":[{"_NAME_":"DOCUMENTS_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].url","_RETURN_":"attr are present"},{"_NAME_":"DOCUMENTS_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].label","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_CREATED_AT(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_CREATED_AT_obj in scope:
                        ORDER_CREATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ORDER_CREATED_AT_obj, "$.message.order.created_at")
                        pattern = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        validate = (validation_utils["are_present"](attr)) and (validation_utils["follow_regex"](attr, pattern))

                        if not validate:
                            del ORDER_CREATED_AT_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ORDER_CREATED_AT",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ORDER_CREATED_AT**

                **All of the following must be true:**
                  - $.message.order.created_at must be present in the payload
                  - All elements of $.message.order.created_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ORDER_CREATED_AT","attr":"$.message.order.created_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"}
                """
                                }
                            }]

                        # del ORDER_CREATED_AT_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_CREATED_AT",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_CREATED_AT","attr":"$.message.order.created_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"}
                """
                    }}] + sub_results

                def ORDER_UPDATED_AT(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_UPDATED_AT_obj in scope:
                        ORDER_UPDATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ORDER_UPDATED_AT_obj, "$.message.order.updated_at")
                        pattern = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        validate = (validation_utils["are_present"](attr)) and (validation_utils["follow_regex"](attr, pattern))

                        if not validate:
                            del ORDER_UPDATED_AT_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ORDER_UPDATED_AT",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ORDER_UPDATED_AT**

                **All of the following must be true:**
                  - $.message.order.updated_at must be present in the payload
                  - All elements of $.message.order.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ORDER_UPDATED_AT","attr":"$.message.order.updated_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"}
                """
                                }
                            }]

                        # del ORDER_UPDATED_AT_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_UPDATED_AT",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_UPDATED_AT","attr":"$.message.order.updated_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_ID,
                    ORDER_STATE,
                    ORDER_PROVIDER,
                    ORDER_CANCELLATION,
                    ORDER_ITEMS,
                    ORDER_BILLING,
                    ORDER_FULFILLMENTS,
                    ORDER_QUOTE,
                    ORDER_QUOTE_ADDITIONAL_PROPERTIES,
                    ORDER_PAYMENT,
                    ORDER_PAYMENT_ADDITIONAL_PROPERTIES,
                    ORDER_DOCUMENTS,
                    ORDER_CREATED_AT,
                    ORDER_UPDATED_AT,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del ON_STATUS_ORDER_obj["_EXTERNAL"]

            return [{
                "test_name": "ON_STATUS_ORDER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"ON_STATUS_ORDER","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.order.id","pattern":["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"],"_RETURN_":"attr are present && attr follow regex pattern"},{"_NAME_":"ORDER_STATE","attr":"$.message.order.state","var_enum":["Created","Accepted","In-progress","Completed","Cancelled"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_CANCELLATION","_RETURN_":[{"_NAME_":"CANCELLATION_CANCELLED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.cancelled_by","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON","_RETURN_":[{"_NAME_":"CANCELLATION_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.id","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_STATE_DESCRIPTOR_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Pending","Packed","Agent-assigned","At-pickup","At-delivery","Order-picked-up","Out-for-delivery","Order-delivered","Cancelled","RTO-Initiated","RTO-Disposed","RTO-Delivered"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_ONDC_ORG_PROVIDER_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TRACKING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_ONDC_ORG_TAT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_START_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"FULFILLMENTS_START_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_AGENT","_RETURN_":[{"_NAME_":"FULFILLMENTS_AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.phone","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_VEHICLE","_RETURN_":[{"_NAME_":"FULFILLMENTS_VEHICLE_CATEGORY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.category","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_SIZE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.size","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_REGISTRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.registration","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_STATE","_RETURN_":[{"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_ROUTING","_RETURN_":[{"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_PAYMENT_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_URI","attr":"$.message.order.payment.uri","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TL_METHOD","attr":"$.message.order.payment.tl_method","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_PARAMS","_RETURN_":[{"_NAME_":"PAYMENT_CURRENCY","attr":"$.message.order.payment.params.currency","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TRANSACTION_ID","attr":"$.message.order.payment.params.transaction_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_AMOUNT","attr":"$.message.order.payment.params.amount","_RETURN_":"attr are present"}]},{"_NAME_":"PAYMENT_STATUS","var_enum":["NOT-PAID","PAID"],"attr":"$.message.order.payment.status","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_TYPE","attr":"$.message.order.payment.type","var_enum":["ON-ORDER","ON-FULFILLMENT"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_COLLECTED_BY","var_enum":["BAP","BPP"],"attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_window']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/withholding_amount']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_BASIS","var_enum":["shipment","delivery","return_Window_expiry"],"_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_basis']","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_DOCUMENTS","_RETURN_":[{"_NAME_":"DOCUMENTS_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].url","_RETURN_":"attr are present"},{"_NAME_":"DOCUMENTS_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].label","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_CREATED_AT","attr":"$.message.order.created_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"},{"_NAME_":"ORDER_UPDATED_AT","attr":"$.message.order.updated_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"}]}
        """
            }}] + sub_results

        test_functions = [
            ON_STATUS_CONTEXT,
            ON_STATUS_ORDER,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_status_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_status_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_status_validations","_RETURN_":[{"_NAME_":"ON_STATUS_CONTEXT","_DESCRIPTION_":"Validate on_status context","action":["on_status"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_status"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_status"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_status"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_status"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_status"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_status"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_status"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_status"]}]}]},{"_NAME_":"ON_STATUS_ORDER","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.order.id","pattern":["^[a-zA-Z0-9-]{1,32}$|^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"],"_RETURN_":"attr are present && attr follow regex pattern"},{"_NAME_":"ORDER_STATE","attr":"$.message.order.state","var_enum":["Created","Accepted","In-progress","Completed","Cancelled"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_CANCELLATION","_RETURN_":[{"_NAME_":"CANCELLATION_CANCELLED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.cancelled_by","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON","_RETURN_":[{"_NAME_":"CANCELLATION_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.id","_RETURN_":"attr are present"},{"_NAME_":"CANCELLATION_REASON_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.cancellation.reason.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_STATE_DESCRIPTOR_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","var_enum":["Pending","Packed","Agent-assigned","At-pickup","At-delivery","Order-picked-up","Out-for-delivery","Order-delivered","Cancelled","RTO-Initiated","RTO-Disposed","RTO-Delivered"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_ONDC_ORG_PROVIDER_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/provider_name']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TRACKING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_ONDC_ORG_TAT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*]['@ondc/org/TAT']","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_DESCRIPTOR_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_START_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.code","var_enum":["1","2","3","4"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.long_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"FULFILLMENTS_START_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_START_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_START_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_BUILDING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_LOCALITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_COUNTRY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_CITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_AREA_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_ADDRESS_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.location.address.state","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_END_TIME","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.time.timestamp","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.code","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_SHORT_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.short_desc","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_LONG_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.instructions.long_desc","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_END_CONTACT","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_EMAIL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].end.contact.email","_RETURN_":"attr are present"}]}]},{"_NAME_":"FULFILLMENTS_AGENT","_RETURN_":[{"_NAME_":"FULFILLMENTS_AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.name","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].agent.phone","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_VEHICLE","_RETURN_":[{"_NAME_":"FULFILLMENTS_VEHICLE_CATEGORY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.category","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_SIZE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.size","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_VEHICLE_REGISTRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].vehicle.registration","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_STATE","_RETURN_":[{"_NAME_":"STATE_READY_TO_SHIP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_ROUTING","_RETURN_":[{"_NAME_":"ROUTING_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='routing')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_TRACKING","_RETURN_":[{"_NAME_":"TRACKING_GPS_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='gps_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL_ENABLED","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url_enabled')].value","_RETURN_":"attr are present"},{"_NAME_":"TRACKING_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='tracking')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[?(@.code=='timestamp')].value","reg":["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"ORDER_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}]}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_PAYMENT_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_URI","attr":"$.message.order.payment.uri","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TL_METHOD","attr":"$.message.order.payment.tl_method","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_PARAMS","_RETURN_":[{"_NAME_":"PAYMENT_CURRENCY","attr":"$.message.order.payment.params.currency","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_TRANSACTION_ID","attr":"$.message.order.payment.params.transaction_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_AMOUNT","attr":"$.message.order.payment.params.amount","_RETURN_":"attr are present"}]},{"_NAME_":"PAYMENT_STATUS","var_enum":["NOT-PAID","PAID"],"attr":"$.message.order.payment.status","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_TYPE","attr":"$.message.order.payment.type","var_enum":["ON-ORDER","ON-FULFILLMENT"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_COLLECTED_BY","var_enum":["BAP","BPP"],"attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_WINDOW","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_window']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_WITHHOLDING_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/withholding_amount']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_BASIS","var_enum":["shipment","delivery","return_Window_expiry"],"_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_basis']","_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_REFERENCE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_reference","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_STATUS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_status","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_DOCUMENTS","_RETURN_":[{"_NAME_":"DOCUMENTS_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].url","_RETURN_":"attr are present"},{"_NAME_":"DOCUMENTS_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.documents[*].label","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_CREATED_AT","attr":"$.message.order.created_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"},{"_NAME_":"ORDER_UPDATED_AT","attr":"$.message.order.updated_at","pattern":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr are present && attr follow regex pattern"}]}]}
"""
    }}] + sub_results

def on_status(input_data):
    total_results = on_status_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "on_status_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
