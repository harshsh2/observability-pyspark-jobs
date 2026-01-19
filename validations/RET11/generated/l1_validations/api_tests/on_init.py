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
                                        "description": r"""#### **CONTEXT_REQUIRED_DOMAIN**

                        - $.context.domain must be present in the payload""",
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
                                        "description": r"""#### **CONTEXT_REQUIRED_ACTION**

                        - $.context.action must be present in the payload""",
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
                                        "description": r"""#### **CONTEXT_REQUIRED_COUNTRY**

                        - $.context.country must be present in the payload""",
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

                        def CONTEXT_REQUIRED_CITY(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for CONTEXT_REQUIRED_CITY_obj in scope:
                                CONTEXT_REQUIRED_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_CITY_obj, "$.context.city")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_init"]}
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
                                        "description": r"""#### **CONTEXT_REQUIRED_VERSION**

                        - $.context.core_version must be present in the payload""",
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
                                        "description": r"""#### **CONTEXT_REQUIRED_BAP_ID**

                        - $.context.bap_id must be present in the payload""",
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
                                        "description": r"""#### **CONTEXT_REQUIRED_BAP_URI**

                        - $.context.bap_uri must be present in the payload""",
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
                                attr = payload_utils["get_json_path"](CONTEXT_REQUIRED_BPP_ID_obj, "$.context.bap_id")
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
                                        "description": r"""#### **CONTEXT_REQUIRED_BPP_ID**

                        - $.context.bap_id must be present in the payload

                        > **Skip if:**
                        >
                        >     - ["on_init"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]}
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
                                        "description": r"""#### **CONTEXT_REQUIRED_BPP_URI**

                        - $.context.bap_uri must be present in the payload

                        > **Skip if:**
                        >
                        >     - ["on_init"] equals ["search"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]}
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
                                        "description": r"""#### **CONTEXT_REQUIRED_TRANSACTION_ID**

                        - $.context.transaction_id must be present in the payload""",
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
                                        "description": r"""#### **CONTEXT_REQUIRED_MESSAGE_ID**

                        - $.context.message_id must be present in the payload""",
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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_init"]}
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
                                        "description": r"""#### **CONTEXT_REQUIRED_TTL**

                        - $.context.ttl must be present in the payload

                        > **Skip if:**
                        >
                        >     - all elements of ["on_init"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update", "on_status"]""",
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
                {"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}]}
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
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]}
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
                                        "description": r"""#### **CONTEXT_ENUM_ACTION**

                        - $.context.action must equal ["on_init"]""",
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
                                version = ["1.2.0","1.2.5"]
                                attr = payload_utils["get_json_path"](CONTEXT_ENUM_VERSION_obj, "$.context.core_version")
                                action = ["on_init"]

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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]}
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
                                        "description": r"""#### **CONTEXT_REG_BAP_URI**

                        - All elements of $.context.bap_uri must follow every regex in ["^https?\:\/\/"]""",
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
                                        "description": r"""#### **CONTEXT_REG_BPP_URI**

                        - All elements of $.context.bpp_uri must follow every regex in ["^https?\:\/\/"]

                        > **Skip if:**
                        >
                        >     - ["on_init"] equals ["search"]""",
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
                                optional_vars = ["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"]
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
                                        "description": r"""#### **CONTEXT_REG_TTL**

                        - All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T)(\\d+Y)?(\\d+M)?(\\d+W)?(\\d+D)?(T(?=\\d)(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

                        > **Skip if:**
                        >
                        >     - all elements of ["on_init"] are in ["on_search", "on_select", "on_confirm", "on_init", "on_cancel", "on_track", "on_update"]""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                        {"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}
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
                {"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}]}
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
        {"_NAME_":"ON_INIT_CONTEXT","_DESCRIPTION_":"Validate on_init context","action":["on_init"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}]}]}
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

                def ORDER_ITEMS_ADDITIONAL_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_ITEMS_ADDITIONAL_TAGS_obj in scope:
                        ORDER_ITEMS_ADDITIONAL_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

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
                                        "description": r"""#### **ITEMS_TAGS_RTO_ACTION**

                        - All elements of $.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value is not in the payload""",
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
                            ITEMS_TAGS_NP_FEES,
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
                {"_NAME_":"ORDER_ITEMS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]}
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

                def ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES_obj in scope:
                        ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"] = input_data["external_data"]

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

                        test_functions = [
                            FULFILLMENTS_TRACKING,
                        ]

                        all_results = []
                        for fn in test_functions:
                            sub_result = fn(input_data)
                            all_results.extend(sub_result)

                        sub_results = all_results
                        valid = all(r["valid"] for r in sub_results)

                        # del ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES_obj["_EXTERNAL"]

                    return [{
                        "test_name": "ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}]}
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
                                        "description": r"""#### **FULFILLMENTS_TAGS_RTO_ACTION**

                        - All elements of $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value must be in ["yes", "no"]

                        > **Skip if:**
                        >
                        >     - $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value is not in the payload""",
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
                {"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]}
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

                def ORDER_QUOTE_ADDITIONAL_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_QUOTE_ADDITIONAL_TAGS_obj in scope:
                        ORDER_QUOTE_ADDITIONAL_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_FINANCE_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_FINANCE_TERMS_obj in scope:
                                TAGS_FINANCE_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_FINANCE_SUBVENTION_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FINANCE_SUBVENTION_TYPE_obj in scope:
                                        TAGS_FINANCE_SUBVENTION_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_SUBVENTION_TYPE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_FINANCE_SUBVENTION_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_FINANCE_SUBVENTION_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_FINANCE_SUBVENTION_TYPE**

                                - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_FINANCE_SUBVENTION_TYPE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FINANCE_SUBVENTION_TYPE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_FINANCE_SUBVENTION_AMOUNT(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FINANCE_SUBVENTION_AMOUNT_obj in scope:
                                        TAGS_FINANCE_SUBVENTION_AMOUNT_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_SUBVENTION_AMOUNT_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_FINANCE_SUBVENTION_AMOUNT_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_FINANCE_SUBVENTION_AMOUNT",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_FINANCE_SUBVENTION_AMOUNT**

                                - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_SUBVENTION_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_FINANCE_SUBVENTION_AMOUNT_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FINANCE_SUBVENTION_AMOUNT",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_SUBVENTION_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_FINANCE_PROVIDER_TAX_NUMBER(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FINANCE_PROVIDER_TAX_NUMBER_obj in scope:
                                        TAGS_FINANCE_PROVIDER_TAX_NUMBER_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_PROVIDER_TAX_NUMBER_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_FINANCE_PROVIDER_TAX_NUMBER_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_FINANCE_PROVIDER_TAX_NUMBER",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_FINANCE_PROVIDER_TAX_NUMBER**

                                - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_FINANCE_PROVIDER_TAX_NUMBER_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FINANCE_PROVIDER_TAX_NUMBER",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_FINANCE_BANK_ACCOUNT_NO(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FINANCE_BANK_ACCOUNT_NO_obj in scope:
                                        TAGS_FINANCE_BANK_ACCOUNT_NO_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_BANK_ACCOUNT_NO_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_FINANCE_BANK_ACCOUNT_NO_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_FINANCE_BANK_ACCOUNT_NO",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_FINANCE_BANK_ACCOUNT_NO**

                                - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_FINANCE_BANK_ACCOUNT_NO_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FINANCE_BANK_ACCOUNT_NO",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_FINANCE_IFSC_CODE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_FINANCE_IFSC_CODE_obj in scope:
                                        TAGS_FINANCE_IFSC_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_FINANCE_IFSC_CODE_obj, "$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_FINANCE_IFSC_CODE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_FINANCE_IFSC_CODE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_FINANCE_IFSC_CODE**

                                - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_FINANCE_IFSC_CODE_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_FINANCE_IFSC_CODE",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_FINANCE_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_FINANCE_SUBVENTION_TYPE,
                                    TAGS_FINANCE_SUBVENTION_AMOUNT,
                                    TAGS_FINANCE_PROVIDER_TAX_NUMBER,
                                    TAGS_FINANCE_BANK_ACCOUNT_NO,
                                    TAGS_FINANCE_IFSC_CODE,
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
                        {"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_SUBVENTION_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value","_RETURN_":"attr are present"}]}
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

                        test_functions = [
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
                {"_NAME_":"ORDER_QUOTE_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_SUBVENTION_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value","_RETURN_":"attr are present"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}]}]}
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

                def ORDER_PAYMENT_TAGS(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for ORDER_PAYMENT_TAGS_obj in scope:
                        ORDER_PAYMENT_TAGS_obj["_EXTERNAL"] = input_data["external_data"]

                        def TAGS_BPP_TERMS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BPP_TERMS_obj in scope:
                                TAGS_BPP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]

                                def TAGS_BPP_TERMS_MAX_LIABILITY_CAP(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_MAX_LIABILITY_CAP_obj in scope:
                                        TAGS_BPP_TERMS_MAX_LIABILITY_CAP_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_MAX_LIABILITY_CAP_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_MAX_LIABILITY_CAP_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_MAX_LIABILITY_CAP",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_MAX_LIABILITY_CAP**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY_CAP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_MAX_LIABILITY_CAP_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_MAX_LIABILITY_CAP",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY_CAP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_MAX_LIABILITY(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_MAX_LIABILITY_obj in scope:
                                        TAGS_BPP_TERMS_MAX_LIABILITY_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_MAX_LIABILITY_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_MAX_LIABILITY_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_MAX_LIABILITY",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_MAX_LIABILITY**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_MAX_LIABILITY_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_MAX_LIABILITY",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_MANDATORY_ARBITRATION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj in scope:
                                        TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_MANDATORY_ARBITRATION_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_MANDATORY_ARBITRATION",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_MANDATORY_ARBITRATION**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","_RETURN_":"attr are present"}
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
                                {"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_COURT_JURISDICTION(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_COURT_JURISDICTION_obj in scope:
                                        TAGS_BPP_TERMS_COURT_JURISDICTION_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_COURT_JURISDICTION_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_COURT_JURISDICTION_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_COURT_JURISDICTION",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_COURT_JURISDICTION**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_COURT_JURISDICTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_COURT_JURISDICTION_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_COURT_JURISDICTION",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_COURT_JURISDICTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_DELAY_INTEREST(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_DELAY_INTEREST_obj in scope:
                                        TAGS_BPP_TERMS_DELAY_INTEREST_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_DELAY_INTEREST_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_DELAY_INTEREST_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_DELAY_INTEREST",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_DELAY_INTEREST**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_DELAY_INTEREST","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_DELAY_INTEREST_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_DELAY_INTEREST",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_DELAY_INTEREST","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_NP_TYPE(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_NP_TYPE_obj in scope:
                                        TAGS_BPP_TERMS_NP_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_NP_TYPE_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_NP_TYPE_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_NP_TYPE",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_NP_TYPE**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","_RETURN_":"attr are present"}
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
                                {"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_TAX_NUMBER(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_TAX_NUMBER_obj in scope:
                                        TAGS_BPP_TERMS_TAX_NUMBER_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_TAX_NUMBER_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_TAX_NUMBER_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_TAX_NUMBER",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_TAX_NUMBER**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_TAX_NUMBER_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_TAX_NUMBER",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER_obj in scope:
                                        TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"}
                                """
                                                }
                                            }]

                                        # del TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER_obj["_EXTERNAL"]

                                    return [{
                                        "test_name": "TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER",
                                        "valid": valid,
                                        "code": 200 if valid else 30000, 
                                        "_debug_info": {
                                            "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                def TAGS_BPP_TERMS_ACCEPT_BAP_TERMS(input_data):
                                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                                    sub_results = []
                                    valid = True

                                    for TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj in scope:
                                        TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj["_EXTERNAL"] = input_data["external_data"]
                                        attr = payload_utils["get_json_path"](TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj, "$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value")

                                        skip_check = not (validation_utils["are_present"](attr))
                                        if skip_check:
                                            continue

                                        validate = validation_utils["are_present"](attr)

                                        if not validate:
                                            del TAGS_BPP_TERMS_ACCEPT_BAP_TERMS_obj["_EXTERNAL"]
                                            return [{
                                                "test_name": "TAGS_BPP_TERMS_ACCEPT_BAP_TERMS",
                                                "valid": False,
                                                "code": 30000,
                                                "description": r"""#### **TAGS_BPP_TERMS_ACCEPT_BAP_TERMS**

                                - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value must be present in the payload

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value is not in the payload""",
                                                "_debug_info": {
                                                    "fed_config": r"""
                                {"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","_RETURN_":"attr are present"}
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
                                {"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","_RETURN_":"attr are present"}
                                """
                                    }}] + sub_results

                                test_functions = [
                                    TAGS_BPP_TERMS_MAX_LIABILITY_CAP,
                                    TAGS_BPP_TERMS_MAX_LIABILITY,
                                    TAGS_BPP_TERMS_MANDATORY_ARBITRATION,
                                    TAGS_BPP_TERMS_COURT_JURISDICTION,
                                    TAGS_BPP_TERMS_DELAY_INTEREST,
                                    TAGS_BPP_TERMS_NP_TYPE,
                                    TAGS_BPP_TERMS_TAX_NUMBER,
                                    TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER,
                                    TAGS_BPP_TERMS_ACCEPT_BAP_TERMS,
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
                        {"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY_CAP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_COURT_JURISDICTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_DELAY_INTEREST","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","_RETURN_":"attr are present"}]}
                        """
                            }}] + sub_results

                        def TAGS_BPP_COLLECT(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for TAGS_BPP_COLLECT_obj in scope:
                                TAGS_BPP_COLLECT_obj["_EXTERNAL"] = input_data["external_data"]

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
                                                "description": r"""#### **TAGS_BPP_COLLECT_SUCCESS**

                                - All elements of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value must be in ["Y", "N"]

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value is not in the payload""",
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
                                                "description": r"""#### **TAGS_BPP_COLLECT_ERROR**

                                - All elements of $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value must be in ["Y", "N"]

                                > **Skip if:**
                                >
                                >     - $.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value is not in the payload""",
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
                        {"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}
                        """
                            }}] + sub_results

                        test_functions = [
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
                {"_NAME_":"ORDER_PAYMENT_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY_CAP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_COURT_JURISDICTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_DELAY_INTEREST","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}]}
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
                        {"_NAME_":"OFFERS_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].id","_RETURN_":"attr are present"}
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
                        {"_NAME_":"OFFERS_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].id","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

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
                                        "description": r"""#### **OFFERS_DESCRIPTOR_CODE**

                        - All elements of $.message.order.offers[*].descriptor.code must be in ["discount", "buyXgetY", "freebie", "slab", "combo"]

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].descriptor.code is not in the payload""",
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

                        def OFFERS_DESCRIPTOR_IMAGES(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_DESCRIPTOR_IMAGES_obj in scope:
                                OFFERS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_DESCRIPTOR_IMAGES_obj, "$.message.order.offers[*].descriptor.images[*]")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_DESCRIPTOR_IMAGES",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_DESCRIPTOR_IMAGES**

                        - $.message.order.offers[*].descriptor.images[*] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].descriptor.images[*] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_DESCRIPTOR_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.images[*]","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_DESCRIPTOR_IMAGES_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_DESCRIPTOR_IMAGES",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_DESCRIPTOR_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.images[*]","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def OFFERS_LOCATION_IDS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_LOCATION_IDS_obj in scope:
                                OFFERS_LOCATION_IDS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_LOCATION_IDS_obj, "$.message.order.offers[*].location_ids[*]")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_LOCATION_IDS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_LOCATION_IDS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_LOCATION_IDS**

                        - $.message.order.offers[*].location_ids[*] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].location_ids[*] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_LOCATION_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].location_ids[*]","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_LOCATION_IDS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_LOCATION_IDS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_LOCATION_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].location_ids[*]","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def OFFERS_ITEM_IDS(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_ITEM_IDS_obj in scope:
                                OFFERS_ITEM_IDS_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_ITEM_IDS_obj, "$.message.order.offers[*].item_ids[*]")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_ITEM_IDS_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_ITEM_IDS",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_ITEM_IDS**

                        - $.message.order.offers[*].item_ids[*] must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].item_ids[*] is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_ITEM_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].item_ids[*]","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_ITEM_IDS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_ITEM_IDS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_ITEM_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].item_ids[*]","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def OFFERS_TIME_LABEL(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_TIME_LABEL_obj in scope:
                                OFFERS_TIME_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_TIME_LABEL_obj, "$.message.order.offers[*].time.label")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_TIME_LABEL_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_TIME_LABEL",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_TIME_LABEL**

                        - $.message.order.offers[*].time.label must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].time.label is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_TIME_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.label","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_TIME_LABEL_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_TIME_LABEL",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_TIME_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.label","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def OFFERS_TIME_RANGE_START(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_TIME_RANGE_START_obj in scope:
                                OFFERS_TIME_RANGE_START_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_TIME_RANGE_START_obj, "$.message.order.offers[*].time.range.start")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_TIME_RANGE_START_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_TIME_RANGE_START",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_TIME_RANGE_START**

                        - $.message.order.offers[*].time.range.start must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].time.range.start is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.start","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_TIME_RANGE_START_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_TIME_RANGE_START",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.start","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        def OFFERS_TIME_RANGE_END(input_data):
                            scope = payload_utils["get_json_path"](input_data["payload"], "$")
                            sub_results = []
                            valid = True

                            for OFFERS_TIME_RANGE_END_obj in scope:
                                OFFERS_TIME_RANGE_END_obj["_EXTERNAL"] = input_data["external_data"]
                                attr = payload_utils["get_json_path"](OFFERS_TIME_RANGE_END_obj, "$.message.order.offers[*].time.range.end")

                                skip_check = not (validation_utils["are_present"](attr))
                                if skip_check:
                                    continue

                                validate = validation_utils["are_present"](attr)

                                if not validate:
                                    del OFFERS_TIME_RANGE_END_obj["_EXTERNAL"]
                                    return [{
                                        "test_name": "OFFERS_TIME_RANGE_END",
                                        "valid": False,
                                        "code": 30000,
                                        "description": r"""#### **OFFERS_TIME_RANGE_END**

                        - $.message.order.offers[*].time.range.end must be present in the payload

                        > **Skip if:**
                        >
                        >     - $.message.order.offers[*].time.range.end is not in the payload""",
                                        "_debug_info": {
                                            "fed_config": r"""
                        {"_NAME_":"OFFERS_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.end","_RETURN_":"attr are present"}
                        """
                                        }
                                    }]

                                # del OFFERS_TIME_RANGE_END_obj["_EXTERNAL"]

                            return [{
                                "test_name": "OFFERS_TIME_RANGE_END",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"OFFERS_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.end","_RETURN_":"attr are present"}
                        """
                            }}] + sub_results

                        test_functions = [
                            OFFERS_ID,
                            OFFERS_DESCRIPTOR_CODE,
                            OFFERS_DESCRIPTOR_IMAGES,
                            OFFERS_LOCATION_IDS,
                            OFFERS_ITEM_IDS,
                            OFFERS_TIME_LABEL,
                            OFFERS_TIME_RANGE_START,
                            OFFERS_TIME_RANGE_END,
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
                {"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].id","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"OFFERS_DESCRIPTOR_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_LOCATION_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].location_ids[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_ITEM_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].item_ids[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.label","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.start","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.end","_RETURN_":"attr are present"}]}
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

                                # del TAGS_BAP_TERMS_obj["_EXTERNAL"]

                            return [{
                                "test_name": "TAGS_BAP_TERMS",
                                "valid": valid,
                                "code": 200 if valid else 30000, 
                                "_debug_info": {
                                    "fed_config": r"""
                        {"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}
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
                {"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}]}
                """
                    }}] + sub_results

                test_functions = [
                    ORDER_PROVIDER,
                    ORDER_ITEMS,
                    ORDER_ITEMS_ADDITIONAL_TAGS,
                    ORDER_BILLING,
                    ORDER_FULFILLMENTS,
                    ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES,
                    ORDER_FULFILLMENTS_ADDITIONAL_TAGS,
                    ORDER_QUOTE,
                    ORDER_QUOTE_ADDITIONAL_PROPERTIES,
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
        {"_NAME_":"ON_INIT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_SUBVENTION_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value","_RETURN_":"attr are present"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_PAYMENT_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY_CAP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_COURT_JURISDICTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_DELAY_INTEREST","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].id","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"OFFERS_DESCRIPTOR_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_LOCATION_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].location_ids[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_ITEM_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].item_ids[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.label","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.start","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.end","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}]}]}
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
{"_NAME_":"on_init_validations","_RETURN_":[{"_NAME_":"ON_INIT_CONTEXT","_DESCRIPTION_":"Validate on_init context","action":["on_init"],"_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED","_RETURN_":[{"_NAME_":"CONTEXT_REQUIRED_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_ACTION","attr":"$.context.action","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_CITY","attr":"$.context.city","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_ID","search":["search"],"attr":"$.context.bap_id","_CONTINUE_":"(action equal to search)","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_BPP_URI","search":["search"],"_CONTINUE_":"(action equal to search)","attr":"$.context.bap_uri","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present","action":["on_init"]},{"_NAME_":"CONTEXT_REQUIRED_TTL","attr":"$.context.ttl","optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update","on_status"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr are present","action":["on_init"]}]},{"_NAME_":"CONTEXT_ENUM","_RETURN_":[{"_NAME_":"CONTEXT_ENUM_DOMAIN","domain":["ONDC:RET11"],"attr":"$.context.domain","_RETURN_":"attr equal to domain","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_ACTION","attr":"$.context.action","_RETURN_":"attr equal to action","action":["on_init"]},{"_NAME_":"CONTEXT_ENUM_VERSION","version":["1.2.0","1.2.5"],"attr":"$.context.core_version","_RETURN_":"attr all in version","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BAP_URI","attr":"$.context.bap_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","action":["on_init"]},{"_NAME_":"CONTEXT_REG_BPP_URI","attr":"$.context.bpp_uri","reg":["^https?\\:\\/\\/"],"_RETURN_":"attr follow regex reg","search":["search"],"_CONTINUE_":"(action equal to search)","action":["on_init"]},{"_NAME_":"CONTEXT_REG_TTL","attr":"$.context.ttl","reg":["^P(?=\\\\d|T)(\\\\d+Y)?(\\\\d+M)?(\\\\d+W)?(\\\\d+D)?(T(?=\\\\d)(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"],"optional_vars":["on_search","on_select","on_confirm","on_init","on_cancel","on_track","on_update"],"_CONTINUE_":"(action all in optional_vars)","_RETURN_":"attr follow regex reg","action":["on_init"]}]}]},{"_NAME_":"ON_INIT_ORDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER","_RETURN_":[{"_NAME_":"ORDER_PROVIDER_ID","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"ORDER_PROVIDER_LOCATIONS_ID","attr":"$.message.order.provider.locations[*].id","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS","_RETURN_":[{"_NAME_":"ITEMS_ID","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_PARENT_ITEM_ID","attr":"$.message.order.items[*].parent_item_id","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_FULFILLMENT_ID","attr":"$.message.order.items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_QUANTITY_COUNT","attr":"$.message.order.items[*].quantity.count","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_TYPE","attr":"$.message.order.items[*].tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ITEMS_TAGS_PARENT_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='parent')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_ITEMS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"ITEMS_TAGS_NP_FEES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"ITEMS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.items[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_BILLING","_RETURN_":[{"_NAME_":"BILLING_NAME","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS","_RETURN_":[{"_NAME_":"BILLING_ADDRESS_NAME","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_BUILDING","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_LOCALITY","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_CITY","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_STATE","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_COUNTRY","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"BILLING_ADDRESS_AREA_CODE","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}]},{"_NAME_":"BILLING_PHONE","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"BILLING_EMAIL","attr":"$.message.order.billing.email","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BILLING_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"BILLING_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS","_RETURN_":[{"_NAME_":"FULFILLMENTS_ID","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_LOCATION_GPS","attr":"$.message.order.fulfillments[*].end.location.gps","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_END_CONTACT_PHONE","attr":"$.message.order.fulfillments[*].end.contact.phone","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"FULFILLMENTS_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_FULFILLMENTS_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS","_RETURN_":[{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_WEIGHT_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='weight_value')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_DIM_UNIT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='dim_unit')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_LENGTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='length')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_BREADTH","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='breadth')].value","_RETURN_":"attr are present"},{"_NAME_":"FULFILLMENTS_TAGS_ORDER_DETAILS_HEIGHT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='order_details')].list[?(@.code=='height')].value","_RETURN_":"attr are present"}]},{"_NAME_":"FULFILLMENTS_TAGS_RTO_ACTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[?(@.code=='return_to_origin')].value","var_enum":["yes","no"],"_RETURN_":"attr all in var_enum"}]},{"_NAME_":"ORDER_QUOTE","_RETURN_":[{"_NAME_":"QUOTE_PRICE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_PRICE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"QUOTE_BREAKUP","_RETURN_":[{"_NAME_":"BREAKUP_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_QUANTITY_COUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_quantity'].count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE","attr":"$.message.order.quote.breakup[*].title","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","var_enum":["item","delivery","packing","tax","misc","discount","offer"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_TTL","attr":"$.message.order.quote.breakup[*].ttl","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_PARENT_ITEM_ID","attr":"$.message.order.quote.breakup[*].item.parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_AVAILABLE_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.available.count","var_enum":["99","0"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_QUANTITY_MAXIMUM_COUNT","attr":"$.message.order.quote.breakup[*].item.quantity.maximum.count","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_CURRENCY","attr":"$.message.order.quote.breakup[*].item.price.currency","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_PRICE_VALUE","attr":"$.message.order.quote.breakup[*].item.price.value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='type')].list[?(@.code=='type')].value","var_enum":["item","customization"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_PARENT_ID","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='parent')].list[?(@.code=='id')].value","_CONTINUE_":"!(attr are present)","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_TYPE","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='type')].value","var_enum":["fulfillment","order","item"],"_CONTINUE_":"!(attr are present)","_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_QUOTE_SUBTYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='quote')].list[?(@.code=='subtype')].value","var_enum":["delivery","packaging","misc"],"_RETURN_":"attr all in var_enum"}]}]}]}]}]}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_PROPERTIES","_RETURN_":[{"_NAME_":"QUOTE_TTL","attr":"$.message.order.quote.ttl","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_QUOTE_ADDITIONAL_TAGS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_TERMS","_RETURN_":[{"_NAME_":"TAGS_FINANCE_SUBVENTION_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_SUBVENTION_AMOUNT","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='subvention_amount')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='bank_account_no')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_FINANCE_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='finance_terms')].list[?(@.code=='ifsc_code')].value","_RETURN_":"attr are present"}]},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES","_RETURN_":[{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='id')].value","_RETURN_":"attr are present"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_type')].value","var_enum":["percent"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"BREAKUP_ITEM_ITEM_TAGS_TAGS_NP_FEES_CHANNEL_MARGIN_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.quote.breakup[*].item.tags[?(@.code=='np_fees')].list[?(@.code=='channel_margin_value')].value","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_PAYMENT","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_TYPE","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_type']","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_BUYER_APP_FINDER_FEE_AMOUNT","attr":"$.message.order.payment['@ondc/org/buyer_app_finder_fee_amount']","reg":["^(\\\\d*.?\\\\d{1,2})$"],"_RETURN_":"attr are present && attr follow regex reg"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS","_RETURN_":[{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_COUNTERPARTY","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_PHASE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_phase","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_TYPE","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_type","var_enum":["upi","neft","rtgs"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_UPI_ADDRESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].upi_address","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_BANK_ACCOUNT_NO","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_bank_account_no","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_SETTLEMENT_IFSC_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_ifsc_code","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BANK_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].bank_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BENEFICIARY_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].beneficiary_name","_RETURN_":"attr are present"},{"_NAME_":"PAYMENT_ONDC_ORG_SETTLEMENT_DETAILS_BRANCH_NAME","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment['@ondc/org/settlement_details'][*].branch_name","_RETURN_":"attr are present"}]}]},{"_NAME_":"ORDER_PAYMENT_TAGS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS","_RETURN_":[{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY_CAP","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability_cap')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MAX_LIABILITY","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='max_liability')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_MANDATORY_ARBITRATION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='mandatory_arbitration')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_COURT_JURISDICTION","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='court_jurisdiction')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_DELAY_INTEREST","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='delay_interest')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_NP_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='np_type')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_PROVIDER_TAX_NUMBER","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='provider_tax_number')].value","_RETURN_":"attr are present"},{"_NAME_":"TAGS_BPP_TERMS_ACCEPT_BAP_TERMS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_terms')].list[?(@.code=='accept_bap_terms')].value","_RETURN_":"attr are present"}]},{"_NAME_":"TAGS_BPP_COLLECT","_RETURN_":[{"_NAME_":"TAGS_BPP_COLLECT_SUCCESS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='success')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"TAGS_BPP_COLLECT_ERROR","_CONTINUE_":"!(attr are present)","attr":"$.message.order.payment.tags[?(@.code=='bpp_collect')].list[?(@.code=='error')].value","var_enum":["Y","N"],"_RETURN_":"attr all in var_enum"}]}]},{"_NAME_":"ORDER_OFFERS","_RETURN_":[{"_NAME_":"OFFERS_ID","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].id","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_DESCRIPTOR_CODE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.code","var_enum":["discount","buyXgetY","freebie","slab","combo"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"OFFERS_DESCRIPTOR_IMAGES","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].descriptor.images[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_LOCATION_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].location_ids[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_ITEM_IDS","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].item_ids[*]","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_LABEL","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.label","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_RANGE_START","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.start","_RETURN_":"attr are present"},{"_NAME_":"OFFERS_TIME_RANGE_END","_CONTINUE_":"!(attr are present)","attr":"$.message.order.offers[*].time.range.end","_RETURN_":"attr are present"}]},{"_NAME_":"ORDER_TAGS","_RETURN_":[{"_NAME_":"TAGS_BAP_TERMS","_RETURN_":[{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_TYPE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_type')].value","var_enum":["percent","amount"],"_RETURN_":"attr all in var_enum"},{"_NAME_":"ORDER_TAGS_BAP_TERMS_FINANCE_COST_VALUE","_CONTINUE_":"!(attr are present)","attr":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='finance_const_value')].value","_RETURN_":"attr are present"}]}]}]}]}
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
