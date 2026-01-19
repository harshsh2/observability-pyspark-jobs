from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def select_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for select_validations_obj in scope:
        select_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def SELECT_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SELECT_CONTEXT_obj in scope:
                SELECT_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["select"]

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
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]}
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
                                action = ["select"]

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
                        >     - ["select"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["select"]}
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
                                action = ["select"]

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
                        >     - ["select"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["select"]}
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
                                action = ["select"]

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
                        >     - all elements of ["select"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["select"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["select"]}]}
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
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["select"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["select"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["select"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["select"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["select"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["select"]}
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
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["select"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["select"]}
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
                                action = ["select"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["select"]}
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
                                action = ["select"]

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
                        >     - ["select"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["select"]}
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
                                action = ["select"]

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
                        >     - all elements of ["select"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["select"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["select"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["select"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["select"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["select"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["select"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["select"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["select"]}]}
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

                # del SELECT_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "SELECT_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SELECT_CONTEXT","_DESCRIPTION_":"Validate select context","action":["select"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["select"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["select"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["select"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["select"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["select"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["select"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["select"]}]}]}
        """
            }}] + sub_results

        def SELECT_ORDER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for SELECT_ORDER_obj in scope:
                SELECT_ORDER_obj["_EXTERNAL"] = input_data["external_data"]

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

                        def ITEMS_DESCRIPTOR_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_DESCRIPTOR_TAGS_obj in scope:
                                ITEMS_DESCRIPTOR_TAGS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_DESCRIPTOR_TAGS_obj, "$.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_DESCRIPTOR_TAGS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_DESCRIPTOR_TAGS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ITEMS_DESCRIPTOR_TAGS**

                        - $.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_DESCRIPTOR_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ITEMS_DESCRIPTOR_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ITEMS_DESCRIPTOR_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ITEMS_DESCRIPTOR_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value","_RETURN_":"attr are present"}
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

                        def ITEMS_LOCATION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ITEMS_LOCATION_ID_obj in scope:
                                ITEMS_LOCATION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ITEMS_LOCATION_ID_obj, "$.message.order.items[*].location_id")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ITEMS_LOCATION_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ITEMS_LOCATION_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ITEMS_LOCATION_ID**

                        - $.message.order.items[*].location_id must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_RETURN_":"attr are present"}
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
                        {"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_RETURN_":"attr are present"}
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
                            ITEMS_DESCRIPTOR_TAGS,
                            ITEMS_PARENT_ITEM_ID,
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
                {"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}
                """
                    }}] + sub_results

                def ORDER_OFFERS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_OFFERS_obj in scope:
                        ORDER_OFFERS_obj["_EXTERNAL"] = input_data["external_data"]

                        def OFFERS_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_ID_obj in scope:
                                OFFERS_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_ID_obj, "$.message.order.offers[*].id")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_ID**

                        - $.message.order.offers[*].id must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].id is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def OFFERS_TAGS_SELECTION_APPLY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_TAGS_SELECTION_APPLY_obj in scope:
                                OFFERS_TAGS_SELECTION_APPLY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_TAGS_SELECTION_APPLY_obj, "$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value")
                                var_enum = ["yes","no"]

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["all_in"](attr, var_enum)

                                if not validate:
                                    del OFFERS_TAGS_SELECTION_APPLY_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_TAGS_SELECTION_APPLY",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_TAGS_SELECTION_APPLY**

                        - All elements of $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_TAGS_SELECTION_APPLY","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                        """
                                        }
                                    }]

                                # del OFFERS_TAGS_SELECTION_APPLY_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_TAGS_SELECTION_APPLY",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_TAGS_SELECTION_APPLY","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}
                        """
                            }}] + sub_results

                        test_functions = [
                            OFFERS_ID,
                            OFFERS_TAGS_SELECTION_APPLY,
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
                {"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TAGS_SELECTION_APPLY","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]}
                """
                    }}] + sub_results

                def ORDER_FULFILLMENTS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_FULFILLMENTS_obj in scope:
                        ORDER_FULFILLMENTS_obj["_EXTERNAL"] = input_data["external_data"]

                        def FULFILLMENT_END_LOCATION_GPS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENT_END_LOCATION_GPS_obj in scope:
                                FULFILLMENT_END_LOCATION_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENT_END_LOCATION_GPS_obj, "$.message.order.fulfillments[*].end.location.gps")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENT_END_LOCATION_GPS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENT_END_LOCATION_GPS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENT_END_LOCATION_GPS**

                        - $.message.order.fulfillments[*].end.location.gps must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENT_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENT_END_LOCATION_GPS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENT_END_LOCATION_GPS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENT_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE_obj in scope:
                                FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE_obj, "$.message.order.fulfillments[*].end.location.address.area_code")

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE**

                        - $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            FULFILLMENT_END_LOCATION_GPS,
                            FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE,
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
                {"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENT_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_TAGS_obj in scope:
                        ORDER_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def ORDER_TAGS_TYPE(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ORDER_TAGS_TYPE_obj in scope:
                                ORDER_TAGS_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ORDER_TAGS_TYPE_obj, "$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ORDER_TAGS_TYPE_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ORDER_TAGS_TYPE",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ORDER_TAGS_TYPE**

                        - $.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ORDER_TAGS_TYPE","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ORDER_TAGS_TYPE_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ORDER_TAGS_TYPE",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ORDER_TAGS_TYPE","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def ORDER_TAGS_PARENT_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ORDER_TAGS_PARENT_ID_obj in scope:
                                ORDER_TAGS_PARENT_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](ORDER_TAGS_PARENT_ID_obj, "$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del ORDER_TAGS_PARENT_ID_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "ORDER_TAGS_PARENT_ID",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **ORDER_TAGS_PARENT_ID**

                        - $.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"ORDER_TAGS_PARENT_ID","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del ORDER_TAGS_PARENT_ID_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ORDER_TAGS_PARENT_ID",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ORDER_TAGS_PARENT_ID","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            ORDER_TAGS_TYPE,
                            ORDER_TAGS_PARENT_ID,
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
                {"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"ORDER_TAGS_TYPE","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ORDER_TAGS_PARENT_ID","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_PROVIDER,
                    ORDER_ITEMS,
                    ORDER_OFFERS,
                    ORDER_FULFILLMENTS,
                    ORDER_TAGS,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del SELECT_ORDER_obj["_EXTERNAL"]

            return [{
                "test_name": "SELECT_ORDER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"SELECT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TAGS_SELECTION_APPLY","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENT_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"ORDER_TAGS_TYPE","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ORDER_TAGS_PARENT_ID","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}
        """
            }}] + sub_results

        test_functions = [
            SELECT_CONTEXT,
            SELECT_ORDER,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del select_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "select_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"select_validations","_RETURN_":[{"_NAME_":"SELECT_CONTEXT","_DESCRIPTION_":"Validate select context","action":["select"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["select"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["select"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["select"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["select"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["select"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["select"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["select"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["select"]}]}]},{"_NAME_":"SELECT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_DESCRIPTOR_TAGS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].descriptor.tags[?(@.code=='customization')].list[?(@.code=='input_text')].value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_LOCATION_ID","attr":"$.message.order.items[*].location_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TAGS_SELECTION_APPLY","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enum":["yes","no"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENT_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENT_END_LOCATION_ADDRESS_AREA_CODE","attr":"$.message.order.fulfillments[*].end.location.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"ORDER_TAGS_TYPE","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='source')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ORDER_TAGS_PARENT_ID","attr":"$.message.order.tags[?(@.code=='bnp_demand_signal')].list[?(@.code=='campaign')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}]}]}]}
"""
    }}] + sub_results

def select(input_data):
    total_results = select_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "select_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
