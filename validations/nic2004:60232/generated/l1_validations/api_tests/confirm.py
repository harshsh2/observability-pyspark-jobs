from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def confirm_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for confirm_validations_obj in scope:
        confirm_validations_obj["_EXTERNAL"] = input_data["external_data"]

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

        def REQUIRED_MESSAGE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_obj in scope:
                REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_obj, "$.message.order.id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID**: $.message.order.id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.order.id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.order.id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_obj in scope:
                REQUIRED_MESSAGE_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_obj, "$.message.order.state")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE**: $.message.order.state must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE","attr":"$.message.order.state","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE","attr":"$.message.order.state","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_16(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_16_obj in scope:
                REQUIRED_MESSAGE_ID_16_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_16_obj, "$.message.order.provider.id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_16_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_16",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_16**: $.message.order.provider.id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_16_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_16",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CATEGORY_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CATEGORY_ID_obj in scope:
                REQUIRED_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CATEGORY_ID_obj, "$.message.order.items[*].category_id")
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CATEGORY_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CATEGORY_ID**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_CATEGORY_ID.1**: $.message.order.items[*].category_id must be present in the payload
          - **condition REQUIRED_MESSAGE_CATEGORY_ID.2**: every element of $.message.order.items[*].category_id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.order.items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CATEGORY_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.order.items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LABEL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LABEL_obj in scope:
                REQUIRED_MESSAGE_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LABEL_obj, "$.message.order.items[*].time.label")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LABEL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LABEL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LABEL**: $.message.order.items[*].time.label must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.order.items[*].time.label","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LABEL_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LABEL",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.order.items[*].time.label","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DURATION(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_obj in scope:
                REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_obj, "$.message.order.items[*].time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION**: $.message.order.items[*].time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.order.items[*].time.duration","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_DURATION",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.order.items[*].time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TIMESTAMP(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TIMESTAMP_obj in scope:
                REQUIRED_MESSAGE_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TIMESTAMP_obj, "$.message.order.items[*].time.timestamp")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_TIMESTAMP_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TIMESTAMP",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TIMESTAMP**: $.message.order.items[*].time.timestamp must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.order.items[*].time.timestamp","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TIMESTAMP_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TIMESTAMP",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.order.items[*].time.timestamp","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CURRENCY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CURRENCY_obj in scope:
                REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_obj, "$.message.order.quote.price.currency")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CURRENCY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CURRENCY**: $.message.order.quote.price.currency must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CURRENCY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_obj in scope:
                REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_obj, "$.message.order.quote.price.value")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE**: $.message.order.quote.price.value must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID_obj in scope:
                REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID_obj, "$.message.order.quote.breakup[*]['@ondc/org/item_id']")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID**: $.message.order.quote.breakup[*]['@ondc/org/item_id'] must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj in scope:
                REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj, "$.message.order.quote.breakup[*]['@ondc/org/title_type']")
                enumList = ["delivery","rto","tax","diff","tax_diff","discount","cod","surge"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE.1**: $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be present in the payload
          - **condition REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE.2**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["delivery", "rto", "tax", "diff", "tax_diff", "discount", "cod", "surge"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_RETURN_":"attr are present && attr all in enumList","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_RETURN_":"attr are present && attr all in enumList","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CURRENCY_25(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CURRENCY_25_obj in scope:
                REQUIRED_MESSAGE_CURRENCY_25_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_25_obj, "$.message.order.quote.breakup[*].price.currency")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CURRENCY_25_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CURRENCY_25",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CURRENCY_25**: $.message.order.quote.breakup[*].price.currency must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY_25","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CURRENCY_25_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CURRENCY_25",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY_25","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_26(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_26_obj in scope:
                REQUIRED_MESSAGE_VALUE_26_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_26_obj, "$.message.order.quote.breakup[*].price.value")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_26_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_26",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_26**: $.message.order.quote.breakup[*].price.value must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_26","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_26_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_26",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_26","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_27(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_27_obj in scope:
                REQUIRED_MESSAGE_ID_27_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_27_obj, "$.message.order.fulfillments[*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_27_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_27",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_27**: $.message.order.fulfillments[*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_27","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_27_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_27",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_27","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_obj in scope:
                REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_obj, "$.message.order.fulfillments[*].type")
                enumList = ["Delivery","Return","Batch","RTO"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE.1**: $.message.order.fulfillments[*].type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE.2**: every element of $.message.order.fulfillments[*].type must be in ["Delivery", "Return", "Batch", "RTO"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DURATION_29(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_29_obj in scope:
                REQUIRED_MESSAGE_DURATION_29_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_29_obj, "$.message.order.fulfillments[*].start.time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_29_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION_29",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION_29**: $.message.order.fulfillments[*].start.time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION_29","attr":"$.message.order.fulfillments[*].start.time.duration","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_DURATION_29_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_DURATION_29",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION_29","attr":"$.message.order.fulfillments[*].start.time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_obj in scope:
                REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_obj, "$.message.order.fulfillments[*].start.person.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME**: $.message.order.fulfillments[*].start.person.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.order.fulfillments[*].start.person.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.order.fulfillments[*].start.person.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_31(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_31_obj in scope:
                REQUIRED_MESSAGE_ID_31_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_31_obj, "$.message.order.fulfillments[*].start.location.id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_31_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_31",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_31**: $.message.order.fulfillments[*].start.location.id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_31","attr":"$.message.order.fulfillments[*].start.location.id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_31_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_31",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_31","attr":"$.message.order.fulfillments[*].start.location.id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_GPS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_GPS_obj in scope:
                REQUIRED_MESSAGE_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_obj, "$.message.order.fulfillments[*].start.location.gps")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_GPS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_GPS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_GPS**: $.message.order.fulfillments[*].start.location.gps must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_GPS_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_GPS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_33(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_33_obj in scope:
                REQUIRED_MESSAGE_NAME_33_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_33_obj, "$.message.order.fulfillments[*].start.location.address.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_33_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_33",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_33**: $.message.order.fulfillments[*].start.location.address.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_33","attr":"$.message.order.fulfillments[*].start.location.address.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_33_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_33",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_33","attr":"$.message.order.fulfillments[*].start.location.address.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_obj in scope:
                REQUIRED_MESSAGE_BUILDING_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_obj, "$.message.order.fulfillments[*].start.location.address.building")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING**: $.message.order.fulfillments[*].start.location.address.building must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING","attr":"$.message.order.fulfillments[*].start.location.address.building","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING","attr":"$.message.order.fulfillments[*].start.location.address.building","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_obj, "$.message.order.fulfillments[*].start.location.address.locality")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY**: $.message.order.fulfillments[*].start.location.address.locality must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_obj in scope:
                REQUIRED_MESSAGE_CITY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_obj, "$.message.order.fulfillments[*].start.location.address.city")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY**: $.message.order.fulfillments[*].start.location.address.city must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_37(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_37_obj in scope:
                REQUIRED_MESSAGE_STATE_37_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_37_obj, "$.message.order.fulfillments[*].start.location.address.state")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_37_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_37",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_37**: $.message.order.fulfillments[*].start.location.address.state must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_37","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_37_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_37",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_37","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COUNTRY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COUNTRY_obj in scope:
                REQUIRED_MESSAGE_COUNTRY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_obj, "$.message.order.fulfillments[*].start.location.address.country")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COUNTRY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COUNTRY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COUNTRY**: $.message.order.fulfillments[*].start.location.address.country must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY","attr":"$.message.order.fulfillments[*].start.location.address.country","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COUNTRY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COUNTRY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY","attr":"$.message.order.fulfillments[*].start.location.address.country","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_obj, "$.message.order.fulfillments[*].start.location.address.area_code")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE**: $.message.order.fulfillments[*].start.location.address.area_code must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_PHONE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PHONE_obj in scope:
                REQUIRED_MESSAGE_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_obj, "$.message.order.fulfillments[*].start.contact.phone")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PHONE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PHONE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PHONE**: $.message.order.fulfillments[*].start.contact.phone must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_PHONE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_PHONE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_EMAIL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_EMAIL_obj in scope:
                REQUIRED_MESSAGE_EMAIL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_EMAIL_obj, "$.message.order.fulfillments[*].start.contact.email")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_EMAIL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_EMAIL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_EMAIL**: $.message.order.fulfillments[*].start.contact.email must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_EMAIL_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_EMAIL",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_42(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_42_obj in scope:
                REQUIRED_MESSAGE_NAME_42_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_42_obj, "$.message.order.fulfillments[*].end.person.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_42_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_42_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_42",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_42**: $.message.order.fulfillments[*].end.person.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_42** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_42","attr":"$.message.order.fulfillments[*].end.person.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_42_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_42",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_42","attr":"$.message.order.fulfillments[*].end.person.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_GPS_43(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_GPS_43_obj in scope:
                REQUIRED_MESSAGE_GPS_43_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_43_obj, "$.message.order.fulfillments[*].end.location.gps")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_43_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_GPS_43_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_GPS_43",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_GPS_43**: $.message.order.fulfillments[*].end.location.gps must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_GPS_43** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS_43","attr":"$.message.order.fulfillments[*].end.location.gps","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_GPS_43_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_GPS_43",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS_43","attr":"$.message.order.fulfillments[*].end.location.gps","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_44(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_44_obj in scope:
                REQUIRED_MESSAGE_NAME_44_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_44_obj, "$.message.order.fulfillments[*].end.location.address.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_44_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_44_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_44",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_44**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_44** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_44","attr":"$.message.order.fulfillments[*].end.location.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_44_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_44",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_44","attr":"$.message.order.fulfillments[*].end.location.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING_45(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_45_obj in scope:
                REQUIRED_MESSAGE_BUILDING_45_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_45_obj, "$.message.order.fulfillments[*].end.location.address.building")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_45_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_45_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING_45",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING_45**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_BUILDING_45** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_45","attr":"$.message.order.fulfillments[*].end.location.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_45_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING_45",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_45","attr":"$.message.order.fulfillments[*].end.location.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY_46(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_46_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_46_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_46_obj, "$.message.order.fulfillments[*].end.location.address.locality")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_46_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_46_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY_46",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY_46**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_LOCALITY_46** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_46","attr":"$.message.order.fulfillments[*].end.location.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_46_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY_46",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_46","attr":"$.message.order.fulfillments[*].end.location.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY_47(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_47_obj in scope:
                REQUIRED_MESSAGE_CITY_47_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_47_obj, "$.message.order.fulfillments[*].end.location.address.city")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_47_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_47_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY_47",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY_47**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CITY_47** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_47","attr":"$.message.order.fulfillments[*].end.location.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_47_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY_47",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_47","attr":"$.message.order.fulfillments[*].end.location.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_48(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_48_obj in scope:
                REQUIRED_MESSAGE_STATE_48_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_48_obj, "$.message.order.fulfillments[*].end.location.address.state")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_48_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_48_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_48",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_48**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_STATE_48** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_48","attr":"$.message.order.fulfillments[*].end.location.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_48_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_48",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_48","attr":"$.message.order.fulfillments[*].end.location.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COUNTRY_49(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COUNTRY_49_obj in scope:
                REQUIRED_MESSAGE_COUNTRY_49_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_49_obj, "$.message.order.fulfillments[*].end.location.address.country")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_49_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COUNTRY_49_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COUNTRY_49",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COUNTRY_49**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_COUNTRY_49** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_49","attr":"$.message.order.fulfillments[*].end.location.address.country","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COUNTRY_49_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COUNTRY_49",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_49","attr":"$.message.order.fulfillments[*].end.location.address.country","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_50(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_50_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_50_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_50_obj, "$.message.order.fulfillments[*].end.location.address.area_code")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_50_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_50_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_50",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_50**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_AREA_CODE_50** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_50","attr":"$.message.order.fulfillments[*].end.location.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_50_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_50",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_50","attr":"$.message.order.fulfillments[*].end.location.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_PHONE_51(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PHONE_51_obj in scope:
                REQUIRED_MESSAGE_PHONE_51_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_51_obj, "$.message.order.fulfillments[*].end.contact.phone")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_51_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PHONE_51_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PHONE_51",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PHONE_51**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_PHONE_51** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_51","attr":"$.message.order.fulfillments[*].end.contact.phone","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_PHONE_51_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_PHONE_51",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_51","attr":"$.message.order.fulfillments[*].end.contact.phone","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_EMAIL_52(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_EMAIL_52_obj in scope:
                REQUIRED_MESSAGE_EMAIL_52_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_EMAIL_52_obj, "$.message.order.fulfillments[*].end.contact.email")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_EMAIL_52_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_EMAIL_52_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_EMAIL_52",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_EMAIL_52**: $.message.order.fulfillments[*].end.contact.email must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_EMAIL_52** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL_52","attr":"$.message.order.fulfillments[*].end.contact.email","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_EMAIL_52_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_EMAIL_52",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL_52","attr":"$.message.order.fulfillments[*].end.contact.email","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_53(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_53_obj in scope:
                REQUIRED_MESSAGE_NAME_53_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_53_obj, "$.message.order.billing.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_53_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_53",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_53**: $.message.order.billing.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_53","attr":"$.message.order.billing.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_53_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_53",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_53","attr":"$.message.order.billing.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_54(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_54_obj in scope:
                REQUIRED_MESSAGE_NAME_54_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_54_obj, "$.message.order.billing.address.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_54_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_54",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_54**: $.message.order.billing.address.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_54","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_54_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_54",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_54","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING_55(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_55_obj in scope:
                REQUIRED_MESSAGE_BUILDING_55_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_55_obj, "$.message.order.billing.address.building")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_55_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING_55",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING_55**: $.message.order.billing.address.building must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_55","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_55_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING_55",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_55","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY_56(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_56_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_56_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_56_obj, "$.message.order.billing.address.locality")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_56_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY_56",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY_56**: $.message.order.billing.address.locality must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_56","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_56_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY_56",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_56","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY_57(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_57_obj in scope:
                REQUIRED_MESSAGE_CITY_57_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_57_obj, "$.message.order.billing.address.city")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_57_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY_57",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY_57**: $.message.order.billing.address.city must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_57","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_57_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY_57",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_57","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_58(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_58_obj in scope:
                REQUIRED_MESSAGE_STATE_58_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_58_obj, "$.message.order.billing.address.state")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_58_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_58",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_58**: $.message.order.billing.address.state must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_58","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_58_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_58",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_58","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COUNTRY_59(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COUNTRY_59_obj in scope:
                REQUIRED_MESSAGE_COUNTRY_59_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_59_obj, "$.message.order.billing.address.country")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COUNTRY_59_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COUNTRY_59",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COUNTRY_59**: $.message.order.billing.address.country must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_59","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COUNTRY_59_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COUNTRY_59",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_59","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_60(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_60_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_60_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_60_obj, "$.message.order.billing.address.area_code")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_60_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_60",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_60**: $.message.order.billing.address.area_code must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_60","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_60_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_60",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_60","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TAX_NUMBER(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TAX_NUMBER_obj in scope:
                REQUIRED_MESSAGE_TAX_NUMBER_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TAX_NUMBER_obj, "$.message.order.billing.tax_number")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_TAX_NUMBER_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TAX_NUMBER",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TAX_NUMBER**: $.message.order.billing.tax_number must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TAX_NUMBER_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TAX_NUMBER",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_PHONE_62(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PHONE_62_obj in scope:
                REQUIRED_MESSAGE_PHONE_62_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_62_obj, "$.message.order.billing.phone")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PHONE_62_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PHONE_62",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PHONE_62**: $.message.order.billing.phone must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_62","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_PHONE_62_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_PHONE_62",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_62","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_EMAIL_63(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_EMAIL_63_obj in scope:
                REQUIRED_MESSAGE_EMAIL_63_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_EMAIL_63_obj, "$.message.order.billing.email")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_EMAIL_63_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_EMAIL_63",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_EMAIL_63**: $.message.order.billing.email must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL_63","attr":"$.message.order.billing.email","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_EMAIL_63_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_EMAIL_63",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL_63","attr":"$.message.order.billing.email","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CREATED_AT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CREATED_AT_obj in scope:
                REQUIRED_MESSAGE_CREATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CREATED_AT_obj, "$.message.order.billing.created_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CREATED_AT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CREATED_AT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CREATED_AT**: $.message.order.billing.created_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CREATED_AT_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CREATED_AT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UPDATED_AT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATED_AT_obj in scope:
                REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATED_AT_obj, "$.message.order.billing.updated_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATED_AT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATED_AT**: $.message.order.billing.updated_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UPDATED_AT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COLLECTED_BY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COLLECTED_BY_obj in scope:
                REQUIRED_MESSAGE_COLLECTED_BY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COLLECTED_BY_obj, "$.message.order.payment.collected_by")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COLLECTED_BY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COLLECTED_BY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COLLECTED_BY**: $.message.order.payment.collected_by must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COLLECTED_BY","attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COLLECTED_BY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COLLECTED_BY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COLLECTED_BY","attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TYPE_67(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_67_obj in scope:
                REQUIRED_MESSAGE_TYPE_67_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_67_obj, "$.message.order.payment.type")
                enumList = ["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_67_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE_67",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE_67**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE_67.1**: $.message.order.payment.type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE_67.2**: every element of $.message.order.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT", "POST-FULFILLMENT"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE_67","attr":"$.message.order.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TYPE_67_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TYPE_67",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE_67","attr":"$.message.order.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_68(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_68_obj in scope:
                REQUIRED_MESSAGE_NAME_68_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_68_obj, "$.message.order['@ondc/org/linked_order'].items[*].descriptor.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_68_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_68_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_68",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_68**: $.message.order['@ondc/org/linked_order'].items[*].descriptor.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_68** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_68","attr":"$.message.order['@ondc/org/linked_order'].items[*].descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_68_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_68",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_68","attr":"$.message.order['@ondc/org/linked_order'].items[*].descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COUNT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COUNT_obj in scope:
                REQUIRED_MESSAGE_COUNT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNT_obj, "$.message.order['@ondc/org/linked_order'].items[*].quantity.count")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNT_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COUNT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COUNT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COUNT**: $.message.order['@ondc/org/linked_order'].items[*].quantity.count must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_COUNT** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.count","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COUNT_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COUNT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.count","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_obj in scope:
                REQUIRED_MESSAGE_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_obj, "$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT**: $.message.order['@ondc/org/linked_order'].items[*].quantity.measure.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_71(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_71_obj in scope:
                REQUIRED_MESSAGE_VALUE_71_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_71_obj, "$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_71_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_71_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_71",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_71**: $.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_71** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_71","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_71_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_71",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_71","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CURRENCY_72(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CURRENCY_72_obj in scope:
                REQUIRED_MESSAGE_CURRENCY_72_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_72_obj, "$.message.order['@ondc/org/linked_order'].items[*].price.currency")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_72_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CURRENCY_72_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CURRENCY_72",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CURRENCY_72**: $.message.order['@ondc/org/linked_order'].items[*].price.currency must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CURRENCY_72** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY_72","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.currency","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CURRENCY_72_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CURRENCY_72",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY_72","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.currency","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_73(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_73_obj in scope:
                REQUIRED_MESSAGE_VALUE_73_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_73_obj, "$.message.order['@ondc/org/linked_order'].items[*].price.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_73_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_73_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_73",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_73**: $.message.order['@ondc/org/linked_order'].items[*].price.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_73** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_73","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_73_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_73",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_73","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_74(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_74_obj in scope:
                REQUIRED_MESSAGE_NAME_74_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_74_obj, "$.message.order['@ondc/org/linked_order'].provider.descriptor.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_74_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_74_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_74",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_74**: $.message.order['@ondc/org/linked_order'].provider.descriptor.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_74** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_74","attr":"$.message.order['@ondc/org/linked_order'].provider.descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_74_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_74",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_74","attr":"$.message.order['@ondc/org/linked_order'].provider.descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_75(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_75_obj in scope:
                REQUIRED_MESSAGE_NAME_75_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_75_obj, "$.message.order['@ondc/org/linked_order'].provider.address.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_75_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_75_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_75",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_75**: $.message.order['@ondc/org/linked_order'].provider.address.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_75** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_75","attr":"$.message.order['@ondc/org/linked_order'].provider.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_75_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_75",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_75","attr":"$.message.order['@ondc/org/linked_order'].provider.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING_76(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_76_obj in scope:
                REQUIRED_MESSAGE_BUILDING_76_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_76_obj, "$.message.order['@ondc/org/linked_order'].provider.address.building")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_76_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_76_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING_76",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING_76**: $.message.order['@ondc/org/linked_order'].provider.address.building must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_BUILDING_76** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_76","attr":"$.message.order['@ondc/org/linked_order'].provider.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_76_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING_76",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_76","attr":"$.message.order['@ondc/org/linked_order'].provider.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY_77(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_77_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_77_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_77_obj, "$.message.order['@ondc/org/linked_order'].provider.address.locality")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_77_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_77_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY_77",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY_77**: $.message.order['@ondc/org/linked_order'].provider.address.locality must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_LOCALITY_77** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_77","attr":"$.message.order['@ondc/org/linked_order'].provider.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_77_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY_77",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_77","attr":"$.message.order['@ondc/org/linked_order'].provider.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY_78(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_78_obj in scope:
                REQUIRED_MESSAGE_CITY_78_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_78_obj, "$.message.order['@ondc/org/linked_order'].provider.address.city")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_78_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_78_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY_78",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY_78**: $.message.order['@ondc/org/linked_order'].provider.address.city must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CITY_78** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_78","attr":"$.message.order['@ondc/org/linked_order'].provider.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_78_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY_78",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_78","attr":"$.message.order['@ondc/org/linked_order'].provider.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_79(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_79_obj in scope:
                REQUIRED_MESSAGE_STATE_79_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_79_obj, "$.message.order['@ondc/org/linked_order'].provider.address.state")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_79_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_79_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_79",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_79**: $.message.order['@ondc/org/linked_order'].provider.address.state must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_STATE_79** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_79","attr":"$.message.order['@ondc/org/linked_order'].provider.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_79_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_79",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_79","attr":"$.message.order['@ondc/org/linked_order'].provider.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_80(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_80_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_80_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_80_obj, "$.message.order['@ondc/org/linked_order'].provider.address.area_code")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_80_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_80_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_80",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_80**: $.message.order['@ondc/org/linked_order'].provider.address.area_code must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_AREA_CODE_80** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_80","attr":"$.message.order['@ondc/org/linked_order'].provider.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_80_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_80",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_80","attr":"$.message.order['@ondc/org/linked_order'].provider.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_81(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_81_obj in scope:
                REQUIRED_MESSAGE_ID_81_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_81_obj, "$.message.order['@ondc/org/linked_order'].order.id")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_81_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_81_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_81",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_81**: $.message.order['@ondc/org/linked_order'].order.id must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_ID_81** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_81","attr":"$.message.order['@ondc/org/linked_order'].order.id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_81_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_81",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_81","attr":"$.message.order['@ondc/org/linked_order'].order.id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_82(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_82_obj in scope:
                REQUIRED_MESSAGE_UNIT_82_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_82_obj, "$.message.order['@ondc/org/linked_order'].order.weight.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_82_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_82_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_82",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_82**: $.message.order['@ondc/org/linked_order'].order.weight.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_82** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_82","attr":"$.message.order['@ondc/org/linked_order'].order.weight.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_82_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_82",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_82","attr":"$.message.order['@ondc/org/linked_order'].order.weight.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_83(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_83_obj in scope:
                REQUIRED_MESSAGE_VALUE_83_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_83_obj, "$.message.order['@ondc/org/linked_order'].order.weight.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_83_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_83_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_83",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_83**: $.message.order['@ondc/org/linked_order'].order.weight.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_83** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_83","attr":"$.message.order['@ondc/org/linked_order'].order.weight.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_83_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_83",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_83","attr":"$.message.order['@ondc/org/linked_order'].order.weight.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_84(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_84_obj in scope:
                REQUIRED_MESSAGE_UNIT_84_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_84_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_84_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_84_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_84",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_84**: $.message.order['@ondc/org/linked_order'].order.dimensions.length.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_84** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_84","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_84_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_84",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_84","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_85(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_85_obj in scope:
                REQUIRED_MESSAGE_VALUE_85_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_85_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.length.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_85_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_85_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_85",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_85**: $.message.order['@ondc/org/linked_order'].order.dimensions.length.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_85** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_85","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_85_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_85",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_85","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_86(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_86_obj in scope:
                REQUIRED_MESSAGE_UNIT_86_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_86_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_86_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_86_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_86",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_86**: $.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_86** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_86","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_86_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_86",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_86","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_87(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_87_obj in scope:
                REQUIRED_MESSAGE_VALUE_87_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_87_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_87_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_87_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_87",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_87**: $.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_87** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_87","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_87_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_87",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_87","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_88(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_88_obj in scope:
                REQUIRED_MESSAGE_UNIT_88_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_88_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_88_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_88_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_88",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_88**: $.message.order['@ondc/org/linked_order'].order.dimensions.height.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_88** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_88","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_88_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_88",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_88","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_89(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_89_obj in scope:
                REQUIRED_MESSAGE_VALUE_89_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_89_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.height.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_89_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_89_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_89",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_89**: $.message.order['@ondc/org/linked_order'].order.dimensions.height.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_89** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_89","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_89_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_89",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_89","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CREATED_AT_90(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CREATED_AT_90_obj in scope:
                REQUIRED_MESSAGE_CREATED_AT_90_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CREATED_AT_90_obj, "$.message.order.created_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CREATED_AT_90_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CREATED_AT_90",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CREATED_AT_90**: $.message.order.created_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CREATED_AT_90","attr":"$.message.order.created_at","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CREATED_AT_90_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CREATED_AT_90",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CREATED_AT_90","attr":"$.message.order.created_at","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UPDATED_AT_91(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATED_AT_91_obj in scope:
                REQUIRED_MESSAGE_UPDATED_AT_91_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATED_AT_91_obj, "$.message.order.updated_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATED_AT_91_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATED_AT_91",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATED_AT_91**: $.message.order.updated_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_91","attr":"$.message.order.updated_at","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UPDATED_AT_91_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UPDATED_AT_91",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_91","attr":"$.message.order.updated_at","_RETURN_":"attr are present"}
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

        def VALID_ENUM_MESSAGE_CATEGORY_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_CATEGORY_ID_obj in scope:
                VALID_ENUM_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CATEGORY_ID_obj, "$.message.order.items[*].category_id")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_CATEGORY_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CATEGORY_ID**: every element of $.message.order.items[*].category_id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CATEGORY_ID** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.items[*].category_id must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.order.items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_CATEGORY_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.order.items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj in scope:
                VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["delivery","rto","tax","diff","tax_diff","discount","cod","surge"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj, "$.message.order.quote.breakup[*]['@ondc/org/title_type']")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE**: every element of $.message.order.quote.breakup[*]['@ondc/org/title_type'] must be in ["delivery", "rto", "tax", "diff", "tax_diff", "discount", "cod", "surge"]

        	> Note: **Condition VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.quote.breakup[*]['@ondc/org/title_type'] must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"],"enumPath":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"],"enumPath":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Delivery","Return","Batch","RTO"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_obj, "$.message.order.fulfillments[*].type")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE**: every element of $.message.order.fulfillments[*].type must be in ["Delivery", "Return", "Batch", "RTO"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.order.fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.order.fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE_5(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_5_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_5_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["OTP"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_5_obj, "$.message.order.fulfillments[*].start.authorization.type")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_TYPE_5_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_TYPE_5",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE_5**: every element of $.message.order.fulfillments[*].start.authorization.type must be in ["OTP"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE_5** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].start.authorization.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_TYPE_5_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_TYPE_5",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_CODE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_CODE_obj in scope:
                VALID_ENUM_MESSAGE_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["2","3","4","5"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CODE_obj, "$.message.order.fulfillments[*].start.instructions.code")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_CODE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_CODE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CODE**: every element of $.message.order.fulfillments[*].start.instructions.code must be in ["2", "3", "4", "5"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CODE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].start.instructions.code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.order.fulfillments[*].start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_CODE_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_CODE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.order.fulfillments[*].start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE_7(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_7_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_7_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["OTP"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_7_obj, "$.message.order.fulfillments[*].end.authorization.type")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_TYPE_7_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_TYPE_7",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE_7**: every element of $.message.order.fulfillments[*].end.authorization.type must be in ["OTP"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE_7** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].end.authorization.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_TYPE_7_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_TYPE_7",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_CODE_8(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_CODE_8_obj in scope:
                VALID_ENUM_MESSAGE_CODE_8_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["1","2","3","5"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CODE_8_obj, "$.message.order.fulfillments[*].end.instructions.code")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_CODE_8_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_CODE_8",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CODE_8**: every element of $.message.order.fulfillments[*].end.instructions.code must be in ["1", "2", "3", "5"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CODE_8** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].end.instructions.code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE_8","enumList":["1","2","3","5"],"enumPath":"$.message.order.fulfillments[*].end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_CODE_8_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_CODE_8",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE_8","enumList":["1","2","3","5"],"enumPath":"$.message.order.fulfillments[*].end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_CODE_9(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_CODE_9_obj in scope:
                VALID_ENUM_MESSAGE_CODE_9_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CODE_9_obj, "$.message.order.fulfillments[*].state.descriptor.code")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_CODE_9_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_CODE_9",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CODE_9**: every element of $.message.order.fulfillments[*].state.descriptor.code must be in ["Pending", "Cancelled", "Order-picked-up", "RTO", "RTO-Initiated", "RTO-Delivered", "RTO-Disposed", "Out-for-pickup", "At-destination-hub", "In-transit", "At-pickup", "Out-for-delivery", "At-delivery", "Searching-for-Agent", "Agent-assigned", "Pickup-failed", "Pickup-rescheduled", "Delivery-failed", "Delivery-rescheduled", "Order-delivered"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CODE_9** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].state.descriptor.code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE_9","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"],"enumPath":"$.message.order.fulfillments[*].state.descriptor.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_CODE_9_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_CODE_9",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE_9","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"],"enumPath":"$.message.order.fulfillments[*].state.descriptor.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE_10(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_10_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_10_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_10_obj, "$.message.order.payment.type")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_TYPE_10_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_TYPE_10",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE_10**: every element of $.message.order.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT", "POST-FULFILLMENT"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE_10** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.payment.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_10","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.order.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_TYPE_10_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_TYPE_10",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_10","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.order.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY_obj in scope:
                VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["lbnp","lsp"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY_obj, "$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY**: every element of $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must be in ["lbnp", "lsp"]

        	> Note: **Condition VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY","enumList":["lbnp","lsp"],"enumPath":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY","enumList":["lbnp","lsp"],"enumPath":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def validate_tag_0(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_0_obj in scope:
                validate_tag_0_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["type"]
                tagPath = payload_utils["get_json_path"](validate_tag_0_obj, "$.message.order.items[*].tags[*].code")

                skip_check = not (validation_utils["are_present"](tagPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](tagPath, validTags)

                if not validate:
                    del validate_tag_0_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0**: every element of $.message.order.items[*].tags[*].code must be in ["type"]

        	> Note: **Condition validate_tag_0** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.items[*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0","validTags":["type"],"tagPath":"$.message.order.items[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
                        }
                    }]

                # del validate_tag_0_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0","validTags":["type"],"tagPath":"$.message.order.items[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_0_type(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.items[*].tags[?(@.code=='type')]")
            sub_results = []
            valid = True

            for validate_tag_0_type_obj in scope:
                validate_tag_0_type_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_type_obj, "$.list[*].code")
                validValues = ["type"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_type_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_type",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_type**: every element of $.message.order.items[*].tags[?(@.code=='type')].list[*].code must be in ["type"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_type","_SCOPE_":"$.message.order.items[*].tags[?(@.code=='type')]","subTags":"$.list[*].code","validValues":["type"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_type_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_type",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_type","_SCOPE_":"$.message.order.items[*].tags[?(@.code=='type')]","subTags":"$.list[*].code","validValues":["type"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_1_obj in scope:
                validate_tag_1_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["masked_contact"]
                tagPath = payload_utils["get_json_path"](validate_tag_1_obj, "$.message.order.fulfillments[*].start.contact.tags[*].code")

                skip_check = not (validation_utils["are_present"](tagPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](tagPath, validTags)

                if not validate:
                    del validate_tag_1_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1**: every element of $.message.order.fulfillments[*].start.contact.tags[*].code must be in ["masked_contact"]

        	> Note: **Condition validate_tag_1** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].start.contact.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].start.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
                        }
                    }]

                # del validate_tag_1_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].start.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_1_masked_contact(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]")
            sub_results = []
            valid = True

            for validate_tag_1_masked_contact_obj in scope:
                validate_tag_1_masked_contact_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_masked_contact_obj, "$.list[*].code")
                validValues = ["type","setup","token"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_masked_contact_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_masked_contact",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_masked_contact**: every element of $.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')].list[*].code must be in ["type", "setup", "token"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_masked_contact_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_masked_contact",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_2_obj in scope:
                validate_tag_2_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["masked_contact"]
                tagPath = payload_utils["get_json_path"](validate_tag_2_obj, "$.message.order.fulfillments[*].end.contact.tags[*].code")

                skip_check = not (validation_utils["are_present"](tagPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](tagPath, validTags)

                if not validate:
                    del validate_tag_2_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2**: every element of $.message.order.fulfillments[*].end.contact.tags[*].code must be in ["masked_contact"]

        	> Note: **Condition validate_tag_2** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].end.contact.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].end.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
                        }
                    }]

                # del validate_tag_2_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].end.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_2_masked_contact(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]")
            sub_results = []
            valid = True

            for validate_tag_2_masked_contact_obj in scope:
                validate_tag_2_masked_contact_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_masked_contact_obj, "$.list[*].code")
                validValues = ["type","setup","token"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_masked_contact_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_masked_contact",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_masked_contact**: every element of $.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')].list[*].code must be in ["type", "setup", "token"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_masked_contact_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_masked_contact",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_3_obj in scope:
                validate_tag_3_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["linked_provider","linked_order","linked_order_item","cod_settlement_detail","fulfill_request","fulfill_response","state","rto_action","provider","order","rto_verification","items","reverseqc_input"]
                tagPath = payload_utils["get_json_path"](validate_tag_3_obj, "$.message.order.fulfillments[*].tags[*].code")

                skip_check = not (validation_utils["are_present"](tagPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](tagPath, validTags)

                if not validate:
                    del validate_tag_3_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["linked_provider", "linked_order", "linked_order_item", "cod_settlement_detail", "fulfill_request", "fulfill_response", "state", "rto_action", "provider", "order", "rto_verification", "items", "reverseqc_input"]

        	> Note: **Condition validate_tag_3** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3","validTags":["linked_provider","linked_order","linked_order_item","cod_settlement_detail","fulfill_request","fulfill_response","state","rto_action","provider","order","rto_verification","items","reverseqc_input"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
                        }
                    }]

                # del validate_tag_3_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3","validTags":["linked_provider","linked_order","linked_order_item","cod_settlement_detail","fulfill_request","fulfill_response","state","rto_action","provider","order","rto_verification","items","reverseqc_input"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_3_linked_provider(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]")
            sub_results = []
            valid = True

            for validate_tag_3_linked_provider_obj in scope:
                validate_tag_3_linked_provider_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_linked_provider_obj, "$.list[*].code")
                validValues = ["id","name","address","cred_code","cred_desc","tax_id"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_linked_provider_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_linked_provider",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_linked_provider**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_provider')].list[*].code must be in ["id", "name", "address", "cred_code", "cred_desc", "tax_id"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_linked_provider_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_linked_provider",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_linked_order(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]")
            sub_results = []
            valid = True

            for validate_tag_3_linked_order_obj in scope:
                validate_tag_3_linked_order_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_linked_order_obj, "$.list[*].code")
                validValues = ["id","prep_time","cod_order","currency","declared_value","collection_amount","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_linked_order_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_linked_order",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_linked_order**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order')].list[*].code must be in ["id", "prep_time", "cod_order", "currency", "declared_value", "collection_amount", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height", "shipment_type"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","currency","declared_value","collection_amount","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_linked_order_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_linked_order",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","currency","declared_value","collection_amount","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_linked_order_item(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]")
            sub_results = []
            valid = True

            for validate_tag_3_linked_order_item_obj in scope:
                validate_tag_3_linked_order_item_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_linked_order_item_obj, "$.list[*].code")
                validValues = ["category","name","currency","value","quantity","weight_unit","weight_value","return_to_origin","hsn_code","ebn_exempt"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_linked_order_item_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_linked_order_item",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_linked_order_item**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')].list[*].code must be in ["category", "name", "currency", "value", "quantity", "weight_unit", "weight_value", "return_to_origin", "hsn_code", "ebn_exempt"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","return_to_origin","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_linked_order_item_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_linked_order_item",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","return_to_origin","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_cod_settlement_detail(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]")
            sub_results = []
            valid = True

            for validate_tag_3_cod_settlement_detail_obj in scope:
                validate_tag_3_cod_settlement_detail_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_cod_settlement_detail_obj, "$.list[*].code")
                validValues = ["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_cod_settlement_detail_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_cod_settlement_detail",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_cod_settlement_detail**: every element of $.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')].list[*].code must be in ["settlement_window", "settlement_type", "beneficiary_name", "upi_address", "bank_account_no", "ifsc_code", "bank_name", "branch_name"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_cod_settlement_detail","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]","subTags":"$.list[*].code","validValues":["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_cod_settlement_detail_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_cod_settlement_detail",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_cod_settlement_detail","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]","subTags":"$.list[*].code","validValues":["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_fulfill_request(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]")
            sub_results = []
            valid = True

            for validate_tag_3_fulfill_request_obj in scope:
                validate_tag_3_fulfill_request_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_fulfill_request_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_fulfill_request_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_fulfill_request",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_fulfill_request**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')].list[*].code must be in ["rider_count", "order_count", "rate_basis", "motorable_distance", "pickup_slot_start", "pickup_slot_end", "delivery_slot_start", "delivery_slot_end"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_fulfill_request_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_fulfill_request",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_fulfill_response(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]")
            sub_results = []
            valid = True

            for validate_tag_3_fulfill_response_obj in scope:
                validate_tag_3_fulfill_response_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_fulfill_response_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_fulfill_response_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_fulfill_response",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_fulfill_response**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')].list[*].code must be in ["rider_count", "order_count", "rate_basis"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_fulfill_response_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_fulfill_response",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_state(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='state')]")
            sub_results = []
            valid = True

            for validate_tag_3_state_obj in scope:
                validate_tag_3_state_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_state_obj, "$.list[*].code")
                validValues = ["ready_to_ship"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_state_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_state",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_state**: every element of $.message.order.fulfillments[*].tags[?(@.code=='state')].list[*].code must be in ["ready_to_ship"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_state","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='state')]","subTags":"$.list[*].code","validValues":["ready_to_ship"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_state_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_state",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_state","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='state')]","subTags":"$.list[*].code","validValues":["ready_to_ship"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_rto_action(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='rto_action')]")
            sub_results = []
            valid = True

            for validate_tag_3_rto_action_obj in scope:
                validate_tag_3_rto_action_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_rto_action_obj, "$.list[*].code")
                validValues = ["return_to_origin"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_rto_action_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_rto_action",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_rto_action**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rto_action')].list[*].code must be in ["return_to_origin"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_rto_action","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')]","subTags":"$.list[*].code","validValues":["return_to_origin"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_rto_action_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_rto_action",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_rto_action","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')]","subTags":"$.list[*].code","validValues":["return_to_origin"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_provider(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='provider')]")
            sub_results = []
            valid = True

            for validate_tag_3_provider_obj in scope:
                validate_tag_3_provider_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_provider_obj, "$.list[*].code")
                validValues = ["name","address","tax_id"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_provider_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_provider",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_provider**: every element of $.message.order.fulfillments[*].tags[?(@.code=='provider')].list[*].code must be in ["name", "address", "tax_id"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='provider')]","subTags":"$.list[*].code","validValues":["name","address","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_provider_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_provider",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='provider')]","subTags":"$.list[*].code","validValues":["name","address","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_order(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='order')]")
            sub_results = []
            valid = True

            for validate_tag_3_order_obj in scope:
                validate_tag_3_order_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_order_obj, "$.list[*].code")
                validValues = ["id","weight_unit","weight_value","dim_unit","length","breadth","height"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_order_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_order",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_order**: every element of $.message.order.fulfillments[*].tags[?(@.code=='order')].list[*].code must be in ["id", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='order')]","subTags":"$.list[*].code","validValues":["id","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_order_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_order",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='order')]","subTags":"$.list[*].code","validValues":["id","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_rto_verification(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]")
            sub_results = []
            valid = True

            for validate_tag_3_rto_verification_obj in scope:
                validate_tag_3_rto_verification_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_rto_verification_obj, "$.list[*].code")
                validValues = ["code","short_desc"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_rto_verification_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_rto_verification",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_rto_verification**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rto_verification')].list[*].code must be in ["code", "short_desc"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_rto_verification_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_rto_verification",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_items(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='items')]")
            sub_results = []
            valid = True

            for validate_tag_3_items_obj in scope:
                validate_tag_3_items_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_items_obj, "$.list[*].code")
                validValues = ["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_items_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_items",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_items**: every element of $.message.order.fulfillments[*].tags[?(@.code=='items')].list[*].code must be in ["category", "name", "currency", "value", "quantity", "weight_unit", "weight_value", "hsn_code", "ebn_exempt"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_items","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='items')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_items_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_items",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_items","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='items')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_reverseqc_input(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_input')]")
            sub_results = []
            valid = True

            for validate_tag_3_reverseqc_input_obj in scope:
                validate_tag_3_reverseqc_input_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_reverseqc_input_obj, "$.list[*].code")
                validValues = ["P001","P003","Q001"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_reverseqc_input_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_reverseqc_input",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_reverseqc_input**: every element of $.message.order.fulfillments[*].tags[?(@.code=='reverseqc_input')].list[*].code must be in ["P001", "P003", "Q001"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_reverseqc_input","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_input')]","subTags":"$.list[*].code","validValues":["P001","P003","Q001"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_reverseqc_input_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_reverseqc_input",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_reverseqc_input","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_input')]","subTags":"$.list[*].code","validValues":["P001","P003","Q001"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_4(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_4_obj in scope:
                validate_tag_4_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["bap_terms","lbnp_sla_terms"]
                tagPath = payload_utils["get_json_path"](validate_tag_4_obj, "$.message.order.tags[*].code")

                skip_check = not (validation_utils["are_present"](tagPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](tagPath, validTags)

                if not validate:
                    del validate_tag_4_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_4",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_4**: every element of $.message.order.tags[*].code must be in ["bap_terms", "lbnp_sla_terms"]

        	> Note: **Condition validate_tag_4** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_4","validTags":["bap_terms","lbnp_sla_terms"],"tagPath":"$.message.order.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
                        }
                    }]

                # del validate_tag_4_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_4",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_4","validTags":["bap_terms","lbnp_sla_terms"],"tagPath":"$.message.order.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_4_bap_terms(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.tags[?(@.code=='bap_terms')]")
            sub_results = []
            valid = True

            for validate_tag_4_bap_terms_obj in scope:
                validate_tag_4_bap_terms_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_4_bap_terms_obj, "$.list[*].code")
                validValues = ["accept_bpp_terms","phone"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_4_bap_terms_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_4_bap_terms",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_4_bap_terms**: every element of $.message.order.tags[?(@.code=='bap_terms')].list[*].code must be in ["accept_bpp_terms", "phone"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_4_bap_terms","_SCOPE_":"$.message.order.tags[?(@.code=='bap_terms')]","subTags":"$.list[*].code","validValues":["accept_bpp_terms","phone"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_4_bap_terms_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_4_bap_terms",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_4_bap_terms","_SCOPE_":"$.message.order.tags[?(@.code=='bap_terms')]","subTags":"$.list[*].code","validValues":["accept_bpp_terms","phone"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_4_lbnp_sla_terms(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.tags[?(@.code=='lbnp_sla_terms')]")
            sub_results = []
            valid = True

            for validate_tag_4_lbnp_sla_terms_obj in scope:
                validate_tag_4_lbnp_sla_terms_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_4_lbnp_sla_terms_obj, "$.list[*].code")
                validValues = ["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_4_lbnp_sla_terms_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_4_lbnp_sla_terms",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_4_lbnp_sla_terms**: every element of $.message.order.tags[?(@.code=='lbnp_sla_terms')].list[*].code must be in ["metric", "base_unit", "base_min", "base_max", "penalty_min", "penalty_max", "penalty_unit", "penalty_value"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_4_lbnp_sla_terms","_SCOPE_":"$.message.order.tags[?(@.code=='lbnp_sla_terms')]","subTags":"$.list[*].code","validValues":["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_4_lbnp_sla_terms_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_4_lbnp_sla_terms",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_4_lbnp_sla_terms","_SCOPE_":"$.message.order.tags[?(@.code=='lbnp_sla_terms')]","subTags":"$.list[*].code","validValues":["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def confirm_fulfillment_id_validations(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for confirm_fulfillment_id_validations_obj in scope:
                confirm_fulfillment_id_validations_obj["_EXTERNAL"] = input_data["external_data"]

                def validate_fulfillment_id_in_items(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for validate_fulfillment_id_in_items_obj in scope:
                        validate_fulfillment_id_in_items_obj["_EXTERNAL"] = input_data["external_data"]
                        fulfillment_id = payload_utils["get_json_path"](validate_fulfillment_id_in_items_obj, "$.message.order.items[*].fulfillment_id")
                        fulfillment_ids = payload_utils["get_json_path"](validate_fulfillment_id_in_items_obj, "$.message.order.items[*].fulfillment_ids[*]")

                        validate = (validation_utils["are_present"](fulfillment_id)) or (validation_utils["are_present"](fulfillment_ids))

                        if not validate:
                            del validate_fulfillment_id_in_items_obj["_EXTERNAL"]
                            return [{
                                "test_name": "validate_fulfillment_id_in_items",
                                "valid": False,
                                "code": 30000,
                                "description": r"""fulfillment_id or fulfillment_ids should be present in items""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"validate_fulfillment_id_in_items","_DESCRIPTION_":"fulfillment_id or fulfillment_ids should be present in items","fulfillment_id":"$.message.order.items[*].fulfillment_id","fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"fulfillment_id are present || fulfillment_ids are present"}
                """
                                }
                            }]

                        # del validate_fulfillment_id_in_items_obj["_EXTERNAL"]

                    return [{
                        "test_name": "validate_fulfillment_id_in_items",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"validate_fulfillment_id_in_items","_DESCRIPTION_":"fulfillment_id or fulfillment_ids should be present in items","fulfillment_id":"$.message.order.items[*].fulfillment_id","fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"fulfillment_id are present || fulfillment_ids are present"}
                """
                    }}] + sub_results

                def validate_fulfillment_id_in_fulfillments(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for validate_fulfillment_id_in_fulfillments_obj in scope:
                        validate_fulfillment_id_in_fulfillments_obj["_EXTERNAL"] = input_data["external_data"]
                        fulfillment_id = payload_utils["get_json_path"](validate_fulfillment_id_in_fulfillments_obj, "$.message.order.fulfillments[*].id")
                        item_fulfillment_id = payload_utils["get_json_path"](validate_fulfillment_id_in_fulfillments_obj, "$.message.order.items[*].fulfillment_id")
                        item_fulfillment_ids = payload_utils["get_json_path"](validate_fulfillment_id_in_fulfillments_obj, "$.message.order.items[*].fulfillment_ids[*]")

                        validate = (validation_utils["all_in"](item_fulfillment_id, fulfillment_id)) or (validation_utils["all_in"](item_fulfillment_ids, fulfillment_id))

                        if not validate:
                            del validate_fulfillment_id_in_fulfillments_obj["_EXTERNAL"]
                            return [{
                                "test_name": "validate_fulfillment_id_in_fulfillments",
                                "valid": False,
                                "code": 30000,
                                "description": r"""Fulfillment id in items should be mapped correctly in fulfillments array""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"validate_fulfillment_id_in_fulfillments","_DESCRIPTION_":"Fulfillment id in items should be mapped correctly in fulfillments array","fulfillment_id":"$.message.order.fulfillments[*].id","item_fulfillment_id":"$.message.order.items[*].fulfillment_id","item_fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"item_fulfillment_id all in fulfillment_id || item_fulfillment_ids all in fulfillment_id"}
                """
                                }
                            }]

                        # del validate_fulfillment_id_in_fulfillments_obj["_EXTERNAL"]

                    return [{
                        "test_name": "validate_fulfillment_id_in_fulfillments",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"validate_fulfillment_id_in_fulfillments","_DESCRIPTION_":"Fulfillment id in items should be mapped correctly in fulfillments array","fulfillment_id":"$.message.order.fulfillments[*].id","item_fulfillment_id":"$.message.order.items[*].fulfillment_id","item_fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"item_fulfillment_id all in fulfillment_id || item_fulfillment_ids all in fulfillment_id"}
                """
                    }}] + sub_results

                test_functions = [
                    validate_fulfillment_id_in_items,
                    validate_fulfillment_id_in_fulfillments,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del confirm_fulfillment_id_validations_obj["_EXTERNAL"]

            return [{
                "test_name": "confirm_fulfillment_id_validations",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"confirm_fulfillment_id_validations","_RETURN_":[{"_NAME_":"validate_fulfillment_id_in_items","_DESCRIPTION_":"fulfillment_id or fulfillment_ids should be present in items","fulfillment_id":"$.message.order.items[*].fulfillment_id","fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"fulfillment_id are present || fulfillment_ids are present"},{"_NAME_":"validate_fulfillment_id_in_fulfillments","_DESCRIPTION_":"Fulfillment id in items should be mapped correctly in fulfillments array","fulfillment_id":"$.message.order.fulfillments[*].id","item_fulfillment_id":"$.message.order.items[*].fulfillment_id","item_fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"item_fulfillment_id all in fulfillment_id || item_fulfillment_ids all in fulfillment_id"}]}
        """
            }}] + sub_results

        def instructions_validations(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for instructions_validations_obj in scope:
                instructions_validations_obj["_EXTERNAL"] = input_data["external_data"]

                def start_instructions_short_desc_present(input_data):
                    scope = payload_utils["get_json_path"](input_data["payload"], "$")
                    sub_results = []
                    valid = True

                    for start_instructions_short_desc_present_obj in scope:
                        start_instructions_short_desc_present_obj["_EXTERNAL"] = input_data["external_data"]
                        ship_status = ["yes"]
                        instructions_code = payload_utils["get_json_path"](start_instructions_short_desc_present_obj, "$.message.order.fulfillments[*].start.instructions.code")
                        instructions_short_desc = payload_utils["get_json_path"](start_instructions_short_desc_present_obj, "$.message.order.fulfillments[*].start.instructions.short_desc")
                        shipStatus = payload_utils["get_json_path"](start_instructions_short_desc_present_obj, "$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value")

                        skip_check = not (validation_utils["all_in"](shipStatus, ship_status))
                        if skip_check:
                            continue

                        validate = (validation_utils["are_present"](instructions_code)) and (validation_utils["are_present"](instructions_short_desc))

                        if not validate:
                            del start_instructions_short_desc_present_obj["_EXTERNAL"]
                            return [{
                                "test_name": "start_instructions_short_desc_present",
                                "valid": False,
                                "code": 30000,
                                "description": r"""In start instructions, short description is required when ready_to_ship = yes

                	> Note: **Condition start_instructions_short_desc_present** can be skipped if the following conditions are met:
                	>
                	> - **condition B**: every element of $.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value must **not** be in ["yes"]""",
                                "_debug_info": {
                                    "fed_config": r"""
                {"_NAME_":"start_instructions_short_desc_present","_DESCRIPTION_":"In start instructions, short description is required when ready_to_ship = yes","ship_status":["yes"],"instructions_code":"$.message.order.fulfillments[*].start.instructions.code","instructions_short_desc":"$.message.order.fulfillments[*].start.instructions.short_desc","shipStatus":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_CONTINUE_":"!(shipStatus all in ship_status)","_RETURN_":"instructions_code are present && instructions_short_desc are present"}
                """
                                }
                            }]

                        # del start_instructions_short_desc_present_obj["_EXTERNAL"]

                    return [{
                        "test_name": "start_instructions_short_desc_present",
                        "valid": valid,
                        "code": 200 if valid else 30000, 
                        "_debug_info": {
                            "fed_config": r"""
                {"_NAME_":"start_instructions_short_desc_present","_DESCRIPTION_":"In start instructions, short description is required when ready_to_ship = yes","ship_status":["yes"],"instructions_code":"$.message.order.fulfillments[*].start.instructions.code","instructions_short_desc":"$.message.order.fulfillments[*].start.instructions.short_desc","shipStatus":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_CONTINUE_":"!(shipStatus all in ship_status)","_RETURN_":"instructions_code are present && instructions_short_desc are present"}
                """
                    }}] + sub_results

                test_functions = [
                    start_instructions_short_desc_present,
                ]

                all_results = []
                for fn in test_functions:
                    sub_result = fn(input_data)
                    all_results.extend(sub_result)

                sub_results = all_results
                valid = all(r["valid"] for r in sub_results)

                # del instructions_validations_obj["_EXTERNAL"]

            return [{
                "test_name": "instructions_validations",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"instructions_validations","_RETURN_":[{"_NAME_":"start_instructions_short_desc_present","_DESCRIPTION_":"In start instructions, short description is required when ready_to_ship = yes","ship_status":["yes"],"instructions_code":"$.message.order.fulfillments[*].start.instructions.code","instructions_short_desc":"$.message.order.fulfillments[*].start.instructions.short_desc","shipStatus":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_CONTINUE_":"!(shipStatus all in ship_status)","_RETURN_":"instructions_code are present && instructions_short_desc are present"}]}
        """
            }}] + sub_results

        def accept_bpp_terms(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for accept_bpp_terms_obj in scope:
                accept_bpp_terms_obj["_EXTERNAL"] = input_data["external_data"]
                tags = payload_utils["get_json_path"](accept_bpp_terms_obj, "$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='accept_bpp_terms')].value")
                acceptance = ["yes"]

                validate = validation_utils["all_in"](tags, acceptance)

                if not validate:
                    del accept_bpp_terms_obj["_EXTERNAL"]
                    return [{
                        "test_name": "accept_bpp_terms",
                        "valid": False,
                        "code": 30000,
                        "description": r"""Acceptance to the LSP terms should be provided by LBNP in order/tags""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"accept_bpp_terms","_DESCRIPTION_":"Acceptance to the LSP terms should be provided by LBNP in order/tags","tags":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='accept_bpp_terms')].value","acceptance":["yes"],"_RETURN_":"tags all in acceptance"}
        """
                        }
                    }]

                # del accept_bpp_terms_obj["_EXTERNAL"]

            return [{
                "test_name": "accept_bpp_terms",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"accept_bpp_terms","_DESCRIPTION_":"Acceptance to the LSP terms should be provided by LBNP in order/tags","tags":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='accept_bpp_terms')].value","acceptance":["yes"],"_RETURN_":"tags all in acceptance"}
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
            REQUIRED_MESSAGE_ID,
            REQUIRED_MESSAGE_STATE,
            REQUIRED_MESSAGE_ID_16,
            REQUIRED_MESSAGE_CATEGORY_ID,
            REQUIRED_MESSAGE_LABEL,
            REQUIRED_MESSAGE_DURATION,
            REQUIRED_MESSAGE_TIMESTAMP,
            REQUIRED_MESSAGE_CURRENCY,
            REQUIRED_MESSAGE_VALUE,
            REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID,
            REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE,
            REQUIRED_MESSAGE_CURRENCY_25,
            REQUIRED_MESSAGE_VALUE_26,
            REQUIRED_MESSAGE_ID_27,
            REQUIRED_MESSAGE_TYPE,
            REQUIRED_MESSAGE_DURATION_29,
            REQUIRED_MESSAGE_NAME,
            REQUIRED_MESSAGE_ID_31,
            REQUIRED_MESSAGE_GPS,
            REQUIRED_MESSAGE_NAME_33,
            REQUIRED_MESSAGE_BUILDING,
            REQUIRED_MESSAGE_LOCALITY,
            REQUIRED_MESSAGE_CITY,
            REQUIRED_MESSAGE_STATE_37,
            REQUIRED_MESSAGE_COUNTRY,
            REQUIRED_MESSAGE_AREA_CODE,
            REQUIRED_MESSAGE_PHONE,
            REQUIRED_MESSAGE_EMAIL,
            REQUIRED_MESSAGE_NAME_42,
            REQUIRED_MESSAGE_GPS_43,
            REQUIRED_MESSAGE_NAME_44,
            REQUIRED_MESSAGE_BUILDING_45,
            REQUIRED_MESSAGE_LOCALITY_46,
            REQUIRED_MESSAGE_CITY_47,
            REQUIRED_MESSAGE_STATE_48,
            REQUIRED_MESSAGE_COUNTRY_49,
            REQUIRED_MESSAGE_AREA_CODE_50,
            REQUIRED_MESSAGE_PHONE_51,
            REQUIRED_MESSAGE_EMAIL_52,
            REQUIRED_MESSAGE_NAME_53,
            REQUIRED_MESSAGE_NAME_54,
            REQUIRED_MESSAGE_BUILDING_55,
            REQUIRED_MESSAGE_LOCALITY_56,
            REQUIRED_MESSAGE_CITY_57,
            REQUIRED_MESSAGE_STATE_58,
            REQUIRED_MESSAGE_COUNTRY_59,
            REQUIRED_MESSAGE_AREA_CODE_60,
            REQUIRED_MESSAGE_TAX_NUMBER,
            REQUIRED_MESSAGE_PHONE_62,
            REQUIRED_MESSAGE_EMAIL_63,
            REQUIRED_MESSAGE_CREATED_AT,
            REQUIRED_MESSAGE_UPDATED_AT,
            REQUIRED_MESSAGE_COLLECTED_BY,
            REQUIRED_MESSAGE_TYPE_67,
            REQUIRED_MESSAGE_NAME_68,
            REQUIRED_MESSAGE_COUNT,
            REQUIRED_MESSAGE_UNIT,
            REQUIRED_MESSAGE_VALUE_71,
            REQUIRED_MESSAGE_CURRENCY_72,
            REQUIRED_MESSAGE_VALUE_73,
            REQUIRED_MESSAGE_NAME_74,
            REQUIRED_MESSAGE_NAME_75,
            REQUIRED_MESSAGE_BUILDING_76,
            REQUIRED_MESSAGE_LOCALITY_77,
            REQUIRED_MESSAGE_CITY_78,
            REQUIRED_MESSAGE_STATE_79,
            REQUIRED_MESSAGE_AREA_CODE_80,
            REQUIRED_MESSAGE_ID_81,
            REQUIRED_MESSAGE_UNIT_82,
            REQUIRED_MESSAGE_VALUE_83,
            REQUIRED_MESSAGE_UNIT_84,
            REQUIRED_MESSAGE_VALUE_85,
            REQUIRED_MESSAGE_UNIT_86,
            REQUIRED_MESSAGE_VALUE_87,
            REQUIRED_MESSAGE_UNIT_88,
            REQUIRED_MESSAGE_VALUE_89,
            REQUIRED_MESSAGE_CREATED_AT_90,
            REQUIRED_MESSAGE_UPDATED_AT_91,
            VALID_ENUM_CONTEXT_DOMAIN,
            VALID_ENUM_MESSAGE_CATEGORY_ID,
            VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE,
            VALID_ENUM_MESSAGE_TYPE,
            VALID_ENUM_MESSAGE_TYPE_5,
            VALID_ENUM_MESSAGE_CODE,
            VALID_ENUM_MESSAGE_TYPE_7,
            VALID_ENUM_MESSAGE_CODE_8,
            VALID_ENUM_MESSAGE_CODE_9,
            VALID_ENUM_MESSAGE_TYPE_10,
            VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY,
            validate_tag_0,
            validate_tag_0_type,
            validate_tag_1,
            validate_tag_1_masked_contact,
            validate_tag_2,
            validate_tag_2_masked_contact,
            validate_tag_3,
            validate_tag_3_linked_provider,
            validate_tag_3_linked_order,
            validate_tag_3_linked_order_item,
            validate_tag_3_cod_settlement_detail,
            validate_tag_3_fulfill_request,
            validate_tag_3_fulfill_response,
            validate_tag_3_state,
            validate_tag_3_rto_action,
            validate_tag_3_provider,
            validate_tag_3_order,
            validate_tag_3_rto_verification,
            validate_tag_3_items,
            validate_tag_3_reverseqc_input,
            validate_tag_4,
            validate_tag_4_bap_terms,
            validate_tag_4_lbnp_sla_terms,
            confirm_fulfillment_id_validations,
            instructions_validations,
            accept_bpp_terms,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del confirm_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "confirm_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"confirm_validations","_RETURN_":[{"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]},{"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TTL","attr":"$.context.ttl","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.order.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE","attr":"$.message.order.state","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.order.items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]},{"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.order.items[*].time.label","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.order.items[*].time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.order.items[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_RETURN_":"attr are present && attr all in enumList","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"]},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY_25","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_26","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_27","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]},{"_NAME_":"REQUIRED_MESSAGE_DURATION_29","attr":"$.message.order.fulfillments[*].start.time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.order.fulfillments[*].start.person.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_31","attr":"$.message.order.fulfillments[*].start.location.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_33","attr":"$.message.order.fulfillments[*].start.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING","attr":"$.message.order.fulfillments[*].start.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_37","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNTRY","attr":"$.message.order.fulfillments[*].start.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_42","attr":"$.message.order.fulfillments[*].end.person.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_GPS_43","attr":"$.message.order.fulfillments[*].end.location.gps","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_44","attr":"$.message.order.fulfillments[*].end.location.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING_45","attr":"$.message.order.fulfillments[*].end.location.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY_46","attr":"$.message.order.fulfillments[*].end.location.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY_47","attr":"$.message.order.fulfillments[*].end.location.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_48","attr":"$.message.order.fulfillments[*].end.location.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNTRY_49","attr":"$.message.order.fulfillments[*].end.location.address.country","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_50","attr":"$.message.order.fulfillments[*].end.location.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE_51","attr":"$.message.order.fulfillments[*].end.contact.phone","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_EMAIL_52","attr":"$.message.order.fulfillments[*].end.contact.email","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_53","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_54","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING_55","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY_56","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY_57","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_58","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNTRY_59","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_60","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE_62","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_EMAIL_63","attr":"$.message.order.billing.email","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COLLECTED_BY","attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE_67","attr":"$.message.order.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]},{"_NAME_":"REQUIRED_MESSAGE_NAME_68","attr":"$.message.order['@ondc/org/linked_order'].items[*].descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.count","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_71","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY_72","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.currency","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_73","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_74","attr":"$.message.order['@ondc/org/linked_order'].provider.descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_75","attr":"$.message.order['@ondc/org/linked_order'].provider.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING_76","attr":"$.message.order['@ondc/org/linked_order'].provider.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY_77","attr":"$.message.order['@ondc/org/linked_order'].provider.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY_78","attr":"$.message.order['@ondc/org/linked_order'].provider.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_79","attr":"$.message.order['@ondc/org/linked_order'].provider.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_80","attr":"$.message.order['@ondc/org/linked_order'].provider.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_81","attr":"$.message.order['@ondc/org/linked_order'].order.id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_82","attr":"$.message.order['@ondc/org/linked_order'].order.weight.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_83","attr":"$.message.order['@ondc/org/linked_order'].order.weight.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_84","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_85","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_86","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_87","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_88","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_89","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CREATED_AT_90","attr":"$.message.order.created_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_91","attr":"$.message.order.updated_at","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.order.items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"],"enumPath":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.order.fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.order.fulfillments[*].start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_8","enumList":["1","2","3","5"],"enumPath":"$.message.order.fulfillments[*].end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_9","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"],"enumPath":"$.message.order.fulfillments[*].state.descriptor.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_10","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.order.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY","enumList":["lbnp","lsp"],"enumPath":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"validate_tag_0","validTags":["type"],"tagPath":"$.message.order.items[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_0_type","_SCOPE_":"$.message.order.items[*].tags[?(@.code=='type')]","subTags":"$.list[*].code","validValues":["type"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].start.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_1_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].end.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_2_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3","validTags":["linked_provider","linked_order","linked_order_item","cod_settlement_detail","fulfill_request","fulfill_response","state","rto_action","provider","order","rto_verification","items","reverseqc_input"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_3_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","currency","declared_value","collection_amount","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","return_to_origin","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_cod_settlement_detail","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]","subTags":"$.list[*].code","validValues":["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_state","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='state')]","subTags":"$.list[*].code","validValues":["ready_to_ship"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_rto_action","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_action')]","subTags":"$.list[*].code","validValues":["return_to_origin"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='provider')]","subTags":"$.list[*].code","validValues":["name","address","tax_id"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='order')]","subTags":"$.list[*].code","validValues":["id","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_items","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='items')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_reverseqc_input","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='reverseqc_input')]","subTags":"$.list[*].code","validValues":["P001","P003","Q001"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_4","validTags":["bap_terms","lbnp_sla_terms"],"tagPath":"$.message.order.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_4_bap_terms","_SCOPE_":"$.message.order.tags[?(@.code=='bap_terms')]","subTags":"$.list[*].code","validValues":["accept_bpp_terms","phone"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_4_lbnp_sla_terms","_SCOPE_":"$.message.order.tags[?(@.code=='lbnp_sla_terms')]","subTags":"$.list[*].code","validValues":["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"confirm_fulfillment_id_validations","_RETURN_":[{"_NAME_":"validate_fulfillment_id_in_items","_DESCRIPTION_":"fulfillment_id or fulfillment_ids should be present in items","fulfillment_id":"$.message.order.items[*].fulfillment_id","fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"fulfillment_id are present || fulfillment_ids are present"},{"_NAME_":"validate_fulfillment_id_in_fulfillments","_DESCRIPTION_":"Fulfillment id in items should be mapped correctly in fulfillments array","fulfillment_id":"$.message.order.fulfillments[*].id","item_fulfillment_id":"$.message.order.items[*].fulfillment_id","item_fulfillment_ids":"$.message.order.items[*].fulfillment_ids[*]","_RETURN_":"item_fulfillment_id all in fulfillment_id || item_fulfillment_ids all in fulfillment_id"}]},{"_NAME_":"instructions_validations","_RETURN_":[{"_NAME_":"start_instructions_short_desc_present","_DESCRIPTION_":"In start instructions, short description is required when ready_to_ship = yes","ship_status":["yes"],"instructions_code":"$.message.order.fulfillments[*].start.instructions.code","instructions_short_desc":"$.message.order.fulfillments[*].start.instructions.short_desc","shipStatus":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_CONTINUE_":"!(shipStatus all in ship_status)","_RETURN_":"instructions_code are present && instructions_short_desc are present"}]},{"_NAME_":"accept_bpp_terms","_DESCRIPTION_":"Acceptance to the LSP terms should be provided by LBNP in order/tags","tags":"$.message.order.tags[?(@.code=='bap_terms')].list[?(@.code=='accept_bpp_terms')].value","acceptance":["yes"],"_RETURN_":"tags all in acceptance"}]}
"""
    }}] + sub_results

def confirm(input_data):
    total_results = confirm_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "confirm_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
