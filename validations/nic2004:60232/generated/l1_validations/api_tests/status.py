from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def status_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for status_validations_obj in scope:
        status_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def REQUIRED_CONTEXT_DOMAIN(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_DOMAIN_obj in scope:
                REQUIRED_CONTEXT_DOMAIN_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_DOMAIN_obj, "$.context.domain")
                enumList = ["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_CONTEXT_DOMAIN_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_DOMAIN",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_DOMAIN**: all of the following sub conditions must be met:

          - **condition REQUIRED_CONTEXT_DOMAIN.1**: $.context.domain must be present in the payload
          - **condition REQUIRED_CONTEXT_DOMAIN.2**: every element of $.context.domain must be in ["ONDC:LOG10", "ONDC:LOG11", "nic2004:60232"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_DOMAIN_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_DOMAIN",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_COUNTRY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_COUNTRY_obj in scope:
                REQUIRED_CONTEXT_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_COUNTRY_obj, "$.context.country")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_COUNTRY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_COUNTRY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_COUNTRY**: $.context.country must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_COUNTRY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_COUNTRY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_CITY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_CITY_obj in scope:
                REQUIRED_CONTEXT_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_CITY_obj, "$.context.city")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_CITY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_CITY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_CITY**: $.context.city must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_CITY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_CITY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_ACTION(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_ACTION_obj in scope:
                REQUIRED_CONTEXT_ACTION_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_ACTION_obj, "$.context.action")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_ACTION_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_ACTION",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_ACTION**: $.context.action must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_ACTION_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_ACTION",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_CORE_VERSION(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_CORE_VERSION_obj in scope:
                REQUIRED_CONTEXT_CORE_VERSION_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_CORE_VERSION_obj, "$.context.core_version")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_CORE_VERSION_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_CORE_VERSION",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_CORE_VERSION**: $.context.core_version must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_CORE_VERSION_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_CORE_VERSION",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_BAP_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_BAP_ID_obj in scope:
                REQUIRED_CONTEXT_BAP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_BAP_ID_obj, "$.context.bap_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_BAP_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_BAP_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_BAP_ID**: $.context.bap_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_BAP_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_BAP_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_BAP_URI(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_BAP_URI_obj in scope:
                REQUIRED_CONTEXT_BAP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_BAP_URI_obj, "$.context.bap_uri")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_BAP_URI_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_BAP_URI",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_BAP_URI**: $.context.bap_uri must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_BAP_URI_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_BAP_URI",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_BPP_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_BPP_ID_obj in scope:
                REQUIRED_CONTEXT_BPP_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_BPP_ID_obj, "$.context.bpp_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_BPP_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_BPP_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_BPP_ID**: $.context.bpp_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_BPP_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_BPP_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_BPP_URI(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_BPP_URI_obj in scope:
                REQUIRED_CONTEXT_BPP_URI_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_BPP_URI_obj, "$.context.bpp_uri")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_BPP_URI_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_BPP_URI",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_BPP_URI**: $.context.bpp_uri must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_BPP_URI_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_BPP_URI",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_TRANSACTION_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_TRANSACTION_ID_obj in scope:
                REQUIRED_CONTEXT_TRANSACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_TRANSACTION_ID_obj, "$.context.transaction_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_TRANSACTION_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_TRANSACTION_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_TRANSACTION_ID**: $.context.transaction_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_TRANSACTION_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_TRANSACTION_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_MESSAGE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_MESSAGE_ID_obj in scope:
                REQUIRED_CONTEXT_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_MESSAGE_ID_obj, "$.context.message_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_MESSAGE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_MESSAGE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_MESSAGE_ID**: $.context.message_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_MESSAGE_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_MESSAGE_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_TIMESTAMP(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_TIMESTAMP_obj in scope:
                REQUIRED_CONTEXT_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_TIMESTAMP_obj, "$.context.timestamp")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_TIMESTAMP_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_TIMESTAMP",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_TIMESTAMP**: $.context.timestamp must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_TIMESTAMP_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_TIMESTAMP",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_CONTEXT_TTL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_CONTEXT_TTL_obj in scope:
                REQUIRED_CONTEXT_TTL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_CONTEXT_TTL_obj, "$.context.ttl")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_CONTEXT_TTL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_CONTEXT_TTL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_CONTEXT_TTL**: $.context.ttl must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_TTL","attr":"$.context.ttl","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_CONTEXT_TTL_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_CONTEXT_TTL",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_CONTEXT_TTL","attr":"$.context.ttl","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ORDER_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ORDER_ID_obj in scope:
                REQUIRED_MESSAGE_ORDER_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ORDER_ID_obj, "$.message.order_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ORDER_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ORDER_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ORDER_ID**: $.message.order_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ORDER_ID","attr":"$.message.order_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ORDER_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ORDER_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ORDER_ID","attr":"$.message.order_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def VALID_ENUM_CONTEXT_DOMAIN(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_CONTEXT_DOMAIN_obj in scope:
                VALID_ENUM_CONTEXT_DOMAIN_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_CONTEXT_DOMAIN_obj, "$.context.domain")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_CONTEXT_DOMAIN_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_CONTEXT_DOMAIN",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_CONTEXT_DOMAIN**: every element of $.context.domain must be in ["ONDC:LOG10", "ONDC:LOG11", "nic2004:60232"]

        	> Note: **Condition VALID_ENUM_CONTEXT_DOMAIN** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.context.domain must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_CONTEXT_DOMAIN_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_CONTEXT_DOMAIN",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        test_functions = [
            REQUIRED_CONTEXT_DOMAIN,
            REQUIRED_CONTEXT_COUNTRY,
            REQUIRED_CONTEXT_CITY,
            REQUIRED_CONTEXT_ACTION,
            REQUIRED_CONTEXT_CORE_VERSION,
            REQUIRED_CONTEXT_BAP_ID,
            REQUIRED_CONTEXT_BAP_URI,
            REQUIRED_CONTEXT_BPP_ID,
            REQUIRED_CONTEXT_BPP_URI,
            REQUIRED_CONTEXT_TRANSACTION_ID,
            REQUIRED_CONTEXT_MESSAGE_ID,
            REQUIRED_CONTEXT_TIMESTAMP,
            REQUIRED_CONTEXT_TTL,
            REQUIRED_MESSAGE_ORDER_ID,
            VALID_ENUM_CONTEXT_DOMAIN,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del status_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "status_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"status_validations","_RETURN_":[{"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]},{"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TTL","attr":"$.context.ttl","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ORDER_ID","attr":"$.message.order_id","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}]}
"""
    }}] + sub_results

def status(input_data):
    total_results = status_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "status_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
