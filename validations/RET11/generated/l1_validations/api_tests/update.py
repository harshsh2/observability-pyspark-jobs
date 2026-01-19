from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def update_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for update_validations_obj in scope:
        update_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def UPDATE_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for UPDATE_CONTEXT_obj in scope:
                UPDATE_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["update"]

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
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]}
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
                                action = ["update"]

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
                        >     - ["update"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["update"]}
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
                                action = ["update"]

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
                        >     - ["update"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["update"]}
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
                                action = ["update"]

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
                        >     - all elements of ["update"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["update"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["update"]}]}
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
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["update"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["update"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["update"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["update"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["update"]}
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
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["update"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["update"]}
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
                                action = ["update"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["update"]}
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
                                action = ["update"]

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
                        >     - ["update"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["update"]}
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
                                action = ["update"]

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
                        >     - all elements of ["update"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["update"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["update"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["update"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["update"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["update"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["update"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["update"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["update"]}]}
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

                # del UPDATE_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "UPDATE_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"UPDATE_CONTEXT","_DESCRIPTION_":"Validate update context","action":["update"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["update"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["update"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["update"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["update"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["update"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["update"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["update"]}]}]}
        """
            }}] + sub_results

        def UPDATE_TARGET(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for UPDATE_TARGET_obj in scope:
                UPDATE_TARGET_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](UPDATE_TARGET_obj, "$.message.update_target")
                var_enum = ["payment","item","billing","fulfillment"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, var_enum))

                if not validate:
                    del UPDATE_TARGET_obj["_EXTERNAL"]
                    return [{
                        "test_name": "UPDATE_TARGET",
                        "valid": False,
                        "code": 30000,
                        "description": r"""#### **UPDATE_TARGET**

        **All of the following must be true:**
          - $.message.update_target must be present in the payload
          - All elements of $.message.update_target must be in ["payment", "item", "billing", "fulfillment"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"UPDATE_TARGET","attr":"$.message.update_target","var_enum":["payment","item","billing","fulfillment"],"_RETURN_":"attr are present && attr all in var_enum"}
        """
                        }
                    }]

                # del UPDATE_TARGET_obj["_EXTERNAL"]

            return [{
                "test_name": "UPDATE_TARGET",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"UPDATE_TARGET","attr":"$.message.update_target","var_enum":["payment","item","billing","fulfillment"],"_RETURN_":"attr are present && attr all in var_enum"}
        """
            }}] + sub_results

        def UPDATE_ORDER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for UPDATE_ORDER_obj in scope:
                UPDATE_ORDER_obj["_EXTERNAL"] = input_data["external_data"]

                def ORDER_ID(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_ID_obj in scope:
                        ORDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](ORDER_ID_obj, "$.message.order.id")

                        validate = validation_utils["are_present"](attr)

                        if not validate:
                            del ORDER_ID_obj["_EXTERNAL"]
                            return [{
                                "test_name": "ORDER_ID",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **ORDER_ID**

                - $.message.order.id must be present in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"ORDER_ID","attr":"$.message.order.id","_RETURN_":"attr are present"}
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
                {"_NAME_":"ORDER_ID","attr":"$.message.order.id","_RETURN_":"attr are present"}
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

                        def FULFILLMENTS_END(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_END_obj in scope:
                                FULFILLMENTS_END_obj["_EXTERNAL"] = input_data["external_data"]

                                def FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj in scope:
                                        FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj, "$.message.order.fulfillments[*].end.instructions.additional_desc.content_type")
                                        var_enum = ["text/plain","text/html"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE**

                                - $.message.order.fulfillments[*].end.instructions.additional_desc.content_type must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].end.instructions.additional_desc.content_type is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","attr":"$.message.order.fulfillments[*].end.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","attr":"$.message.order.fulfillments[*].end.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE,
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
                        {"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","attr":"$.message.order.fulfillments[*].end.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def FULFILLMENTS_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENTS_TAGS_obj in scope:
                                FULFILLMENTS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_RETURN_REQUEST(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_RETURN_REQUEST_obj in scope:
                                        TAGS_RETURN_REQUEST_obj["_EXTERNAL"] = input_data["external_data"]

                                        def RETURN_REQUEST_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_ID_obj in scope:
                                                RETURN_REQUEST_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RETURN_REQUEST_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_ITEM_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_ITEM_ID_obj in scope:
                                                RETURN_REQUEST_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_ITEM_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RETURN_REQUEST_ITEM_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_ITEM_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_ITEM_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_ITEM_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_ITEM_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_PARENT_ITEM_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_PARENT_ITEM_ID_obj in scope:
                                                RETURN_REQUEST_PARENT_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_PARENT_ITEM_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RETURN_REQUEST_PARENT_ITEM_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_PARENT_ITEM_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_PARENT_ITEM_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_PARENT_ITEM_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_PARENT_ITEM_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_ITEM_QUANTITY(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_ITEM_QUANTITY_obj in scope:
                                                RETURN_REQUEST_ITEM_QUANTITY_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_ITEM_QUANTITY_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RETURN_REQUEST_ITEM_QUANTITY_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_ITEM_QUANTITY",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_ITEM_QUANTITY**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_ITEM_QUANTITY_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_ITEM_QUANTITY",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_REASON_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_REASON_ID_obj in scope:
                                                RETURN_REQUEST_REASON_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_REASON_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value")
                                                reg = ["^\\d{3}$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del RETURN_REQUEST_REASON_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_REASON_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_REASON_ID**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value must follow every regex in ["^\d{3}$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_REASON_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_REASON_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_REASON_DESC(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_REASON_DESC_obj in scope:
                                                RETURN_REQUEST_REASON_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_REASON_DESC_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RETURN_REQUEST_REASON_DESC_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_REASON_DESC",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_REASON_DESC**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_REASON_DESC_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_REASON_DESC",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_IMAGES(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_IMAGES_obj in scope:
                                                RETURN_REQUEST_IMAGES_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_IMAGES_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RETURN_REQUEST_IMAGES_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_IMAGES",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_IMAGES**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_IMAGES_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_IMAGES",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_TTL_APPROVAL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_TTL_APPROVAL_obj in scope:
                                                RETURN_REQUEST_TTL_APPROVAL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_TTL_APPROVAL_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value")
                                                reg = ["^PT[0-9]+H$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del RETURN_REQUEST_TTL_APPROVAL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_TTL_APPROVAL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_TTL_APPROVAL**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value must follow every regex in ["^PT[0-9]+H$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_TTL_APPROVAL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_TTL_APPROVAL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def RETURN_REQUEST_TTL_REVERSEQC(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RETURN_REQUEST_TTL_REVERSEQC_obj in scope:
                                                RETURN_REQUEST_TTL_REVERSEQC_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RETURN_REQUEST_TTL_REVERSEQC_obj, "$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value")
                                                reg = ["^P[0-9]+D$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del RETURN_REQUEST_TTL_REVERSEQC_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RETURN_REQUEST_TTL_REVERSEQC",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RETURN_REQUEST_TTL_REVERSEQC**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value must follow every regex in ["^P[0-9]+D$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del RETURN_REQUEST_TTL_REVERSEQC_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RETURN_REQUEST_TTL_REVERSEQC",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            RETURN_REQUEST_ID,
                                            RETURN_REQUEST_ITEM_ID,
                                            RETURN_REQUEST_PARENT_ITEM_ID,
                                            RETURN_REQUEST_ITEM_QUANTITY,
                                            RETURN_REQUEST_REASON_ID,
                                            RETURN_REQUEST_REASON_DESC,
                                            RETURN_REQUEST_IMAGES,
                                            RETURN_REQUEST_TTL_APPROVAL,
                                            RETURN_REQUEST_TTL_REVERSEQC,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_RETURN_REQUEST_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_RETURN_REQUEST",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_RETURN_REQUEST","_RETURN_":[{"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_STATE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_STATE_obj in scope:
                                        TAGS_UPDATE_STATE_obj["_EXTERNAL"] = input_data["external_data"]

                                        def UPDATE_STATE_STATE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for UPDATE_STATE_STATE_obj in scope:
                                                UPDATE_STATE_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](UPDATE_STATE_STATE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value")
                                                var_enum = ["Order-picked-up","Order-delivered"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del UPDATE_STATE_STATE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "UPDATE_STATE_STATE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **UPDATE_STATE_STATE**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del UPDATE_STATE_STATE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "UPDATE_STATE_STATE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def UPDATE_STATE_REASON_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for UPDATE_STATE_REASON_ID_obj in scope:
                                                UPDATE_STATE_REASON_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](UPDATE_STATE_REASON_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del UPDATE_STATE_REASON_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "UPDATE_STATE_REASON_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **UPDATE_STATE_REASON_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del UPDATE_STATE_REASON_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "UPDATE_STATE_REASON_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            UPDATE_STATE_STATE,
                                            UPDATE_STATE_REASON_ID,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_STATE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_STATE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_STATE","_RETURN_":[{"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_CANCEL_REQUEST(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_CANCEL_REQUEST_obj in scope:
                                        TAGS_CANCEL_REQUEST_obj["_EXTERNAL"] = input_data["external_data"]

                                        def CANCEL_REQUEST_RETRY_COUNT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for CANCEL_REQUEST_RETRY_COUNT_obj in scope:
                                                CANCEL_REQUEST_RETRY_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](CANCEL_REQUEST_RETRY_COUNT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del CANCEL_REQUEST_RETRY_COUNT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "CANCEL_REQUEST_RETRY_COUNT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **CANCEL_REQUEST_RETRY_COUNT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del CANCEL_REQUEST_RETRY_COUNT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "CANCEL_REQUEST_RETRY_COUNT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def CANCEL_REQUEST_REASON_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for CANCEL_REQUEST_REASON_ID_obj in scope:
                                                CANCEL_REQUEST_REASON_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](CANCEL_REQUEST_REASON_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del CANCEL_REQUEST_REASON_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "CANCEL_REQUEST_REASON_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **CANCEL_REQUEST_REASON_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del CANCEL_REQUEST_REASON_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "CANCEL_REQUEST_REASON_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def CANCEL_REQUEST_INITIATED_BY(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for CANCEL_REQUEST_INITIATED_BY_obj in scope:
                                                CANCEL_REQUEST_INITIATED_BY_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](CANCEL_REQUEST_INITIATED_BY_obj, "$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del CANCEL_REQUEST_INITIATED_BY_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "CANCEL_REQUEST_INITIATED_BY",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **CANCEL_REQUEST_INITIATED_BY**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del CANCEL_REQUEST_INITIATED_BY_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "CANCEL_REQUEST_INITIATED_BY",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            CANCEL_REQUEST_RETRY_COUNT,
                                            CANCEL_REQUEST_REASON_ID,
                                            CANCEL_REQUEST_INITIATED_BY,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_CANCEL_REQUEST_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_CANCEL_REQUEST",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_CANCEL_REQUEST","_RETURN_":[{"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_FULFILLMENT_TIME(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_FULFILLMENT_TIME_obj in scope:
                                        TAGS_UPDATE_FULFILLMENT_TIME_obj["_EXTERNAL"] = input_data["external_data"]

                                        def UPDATE_FULFILLMENT_TIME_STATE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for UPDATE_FULFILLMENT_TIME_STATE_obj in scope:
                                                UPDATE_FULFILLMENT_TIME_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](UPDATE_FULFILLMENT_TIME_STATE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value")
                                                var_enum = ["Order-picked-up"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del UPDATE_FULFILLMENT_TIME_STATE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "UPDATE_FULFILLMENT_TIME_STATE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **UPDATE_FULFILLMENT_TIME_STATE**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value must be in ["Order-picked-up"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del UPDATE_FULFILLMENT_TIME_STATE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "UPDATE_FULFILLMENT_TIME_STATE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def UPDATE_FULFILLMENT_TIME_TIMESTAMP(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for UPDATE_FULFILLMENT_TIME_TIMESTAMP_obj in scope:
                                                UPDATE_FULFILLMENT_TIME_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](UPDATE_FULFILLMENT_TIME_TIMESTAMP_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del UPDATE_FULFILLMENT_TIME_TIMESTAMP_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "UPDATE_FULFILLMENT_TIME_TIMESTAMP",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **UPDATE_FULFILLMENT_TIME_TIMESTAMP**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del UPDATE_FULFILLMENT_TIME_TIMESTAMP_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "UPDATE_FULFILLMENT_TIME_TIMESTAMP",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def UPDATE_FULFILLMENT_TIME_START(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for UPDATE_FULFILLMENT_TIME_START_obj in scope:
                                                UPDATE_FULFILLMENT_TIME_START_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](UPDATE_FULFILLMENT_TIME_START_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del UPDATE_FULFILLMENT_TIME_START_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "UPDATE_FULFILLMENT_TIME_START",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **UPDATE_FULFILLMENT_TIME_START**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del UPDATE_FULFILLMENT_TIME_START_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "UPDATE_FULFILLMENT_TIME_START",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def UPDATE_FULFILLMENT_TIME_END(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for UPDATE_FULFILLMENT_TIME_END_obj in scope:
                                                UPDATE_FULFILLMENT_TIME_END_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](UPDATE_FULFILLMENT_TIME_END_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del UPDATE_FULFILLMENT_TIME_END_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "UPDATE_FULFILLMENT_TIME_END",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **UPDATE_FULFILLMENT_TIME_END**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del UPDATE_FULFILLMENT_TIME_END_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "UPDATE_FULFILLMENT_TIME_END",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            UPDATE_FULFILLMENT_TIME_STATE,
                                            UPDATE_FULFILLMENT_TIME_TIMESTAMP,
                                            UPDATE_FULFILLMENT_TIME_START,
                                            UPDATE_FULFILLMENT_TIME_END,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_FULFILLMENT_TIME_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_FULFILLMENT_TIME",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_FULFILLMENT_TIME","_RETURN_":[{"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_AGENT_DETAILS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_AGENT_DETAILS_obj in scope:
                                        TAGS_UPDATE_AGENT_DETAILS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def AGENT_NAME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for AGENT_NAME_obj in scope:
                                                AGENT_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](AGENT_NAME_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del AGENT_NAME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "AGENT_NAME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **AGENT_NAME**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del AGENT_NAME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "AGENT_NAME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def AGENT_PHONE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for AGENT_PHONE_obj in scope:
                                                AGENT_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](AGENT_PHONE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del AGENT_PHONE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "AGENT_PHONE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **AGENT_PHONE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del AGENT_PHONE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "AGENT_PHONE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def AGENT_PROVIDER_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for AGENT_PROVIDER_ID_obj in scope:
                                                AGENT_PROVIDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](AGENT_PROVIDER_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del AGENT_PROVIDER_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "AGENT_PROVIDER_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **AGENT_PROVIDER_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del AGENT_PROVIDER_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "AGENT_PROVIDER_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            AGENT_NAME,
                                            AGENT_PHONE,
                                            AGENT_PROVIDER_ID,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_AGENT_DETAILS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_AGENT_DETAILS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_AGENT_DETAILS","_RETURN_":[{"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_LABEL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_LABEL_obj in scope:
                                        TAGS_UPDATE_LABEL_obj["_EXTERNAL"] = input_data["external_data"]

                                        def LABEL_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LABEL_TYPE_obj in scope:
                                                LABEL_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LABEL_TYPE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value")
                                                var_enum = ["webp","png","jpeg","pdf"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del LABEL_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LABEL_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LABEL_TYPE**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value must be in ["webp", "png", "jpeg", "pdf"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del LABEL_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LABEL_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def LABEL_URL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LABEL_URL_obj in scope:
                                                LABEL_URL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LABEL_URL_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LABEL_URL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LABEL_URL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LABEL_URL**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LABEL_URL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LABEL_URL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LABEL_SHIPPING(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LABEL_SHIPPING_obj in scope:
                                                LABEL_SHIPPING_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LABEL_SHIPPING_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LABEL_SHIPPING_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LABEL_SHIPPING",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LABEL_SHIPPING**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LABEL_SHIPPING_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LABEL_SHIPPING",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            LABEL_TYPE,
                                            LABEL_URL,
                                            LABEL_SHIPPING,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_LABEL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_LABEL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_LABEL","_RETURN_":[{"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"},{"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_REVERSEQC_OUTPUT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_REVERSEQC_OUTPUT_obj in scope:
                                        TAGS_REVERSEQC_OUTPUT_obj["_EXTERNAL"] = input_data["external_data"]

                                        def RQC_P001(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RQC_P001_obj in scope:
                                                RQC_P001_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RQC_P001_obj, "$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RQC_P001_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RQC_P001",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RQC_P001**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RQC_P001_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RQC_P001",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RQC_P003(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RQC_P003_obj in scope:
                                                RQC_P003_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RQC_P003_obj, "$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del RQC_P003_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RQC_P003",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RQC_P003**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del RQC_P003_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RQC_P003",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def RQC_Q001(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for RQC_Q001_obj in scope:
                                                RQC_Q001_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](RQC_Q001_obj, "$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value")
                                                var_enum = ["yes","no"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del RQC_Q001_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "RQC_Q001",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **RQC_Q001**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value must be in ["yes", "no"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del RQC_Q001_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "RQC_Q001",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            RQC_P001,
                                            RQC_P003,
                                            RQC_Q001,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_REVERSEQC_OUTPUT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_REVERSEQC_OUTPUT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_REVERSEQC_OUTPUT","_RETURN_":[{"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                def TAGS_BNP_RECEIVABLES_CLAIM(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BNP_RECEIVABLES_CLAIM_obj in scope:
                                        TAGS_BNP_RECEIVABLES_CLAIM_obj["_EXTERNAL"] = input_data["external_data"]

                                        def CLAIM_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for CLAIM_TYPE_obj in scope:
                                                CLAIM_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](CLAIM_TYPE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del CLAIM_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "CLAIM_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **CLAIM_TYPE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del CLAIM_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "CLAIM_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def CLAIM_CURRENCY(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for CLAIM_CURRENCY_obj in scope:
                                                CLAIM_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](CLAIM_CURRENCY_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del CLAIM_CURRENCY_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "CLAIM_CURRENCY",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **CLAIM_CURRENCY**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del CLAIM_CURRENCY_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "CLAIM_CURRENCY",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def CLAIM_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for CLAIM_VALUE_obj in scope:
                                                CLAIM_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](CLAIM_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del CLAIM_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "CLAIM_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **CLAIM_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del CLAIM_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "CLAIM_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            CLAIM_TYPE,
                                            CLAIM_CURRENCY,
                                            CLAIM_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_BNP_RECEIVABLES_CLAIM_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BNP_RECEIVABLES_CLAIM",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BNP_RECEIVABLES_CLAIM","_RETURN_":[{"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_BNP_DIFF_WEIGHT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BNP_DIFF_WEIGHT_obj in scope:
                                        TAGS_BNP_DIFF_WEIGHT_obj["_EXTERNAL"] = input_data["external_data"]

                                        def DIFF_WEIGHT_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_WEIGHT_UNIT_obj in scope:
                                                DIFF_WEIGHT_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_WEIGHT_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value")
                                                var_enum = ["unit","dozen","gram","kilogram","tonne","litre","millilitre"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del DIFF_WEIGHT_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_WEIGHT_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_WEIGHT_UNIT**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value must be in ["unit", "dozen", "gram", "kilogram", "tonne", "litre", "millilitre"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_WEIGHT_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_WEIGHT_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def DIFF_WEIGHT_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_WEIGHT_VALUE_obj in scope:
                                                DIFF_WEIGHT_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_WEIGHT_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DIFF_WEIGHT_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_WEIGHT_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_WEIGHT_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_WEIGHT_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_WEIGHT_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            DIFF_WEIGHT_UNIT,
                                            DIFF_WEIGHT_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_BNP_DIFF_WEIGHT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BNP_DIFF_WEIGHT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BNP_DIFF_WEIGHT","_RETURN_":[{"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_BNP_DIFF_LENGTH(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BNP_DIFF_LENGTH_obj in scope:
                                        TAGS_BNP_DIFF_LENGTH_obj["_EXTERNAL"] = input_data["external_data"]

                                        def DIFF_LENGTH_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_LENGTH_UNIT_obj in scope:
                                                DIFF_LENGTH_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_LENGTH_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value")
                                                var_enum = ["centimeter","meter"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del DIFF_LENGTH_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_LENGTH_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_LENGTH_UNIT**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value must be in ["centimeter", "meter"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_LENGTH_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_LENGTH_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def DIFF_LENGTH_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_LENGTH_VALUE_obj in scope:
                                                DIFF_LENGTH_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_LENGTH_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DIFF_LENGTH_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_LENGTH_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_LENGTH_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_LENGTH_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_LENGTH_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            DIFF_LENGTH_UNIT,
                                            DIFF_LENGTH_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_BNP_DIFF_LENGTH_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BNP_DIFF_LENGTH",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BNP_DIFF_LENGTH","_RETURN_":[{"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_BNP_DIFF_BREADTH(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BNP_DIFF_BREADTH_obj in scope:
                                        TAGS_BNP_DIFF_BREADTH_obj["_EXTERNAL"] = input_data["external_data"]

                                        def DIFF_BREADTH_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_BREADTH_UNIT_obj in scope:
                                                DIFF_BREADTH_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_BREADTH_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DIFF_BREADTH_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_BREADTH_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_BREADTH_UNIT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_BREADTH_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_BREADTH_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def DIFF_BREADTH_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_BREADTH_VALUE_obj in scope:
                                                DIFF_BREADTH_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_BREADTH_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DIFF_BREADTH_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_BREADTH_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_BREADTH_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_BREADTH_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_BREADTH_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            DIFF_BREADTH_UNIT,
                                            DIFF_BREADTH_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_BNP_DIFF_BREADTH_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BNP_DIFF_BREADTH",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BNP_DIFF_BREADTH","_RETURN_":[{"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_BNP_DIFF_HEIGHT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BNP_DIFF_HEIGHT_obj in scope:
                                        TAGS_BNP_DIFF_HEIGHT_obj["_EXTERNAL"] = input_data["external_data"]

                                        def DIFF_HEIGHT_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_HEIGHT_UNIT_obj in scope:
                                                DIFF_HEIGHT_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_HEIGHT_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DIFF_HEIGHT_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_HEIGHT_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_HEIGHT_UNIT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_HEIGHT_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_HEIGHT_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def DIFF_HEIGHT_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DIFF_HEIGHT_VALUE_obj in scope:
                                                DIFF_HEIGHT_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DIFF_HEIGHT_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del DIFF_HEIGHT_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DIFF_HEIGHT_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DIFF_HEIGHT_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del DIFF_HEIGHT_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DIFF_HEIGHT_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            DIFF_HEIGHT_UNIT,
                                            DIFF_HEIGHT_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_BNP_DIFF_HEIGHT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BNP_DIFF_HEIGHT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BNP_DIFF_HEIGHT","_RETURN_":[{"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_VERIFICATION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_VERIFICATION_obj in scope:
                                        TAGS_UPDATE_VERIFICATION_obj["_EXTERNAL"] = input_data["external_data"]

                                        def VERIFICATION_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for VERIFICATION_TYPE_obj in scope:
                                                VERIFICATION_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](VERIFICATION_TYPE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del VERIFICATION_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "VERIFICATION_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **VERIFICATION_TYPE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del VERIFICATION_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "VERIFICATION_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def VERIFICATION_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for VERIFICATION_VALUE_obj in scope:
                                                VERIFICATION_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](VERIFICATION_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del VERIFICATION_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "VERIFICATION_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **VERIFICATION_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del VERIFICATION_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "VERIFICATION_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            VERIFICATION_TYPE,
                                            VERIFICATION_VALUE,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_VERIFICATION_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_VERIFICATION",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_VERIFICATION","_RETURN_":[{"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_STATE_TIMESTAMPS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_STATE_TIMESTAMPS_obj in scope:
                                        TAGS_UPDATE_STATE_TIMESTAMPS_obj["_EXTERNAL"] = input_data["external_data"]

                                        def STATE_TIMESTAMP(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for STATE_TIMESTAMP_obj in scope:
                                                STATE_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](STATE_TIMESTAMP_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del STATE_TIMESTAMP_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "STATE_TIMESTAMP",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **STATE_TIMESTAMP**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del STATE_TIMESTAMP_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "STATE_TIMESTAMP",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def STATE_START_TIME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for STATE_START_TIME_obj in scope:
                                                STATE_START_TIME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](STATE_START_TIME_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del STATE_START_TIME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "STATE_START_TIME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **STATE_START_TIME**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del STATE_START_TIME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "STATE_START_TIME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def STATE_END_TIME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for STATE_END_TIME_obj in scope:
                                                STATE_END_TIME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](STATE_END_TIME_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del STATE_END_TIME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "STATE_END_TIME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **STATE_END_TIME**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del STATE_END_TIME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "STATE_END_TIME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            STATE_TIMESTAMP,
                                            STATE_START_TIME,
                                            STATE_END_TIME,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_STATE_TIMESTAMPS_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_STATE_TIMESTAMPS",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_STATE_TIMESTAMPS","_RETURN_":[{"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_FULFILLMENT_DELAY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_FULFILLMENT_DELAY_obj in scope:
                                        TAGS_UPDATE_FULFILLMENT_DELAY_obj["_EXTERNAL"] = input_data["external_data"]

                                        def DELAY_STATE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_STATE_obj in scope:
                                                DELAY_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_STATE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value")
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

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value must be in ["Order-picked-up", "Order-delivered"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"}
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
                                        {"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        def DELAY_REASON_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_REASON_ID_obj in scope:
                                                DELAY_REASON_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_REASON_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value")

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

                                        - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
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
                                        {"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def DELAY_START_TIME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_START_TIME_obj in scope:
                                                DELAY_START_TIME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_START_TIME_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del DELAY_START_TIME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DELAY_START_TIME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DELAY_START_TIME**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del DELAY_START_TIME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DELAY_START_TIME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def DELAY_END_TIME(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_END_TIME_obj in scope:
                                                DELAY_END_TIME_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_END_TIME_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value")
                                                reg = ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del DELAY_END_TIME_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DELAY_END_TIME",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DELAY_END_TIME**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del DELAY_END_TIME_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DELAY_END_TIME",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        def DELAY_ATTEMPT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for DELAY_ATTEMPT_obj in scope:
                                                DELAY_ATTEMPT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](DELAY_ATTEMPT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value")
                                                var_enum = ["yes","no"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["all_in"](attr, var_enum)

                                                if not validate:
                                                    del DELAY_ATTEMPT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "DELAY_ATTEMPT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **DELAY_ATTEMPT**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value must be in ["yes", "no"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                                        """
                                                        }
                                                    }]

                                                # del DELAY_ATTEMPT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "DELAY_ATTEMPT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            DELAY_STATE,
                                            DELAY_REASON_ID,
                                            DELAY_START_TIME,
                                            DELAY_END_TIME,
                                            DELAY_ATTEMPT,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_UPDATE_FULFILLMENT_DELAY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_FULFILLMENT_DELAY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]}
                                """
                                    }}] + sub_results

                                def TAGS_LINKED_ORDER_DIFF(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_LINKED_ORDER_DIFF_obj in scope:
                                        TAGS_LINKED_ORDER_DIFF_obj["_EXTERNAL"] = input_data["external_data"]

                                        def LINKED_ORDER_ID(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_ORDER_ID_obj in scope:
                                                LINKED_ORDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_ORDER_ID_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_ORDER_ID_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_ORDER_ID",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_ORDER_ID**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_ORDER_ID_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_ORDER_ID",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LINKED_WEIGHT_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_WEIGHT_UNIT_obj in scope:
                                                LINKED_WEIGHT_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_WEIGHT_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_WEIGHT_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_WEIGHT_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_WEIGHT_UNIT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_WEIGHT_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_WEIGHT_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LINKED_WEIGHT_VALUE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_WEIGHT_VALUE_obj in scope:
                                                LINKED_WEIGHT_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_WEIGHT_VALUE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_WEIGHT_VALUE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_WEIGHT_VALUE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_WEIGHT_VALUE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_WEIGHT_VALUE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_WEIGHT_VALUE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LINKED_DIM_UNIT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_DIM_UNIT_obj in scope:
                                                LINKED_DIM_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_DIM_UNIT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_DIM_UNIT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_DIM_UNIT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_DIM_UNIT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_DIM_UNIT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_DIM_UNIT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LINKED_LENGTH(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_LENGTH_obj in scope:
                                                LINKED_LENGTH_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_LENGTH_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_LENGTH_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_LENGTH",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_LENGTH**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_LENGTH_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_LENGTH",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LINKED_BREADTH(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_BREADTH_obj in scope:
                                                LINKED_BREADTH_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_BREADTH_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_BREADTH_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_BREADTH",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_BREADTH**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_BREADTH_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_BREADTH",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def LINKED_HEIGHT(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for LINKED_HEIGHT_obj in scope:
                                                LINKED_HEIGHT_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](LINKED_HEIGHT_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del LINKED_HEIGHT_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "LINKED_HEIGHT",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **LINKED_HEIGHT**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del LINKED_HEIGHT_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "LINKED_HEIGHT",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            LINKED_ORDER_ID,
                                            LINKED_WEIGHT_UNIT,
                                            LINKED_WEIGHT_VALUE,
                                            LINKED_DIM_UNIT,
                                            LINKED_LENGTH,
                                            LINKED_BREADTH,
                                            LINKED_HEIGHT,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_LINKED_ORDER_DIFF_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_LINKED_ORDER_DIFF",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_LINKED_ORDER_DIFF","_RETURN_":[{"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]}
                                """
                                    }}] + sub_results

                                def TAGS_LINKED_ORDER_DIFF_PROOF(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_LINKED_ORDER_DIFF_PROOF_obj in scope:
                                        TAGS_LINKED_ORDER_DIFF_PROOF_obj["_EXTERNAL"] = input_data["external_data"]

                                        def PROOF_TYPE(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for PROOF_TYPE_obj in scope:
                                                PROOF_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](PROOF_TYPE_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value")

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["are_present"](attr)

                                                if not validate:
                                                    del PROOF_TYPE_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "PROOF_TYPE",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **PROOF_TYPE**

                                        - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value must be present in the payload

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                                        }
                                                    }]

                                                # del PROOF_TYPE_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "PROOF_TYPE",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"}
                                        """
                                            }}] + sub_results

                                        def PROOF_URL(input_data):
                                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                            sub_results = []
                                            valid = True

                                            for PROOF_URL_obj in scope:
                                                PROOF_URL_obj["_EXTERNAL"] = input_data["external_data"]
                                                attr = payload_utils["get_json_path"](PROOF_URL_obj, "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value")
                                                reg = ["^https?://.*$"]

                                                skip_check = not (validation_utils["are_present"](attr))
                                                if skip_check:
                                                    continue

                                                validate = validation_utils["follow_regex"](attr, reg)

                                                if not validate:
                                                    del PROOF_URL_obj["_EXTERNAL"]
                                                    return [{
                                                        "test_name": "PROOF_URL",
                                                        "valid": False,
                                                        "code": 30000,
                                                        "description": r"""#### **PROOF_URL**

                                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]

                                        > **Skip if:**
                                        >
                                        >     - $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value is not in the payload""",
                                                        "_debug_info": {
                                                            "fed_config": r"""
                                        {"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                                        }
                                                    }]

                                                # del PROOF_URL_obj["_EXTERNAL"]

                                            return [{
                                                "test_name": "PROOF_URL",
                                                "valid": valid,
                                                "code": 200 if valid else 30000, 
                                                "_debug_info": {
                                                    "fed_config": r"""
                                        {"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}
                                        """
                                            }}] + sub_results

                                        test_functions = [
                                            PROOF_TYPE,
                                            PROOF_URL,
                                        ]

                                        all_results = []
                                        for fn in test_functions:
                                            sub_result = fn(input_data)
                                            all_results.extend(sub_result)

                                        sub_results = all_results
                                        valid = all(r["valid"] for r in sub_results)

                                        # del TAGS_LINKED_ORDER_DIFF_PROOF_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_LINKED_ORDER_DIFF_PROOF",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_LINKED_ORDER_DIFF_PROOF","_RETURN_":[{"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]}
                                """
                                    }}] + sub_results

                                def TAGS_UPDATE_SALE_INVOICE_URL(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_UPDATE_SALE_INVOICE_URL_obj in scope:
                                        TAGS_UPDATE_SALE_INVOICE_URL_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_UPDATE_SALE_INVOICE_URL_obj, "$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value")
                                        reg = ["^https?://.*$"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = (validation_utils["are_present"](attr)) and (validation_utils["follow_regex"](attr, reg))

                                        if not validate:
                                            del TAGS_UPDATE_SALE_INVOICE_URL_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_UPDATE_SALE_INVOICE_URL",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_UPDATE_SALE_INVOICE_URL**

                                **All of the following must be true:**
                                  - $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must be present in the payload
                                  - All elements of $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value must follow every regex in ["^https?://.*$"]

                                > **Skip if:**
                                >
                                >     - $.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_SALE_INVOICE_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr are present && attr follow regex reg"}
                                """
                                                }
                                            }]

                                        # del TAGS_UPDATE_SALE_INVOICE_URL_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_UPDATE_SALE_INVOICE_URL",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_UPDATE_SALE_INVOICE_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr are present && attr follow regex reg"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_RETURN_REQUEST,
                                    TAGS_UPDATE_STATE,
                                    TAGS_CANCEL_REQUEST,
                                    TAGS_UPDATE_FULFILLMENT_TIME,
                                    TAGS_UPDATE_AGENT_DETAILS,
                                    TAGS_UPDATE_LABEL,
                                    TAGS_REVERSEQC_OUTPUT,
                                    TAGS_BNP_RECEIVABLES_CLAIM,
                                    TAGS_BNP_DIFF_WEIGHT,
                                    TAGS_BNP_DIFF_LENGTH,
                                    TAGS_BNP_DIFF_BREADTH,
                                    TAGS_BNP_DIFF_HEIGHT,
                                    TAGS_UPDATE_VERIFICATION,
                                    TAGS_UPDATE_STATE_TIMESTAMPS,
                                    TAGS_UPDATE_FULFILLMENT_DELAY,
                                    TAGS_LINKED_ORDER_DIFF,
                                    TAGS_LINKED_ORDER_DIFF_PROOF,
                                    TAGS_UPDATE_SALE_INVOICE_URL,
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
                        {"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_RETURN_REQUEST","_RETURN_":[{"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_STATE","_RETURN_":[{"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_CANCEL_REQUEST","_RETURN_":[{"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_TIME","_RETURN_":[{"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_AGENT_DETAILS","_RETURN_":[{"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_LABEL","_RETURN_":[{"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"},{"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_REVERSEQC_OUTPUT","_RETURN_":[{"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_BNP_RECEIVABLES_CLAIM","_RETURN_":[{"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_WEIGHT","_RETURN_":[{"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_LENGTH","_RETURN_":[{"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_BREADTH","_RETURN_":[{"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_HEIGHT","_RETURN_":[{"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_VERIFICATION","_RETURN_":[{"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_STATE_TIMESTAMPS","_RETURN_":[{"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF","_RETURN_":[{"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF_PROOF","_RETURN_":[{"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_SALE_INVOICE_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr are present && attr follow regex reg"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILLMENTS_ID,
                            FULFILLMENTS_TYPE,
                            FULFILLMENTS_END,
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
                {"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","attr":"$.message.order.fulfillments[*].end.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_RETURN_REQUEST","_RETURN_":[{"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_STATE","_RETURN_":[{"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_CANCEL_REQUEST","_RETURN_":[{"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_TIME","_RETURN_":[{"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_AGENT_DETAILS","_RETURN_":[{"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_LABEL","_RETURN_":[{"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"},{"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_REVERSEQC_OUTPUT","_RETURN_":[{"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_BNP_RECEIVABLES_CLAIM","_RETURN_":[{"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_WEIGHT","_RETURN_":[{"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_LENGTH","_RETURN_":[{"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_BREADTH","_RETURN_":[{"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_HEIGHT","_RETURN_":[{"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_VERIFICATION","_RETURN_":[{"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_STATE_TIMESTAMPS","_RETURN_":[{"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF","_RETURN_":[{"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF_PROOF","_RETURN_":[{"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_SALE_INVOICE_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr are present && attr follow regex reg"}]}]}
                """
                    }}] + sub_results

                def ORDER_PAYMENT(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PAYMENT_obj in scope:
                        ORDER_PAYMENT_obj["_EXTERNAL"] = input_data["external_data"]

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
                                        var_enum = ["upi","neft","rtgs","wallet","netbanking","paylater","card"]

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE**

                                - All elements of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_type must be in ["upi", "neft", "rtgs", "wallet", "netbanking", "paylater", "card"]""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs","wallet","netbanking","paylater","card"],"_RETURN_":"attr all in var_enum"}
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
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs","wallet","netbanking","paylater","card"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT_obj in scope:
                                        PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT**

                                - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                                {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT,
                                    PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP,
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
                        {"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs","wallet","netbanking","paylater","card"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        test_functions = [
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
                {"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs","wallet","netbanking","paylater","card"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_ID,
                    ORDER_FULFILLMENTS,
                    ORDER_PAYMENT,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del UPDATE_ORDER_obj["_EXTERNAL"]

            return [{
                "test_name": "UPDATE_ORDER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"UPDATE_ORDER","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.order.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","attr":"$.message.order.fulfillments[*].end.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_RETURN_REQUEST","_RETURN_":[{"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_STATE","_RETURN_":[{"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_CANCEL_REQUEST","_RETURN_":[{"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_TIME","_RETURN_":[{"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_AGENT_DETAILS","_RETURN_":[{"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_LABEL","_RETURN_":[{"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"},{"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_REVERSEQC_OUTPUT","_RETURN_":[{"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_BNP_RECEIVABLES_CLAIM","_RETURN_":[{"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_WEIGHT","_RETURN_":[{"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_LENGTH","_RETURN_":[{"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_BREADTH","_RETURN_":[{"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_HEIGHT","_RETURN_":[{"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_VERIFICATION","_RETURN_":[{"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_STATE_TIMESTAMPS","_RETURN_":[{"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF","_RETURN_":[{"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF_PROOF","_RETURN_":[{"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_SALE_INVOICE_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr are present && attr follow regex reg"}]}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs","wallet","netbanking","paylater","card"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}]}
        """
            }}] + sub_results

        test_functions = [
            UPDATE_CONTEXT,
            UPDATE_TARGET,
            UPDATE_ORDER,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del update_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "update_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"update_validations","_RETURN_":[{"_NAME_":"UPDATE_CONTEXT","_DESCRIPTION_":"Validate update context","action":["update"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["update"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["update"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["update"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["update"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["update"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["update"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["update"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["update"]}]}]},{"_NAME_":"UPDATE_TARGET","attr":"$.message.update_target","var_enum":["payment","item","billing","fulfillment"],"_RETURN_":"attr are present && attr all in var_enum"},{"_NAME_":"UPDATE_ORDER","_RETURN_":[{"_NAME_":"ORDER_ID","attr":"$.message.order.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END","_RETURN_":[{"_NAME_":"FULFILLMENTS_END_INSTRUCTIONS_ADDITIONAL_DESC_CONTENT_TYPE","attr":"$.message.order.fulfillments[*].end.instructions.additional_desc.content_type","var_enum":["text/plain","text/html"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS","_RETURN_":[{"_NAME_":"TAGS_RETURN_REQUEST","_RETURN_":[{"_NAME_":"RETURN_REQUEST_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_PARENT_ITEM_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='parent_item_id')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_ITEM_QUANTITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='item_quantity')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_id')].value","reg":["^\\d{3}$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_REASON_DESC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='reason_desc')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='images')].value","_RETURN_":"attr are present"},{"_NAME_":"RETURN_REQUEST_TTL_APPROVAL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_approval')].value","reg":["^PT[0-9]+H$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"RETURN_REQUEST_TTL_REVERSEQC","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='return_request')].list[?(@.code=='ttl_reverseqc')].value","reg":["^P[0-9]+D$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_STATE","_RETURN_":[{"_NAME_":"UPDATE_STATE_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_STATE_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_CANCEL_REQUEST","_RETURN_":[{"_NAME_":"CANCEL_REQUEST_RETRY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='retry_count')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"CANCEL_REQUEST_INITIATED_BY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='cancel_request')].list[?(@.code=='initiated_by')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_TIME","_RETURN_":[{"_NAME_":"UPDATE_FULFILLMENT_TIME_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='state')].value","var_enum":["Order-picked-up"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"UPDATE_FULFILLMENT_TIME_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_time')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_AGENT_DETAILS","_RETURN_":[{"_NAME_":"AGENT_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='name')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PHONE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='phone')].value","_RETURN_":"attr are present"},{"_NAME_":"AGENT_PROVIDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_agent_details')].list[?(@.code=='provider_id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_LABEL","_RETURN_":[{"_NAME_":"LABEL_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='type')].value","var_enum":["webp","png","jpeg","pdf"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"LABEL_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='url')].value","_RETURN_":"attr are present"},{"_NAME_":"LABEL_SHIPPING","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_label')].list[?(@.code=='shipping')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_REVERSEQC_OUTPUT","_RETURN_":[{"_NAME_":"RQC_P001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P001')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_P003","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='P003')].value","_RETURN_":"attr are present"},{"_NAME_":"RQC_Q001","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_output')].list[?(@.code=='Q001')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_BNP_RECEIVABLES_CLAIM","_RETURN_":[{"_NAME_":"CLAIM_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_CURRENCY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='currency')].value","_RETURN_":"attr are present"},{"_NAME_":"CLAIM_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_receivables_claim')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_WEIGHT","_RETURN_":[{"_NAME_":"DIFF_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='unit')].value","var_enum":["unit","dozen","gram","kilogram","tonne","litre","millilitre"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_weight')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_LENGTH","_RETURN_":[{"_NAME_":"DIFF_LENGTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='unit')].value","var_enum":["centimeter","meter"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DIFF_LENGTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_length')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_BREADTH","_RETURN_":[{"_NAME_":"DIFF_BREADTH_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_BREADTH_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_breadth')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BNP_DIFF_HEIGHT","_RETURN_":[{"_NAME_":"DIFF_HEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='unit')].value","_RETURN_":"attr are present"},{"_NAME_":"DIFF_HEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='bnp_diff_height')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_VERIFICATION","_RETURN_":[{"_NAME_":"VERIFICATION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"VERIFICATION_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_verification')].list[?(@.code=='value')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_UPDATE_STATE_TIMESTAMPS","_RETURN_":[{"_NAME_":"STATE_TIMESTAMP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='timestamp')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"STATE_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_state')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_FULFILLMENT_DELAY","_RETURN_":[{"_NAME_":"DELAY_STATE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='state')].value","var_enum":["Order-picked-up","Order-delivered"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"DELAY_REASON_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='reason_id')].value","_RETURN_":"attr are present"},{"_NAME_":"DELAY_START_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='start_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_END_TIME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='end_time')].value","reg":["^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}\\\\.\\\\d{3}Z$"],"_RETURN_":"attr follow regex reg"},{"_NAME_":"DELAY_ATTEMPT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_fulfillment_delay')].list[?(@.code=='attempt')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF","_RETURN_":[{"_NAME_":"LINKED_ORDER_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"LINKED_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_LINKED_ORDER_DIFF_PROOF","_RETURN_":[{"_NAME_":"PROOF_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='type')].value","_RETURN_":"attr are present"},{"_NAME_":"PROOF_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr follow regex reg"}]},{"_NAME_":"TAGS_UPDATE_SALE_INVOICE_URL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='update_sale_invoice')].list[?(@.code=='url')].value","reg":["^https?://.*$"],"_RETURN_":"attr are present && attr follow regex reg"}]}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs","wallet","netbanking","paylater","card"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_AMOUNT","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_amount","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TIMESTAMP","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_timestamp","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}]}]}
"""
    }}] + sub_results

def update(input_data):
    total_results = update_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "update_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
