from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def update_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for update_validations_obj in scope:
        update_validations_obj["_EXTERNAL"] = input_data["external_data"]

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

        def REQUIRED_MESSAGE_UPDATE_TARGET(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATE_TARGET_obj in scope:
                REQUIRED_MESSAGE_UPDATE_TARGET_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATE_TARGET_obj, "$.message.update_target")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATE_TARGET_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATE_TARGET",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATE_TARGET**: $.message.update_target must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATE_TARGET","attr":"$.message.update_target","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UPDATE_TARGET_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UPDATE_TARGET",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATE_TARGET","attr":"$.message.update_target","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_ID_16(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_16_obj in scope:
                REQUIRED_MESSAGE_ID_16_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_16_obj, "$.message.order.items[*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_16_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_16",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_16**: $.message.order.items[*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_UPDATED_AT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATED_AT_obj in scope:
                REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATED_AT_obj, "$.message.order.updated_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATED_AT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATED_AT**: $.message.order.updated_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.updated_at","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.updated_at","_RETURN_":"attr are present"}
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

        def VALID_ENUM_MESSAGE_STATE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_STATE_obj in scope:
                VALID_ENUM_MESSAGE_STATE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Created","Accepted","In-progress","Completed","Cancelled"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_STATE_obj, "$.message.order.state")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_STATE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_STATE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_STATE**: every element of $.message.order.state must be in ["Created", "Accepted", "In-progress", "Completed", "Cancelled"]

        	> Note: **Condition VALID_ENUM_MESSAGE_STATE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.state must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_STATE","enumList":["Created","Accepted","In-progress","Completed","Cancelled"],"enumPath":"$.message.order.state","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_STATE_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_STATE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_STATE","enumList":["Created","Accepted","In-progress","Completed","Cancelled"],"enumPath":"$.message.order.state","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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

        def validate_tag_0(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_0_obj in scope:
                validate_tag_0_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["state","rider_details","linked_provider","linked_order","linked_order_item","fulfill_request","rto_verification","fulfill_response"]
                tagPath = payload_utils["get_json_path"](validate_tag_0_obj, "$.message.order.fulfillments[*].tags[*].code")

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
                        "description": r"""- **condition validate_tag_0**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["state", "rider_details", "linked_provider", "linked_order", "linked_order_item", "fulfill_request", "rto_verification", "fulfill_response"]

        	> Note: **Condition validate_tag_0** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0","validTags":["state","rider_details","linked_provider","linked_order","linked_order_item","fulfill_request","rto_verification","fulfill_response"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_0","validTags":["state","rider_details","linked_provider","linked_order","linked_order_item","fulfill_request","rto_verification","fulfill_response"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_0_state(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='state')]")
            sub_results = []
            valid = True

            for validate_tag_0_state_obj in scope:
                validate_tag_0_state_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_state_obj, "$.list[*].code")
                validValues = ["ready_to_ship","order_ready"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_state_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_state",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_state**: every element of $.message.order.fulfillments[*].tags[?(@.code=='state')].list[*].code must be in ["ready_to_ship", "order_ready"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_state","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='state')]","subTags":"$.list[*].code","validValues":["ready_to_ship","order_ready"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_state_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_state",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_state","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='state')]","subTags":"$.list[*].code","validValues":["ready_to_ship","order_ready"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_rider_details(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]")
            sub_results = []
            valid = True

            for validate_tag_0_rider_details_obj in scope:
                validate_tag_0_rider_details_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_rider_details_obj, "$.list[*].code")
                validValues = ["name","phone","vehicle_registration"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_rider_details_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_rider_details",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_rider_details**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rider_details')].list[*].code must be in ["name", "phone", "vehicle_registration"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_rider_details","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]","subTags":"$.list[*].code","validValues":["name","phone","vehicle_registration"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_rider_details_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_rider_details",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_rider_details","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]","subTags":"$.list[*].code","validValues":["name","phone","vehicle_registration"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_linked_provider(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]")
            sub_results = []
            valid = True

            for validate_tag_0_linked_provider_obj in scope:
                validate_tag_0_linked_provider_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_linked_provider_obj, "$.list[*].code")
                validValues = ["id","name","address","cred_code","cred_desc","tax_id"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_linked_provider_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_linked_provider",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_linked_provider**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_provider')].list[*].code must be in ["id", "name", "address", "cred_code", "cred_desc", "tax_id"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_linked_provider_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_linked_provider",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_linked_order(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]")
            sub_results = []
            valid = True

            for validate_tag_0_linked_order_obj in scope:
                validate_tag_0_linked_order_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_linked_order_obj, "$.list[*].code")
                validValues = ["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_linked_order_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_linked_order",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_linked_order**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order')].list[*].code must be in ["id", "prep_time", "cod_order", "collection_amount", "currency", "declared_value", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height", "shipment_type"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_linked_order_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_linked_order",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_linked_order_item(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]")
            sub_results = []
            valid = True

            for validate_tag_0_linked_order_item_obj in scope:
                validate_tag_0_linked_order_item_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_linked_order_item_obj, "$.list[*].code")
                validValues = ["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_linked_order_item_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_linked_order_item",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_linked_order_item**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')].list[*].code must be in ["category", "name", "currency", "value", "quantity", "weight_unit", "weight_value", "hsn_code", "ebn_exempt"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_linked_order_item_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_linked_order_item",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_fulfill_request(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]")
            sub_results = []
            valid = True

            for validate_tag_0_fulfill_request_obj in scope:
                validate_tag_0_fulfill_request_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_fulfill_request_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_fulfill_request_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_fulfill_request",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_fulfill_request**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')].list[*].code must be in ["rider_count", "order_count", "rate_basis", "motorable_distance", "pickup_slot_start", "pickup_slot_end", "delivery_slot_start", "delivery_slot_end"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_fulfill_request_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_fulfill_request",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_rto_verification(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]")
            sub_results = []
            valid = True

            for validate_tag_0_rto_verification_obj in scope:
                validate_tag_0_rto_verification_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_rto_verification_obj, "$.list[*].code")
                validValues = ["code","short_desc"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_rto_verification_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_rto_verification",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_rto_verification**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rto_verification')].list[*].code must be in ["code", "short_desc"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_rto_verification_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_rto_verification",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_fulfill_response(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]")
            sub_results = []
            valid = True

            for validate_tag_0_fulfill_response_obj in scope:
                validate_tag_0_fulfill_response_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_fulfill_response_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_fulfill_response_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_fulfill_response",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_fulfill_response**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')].list[*].code must be in ["rider_count", "order_count", "rate_basis"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_fulfill_response_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_fulfill_response",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"}
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
            REQUIRED_MESSAGE_UPDATE_TARGET,
            REQUIRED_MESSAGE_ID,
            REQUIRED_MESSAGE_ID_16,
            REQUIRED_MESSAGE_CATEGORY_ID,
            REQUIRED_MESSAGE_TYPE,
            REQUIRED_MESSAGE_UPDATED_AT,
            VALID_ENUM_CONTEXT_DOMAIN,
            VALID_ENUM_MESSAGE_STATE,
            VALID_ENUM_MESSAGE_CATEGORY_ID,
            VALID_ENUM_MESSAGE_TYPE,
            VALID_ENUM_MESSAGE_TYPE_5,
            VALID_ENUM_MESSAGE_CODE,
            VALID_ENUM_MESSAGE_TYPE_7,
            VALID_ENUM_MESSAGE_CODE_8,
            VALID_ENUM_MESSAGE_CODE_9,
            VALID_ENUM_MESSAGE_TYPE_10,
            VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY,
            VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE,
            validate_tag_0,
            validate_tag_0_state,
            validate_tag_0_rider_details,
            validate_tag_0_linked_provider,
            validate_tag_0_linked_order,
            validate_tag_0_linked_order_item,
            validate_tag_0_fulfill_request,
            validate_tag_0_rto_verification,
            validate_tag_0_fulfill_response,
            instructions_validations,
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
{"_NAME_":"update_validations","_RETURN_":[{"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]},{"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TTL","attr":"$.context.ttl","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATE_TARGET","attr":"$.message.update_target","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.order.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.order.items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]},{"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.updated_at","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_STATE","enumList":["Created","Accepted","In-progress","Completed","Cancelled"],"enumPath":"$.message.order.state","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.order.items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.order.fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.order.fulfillments[*].start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_8","enumList":["1","2","3","5"],"enumPath":"$.message.order.fulfillments[*].end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_9","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"],"enumPath":"$.message.order.fulfillments[*].state.descriptor.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_10","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.order.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY","enumList":["lbnp","lsp"],"enumPath":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"],"enumPath":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"validate_tag_0","validTags":["state","rider_details","linked_provider","linked_order","linked_order_item","fulfill_request","rto_verification","fulfill_response"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_0_state","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='state')]","subTags":"$.list[*].code","validValues":["ready_to_ship","order_ready"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_rider_details","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]","subTags":"$.list[*].code","validValues":["name","phone","vehicle_registration"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"instructions_validations","_RETURN_":[{"_NAME_":"start_instructions_short_desc_present","_DESCRIPTION_":"In start instructions, short description is required when ready_to_ship = yes","ship_status":["yes"],"instructions_code":"$.message.order.fulfillments[*].start.instructions.code","instructions_short_desc":"$.message.order.fulfillments[*].start.instructions.short_desc","shipStatus":"$.message.order.fulfillments[*].tags[?(@.code=='state')].list[?(@.code=='ready_to_ship')].value","_CONTINUE_":"!(shipStatus all in ship_status)","_RETURN_":"instructions_code are present && instructions_short_desc are present"}]}]}
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
