from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def init_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for init_validations_obj in scope:
        init_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def INIT_CONTEXT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for INIT_CONTEXT_obj in scope:
                INIT_CONTEXT_obj["_EXTERNAL"] = input_data["external_data"]
                action = ["init"]

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
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_ACTION_obj in scope:
                                CONTEXT_REQUIRED_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_ACTION_obj, "$.context.action")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_COUNTRY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_COUNTRY_obj in scope:
                                CONTEXT_REQUIRED_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_COUNTRY_obj, "$.context.country")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_VERSION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_VERSION_obj in scope:
                                CONTEXT_REQUIRED_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_VERSION_obj, "$.context.core_version")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_ID_obj in scope:
                                CONTEXT_REQUIRED_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_ID_obj, "$.context.bap_id")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_BAP_URI(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_BAP_URI_obj in scope:
                                CONTEXT_REQUIRED_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BAP_URI_obj, "$.context.bap_uri")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]}
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
                                action = ["init"]

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
                        >     - ["init"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["init"]}
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
                                action = ["init"]

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
                        >     - ["init"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TRANSACTION_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TRANSACTION_ID_obj in scope:
                                CONTEXT_REQUIRED_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TRANSACTION_ID_obj, "$.context.transaction_id")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_MESSAGE_ID(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_MESSAGE_ID_obj in scope:
                                CONTEXT_REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_MESSAGE_ID_obj, "$.context.message_id")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_REQUIRED_TIMESTAMP(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_TIMESTAMP_obj in scope:
                                CONTEXT_REQUIRED_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_TIMESTAMP_obj, "$.context.timestamp")
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["init"]}
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
                                action = ["init"]

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
                        >     - all elements of ["init"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["init"]}
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["init"]}]}
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
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["init"]}
                        """
                            }}] + sub_results

                        def CONTEXT_ENUM_ACTION(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_ENUM_ACTION_obj in scope:
                                CONTEXT_ENUM_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_ACTION_obj, "$.context.action")
                                action = ["init"]

                                validate = validation_utils["equal_to"](attr, action)

                                if not validate:
                                    del CONTEXT_ENUM_ACTION_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "CONTEXT_ENUM_ACTION",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["init"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["init"]}
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
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["init"]}
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
                                action = ["init"]

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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["init"]}
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
                                action = ["init"]

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
                        >     - ["init"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["init"]}
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
                                action = ["init"]

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
                        >     - all elements of ["init"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["init"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["init"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["init"]}]}
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

                # del INIT_CONTEXT_obj["_EXTERNAL"]

            return [{
                "test_name": "INIT_CONTEXT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"INIT_CONTEXT","_DESCRIPTION_":"Validate init context","action":["init"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["init"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["init"]}]}]}
        """
            }}] + sub_results

        def INIT_ORDER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for INIT_ORDER_obj in scope:
                INIT_ORDER_obj["_EXTERNAL"] = input_data["external_data"]

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

                        def OFFERS_TAGS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_TAGS_obj in scope:
                                OFFERS_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                                def OFFERS_TAGS_SELECTION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for OFFERS_TAGS_SELECTION_obj in scope:
                                        OFFERS_TAGS_SELECTION_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](OFFERS_TAGS_SELECTION_obj, "$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value")
                                        var_enums = ["yes","no"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enums)

                                        if not validate:
                                            del OFFERS_TAGS_SELECTION_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "OFFERS_TAGS_SELECTION",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **OFFERS_TAGS_SELECTION**

                                - All elements of $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value must be in ["yes", "no"]

                                > **Skip if:**
                                >
                                >     - $.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"OFFERS_TAGS_SELECTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enums":["yes","no"],"_RETURN_":"attr all in var_enums"}
                                """
                                                }
                                            }]

                                        # del OFFERS_TAGS_SELECTION_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "OFFERS_TAGS_SELECTION",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"OFFERS_TAGS_SELECTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enums":["yes","no"],"_RETURN_":"attr all in var_enums"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    OFFERS_TAGS_SELECTION,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del OFFERS_TAGS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_TAGS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_TAGS","_RETURN_":[{"_NAME_":"OFFERS_TAGS_SELECTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enums":["yes","no"],"_RETURN_":"attr all in var_enums"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            OFFERS_ID,
                            OFFERS_TAGS,
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
                {"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TAGS","_RETURN_":[{"_NAME_":"OFFERS_TAGS_SELECTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enums":["yes","no"],"_RETURN_":"attr all in var_enums"}]}]}
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

                def BILLING_TAX_NUMBER(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for BILLING_TAX_NUMBER_obj in scope:
                        BILLING_TAX_NUMBER_obj["_EXTERNAL"] = input_data["external_data"]
                        attr = payload_utils["get_json_path"](BILLING_TAX_NUMBER_obj, "$.message.order.billing.tax_number")

                        skip_check = not (validation_utils["are_present"](attr))
                        if skip_check:
                            continue

                        validate = validation_utils["are_present"](attr)

                        if not validate:
                            del BILLING_TAX_NUMBER_obj["_EXTERNAL"]
                            return [{
                                "test_name": "BILLING_TAX_NUMBER",
                                "valid": False,
                                "code": 30000,
                                "description": r"""#### **BILLING_TAX_NUMBER**

                - $.message.order.billing.tax_number must be present in the payload

                > **Skip if:**
                >
                >     - $.message.order.billing.tax_number is not in the payload""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"BILLING_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
                """
                                }
                            }]

                        # del BILLING_TAX_NUMBER_obj["_EXTERNAL"]

                    return [{
                        "test_name": "BILLING_TAX_NUMBER",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"BILLING_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"}
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
                                        "description": r"""#### **FULFILLMENTS_END_LOCATION_GPS**

                        - $.message.order.fulfillments[*].end.location.gps must be present in the payload""",
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
                                        "description": r"""#### **FULFILLMENTS_END_CONTACT_PHONE**

                        - $.message.order.fulfillments[*].end.contact.phone must be present in the payload""",
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
                {"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]}
                """
                    }}] + sub_results

                def ORDER_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_TAGS_obj in scope:
                        ORDER_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def ORDER_TAGS_BAP_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for ORDER_TAGS_BAP_TERMS_obj in scope:
                                ORDER_TAGS_BAP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE_obj in scope:
                                        ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE_obj, "$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value")
                                        var_enum = ["percent","amount"]

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["all_in"](attr, var_enum)

                                        if not validate:
                                            del ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE**

                                - All elements of $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value must be in ["percent", "amount"]

                                > **Skip if:**
                                >
                                >     - $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                """
                                                }
                                            }]

                                        # del ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"}
                                """
                                    }}] + sub_results

                                def ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE_obj in scope:
                                        ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE_obj, "$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE**

                                - $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE,
                                    ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE,
                                ]

                                all_results = []
                                for fn in test_functions:
                                    sub_result = fn(input_data)
                                    all_results.extend(sub_result)

                                sub_results = all_results
                                valid = all(r["valid"] for r in sub_results)

                                # del ORDER_TAGS_BAP_TERMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "ORDER_TAGS_BAP_TERMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"ORDER_TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        test_functions = [
                            ORDER_TAGS_BAP_TERMS,
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
                {"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}]}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_PROVIDER,
                    ORDER_ITEMS,
                    ORDER_OFFERS,
                    ORDER_BILLING,
                    BILLING_TAX_NUMBER,
                    ORDER_FULFILLMENTS,
                    ORDER_TAGS,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del INIT_ORDER_obj["_EXTERNAL"]

            return [{
                "test_name": "INIT_ORDER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"INIT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TAGS","_RETURN_":[{"_NAME_":"OFFERS_TAGS_SELECTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enums":["yes","no"],"_RETURN_":"attr all in var_enums"}]}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}]}]}
        """
            }}] + sub_results

        test_functions = [
            INIT_CONTEXT,
            INIT_ORDER,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del init_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "init_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"init_validations","_RETURN_":[{"_NAME_":"INIT_CONTEXT","_DESCRIPTION_":"Validate init context","action":["init"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["init"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["init"]}]}]},{"_NAME_":"INIT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","attr":"$.message.order.offers[*].id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TAGS","_RETURN_":[{"_NAME_":"OFFERS_TAGS_SELECTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].tags[?(@.code=='selection')].list[?(@.code=='apply')].value","var_enums":["yes","no"],"_RETURN_":"attr all in var_enums"}]}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}]}]}]}
"""
    }}] + sub_results

def init(input_data):
    total_results = init_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "init_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
