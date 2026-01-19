from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def search_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for search_validations_obj in scope:
        search_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def SEARCH_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SEARCH_CONTEXT_obj in scope:
                SEARCH_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["search"]

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
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]}
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
                                action = ["search"]

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
                        >     - ["search"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["search"]}
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
                                action = ["search"]

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
                        >     - ["search"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["search"]}
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
                                action = ["search"]

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
                        >     - all elements of ["search"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["search"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["search"]}]}
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
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["search"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["search"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["search"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["search"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["search"]}
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
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["search"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["search"]}
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
                                action = ["search"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["search"]}
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
                                action = ["search"]

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
                        >     - ["search"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["search"]}
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
                                action = ["search"]

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
                        >     - all elements of ["search"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["search"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["search"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["search"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["search"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["search"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["search"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["search"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["search"]}]}
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

                # del SEARCH_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "SEARCH_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SEARCH_CONTEXT","_DESCRIPTION_":"Validate search context","action":["search"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["search"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["search"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["search"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["search"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["search"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["search"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["search"]}]}]}
        """
            }}] + sub_results

        def SEARCH_PAYMENT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SEARCH_PAYMENT_obj in scope:
                SEARCH_PAYMENT_obj["_EXTERNAL"] = input_data["external_data"]

                def PAYMENT_REQUIRED(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for PAYMENT_REQUIRED_obj in scope:
                        PAYMENT_REQUIRED_obj["_EXTERNAL"] = input_data["external_data"]

                        def PAYMENT_REQUIRED_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_REQUIRED_TYPE_obj in scope:
                                PAYMENT_REQUIRED_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_REQUIRED_TYPE_obj, "$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PAYMENT_REQUIRED_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_REQUIRED_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_REQUIRED_TYPE**

                        - $.message.intent.payment['@ondc/org/buyer_app_finder_fee_type'] must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_REQUIRED_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PAYMENT_REQUIRED_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_REQUIRED_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_REQUIRED_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def PAYMENT_REQUIRED_AMOUNT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_REQUIRED_AMOUNT_obj in scope:
                                PAYMENT_REQUIRED_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_REQUIRED_AMOUNT_obj, "$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del PAYMENT_REQUIRED_AMOUNT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_REQUIRED_AMOUNT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_REQUIRED_AMOUNT**

                        - $.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount'] must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_REQUIRED_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del PAYMENT_REQUIRED_AMOUNT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_REQUIRED_AMOUNT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_REQUIRED_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            PAYMENT_REQUIRED_TYPE,
                            PAYMENT_REQUIRED_AMOUNT,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del PAYMENT_REQUIRED_obj["_EXTERNAL"]

                    return [{
                        "test_name": "PAYMENT_REQUIRED",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"PAYMENT_REQUIRED","_RETURN_":[{"_NAME_":"PAYMENT_REQUIRED_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_REQUIRED_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def PAYMENT_ENUM(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for PAYMENT_ENUM_obj in scope:
                        PAYMENT_ENUM_obj["_EXTERNAL"] = input_data["external_data"]

                        def PAYMENT_ENUM_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_ENUM_TYPE_obj in scope:
                                PAYMENT_ENUM_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_ENUM_TYPE_obj, "$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']")
                                var_fee_type = ["percent","amount"]

                                validate = validation_utils["all_in"](attr, var_fee_type)

                                if not validate:
                                    del PAYMENT_ENUM_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_ENUM_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_ENUM_TYPE**

                        - All elements of $.message.intent.payment['@ondc/org/buyer_app_finder_fee_type'] must be in ["percent", "amount"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_ENUM_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","var_fee_type":["percent","amount"],"_RETURN_":"attr all in var_fee_type"}
                        """
                                        }
                                    }]

                                # del PAYMENT_ENUM_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_ENUM_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_ENUM_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","var_fee_type":["percent","amount"],"_RETURN_":"attr all in var_fee_type"}
                        """
                            }}] + sub_results

                        def PAYMENT_REGEX_AMOUNT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for PAYMENT_REGEX_AMOUNT_obj in scope:
                                PAYMENT_REGEX_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](PAYMENT_REGEX_AMOUNT_obj, "$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']")
                                reg = ["^(\\d*.?\\d{1,2})$"]

                                validate = validation_utils["follow_regex"](attr, reg)

                                if not validate:
                                    del PAYMENT_REGEX_AMOUNT_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "PAYMENT_REGEX_AMOUNT",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **PAYMENT_REGEX_AMOUNT**

                        - All elements of $.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount'] must follow every regex in ["^(\\d*.?\\d{1,2})$"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"PAYMENT_REGEX_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr follow regex reg"}
                        """
                                        }
                                    }]

                                # del PAYMENT_REGEX_AMOUNT_obj["_EXTERNAL"]

                            return [{
                                "test_name": "PAYMENT_REGEX_AMOUNT",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"PAYMENT_REGEX_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr follow regex reg"}
                        """
                            }}] + sub_results

                        test_functions = [
                            PAYMENT_ENUM_TYPE,
                            PAYMENT_REGEX_AMOUNT,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del PAYMENT_ENUM_obj["_EXTERNAL"]

                    return [{
                        "test_name": "PAYMENT_ENUM",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"PAYMENT_ENUM","_RETURN_":[{"_NAME_":"PAYMENT_ENUM_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","var_fee_type":["percent","amount"],"_RETURN_":"attr all in var_fee_type"},{"_NAME_":"PAYMENT_REGEX_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr follow regex reg"}]}
                """
                    }}] + sub_results

                test_functions = [
                    PAYMENT_REQUIRED,
                    PAYMENT_ENUM,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del SEARCH_PAYMENT_obj["_EXTERNAL"]

            return [{
                "test_name": "SEARCH_PAYMENT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SEARCH_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_REQUIRED","_RETURN_":[{"_NAME_":"PAYMENT_REQUIRED_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_REQUIRED_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","_RETURN_":"attr are present"}]},{"_NAME_":"PAYMENT_ENUM","_RETURN_":[{"_NAME_":"PAYMENT_ENUM_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","var_fee_type":["percent","amount"],"_RETURN_":"attr all in var_fee_type"},{"_NAME_":"PAYMENT_REGEX_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr follow regex reg"}]}]}
        """
            }}] + sub_results

        def SEARCH_FULFILMENT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SEARCH_FULFILMENT_obj in scope:
                SEARCH_FULFILMENT_obj["_EXTERNAL"] = input_data["external_data"]

                def FULFILMENT_REQUIRED(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for FULFILMENT_REQUIRED_obj in scope:
                        FULFILMENT_REQUIRED_obj["_EXTERNAL"] = input_data["external_data"]

                        def FULFILMENT_REQUIRED_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILMENT_REQUIRED_TYPE_obj in scope:
                                FULFILMENT_REQUIRED_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILMENT_REQUIRED_TYPE_obj, "$.message.intent.fulfillment.type")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILMENT_REQUIRED_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILMENT_REQUIRED_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILMENT_REQUIRED_TYPE**

                        - $.message.intent.fulfillment.type must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.intent.fulfillment.type is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILMENT_REQUIRED_TYPE","attr":"$.message.intent.fulfillment.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILMENT_REQUIRED_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILMENT_REQUIRED_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILMENT_REQUIRED_TYPE","attr":"$.message.intent.fulfillment.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILMENT_REQUIRED_END_LOCATION_GPS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILMENT_REQUIRED_END_LOCATION_GPS_obj in scope:
                                FULFILMENT_REQUIRED_END_LOCATION_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILMENT_REQUIRED_END_LOCATION_GPS_obj, "$.message.intent.fulfillment.end.location.gps")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILMENT_REQUIRED_END_LOCATION_GPS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILMENT_REQUIRED_END_LOCATION_GPS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILMENT_REQUIRED_END_LOCATION_GPS**

                        - $.message.intent.fulfillment.end.location.gps must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.intent.fulfillment.end.location.gps is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_GPS","attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILMENT_REQUIRED_END_LOCATION_GPS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILMENT_REQUIRED_END_LOCATION_GPS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_GPS","attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE_obj in scope:
                                FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE_obj, "$.message.intent.fulfillment.end.location.address.area_code")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE**

                        - $.message.intent.fulfillment.end.location.address.area_code must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.intent.fulfillment.end.location.address.area_code is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE","attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE","attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILMENT_REQUIRED_TYPE,
                            FULFILMENT_REQUIRED_END_LOCATION_GPS,
                            FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del FULFILMENT_REQUIRED_obj["_EXTERNAL"]

                    return [{
                        "test_name": "FULFILMENT_REQUIRED",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"FULFILMENT_REQUIRED","_RETURN_":[{"_NAME_":"FULFILMENT_REQUIRED_TYPE","attr":"$.message.intent.fulfillment.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_GPS","attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE","attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def FULFILMENT_ENUM(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for FULFILMENT_ENUM_obj in scope:
                        FULFILMENT_ENUM_obj["_EXTERNAL"] = input_data["external_data"]

                        def FULFILMENT_ENUM_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILMENT_ENUM_TYPE_obj in scope:
                                FULFILMENT_ENUM_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILMENT_ENUM_TYPE_obj, "$.message.intent.fulfillment.type")
                                var_types = ["Delivery","Self-Pickup","Buyer-Delivery"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_types)

                                if not validate:
                                    del FULFILMENT_ENUM_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILMENT_ENUM_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILMENT_ENUM_TYPE**

                        - All elements of $.message.intent.fulfillment.type must be in ["Delivery", "Self-Pickup", "Buyer-Delivery"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.fulfillment.type is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILMENT_ENUM_TYPE","attr":"$.message.intent.fulfillment.type","var_types":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_types"}
                        """
                                        }
                                    }]

                                # del FULFILMENT_ENUM_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILMENT_ENUM_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILMENT_ENUM_TYPE","attr":"$.message.intent.fulfillment.type","var_types":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_types"}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILMENT_ENUM_TYPE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del FULFILMENT_ENUM_obj["_EXTERNAL"]

                    return [{
                        "test_name": "FULFILMENT_ENUM",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"FULFILMENT_ENUM","_RETURN_":[{"_NAME_":"FULFILMENT_ENUM_TYPE","attr":"$.message.intent.fulfillment.type","var_types":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_types"}]}
                """
                    }}] + sub_results

                test_functions = [
                    FULFILMENT_REQUIRED,
                    FULFILMENT_ENUM,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del SEARCH_FULFILMENT_obj["_EXTERNAL"]

            return [{
                "test_name": "SEARCH_FULFILMENT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SEARCH_FULFILMENT","_RETURN_":[{"_NAME_":"FULFILMENT_REQUIRED","_RETURN_":[{"_NAME_":"FULFILMENT_REQUIRED_TYPE","attr":"$.message.intent.fulfillment.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_GPS","attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE","attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILMENT_ENUM","_RETURN_":[{"_NAME_":"FULFILMENT_ENUM_TYPE","attr":"$.message.intent.fulfillment.type","var_types":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_types"}]}]}
        """
            }}] + sub_results

        def SEARCH_ITEM(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SEARCH_ITEM_obj in scope:
                SEARCH_ITEM_obj["_EXTERNAL"] = input_data["external_data"]

                def ITEM_REQUIRED_DESCRIPTOR_NAME(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ITEM_REQUIRED_DESCRIPTOR_NAME_obj in scope:
                        ITEM_REQUIRED_DESCRIPTOR_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ITEM_REQUIRED_DESCRIPTOR_NAME_obj, "$.message.intent.item.descriptor.name")

                        skip_check = not (validation_utils["are_present"](attr))
                        if skip_check:
                            continue

                        validate = validation_utils["are_present"](attr)

                        if not validate:
                            del ITEM_REQUIRED_DESCRIPTOR_NAME_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ITEM_REQUIRED_DESCRIPTOR_NAME",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ITEM_REQUIRED_DESCRIPTOR_NAME**

                - $.message.intent.item.descriptor.name must be present in the payload

                > **Skip if:**
                >
                >     - $.message.intent.item.descriptor.name is not in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ITEM_REQUIRED_DESCRIPTOR_NAME","attr":"$.message.intent.item.descriptor.name","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                """
                                }
                            }]

                        # del ITEM_REQUIRED_DESCRIPTOR_NAME_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ITEM_REQUIRED_DESCRIPTOR_NAME",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ITEM_REQUIRED_DESCRIPTOR_NAME","attr":"$.message.intent.item.descriptor.name","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                """
                    }}] + sub_results

                test_functions = [
                    ITEM_REQUIRED_DESCRIPTOR_NAME,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del SEARCH_ITEM_obj["_EXTERNAL"]

            return [{
                "test_name": "SEARCH_ITEM",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SEARCH_ITEM","_RETURN_":[{"_NAME_":"ITEM_REQUIRED_DESCRIPTOR_NAME","attr":"$.message.intent.item.descriptor.name","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
        """
            }}] + sub_results

        def SEARCH_CATEGORY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SEARCH_CATEGORY_obj in scope:
                SEARCH_CATEGORY_obj["_EXTERNAL"] = input_data["external_data"]

                def CATEGORY_REQUIRED_ID(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for CATEGORY_REQUIRED_ID_obj in scope:
                        CATEGORY_REQUIRED_ID_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](CATEGORY_REQUIRED_ID_obj, "$.message.intent.category.id")

                        skip_check = not (validation_utils["are_present"](attr))
                        if skip_check:
                            continue

                        validate = validation_utils["are_present"](attr)

                        if not validate:
                            del CATEGORY_REQUIRED_ID_obj["_EXTERNAL"]
                            return [{
                                "test_name": "CATEGORY_REQUIRED_ID",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **CATEGORY_REQUIRED_ID**

                - $.message.intent.category.id must be present in the payload

                > **Skip if:**
                >
                >     - $.message.intent.category.id is not in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"CATEGORY_REQUIRED_ID","attr":"$.message.intent.category.id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                """
                                }
                            }]

                        # del CATEGORY_REQUIRED_ID_obj["_EXTERNAL"]

                    return [{
                        "test_name": "CATEGORY_REQUIRED_ID",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"CATEGORY_REQUIRED_ID","attr":"$.message.intent.category.id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                """
                    }}] + sub_results

                test_functions = [
                    CATEGORY_REQUIRED_ID,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del SEARCH_CATEGORY_obj["_EXTERNAL"]

            return [{
                "test_name": "SEARCH_CATEGORY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SEARCH_CATEGORY","_RETURN_":[{"_NAME_":"CATEGORY_REQUIRED_ID","attr":"$.message.intent.category.id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
        """
            }}] + sub_results

        def SEARCH_TAGS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SEARCH_TAGS_obj in scope:
                SEARCH_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                def SEARCH_TAG_INTENT_GROUP(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for SEARCH_TAG_INTENT_GROUP_obj in scope:
                        SEARCH_TAG_INTENT_GROUP_obj["_EXTERNAL"] = input_data["external_data"]
                        code = payload_utils["get_json_path"](SEARCH_TAG_INTENT_GROUP_obj, "$.message.intent.tags[*].code")
                        var_codes = ["catalog_inc","bap_terms","catalog_full","bnp_features","bap_features","bap_promos","bnp_demand_signal"]

                        skip_check = not (validation_utils["are_present"](code))
                        if skip_check:
                            continue

                        validate = validation_utils["all_in"](code, var_codes)

                        if not validate:
                            del SEARCH_TAG_INTENT_GROUP_obj["_EXTERNAL"]
                            return [{
                                "test_name": "SEARCH_TAG_INTENT_GROUP",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **SEARCH_TAG_INTENT_GROUP**

                - All elements of $.message.intent.tags[*].code must be in ["catalog_inc", "bap_terms", "catalog_full", "bnp_features", "bap_features", "bap_promos", "bnp_demand_signal"]

                > **Skip if:**
                >
                >     - $.message.intent.tags[*].code is not in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"SEARCH_TAG_INTENT_GROUP","code":"$.message.intent.tags[*].code","_CONTINUE_":"!(code are present)","var_codes":["catalog_inc","bap_terms","catalog_full","bnp_features","bap_features","bap_promos","bnp_demand_signal"],"_RETURN_":"code all in var_codes"}
                """
                                }
                            }]

                        # del SEARCH_TAG_INTENT_GROUP_obj["_EXTERNAL"]

                    return [{
                        "test_name": "SEARCH_TAG_INTENT_GROUP",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"SEARCH_TAG_INTENT_GROUP","code":"$.message.intent.tags[*].code","_CONTINUE_":"!(code are present)","var_codes":["catalog_inc","bap_terms","catalog_full","bnp_features","bap_features","bap_promos","bnp_demand_signal"],"_RETURN_":"code all in var_codes"}
                """
                    }}] + sub_results

                def TAGS_BNP_FEATURES(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_BNP_FEATURES_obj in scope:
                        TAGS_BNP_FEATURES_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BNP_FEATURES_PAYLOAD_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BNP_FEATURES_PAYLOAD_TYPE_obj in scope:
                                TAGS_BNP_FEATURES_PAYLOAD_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BNP_FEATURES_PAYLOAD_TYPE_obj, "$.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value")
                                var_payload_types = ["link","inline"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["any_in"](attr, var_payload_types)

                                if not validate:
                                    del TAGS_BNP_FEATURES_PAYLOAD_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BNP_FEATURES_PAYLOAD_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BNP_FEATURES_PAYLOAD_TYPE**

                        - At least one of $.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value must be in ["link", "inline"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BNP_FEATURES_PAYLOAD_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value","var_payload_types":["link","inline"],"_RETURN_":"attr any in var_payload_types"}
                        """
                                        }
                                    }]

                                # del TAGS_BNP_FEATURES_PAYLOAD_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BNP_FEATURES_PAYLOAD_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BNP_FEATURES_PAYLOAD_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value","var_payload_types":["link","inline"],"_RETURN_":"attr any in var_payload_types"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_BNP_FEATURES_PAYLOAD_TYPE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TAGS_BNP_FEATURES_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TAGS_BNP_FEATURES",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TAGS_BNP_FEATURES","_RETURN_":[{"_NAME_":"TAGS_BNP_FEATURES_PAYLOAD_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value","var_payload_types":["link","inline"],"_RETURN_":"attr any in var_payload_types"}]}
                """
                    }}] + sub_results

                def TAGS_BAP_TERMS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_BAP_TERMS_obj in scope:
                        TAGS_BAP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BAP_TERMS_STATIC_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_TERMS_STATIC_TERMS_obj in scope:
                                TAGS_BAP_TERMS_STATIC_TERMS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_TERMS_STATIC_TERMS_obj, "$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del TAGS_BAP_TERMS_STATIC_TERMS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_TERMS_STATIC_TERMS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_TERMS_STATIC_TERMS**

                        - $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_TERMS_STATIC_TERMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_TERMS_STATIC_TERMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def TAGS_BAP_TERMS_STATIC_TERMS_NEW(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_TERMS_STATIC_TERMS_NEW_obj in scope:
                                TAGS_BAP_TERMS_STATIC_TERMS_NEW_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_TERMS_STATIC_TERMS_NEW_obj, "$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value")
                                var_enum_static_terms_new = ["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_static_terms_new)

                                if not validate:
                                    del TAGS_BAP_TERMS_STATIC_TERMS_NEW_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_TERMS_STATIC_TERMS_NEW",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_TERMS_STATIC_TERMS_NEW**

                        - All elements of $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value must be in ["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS_NEW","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value","var_enum_static_terms_new":["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"],"_RETURN_":"attr all in var_enum_static_terms_new"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_TERMS_STATIC_TERMS_NEW_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_TERMS_STATIC_TERMS_NEW",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS_NEW","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value","var_enum_static_terms_new":["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"],"_RETURN_":"attr all in var_enum_static_terms_new"}
                        """
                            }}] + sub_results

                        def TAGS_BAP_TERMS_EFFECTIVE_DATE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_TERMS_EFFECTIVE_DATE_obj in scope:
                                TAGS_BAP_TERMS_EFFECTIVE_DATE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_TERMS_EFFECTIVE_DATE_obj, "$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value")
                                var_date_regex = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, var_date_regex)

                                if not validate:
                                    del TAGS_BAP_TERMS_EFFECTIVE_DATE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_TERMS_EFFECTIVE_DATE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_TERMS_EFFECTIVE_DATE**

                        - All elements of $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS_EFFECTIVE_DATE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value","var_date_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex var_date_regex"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_TERMS_EFFECTIVE_DATE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_TERMS_EFFECTIVE_DATE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS_EFFECTIVE_DATE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value","var_date_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex var_date_regex"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_BAP_TERMS_STATIC_TERMS,
                            TAGS_BAP_TERMS_STATIC_TERMS_NEW,
                            TAGS_BAP_TERMS_EFFECTIVE_DATE,
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
                {"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS_NEW","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value","var_enum_static_terms_new":["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"],"_RETURN_":"attr all in var_enum_static_terms_new"},{"_NAME_":"TAGS_BAP_TERMS_EFFECTIVE_DATE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value","var_date_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex var_date_regex"}]}
                """
                    }}] + sub_results

                def TAGS_CATALOG_FULL(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_CATALOG_FULL_obj in scope:
                        TAGS_CATALOG_FULL_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_CATALOG_FULL_PAYLOAD_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_CATALOG_FULL_PAYLOAD_TYPE_obj in scope:
                                TAGS_CATALOG_FULL_PAYLOAD_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_CATALOG_FULL_PAYLOAD_TYPE_obj, "$.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value")
                                var_enum_payload_type = ["link"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_payload_type)

                                if not validate:
                                    del TAGS_CATALOG_FULL_PAYLOAD_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_CATALOG_FULL_PAYLOAD_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_CATALOG_FULL_PAYLOAD_TYPE**

                        - All elements of $.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value must be in ["link"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_FULL_PAYLOAD_TYPE","attr":"$.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value","var_enum_payload_type":["link"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_payload_type"}
                        """
                                        }
                                    }]

                                # del TAGS_CATALOG_FULL_PAYLOAD_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_CATALOG_FULL_PAYLOAD_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_FULL_PAYLOAD_TYPE","attr":"$.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value","var_enum_payload_type":["link"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_payload_type"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_CATALOG_FULL_PAYLOAD_TYPE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TAGS_CATALOG_FULL_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TAGS_CATALOG_FULL",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TAGS_CATALOG_FULL","_RETURN_":[{"_NAME_":"TAGS_CATALOG_FULL_PAYLOAD_TYPE","attr":"$.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value","var_enum_payload_type":["link"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_payload_type"}]}
                """
                    }}] + sub_results

                def TAGS_CATALOG_INC(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_CATALOG_INC_obj in scope:
                        TAGS_CATALOG_INC_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_CATALOG_INC_START_TIME(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_CATALOG_INC_START_TIME_obj in scope:
                                TAGS_CATALOG_INC_START_TIME_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_CATALOG_INC_START_TIME_obj, "$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value")
                                var_datetime_regex = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, var_datetime_regex)

                                if not validate:
                                    del TAGS_CATALOG_INC_START_TIME_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_CATALOG_INC_START_TIME",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_CATALOG_INC_START_TIME**

                        - All elements of $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_INC_START_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                                        }
                                    }]

                                # del TAGS_CATALOG_INC_START_TIME_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_CATALOG_INC_START_TIME",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_INC_START_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                            }}] + sub_results

                        def TAGS_CATALOG_INC_END_TIME(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_CATALOG_INC_END_TIME_obj in scope:
                                TAGS_CATALOG_INC_END_TIME_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_CATALOG_INC_END_TIME_obj, "$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value")
                                var_datetime_regex = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, var_datetime_regex)

                                if not validate:
                                    del TAGS_CATALOG_INC_END_TIME_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_CATALOG_INC_END_TIME",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_CATALOG_INC_END_TIME**

                        - All elements of $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_INC_END_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                                        }
                                    }]

                                # del TAGS_CATALOG_INC_END_TIME_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_CATALOG_INC_END_TIME",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_INC_END_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                            }}] + sub_results

                        def TAGS_CATALOG_INC_MODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_CATALOG_INC_MODE_obj in scope:
                                TAGS_CATALOG_INC_MODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_CATALOG_INC_MODE_obj, "$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value")
                                var_enum_mode = ["start","stop"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_mode)

                                if not validate:
                                    del TAGS_CATALOG_INC_MODE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_CATALOG_INC_MODE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_CATALOG_INC_MODE**

                        - All elements of $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value must be in ["start", "stop"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_INC_MODE","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value","var_enum_mode":["start","stop"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_mode"}
                        """
                                        }
                                    }]

                                # del TAGS_CATALOG_INC_MODE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_CATALOG_INC_MODE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_CATALOG_INC_MODE","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value","var_enum_mode":["start","stop"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_mode"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_CATALOG_INC_START_TIME,
                            TAGS_CATALOG_INC_END_TIME,
                            TAGS_CATALOG_INC_MODE,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TAGS_CATALOG_INC_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TAGS_CATALOG_INC",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TAGS_CATALOG_INC","_RETURN_":[{"_NAME_":"TAGS_CATALOG_INC_START_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_CATALOG_INC_END_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_CATALOG_INC_MODE","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value","var_enum_mode":["start","stop"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_mode"}]}
                """
                    }}] + sub_results

                def TAGS_BAP_FEATURES(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_BAP_FEATURES_obj in scope:
                        TAGS_BAP_FEATURES_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BAP_FEATURES_ITEM_1(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_FEATURES_ITEM_1_obj in scope:
                                TAGS_BAP_FEATURES_ITEM_1_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_FEATURES_ITEM_1_obj, "$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value")
                                var_enum_bap_features = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_bap_features)

                                if not validate:
                                    del TAGS_BAP_FEATURES_ITEM_1_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_FEATURES_ITEM_1",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_FEATURES_ITEM_1**

                        - All elements of $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_FEATURES_ITEM_1","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_FEATURES_ITEM_1_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_FEATURES_ITEM_1",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_FEATURES_ITEM_1","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}
                        """
                            }}] + sub_results

                        def TAGS_BAP_FEATURES_ITEM_2(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_FEATURES_ITEM_2_obj in scope:
                                TAGS_BAP_FEATURES_ITEM_2_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_FEATURES_ITEM_2_obj, "$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value")
                                var_enum_bap_features = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_bap_features)

                                if not validate:
                                    del TAGS_BAP_FEATURES_ITEM_2_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_FEATURES_ITEM_2",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_FEATURES_ITEM_2**

                        - All elements of $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_FEATURES_ITEM_2","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_FEATURES_ITEM_2_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_FEATURES_ITEM_2",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_FEATURES_ITEM_2","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}
                        """
                            }}] + sub_results

                        def TAGS_BAP_FEATURES_ITEM_3(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_FEATURES_ITEM_3_obj in scope:
                                TAGS_BAP_FEATURES_ITEM_3_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_FEATURES_ITEM_3_obj, "$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value")
                                var_enum_bap_features = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_bap_features)

                                if not validate:
                                    del TAGS_BAP_FEATURES_ITEM_3_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_FEATURES_ITEM_3",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_FEATURES_ITEM_3**

                        - All elements of $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_FEATURES_ITEM_3","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_FEATURES_ITEM_3_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_FEATURES_ITEM_3",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_FEATURES_ITEM_3","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_BAP_FEATURES_ITEM_1,
                            TAGS_BAP_FEATURES_ITEM_2,
                            TAGS_BAP_FEATURES_ITEM_3,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TAGS_BAP_FEATURES_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TAGS_BAP_FEATURES",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TAGS_BAP_FEATURES","_RETURN_":[{"_NAME_":"TAGS_BAP_FEATURES_ITEM_1","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"},{"_NAME_":"TAGS_BAP_FEATURES_ITEM_2","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"},{"_NAME_":"TAGS_BAP_FEATURES_ITEM_3","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}]}
                """
                    }}] + sub_results

                def TAGS_BAP_PROMOS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_BAP_PROMOS_obj in scope:
                        TAGS_BAP_PROMOS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BAP_PROMOS_CATEGORY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_PROMOS_CATEGORY_obj in scope:
                                TAGS_BAP_PROMOS_CATEGORY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_PROMOS_CATEGORY_obj, "$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value")
                                var_enum_promo_categories = ["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Bakery, Cakes & Dairy","Pet Care","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum_promo_categories)

                                if not validate:
                                    del TAGS_BAP_PROMOS_CATEGORY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_PROMOS_CATEGORY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_PROMOS_CATEGORY**

                        - All elements of $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value must be in ["Fruits and Vegetables", "Masala & Seasoning", "Oil & Ghee", "Eggs, Meat & Fish", "Bakery, Cakes & Dairy", "Pet Care", "Detergents and Dishwash", "Dairy and Cheese", "Snacks, Dry Fruits, Nuts", "Pasta, Soup and Noodles", "Cereals and Breakfast", "Sauces, Spreads and Dips", "Chocolates and Biscuits", "Cooking and Baking Needs", "Tinned and Processed Food", "Atta, Flours and Sooji", "Rice and Rice Products", "Dals and Pulses", "Salt, Sugar and Jaggery", "Energy and Soft Drinks", "Water", "Tea and Coffee", "Fruit Juices and Fruit Drinks", "Snacks and Namkeen", "Ready to Cook and Eat", "Pickles and Chutney", "Indian Sweets", "Frozen Vegetables", "Frozen Snacks", "Gift Voucher"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_PROMOS_CATEGORY","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value","var_enum_promo_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Bakery, Cakes & Dairy","Pet Care","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_promo_categories"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_PROMOS_CATEGORY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_PROMOS_CATEGORY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_PROMOS_CATEGORY","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value","var_enum_promo_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Bakery, Cakes & Dairy","Pet Care","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_promo_categories"}
                        """
                            }}] + sub_results

                        def TAGS_BAP_PROMOS_FROM(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_PROMOS_FROM_obj in scope:
                                TAGS_BAP_PROMOS_FROM_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_PROMOS_FROM_obj, "$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value")
                                var_datetime_regex = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, var_datetime_regex)

                                if not validate:
                                    del TAGS_BAP_PROMOS_FROM_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_PROMOS_FROM",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_PROMOS_FROM**

                        - All elements of $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_PROMOS_FROM","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_PROMOS_FROM_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_PROMOS_FROM",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_PROMOS_FROM","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                            }}] + sub_results

                        def TAGS_BAP_PROMOS_TO(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BAP_PROMOS_TO_obj in scope:
                                TAGS_BAP_PROMOS_TO_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BAP_PROMOS_TO_obj, "$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value")
                                var_datetime_regex = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["follow_regex"](attr, var_datetime_regex)

                                if not validate:
                                    del TAGS_BAP_PROMOS_TO_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BAP_PROMOS_TO",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BAP_PROMOS_TO**

                        - All elements of $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_PROMOS_TO","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                                        }
                                    }]

                                # del TAGS_BAP_PROMOS_TO_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_PROMOS_TO",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_PROMOS_TO","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_BAP_PROMOS_CATEGORY,
                            TAGS_BAP_PROMOS_FROM,
                            TAGS_BAP_PROMOS_TO,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TAGS_BAP_PROMOS_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TAGS_BAP_PROMOS",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TAGS_BAP_PROMOS","_RETURN_":[{"_NAME_":"TAGS_BAP_PROMOS_CATEGORY","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value","var_enum_promo_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Bakery, Cakes & Dairy","Pet Care","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_promo_categories"},{"_NAME_":"TAGS_BAP_PROMOS_FROM","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_BAP_PROMOS_TO","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}]}
                """
                    }}] + sub_results

                def TAGS_BNP_DEMAND_SIGNAL(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for TAGS_BNP_DEMAND_SIGNAL_obj in scope:
                        TAGS_BNP_DEMAND_SIGNAL_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM_obj in scope:
                                TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM_obj, "$.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM**

                        - $.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM","attr":"$.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM","attr":"$.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del TAGS_BNP_DEMAND_SIGNAL_obj["_EXTERNAL"]

                    return [{
                        "test_name": "TAGS_BNP_DEMAND_SIGNAL",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"TAGS_BNP_DEMAND_SIGNAL","_RETURN_":[{"_NAME_":"TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM","attr":"$.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                test_functions = [
                    SEARCH_TAG_INTENT_GROUP,
                    TAGS_BNP_FEATURES,
                    TAGS_BAP_TERMS,
                    TAGS_CATALOG_FULL,
                    TAGS_CATALOG_INC,
                    TAGS_BAP_FEATURES,
                    TAGS_BAP_PROMOS,
                    TAGS_BNP_DEMAND_SIGNAL,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del SEARCH_TAGS_obj["_EXTERNAL"]

            return [{
                "test_name": "SEARCH_TAGS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SEARCH_TAGS","_RETURN_":[{"_NAME_":"SEARCH_TAG_INTENT_GROUP","code":"$.message.intent.tags[*].code","_CONTINUE_":"!(code are present)","var_codes":["catalog_inc","bap_terms","catalog_full","bnp_features","bap_features","bap_promos","bnp_demand_signal"],"_RETURN_":"code all in var_codes"},{"_NAME_":"TAGS_BNP_FEATURES","_RETURN_":[{"_NAME_":"TAGS_BNP_FEATURES_PAYLOAD_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value","var_payload_types":["link","inline"],"_RETURN_":"attr any in var_payload_types"}]},{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS_NEW","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value","var_enum_static_terms_new":["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"],"_RETURN_":"attr all in var_enum_static_terms_new"},{"_NAME_":"TAGS_BAP_TERMS_EFFECTIVE_DATE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value","var_date_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex var_date_regex"}]},{"_NAME_":"TAGS_CATALOG_FULL","_RETURN_":[{"_NAME_":"TAGS_CATALOG_FULL_PAYLOAD_TYPE","attr":"$.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value","var_enum_payload_type":["link"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_payload_type"}]},{"_NAME_":"TAGS_CATALOG_INC","_RETURN_":[{"_NAME_":"TAGS_CATALOG_INC_START_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_CATALOG_INC_END_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_CATALOG_INC_MODE","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value","var_enum_mode":["start","stop"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_mode"}]},{"_NAME_":"TAGS_BAP_FEATURES","_RETURN_":[{"_NAME_":"TAGS_BAP_FEATURES_ITEM_1","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"},{"_NAME_":"TAGS_BAP_FEATURES_ITEM_2","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"},{"_NAME_":"TAGS_BAP_FEATURES_ITEM_3","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}]},{"_NAME_":"TAGS_BAP_PROMOS","_RETURN_":[{"_NAME_":"TAGS_BAP_PROMOS_CATEGORY","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value","var_enum_promo_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Bakery, Cakes & Dairy","Pet Care","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_promo_categories"},{"_NAME_":"TAGS_BAP_PROMOS_FROM","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_BAP_PROMOS_TO","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}]},{"_NAME_":"TAGS_BNP_DEMAND_SIGNAL","_RETURN_":[{"_NAME_":"TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM","attr":"$.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}
        """
            }}] + sub_results

        test_functions = [
            SEARCH_CONTEXT,
            SEARCH_PAYMENT,
            SEARCH_FULFILMENT,
            SEARCH_ITEM,
            SEARCH_CATEGORY,
            SEARCH_TAGS,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del search_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "search_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"search_validations","_RETURN_":[{"_NAME_":"SEARCH_CONTEXT","_DESCRIPTION_":"Validate search context","action":["search"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["search"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["search"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["search"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["search"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["search"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["search"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["search"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["search"]}]}]},{"_NAME_":"SEARCH_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_REQUIRED","_RETURN_":[{"_NAME_":"PAYMENT_REQUIRED_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_REQUIRED_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","_RETURN_":"attr are present"}]},{"_NAME_":"PAYMENT_ENUM","_RETURN_":[{"_NAME_":"PAYMENT_ENUM_TYPE","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_type']","var_fee_type":["percent","amount"],"_RETURN_":"attr all in var_fee_type"},{"_NAME_":"PAYMENT_REGEX_AMOUNT","attr":"$.message.intent.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr follow regex reg"}]}]},{"_NAME_":"SEARCH_FULFILMENT","_RETURN_":[{"_NAME_":"FULFILMENT_REQUIRED","_RETURN_":[{"_NAME_":"FULFILMENT_REQUIRED_TYPE","attr":"$.message.intent.fulfillment.type","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_GPS","attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"FULFILMENT_REQUIRED_END_LOCATION_AREA_CODE","attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILMENT_ENUM","_RETURN_":[{"_NAME_":"FULFILMENT_ENUM_TYPE","attr":"$.message.intent.fulfillment.type","var_types":["Delivery","Self-Pickup","Buyer-Delivery"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_types"}]}]},{"_NAME_":"SEARCH_ITEM","_RETURN_":[{"_NAME_":"ITEM_REQUIRED_DESCRIPTOR_NAME","attr":"$.message.intent.item.descriptor.name","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"SEARCH_CATEGORY","_RETURN_":[{"_NAME_":"CATEGORY_REQUIRED_ID","attr":"$.message.intent.category.id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"SEARCH_TAGS","_RETURN_":[{"_NAME_":"SEARCH_TAG_INTENT_GROUP","code":"$.message.intent.tags[*].code","_CONTINUE_":"!(code are present)","var_codes":["catalog_inc","bap_terms","catalog_full","bnp_features","bap_features","bap_promos","bnp_demand_signal"],"_RETURN_":"code all in var_codes"},{"_NAME_":"TAGS_BNP_FEATURES","_RETURN_":[{"_NAME_":"TAGS_BNP_FEATURES_PAYLOAD_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bnp_features')].list[?(@.code=='payload_type')].value","var_payload_types":["link","inline"],"_RETURN_":"attr any in var_payload_types"}]},{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BAP_TERMS_STATIC_TERMS_NEW","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='static_terms_new')].value","var_enum_static_terms_new":["https://github.com/ONDC-Official/NP-Static-Terms/buyerNP_BNP/1.0/tc.pdf"],"_RETURN_":"attr all in var_enum_static_terms_new"},{"_NAME_":"TAGS_BAP_TERMS_EFFECTIVE_DATE","_CONTINUE_":"!(attr are present)","attr":"$.message.intent.tags[?(@.code=='bap_terms')].list[?(@.code=='effective_date')].value","var_date_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex var_date_regex"}]},{"_NAME_":"TAGS_CATALOG_FULL","_RETURN_":[{"_NAME_":"TAGS_CATALOG_FULL_PAYLOAD_TYPE","attr":"$.message.intent.tags[?(@.code=='catalog_full')].list[?(@.code=='payload_type')].value","var_enum_payload_type":["link"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_payload_type"}]},{"_NAME_":"TAGS_CATALOG_INC","_RETURN_":[{"_NAME_":"TAGS_CATALOG_INC_START_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='start_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_CATALOG_INC_END_TIME","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='end_time')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_CATALOG_INC_MODE","attr":"$.message.intent.tags[?(@.code=='catalog_inc')].list[?(@.code=='mode')].value","var_enum_mode":["start","stop"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_mode"}]},{"_NAME_":"TAGS_BAP_FEATURES","_RETURN_":[{"_NAME_":"TAGS_BAP_FEATURES_ITEM_1","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='1')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"},{"_NAME_":"TAGS_BAP_FEATURES_ITEM_2","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='2')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"},{"_NAME_":"TAGS_BAP_FEATURES_ITEM_3","attr":"$.message.intent.tags[?(@.code=='bap_features')].list[?(@.code=='3')].value","var_enum_bap_features":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_bap_features"}]},{"_NAME_":"TAGS_BAP_PROMOS","_RETURN_":[{"_NAME_":"TAGS_BAP_PROMOS_CATEGORY","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='category')].value","var_enum_promo_categories":["Fruits and Vegetables","Masala & Seasoning","Oil & Ghee","Eggs, Meat & Fish","Bakery, Cakes & Dairy","Pet Care","Detergents and Dishwash","Dairy and Cheese","Snacks, Dry Fruits, Nuts","Pasta, Soup and Noodles","Cereals and Breakfast","Sauces, Spreads and Dips","Chocolates and Biscuits","Cooking and Baking Needs","Tinned and Processed Food","Atta, Flours and Sooji","Rice and Rice Products","Dals and Pulses","Salt, Sugar and Jaggery","Energy and Soft Drinks","Water","Tea and Coffee","Fruit Juices and Fruit Drinks","Snacks and Namkeen","Ready to Cook and Eat","Pickles and Chutney","Indian Sweets","Frozen Vegetables","Frozen Snacks","Gift Voucher"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum_promo_categories"},{"_NAME_":"TAGS_BAP_PROMOS_FROM","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='from')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"},{"_NAME_":"TAGS_BAP_PROMOS_TO","attr":"$.message.intent.tags[?(@.code=='bap_promos')].list[?(@.code=='to')].value","var_datetime_regex":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr follow regex var_datetime_regex"}]},{"_NAME_":"TAGS_BNP_DEMAND_SIGNAL","_RETURN_":[{"_NAME_":"TAGS_BNP_DEMAND_SIGNAL_SEARCH_TERM","attr":"$.message.intent.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='search_term')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}]}
"""
    }}] + sub_results

def search(input_data):
    total_results = search_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "search_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
