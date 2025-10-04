from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_update_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_update_validations_obj in scope:
        on_update_validations_obj["_EXTERNAL"] = input_data["external_data"]

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
                enumList = ["Created","Accepted","In-progress","Completed","Cancelled"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_STATE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_STATE.1**: $.message.order.state must be present in the payload
          - **condition REQUIRED_MESSAGE_STATE.2**: every element of $.message.order.state must be in ["Created", "Accepted", "In-progress", "Completed", "Cancelled"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE","attr":"$.message.order.state","_RETURN_":"attr are present && attr all in enumList","enumList":["Created","Accepted","In-progress","Completed","Cancelled"]}
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
        {"_NAME_":"REQUIRED_MESSAGE_STATE","attr":"$.message.order.state","_RETURN_":"attr are present && attr all in enumList","enumList":["Created","Accepted","In-progress","Completed","Cancelled"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_15(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_15_obj in scope:
                REQUIRED_MESSAGE_ID_15_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_15_obj, "$.message.order.provider.id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_15_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_15",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_15**: $.message.order.provider.id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_15","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_15_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_15",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_15","attr":"$.message.order.provider.id","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_CODE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CODE_obj in scope:
                REQUIRED_MESSAGE_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CODE_obj, "$.message.order.fulfillments[*].state.descriptor.code")
                enumList = ["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_CODE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CODE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CODE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_CODE.1**: $.message.order.fulfillments[*].state.descriptor.code must be present in the payload
          - **condition REQUIRED_MESSAGE_CODE.2**: every element of $.message.order.fulfillments[*].state.descriptor.code must be in ["Pending", "Cancelled", "Order-picked-up", "RTO", "RTO-Initiated", "RTO-Delivered", "RTO-Disposed", "Out-for-pickup", "At-destination-hub", "In-transit", "At-pickup", "Out-for-delivery", "At-delivery", "Searching-for-Agent", "Agent-assigned", "Pickup-failed", "Pickup-rescheduled", "Delivery-failed", "Delivery-rescheduled", "Order-delivered"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","_RETURN_":"attr are present && attr all in enumList","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CODE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CODE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","_RETURN_":"attr are present && attr all in enumList","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TRACKING(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TRACKING_obj in scope:
                REQUIRED_MESSAGE_TRACKING_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TRACKING_obj, "$.message.order.fulfillments[*].tracking")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_TRACKING_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TRACKING",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TRACKING**: $.message.order.fulfillments[*].tracking must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TRACKING_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TRACKING",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_ID_32(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_32_obj in scope:
                REQUIRED_MESSAGE_ID_32_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_32_obj, "$.message.order.fulfillments[*].start.location.id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_32_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_32",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_32**: $.message.order.fulfillments[*].start.location.id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_32","attr":"$.message.order.fulfillments[*].start.location.id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_32_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_32",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_32","attr":"$.message.order.fulfillments[*].start.location.id","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_NAME_34(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_34_obj in scope:
                REQUIRED_MESSAGE_NAME_34_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_34_obj, "$.message.order.fulfillments[*].start.location.address.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_34_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_34",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_34**: $.message.order.fulfillments[*].start.location.address.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_34","attr":"$.message.order.fulfillments[*].start.location.address.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_34_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_34",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_34","attr":"$.message.order.fulfillments[*].start.location.address.name","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_STATE_38(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_38_obj in scope:
                REQUIRED_MESSAGE_STATE_38_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_38_obj, "$.message.order.fulfillments[*].start.location.address.state")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_38_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_38",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_38**: $.message.order.fulfillments[*].start.location.address.state must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_38","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_38_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_38",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_38","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_DURATION_43(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_43_obj in scope:
                REQUIRED_MESSAGE_DURATION_43_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_43_obj, "$.message.order.fulfillments[*].start.time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_43_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION_43",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION_43**: $.message.order.fulfillments[*].start.time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION_43","attr":"$.message.order.fulfillments[*].start.time.duration","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_DURATION_43_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_DURATION_43",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION_43","attr":"$.message.order.fulfillments[*].start.time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_START(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_START_obj in scope:
                REQUIRED_MESSAGE_START_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_START_obj, "$.message.order.fulfillments[*].start.time.range.start")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_START_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_START",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_START**: $.message.order.fulfillments[*].start.time.range.start must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_START","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_START_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_START",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_START","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_END(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_END_obj in scope:
                REQUIRED_MESSAGE_END_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_END_obj, "$.message.order.fulfillments[*].start.time.range.end")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_END_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_END",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_END**: $.message.order.fulfillments[*].start.time.range.end must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_END","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_END_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_END",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_END","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_46(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_46_obj in scope:
                REQUIRED_MESSAGE_NAME_46_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_46_obj, "$.message.order.fulfillments[*].end.person.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_46_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_46_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_46",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_46**: $.message.order.fulfillments[*].end.person.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_46** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_46","attr":"$.message.order.fulfillments[*].end.person.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_46_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_46",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_46","attr":"$.message.order.fulfillments[*].end.person.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_GPS_47(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_GPS_47_obj in scope:
                REQUIRED_MESSAGE_GPS_47_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_47_obj, "$.message.order.fulfillments[*].end.location.gps")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_47_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_GPS_47_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_GPS_47",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_GPS_47**: $.message.order.fulfillments[*].end.location.gps must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_GPS_47** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS_47","attr":"$.message.order.fulfillments[*].end.location.gps","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_GPS_47_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_GPS_47",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS_47","attr":"$.message.order.fulfillments[*].end.location.gps","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_48(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_48_obj in scope:
                REQUIRED_MESSAGE_NAME_48_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_48_obj, "$.message.order.fulfillments[*].end.location.address.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_48_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_48_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_48",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_48**: $.message.order.fulfillments[*].end.location.address.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_48** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_48","attr":"$.message.order.fulfillments[*].end.location.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_48_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_48",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_48","attr":"$.message.order.fulfillments[*].end.location.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING_49(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_49_obj in scope:
                REQUIRED_MESSAGE_BUILDING_49_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_49_obj, "$.message.order.fulfillments[*].end.location.address.building")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_49_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_49_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING_49",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING_49**: $.message.order.fulfillments[*].end.location.address.building must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_BUILDING_49** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_49","attr":"$.message.order.fulfillments[*].end.location.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_49_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING_49",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_49","attr":"$.message.order.fulfillments[*].end.location.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY_50(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_50_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_50_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_50_obj, "$.message.order.fulfillments[*].end.location.address.locality")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_50_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_50_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY_50",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY_50**: $.message.order.fulfillments[*].end.location.address.locality must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_LOCALITY_50** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_50","attr":"$.message.order.fulfillments[*].end.location.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_50_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY_50",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_50","attr":"$.message.order.fulfillments[*].end.location.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY_51(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_51_obj in scope:
                REQUIRED_MESSAGE_CITY_51_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_51_obj, "$.message.order.fulfillments[*].end.location.address.city")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_51_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_51_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY_51",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY_51**: $.message.order.fulfillments[*].end.location.address.city must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CITY_51** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_51","attr":"$.message.order.fulfillments[*].end.location.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_51_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY_51",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_51","attr":"$.message.order.fulfillments[*].end.location.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_52(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_52_obj in scope:
                REQUIRED_MESSAGE_STATE_52_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_52_obj, "$.message.order.fulfillments[*].end.location.address.state")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_52_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_52_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_52",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_52**: $.message.order.fulfillments[*].end.location.address.state must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_STATE_52** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_52","attr":"$.message.order.fulfillments[*].end.location.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_52_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_52",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_52","attr":"$.message.order.fulfillments[*].end.location.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COUNTRY_53(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COUNTRY_53_obj in scope:
                REQUIRED_MESSAGE_COUNTRY_53_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_53_obj, "$.message.order.fulfillments[*].end.location.address.country")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_53_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COUNTRY_53_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COUNTRY_53",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COUNTRY_53**: $.message.order.fulfillments[*].end.location.address.country must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_COUNTRY_53** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_53","attr":"$.message.order.fulfillments[*].end.location.address.country","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COUNTRY_53_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COUNTRY_53",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_53","attr":"$.message.order.fulfillments[*].end.location.address.country","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_54(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_54_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_54_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_54_obj, "$.message.order.fulfillments[*].end.location.address.area_code")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_54_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_54_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_54",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_54**: $.message.order.fulfillments[*].end.location.address.area_code must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_AREA_CODE_54** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_54","attr":"$.message.order.fulfillments[*].end.location.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_54_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_54",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_54","attr":"$.message.order.fulfillments[*].end.location.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_PHONE_55(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PHONE_55_obj in scope:
                REQUIRED_MESSAGE_PHONE_55_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_55_obj, "$.message.order.fulfillments[*].end.contact.phone")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_55_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PHONE_55_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PHONE_55",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PHONE_55**: $.message.order.fulfillments[*].end.contact.phone must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_PHONE_55** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_55","attr":"$.message.order.fulfillments[*].end.contact.phone","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_PHONE_55_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_PHONE_55",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_55","attr":"$.message.order.fulfillments[*].end.contact.phone","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_START_56(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_START_56_obj in scope:
                REQUIRED_MESSAGE_START_56_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_START_56_obj, "$.message.order.fulfillments[*].end.time.range.start")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_START_56_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_START_56_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_START_56",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_START_56**: $.message.order.fulfillments[*].end.time.range.start must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_START_56** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_START_56","attr":"$.message.order.fulfillments[*].end.time.range.start","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_START_56_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_START_56",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_START_56","attr":"$.message.order.fulfillments[*].end.time.range.start","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_END_57(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_END_57_obj in scope:
                REQUIRED_MESSAGE_END_57_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_END_57_obj, "$.message.order.fulfillments[*].end.time.range.end")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_END_57_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Delivery"]

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_END_57_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_END_57",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_END_57**: $.message.order.fulfillments[*].end.time.range.end must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_END_57** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.order.fulfillments[*].type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_END_57","attr":"$.message.order.fulfillments[*].end.time.range.end","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_END_57_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_END_57",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_END_57","attr":"$.message.order.fulfillments[*].end.time.range.end","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_58(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_58_obj in scope:
                REQUIRED_MESSAGE_NAME_58_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_58_obj, "$.message.order.billing.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_58_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_58",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_58**: $.message.order.billing.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_58","attr":"$.message.order.billing.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_58_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_58",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_58","attr":"$.message.order.billing.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_59(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_59_obj in scope:
                REQUIRED_MESSAGE_NAME_59_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_59_obj, "$.message.order.billing.address.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_59_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_59",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_59**: $.message.order.billing.address.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_59","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_59_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_59",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_59","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING_60(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_60_obj in scope:
                REQUIRED_MESSAGE_BUILDING_60_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_60_obj, "$.message.order.billing.address.building")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_60_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING_60",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING_60**: $.message.order.billing.address.building must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_60","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_60_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING_60",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_60","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY_61(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_61_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_61_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_61_obj, "$.message.order.billing.address.locality")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_61_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY_61",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY_61**: $.message.order.billing.address.locality must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_61","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_61_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY_61",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_61","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY_62(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_62_obj in scope:
                REQUIRED_MESSAGE_CITY_62_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_62_obj, "$.message.order.billing.address.city")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_62_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY_62",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY_62**: $.message.order.billing.address.city must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_62","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_62_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY_62",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_62","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_63(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_63_obj in scope:
                REQUIRED_MESSAGE_STATE_63_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_63_obj, "$.message.order.billing.address.state")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_63_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_63",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_63**: $.message.order.billing.address.state must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_63","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_63_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_63",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_63","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_COUNTRY_64(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_COUNTRY_64_obj in scope:
                REQUIRED_MESSAGE_COUNTRY_64_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_COUNTRY_64_obj, "$.message.order.billing.address.country")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_COUNTRY_64_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_COUNTRY_64",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_COUNTRY_64**: $.message.order.billing.address.country must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_64","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_COUNTRY_64_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_COUNTRY_64",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_COUNTRY_64","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_65(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_65_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_65_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_65_obj, "$.message.order.billing.address.area_code")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_65_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_65",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_65**: $.message.order.billing.address.area_code must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_65","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_65_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_65",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_65","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_PHONE_67(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PHONE_67_obj in scope:
                REQUIRED_MESSAGE_PHONE_67_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_67_obj, "$.message.order.billing.phone")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PHONE_67_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PHONE_67",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PHONE_67**: $.message.order.billing.phone must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_67","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_PHONE_67_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_PHONE_67",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE_67","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_EMAIL_68(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_EMAIL_68_obj in scope:
                REQUIRED_MESSAGE_EMAIL_68_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_EMAIL_68_obj, "$.message.order.billing.email")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_EMAIL_68_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_EMAIL_68",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_EMAIL_68**: $.message.order.billing.email must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL_68","attr":"$.message.order.billing.email","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_EMAIL_68_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_EMAIL_68",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL_68","attr":"$.message.order.billing.email","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_TYPE_72(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_72_obj in scope:
                REQUIRED_MESSAGE_TYPE_72_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_72_obj, "$.message.order.payment.type")
                enumList = ["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_72_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE_72",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE_72**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE_72.1**: $.message.order.payment.type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE_72.2**: every element of $.message.order.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT", "POST-FULFILLMENT"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE_72","attr":"$.message.order.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TYPE_72_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TYPE_72",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE_72","attr":"$.message.order.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CATEGORY_ID_73(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CATEGORY_ID_73_obj in scope:
                REQUIRED_MESSAGE_CATEGORY_ID_73_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CATEGORY_ID_73_obj, "$.message.order['@ondc/org/linked_order'].items[*].category_id")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CATEGORY_ID_73_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CATEGORY_ID_73_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CATEGORY_ID_73",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CATEGORY_ID_73**: $.message.order['@ondc/org/linked_order'].items[*].category_id must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CATEGORY_ID_73** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID_73","attr":"$.message.order['@ondc/org/linked_order'].items[*].category_id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CATEGORY_ID_73_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CATEGORY_ID_73",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID_73","attr":"$.message.order['@ondc/org/linked_order'].items[*].category_id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_74(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_74_obj in scope:
                REQUIRED_MESSAGE_NAME_74_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_74_obj, "$.message.order['@ondc/org/linked_order'].items[*].descriptor.name")
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
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_74**: $.message.order['@ondc/org/linked_order'].items[*].descriptor.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_74** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_74","attr":"$.message.order['@ondc/org/linked_order'].items[*].descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_NAME_74","attr":"$.message.order['@ondc/org/linked_order'].items[*].descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
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

        def REQUIRED_MESSAGE_VALUE_77(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_77_obj in scope:
                REQUIRED_MESSAGE_VALUE_77_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_77_obj, "$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_77_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_77_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_77",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_77**: $.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_77** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_77","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_77_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_77",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_77","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CURRENCY_78(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CURRENCY_78_obj in scope:
                REQUIRED_MESSAGE_CURRENCY_78_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_78_obj, "$.message.order['@ondc/org/linked_order'].items[*].price.currency")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_78_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CURRENCY_78_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CURRENCY_78",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CURRENCY_78**: $.message.order['@ondc/org/linked_order'].items[*].price.currency must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CURRENCY_78** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY_78","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.currency","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CURRENCY_78_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CURRENCY_78",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY_78","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.currency","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_79(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_79_obj in scope:
                REQUIRED_MESSAGE_VALUE_79_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_79_obj, "$.message.order['@ondc/org/linked_order'].items[*].price.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_79_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_79_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_79",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_79**: $.message.order['@ondc/org/linked_order'].items[*].price.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_79** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_79","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_79_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_79",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_79","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_80(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_80_obj in scope:
                REQUIRED_MESSAGE_NAME_80_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_80_obj, "$.message.order['@ondc/org/linked_order'].provider.descriptor.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_80_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_80_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_80",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_80**: $.message.order['@ondc/org/linked_order'].provider.descriptor.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_80** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_80","attr":"$.message.order['@ondc/org/linked_order'].provider.descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_80_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_80",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_80","attr":"$.message.order['@ondc/org/linked_order'].provider.descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_81(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_81_obj in scope:
                REQUIRED_MESSAGE_NAME_81_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_81_obj, "$.message.order['@ondc/org/linked_order'].provider.address.name")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_81_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_81_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_81",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_81**: $.message.order['@ondc/org/linked_order'].provider.address.name must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_NAME_81** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_81","attr":"$.message.order['@ondc/org/linked_order'].provider.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_81_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_81",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_81","attr":"$.message.order['@ondc/org/linked_order'].provider.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_BUILDING_82(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_BUILDING_82_obj in scope:
                REQUIRED_MESSAGE_BUILDING_82_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_82_obj, "$.message.order['@ondc/org/linked_order'].provider.address.building")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_BUILDING_82_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_BUILDING_82_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_BUILDING_82",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_BUILDING_82**: $.message.order['@ondc/org/linked_order'].provider.address.building must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_BUILDING_82** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_82","attr":"$.message.order['@ondc/org/linked_order'].provider.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_BUILDING_82_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_BUILDING_82",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_BUILDING_82","attr":"$.message.order['@ondc/org/linked_order'].provider.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LOCALITY_83(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LOCALITY_83_obj in scope:
                REQUIRED_MESSAGE_LOCALITY_83_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_83_obj, "$.message.order['@ondc/org/linked_order'].provider.address.locality")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_LOCALITY_83_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LOCALITY_83_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LOCALITY_83",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LOCALITY_83**: $.message.order['@ondc/org/linked_order'].provider.address.locality must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_LOCALITY_83** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_83","attr":"$.message.order['@ondc/org/linked_order'].provider.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LOCALITY_83_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LOCALITY_83",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LOCALITY_83","attr":"$.message.order['@ondc/org/linked_order'].provider.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CITY_84(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CITY_84_obj in scope:
                REQUIRED_MESSAGE_CITY_84_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_84_obj, "$.message.order['@ondc/org/linked_order'].provider.address.city")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CITY_84_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CITY_84_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CITY_84",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CITY_84**: $.message.order['@ondc/org/linked_order'].provider.address.city must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CITY_84** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_84","attr":"$.message.order['@ondc/org/linked_order'].provider.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CITY_84_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CITY_84",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CITY_84","attr":"$.message.order['@ondc/org/linked_order'].provider.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATE_85(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATE_85_obj in scope:
                REQUIRED_MESSAGE_STATE_85_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_85_obj, "$.message.order['@ondc/org/linked_order'].provider.address.state")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATE_85_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_STATE_85_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATE_85",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATE_85**: $.message.order['@ondc/org/linked_order'].provider.address.state must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_STATE_85** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_85","attr":"$.message.order['@ondc/org/linked_order'].provider.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATE_85_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATE_85",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATE_85","attr":"$.message.order['@ondc/org/linked_order'].provider.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_86(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_86_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_86_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_86_obj, "$.message.order['@ondc/org/linked_order'].provider.address.area_code")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_86_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_86_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_86",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_86**: $.message.order['@ondc/org/linked_order'].provider.address.area_code must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_AREA_CODE_86** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_86","attr":"$.message.order['@ondc/org/linked_order'].provider.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_86_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_86",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_86","attr":"$.message.order['@ondc/org/linked_order'].provider.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_87(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_87_obj in scope:
                REQUIRED_MESSAGE_ID_87_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_87_obj, "$.message.order['@ondc/org/linked_order'].order.id")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_87_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_87_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_87",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_87**: $.message.order['@ondc/org/linked_order'].order.id must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_ID_87** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_87","attr":"$.message.order['@ondc/org/linked_order'].order.id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_87_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_87",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_87","attr":"$.message.order['@ondc/org/linked_order'].order.id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_88(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_88_obj in scope:
                REQUIRED_MESSAGE_UNIT_88_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_88_obj, "$.message.order['@ondc/org/linked_order'].order.weight.unit")
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
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_88**: $.message.order['@ondc/org/linked_order'].order.weight.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_88** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_88","attr":"$.message.order['@ondc/org/linked_order'].order.weight.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_88","attr":"$.message.order['@ondc/org/linked_order'].order.weight.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_89(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_89_obj in scope:
                REQUIRED_MESSAGE_VALUE_89_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_89_obj, "$.message.order['@ondc/org/linked_order'].order.weight.value")
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
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_89**: $.message.order['@ondc/org/linked_order'].order.weight.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_89** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_89","attr":"$.message.order['@ondc/org/linked_order'].order.weight.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_89","attr":"$.message.order['@ondc/org/linked_order'].order.weight.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_90(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_90_obj in scope:
                REQUIRED_MESSAGE_UNIT_90_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_90_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_90_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_90_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_90",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_90**: $.message.order['@ondc/org/linked_order'].order.dimensions.length.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_90** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_90","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_90_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_90",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_90","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_91(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_91_obj in scope:
                REQUIRED_MESSAGE_VALUE_91_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_91_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.length.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_91_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_91_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_91",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_91**: $.message.order['@ondc/org/linked_order'].order.dimensions.length.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_91** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_91","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_91_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_91",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_91","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_92(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_92_obj in scope:
                REQUIRED_MESSAGE_UNIT_92_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_92_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_92_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_92_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_92",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_92**: $.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_92** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_92","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_92_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_92",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_92","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_93(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_93_obj in scope:
                REQUIRED_MESSAGE_VALUE_93_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_93_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_93_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_93_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_93",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_93**: $.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_93** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_93","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_93_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_93",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_93","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_94(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_94_obj in scope:
                REQUIRED_MESSAGE_UNIT_94_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_94_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_94_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_94_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_94",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_94**: $.message.order['@ondc/org/linked_order'].order.dimensions.height.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_94** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_94","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_94_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_94",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_94","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_95(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_95_obj in scope:
                REQUIRED_MESSAGE_VALUE_95_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_95_obj, "$.message.order['@ondc/org/linked_order'].order.dimensions.height.value")
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_95_obj, "$.message.order.fulfillments[*].type")
                fulType = ["Batch"]

                skip_check = validation_utils["any_in"](fulfillmentType, fulType)
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_95_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_95",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_95**: $.message.order['@ondc/org/linked_order'].order.dimensions.height.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_95** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: at least one element of $.message.order.fulfillments[*].type must be in ["Batch"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_95","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_95_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_95",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_95","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UPDATED_AT_96(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATED_AT_96_obj in scope:
                REQUIRED_MESSAGE_UPDATED_AT_96_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATED_AT_96_obj, "$.message.order.updated_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATED_AT_96_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATED_AT_96",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATED_AT_96**: $.message.order.updated_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_96","attr":"$.message.order.updated_at","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UPDATED_AT_96_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UPDATED_AT_96",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_96","attr":"$.message.order.updated_at","_RETURN_":"attr are present"}
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
                validTags = ["masked_contact"]
                tagPath = payload_utils["get_json_path"](validate_tag_0_obj, "$.message.order.fulfillments[*].start.contact.tags[*].code")

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
                        "description": r"""- **condition validate_tag_0**: every element of $.message.order.fulfillments[*].start.contact.tags[*].code must be in ["masked_contact"]

        	> Note: **Condition validate_tag_0** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].start.contact.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].start.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_0","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].start.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_0_masked_contact(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]")
            sub_results = []
            valid = True

            for validate_tag_0_masked_contact_obj in scope:
                validate_tag_0_masked_contact_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_masked_contact_obj, "$.list[*].code")
                validValues = ["type","setup","token"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_masked_contact_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_masked_contact",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_masked_contact**: every element of $.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')].list[*].code must be in ["type", "setup", "token"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_masked_contact_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_masked_contact",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_1_obj in scope:
                validate_tag_1_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["masked_contact"]
                tagPath = payload_utils["get_json_path"](validate_tag_1_obj, "$.message.order.fulfillments[*].end.contact.tags[*].code")

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
                        "description": r"""- **condition validate_tag_1**: every element of $.message.order.fulfillments[*].end.contact.tags[*].code must be in ["masked_contact"]

        	> Note: **Condition validate_tag_1** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].end.contact.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].end.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_1","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].end.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_1_masked_contact(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]")
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
                        "description": r"""- **condition validate_tag_1_masked_contact**: every element of $.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')].list[*].code must be in ["type", "setup", "token"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
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
        {"_NAME_":"validate_tag_1_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_2_obj in scope:
                validate_tag_2_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["linked_provider","linked_order","linked_order_item","cod_settlement_detail","rto_verification","shipping_label","fulfill_request","ebn","fulfill_response","rider_details","fulfillment_delay","fulfillment_proof","linked_order_diff","linked_order_diff_proof","tracking"]
                tagPath = payload_utils["get_json_path"](validate_tag_2_obj, "$.message.order.fulfillments[*].tags[*].code")

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
                        "description": r"""- **condition validate_tag_2**: every element of $.message.order.fulfillments[*].tags[*].code must be in ["linked_provider", "linked_order", "linked_order_item", "cod_settlement_detail", "rto_verification", "shipping_label", "fulfill_request", "ebn", "fulfill_response", "rider_details", "fulfillment_delay", "fulfillment_proof", "linked_order_diff", "linked_order_diff_proof", "tracking"]

        	> Note: **Condition validate_tag_2** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.order.fulfillments[*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2","validTags":["linked_provider","linked_order","linked_order_item","cod_settlement_detail","rto_verification","shipping_label","fulfill_request","ebn","fulfill_response","rider_details","fulfillment_delay","fulfillment_proof","linked_order_diff","linked_order_diff_proof","tracking"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_2","validTags":["linked_provider","linked_order","linked_order_item","cod_settlement_detail","rto_verification","shipping_label","fulfill_request","ebn","fulfill_response","rider_details","fulfillment_delay","fulfillment_proof","linked_order_diff","linked_order_diff_proof","tracking"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_2_linked_provider(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]")
            sub_results = []
            valid = True

            for validate_tag_2_linked_provider_obj in scope:
                validate_tag_2_linked_provider_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_linked_provider_obj, "$.list[*].code")
                validValues = ["id","name","address","cred_code","cred_desc","tax_id"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_linked_provider_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_linked_provider",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_linked_provider**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_provider')].list[*].code must be in ["id", "name", "address", "cred_code", "cred_desc", "tax_id"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_linked_provider_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_linked_provider",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_linked_order(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]")
            sub_results = []
            valid = True

            for validate_tag_2_linked_order_obj in scope:
                validate_tag_2_linked_order_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_linked_order_obj, "$.list[*].code")
                validValues = ["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_linked_order_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_linked_order",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_linked_order**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order')].list[*].code must be in ["id", "prep_time", "cod_order", "collection_amount", "currency", "declared_value", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height", "shipment_type"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_linked_order_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_linked_order",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_linked_order_item(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]")
            sub_results = []
            valid = True

            for validate_tag_2_linked_order_item_obj in scope:
                validate_tag_2_linked_order_item_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_linked_order_item_obj, "$.list[*].code")
                validValues = ["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_linked_order_item_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_linked_order_item",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_linked_order_item**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')].list[*].code must be in ["category", "name", "currency", "value", "quantity", "weight_unit", "weight_value", "hsn_code", "ebn_exempt"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_linked_order_item_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_linked_order_item",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_ebn_on_update(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='ebn')]")
            sub_results = []
            valid = True

            for validate_tag_2_ebn_on_update_obj in scope:
                validate_tag_2_ebn_on_update_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_ebn_on_update_obj, "$.list[*].code")
                validValues = ["id","expiry_date"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_ebn_on_update_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_ebn_on_update",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_ebn_on_update**: every element of $.message.order.fulfillments[*].tags[?(@.code=='ebn')].list[*].code must be in ["id", "expiry_date"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_ebn_on_update","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='ebn')]","subTags":"$.list[*].code","validValues":["id","expiry_date"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_ebn_on_update_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_ebn_on_update",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_ebn_on_update","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='ebn')]","subTags":"$.list[*].code","validValues":["id","expiry_date"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_cod_settlement_detail(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]")
            sub_results = []
            valid = True

            for validate_tag_2_cod_settlement_detail_obj in scope:
                validate_tag_2_cod_settlement_detail_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_cod_settlement_detail_obj, "$.list[*].code")
                validValues = ["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_cod_settlement_detail_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_cod_settlement_detail",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_cod_settlement_detail**: every element of $.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')].list[*].code must be in ["settlement_window", "settlement_type", "beneficiary_name", "upi_address", "bank_account_no", "ifsc_code", "bank_name", "branch_name"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_cod_settlement_detail","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]","subTags":"$.list[*].code","validValues":["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_cod_settlement_detail_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_cod_settlement_detail",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_cod_settlement_detail","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]","subTags":"$.list[*].code","validValues":["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_rto_verification(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]")
            sub_results = []
            valid = True

            for validate_tag_2_rto_verification_obj in scope:
                validate_tag_2_rto_verification_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_rto_verification_obj, "$.list[*].code")
                validValues = ["code","short_desc"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_rto_verification_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_rto_verification",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_rto_verification**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rto_verification')].list[*].code must be in ["code", "short_desc"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_rto_verification_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_rto_verification",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_shipping_label(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='shipping_label')]")
            sub_results = []
            valid = True

            for validate_tag_2_shipping_label_obj in scope:
                validate_tag_2_shipping_label_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_shipping_label_obj, "$.list[*].code")
                validValues = ["type","url"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_shipping_label_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_shipping_label",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_shipping_label**: every element of $.message.order.fulfillments[*].tags[?(@.code=='shipping_label')].list[*].code must be in ["type", "url"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_shipping_label","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='shipping_label')]","subTags":"$.list[*].code","validValues":["type","url"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_shipping_label_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_shipping_label",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_shipping_label","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='shipping_label')]","subTags":"$.list[*].code","validValues":["type","url"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_fulfill_request(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]")
            sub_results = []
            valid = True

            for validate_tag_2_fulfill_request_obj in scope:
                validate_tag_2_fulfill_request_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_fulfill_request_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_fulfill_request_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_fulfill_request",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_fulfill_request**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')].list[*].code must be in ["rider_count", "order_count", "rate_basis", "motorable_distance", "pickup_slot_start", "pickup_slot_end", "delivery_slot_start", "delivery_slot_end"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_fulfill_request_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_fulfill_request",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_fulfill_response(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]")
            sub_results = []
            valid = True

            for validate_tag_2_fulfill_response_obj in scope:
                validate_tag_2_fulfill_response_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_fulfill_response_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis","diff_value"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_fulfill_response_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_fulfill_response",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_fulfill_response**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')].list[*].code must be in ["rider_count", "order_count", "rate_basis", "diff_value"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","diff_value"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_fulfill_response_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_fulfill_response",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","diff_value"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_rider_details(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]")
            sub_results = []
            valid = True

            for validate_tag_2_rider_details_obj in scope:
                validate_tag_2_rider_details_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_rider_details_obj, "$.list[*].code")
                validValues = ["name","phone","vehicle_registration"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_rider_details_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_rider_details",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_rider_details**: every element of $.message.order.fulfillments[*].tags[?(@.code=='rider_details')].list[*].code must be in ["name", "phone", "vehicle_registration"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_rider_details","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]","subTags":"$.list[*].code","validValues":["name","phone","vehicle_registration"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_rider_details_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_rider_details",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_rider_details","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]","subTags":"$.list[*].code","validValues":["name","phone","vehicle_registration"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_fulfillment_delay(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')]")
            sub_results = []
            valid = True

            for validate_tag_2_fulfillment_delay_obj in scope:
                validate_tag_2_fulfillment_delay_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_fulfillment_delay_obj, "$.list[*].code")
                validValues = ["state","reason_id","timestamp","attempt"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_fulfillment_delay_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_fulfillment_delay",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_fulfillment_delay**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')].list[*].code must be in ["state", "reason_id", "timestamp", "attempt"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfillment_delay","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')]","subTags":"$.list[*].code","validValues":["state","reason_id","timestamp","attempt"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_fulfillment_delay_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_fulfillment_delay",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfillment_delay","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')]","subTags":"$.list[*].code","validValues":["state","reason_id","timestamp","attempt"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_fulfillment_proof(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_proof')]")
            sub_results = []
            valid = True

            for validate_tag_2_fulfillment_proof_obj in scope:
                validate_tag_2_fulfillment_proof_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_fulfillment_proof_obj, "$.list[*].code")
                validValues = ["state","type","url"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_fulfillment_proof_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_fulfillment_proof",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_fulfillment_proof**: every element of $.message.order.fulfillments[*].tags[?(@.code=='fulfillment_proof')].list[*].code must be in ["state", "type", "url"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfillment_proof","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_proof')]","subTags":"$.list[*].code","validValues":["state","type","url"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_fulfillment_proof_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_fulfillment_proof",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_fulfillment_proof","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_proof')]","subTags":"$.list[*].code","validValues":["state","type","url"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_linked_order_diff(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')]")
            sub_results = []
            valid = True

            for validate_tag_2_linked_order_diff_obj in scope:
                validate_tag_2_linked_order_diff_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_linked_order_diff_obj, "$.list[*].code")
                validValues = ["id","weight_unit","weight_value","dim_unit","length","breadth","height"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_linked_order_diff_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_linked_order_diff",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_linked_order_diff**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')].list[*].code must be in ["id", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order_diff","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')]","subTags":"$.list[*].code","validValues":["id","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_linked_order_diff_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_linked_order_diff",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order_diff","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')]","subTags":"$.list[*].code","validValues":["id","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2_linked_order_diff_proof(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')]")
            sub_results = []
            valid = True

            for validate_tag_2_linked_order_diff_proof_obj in scope:
                validate_tag_2_linked_order_diff_proof_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_linked_order_diff_proof_obj, "$.list[*].code")
                validValues = ["type","url"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_linked_order_diff_proof_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_linked_order_diff_proof",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_linked_order_diff_proof**: every element of $.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')].list[*].code must be in ["type", "url"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order_diff_proof","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')]","subTags":"$.list[*].code","validValues":["type","url"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_linked_order_diff_proof_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_linked_order_diff_proof",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_linked_order_diff_proof","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')]","subTags":"$.list[*].code","validValues":["type","url"],"_RETURN_":"subTags all in validValues"}
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
            REQUIRED_MESSAGE_ID,
            REQUIRED_MESSAGE_STATE,
            REQUIRED_MESSAGE_ID_15,
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
            REQUIRED_MESSAGE_CODE,
            REQUIRED_MESSAGE_TRACKING,
            REQUIRED_MESSAGE_NAME,
            REQUIRED_MESSAGE_ID_32,
            REQUIRED_MESSAGE_GPS,
            REQUIRED_MESSAGE_NAME_34,
            REQUIRED_MESSAGE_BUILDING,
            REQUIRED_MESSAGE_LOCALITY,
            REQUIRED_MESSAGE_CITY,
            REQUIRED_MESSAGE_STATE_38,
            REQUIRED_MESSAGE_COUNTRY,
            REQUIRED_MESSAGE_AREA_CODE,
            REQUIRED_MESSAGE_PHONE,
            REQUIRED_MESSAGE_EMAIL,
            REQUIRED_MESSAGE_DURATION_43,
            REQUIRED_MESSAGE_START,
            REQUIRED_MESSAGE_END,
            REQUIRED_MESSAGE_NAME_46,
            REQUIRED_MESSAGE_GPS_47,
            REQUIRED_MESSAGE_NAME_48,
            REQUIRED_MESSAGE_BUILDING_49,
            REQUIRED_MESSAGE_LOCALITY_50,
            REQUIRED_MESSAGE_CITY_51,
            REQUIRED_MESSAGE_STATE_52,
            REQUIRED_MESSAGE_COUNTRY_53,
            REQUIRED_MESSAGE_AREA_CODE_54,
            REQUIRED_MESSAGE_PHONE_55,
            REQUIRED_MESSAGE_START_56,
            REQUIRED_MESSAGE_END_57,
            REQUIRED_MESSAGE_NAME_58,
            REQUIRED_MESSAGE_NAME_59,
            REQUIRED_MESSAGE_BUILDING_60,
            REQUIRED_MESSAGE_LOCALITY_61,
            REQUIRED_MESSAGE_CITY_62,
            REQUIRED_MESSAGE_STATE_63,
            REQUIRED_MESSAGE_COUNTRY_64,
            REQUIRED_MESSAGE_AREA_CODE_65,
            REQUIRED_MESSAGE_TAX_NUMBER,
            REQUIRED_MESSAGE_PHONE_67,
            REQUIRED_MESSAGE_EMAIL_68,
            REQUIRED_MESSAGE_CREATED_AT,
            REQUIRED_MESSAGE_UPDATED_AT,
            REQUIRED_MESSAGE_COLLECTED_BY,
            REQUIRED_MESSAGE_TYPE_72,
            REQUIRED_MESSAGE_CATEGORY_ID_73,
            REQUIRED_MESSAGE_NAME_74,
            REQUIRED_MESSAGE_COUNT,
            REQUIRED_MESSAGE_UNIT,
            REQUIRED_MESSAGE_VALUE_77,
            REQUIRED_MESSAGE_CURRENCY_78,
            REQUIRED_MESSAGE_VALUE_79,
            REQUIRED_MESSAGE_NAME_80,
            REQUIRED_MESSAGE_NAME_81,
            REQUIRED_MESSAGE_BUILDING_82,
            REQUIRED_MESSAGE_LOCALITY_83,
            REQUIRED_MESSAGE_CITY_84,
            REQUIRED_MESSAGE_STATE_85,
            REQUIRED_MESSAGE_AREA_CODE_86,
            REQUIRED_MESSAGE_ID_87,
            REQUIRED_MESSAGE_UNIT_88,
            REQUIRED_MESSAGE_VALUE_89,
            REQUIRED_MESSAGE_UNIT_90,
            REQUIRED_MESSAGE_VALUE_91,
            REQUIRED_MESSAGE_UNIT_92,
            REQUIRED_MESSAGE_VALUE_93,
            REQUIRED_MESSAGE_UNIT_94,
            REQUIRED_MESSAGE_VALUE_95,
            REQUIRED_MESSAGE_UPDATED_AT_96,
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
            validate_tag_0_masked_contact,
            validate_tag_1,
            validate_tag_1_masked_contact,
            validate_tag_2,
            validate_tag_2_linked_provider,
            validate_tag_2_linked_order,
            validate_tag_2_linked_order_item,
            validate_tag_2_ebn_on_update,
            validate_tag_2_cod_settlement_detail,
            validate_tag_2_rto_verification,
            validate_tag_2_shipping_label,
            validate_tag_2_fulfill_request,
            validate_tag_2_fulfill_response,
            validate_tag_2_rider_details,
            validate_tag_2_fulfillment_delay,
            validate_tag_2_fulfillment_proof,
            validate_tag_2_linked_order_diff,
            validate_tag_2_linked_order_diff_proof,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_update_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_update_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_update_validations","_RETURN_":[{"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]},{"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.order.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE","attr":"$.message.order.state","_RETURN_":"attr are present && attr all in enumList","enumList":["Created","Accepted","In-progress","Completed","Cancelled"]},{"_NAME_":"REQUIRED_MESSAGE_ID_15","attr":"$.message.order.provider.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_16","attr":"$.message.order.items[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.order.items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]},{"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.order.items[*].time.label","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.order.items[*].time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.order.items[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.order.quote.price.currency","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.order.quote.price.value","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGITEM_ID","attr":"$.message.order.quote.breakup[*]['@ondc/org/item_id']","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BREAKUPONDCORGTITLE_TYPE","attr":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_RETURN_":"attr are present && attr all in enumList","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"]},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY_25","attr":"$.message.order.quote.breakup[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_26","attr":"$.message.order.quote.breakup[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_27","attr":"$.message.order.fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.order.fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]},{"_NAME_":"REQUIRED_MESSAGE_CODE","attr":"$.message.order.fulfillments[*].state.descriptor.code","_RETURN_":"attr are present && attr all in enumList","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"]},{"_NAME_":"REQUIRED_MESSAGE_TRACKING","attr":"$.message.order.fulfillments[*].tracking","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.order.fulfillments[*].start.person.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_32","attr":"$.message.order.fulfillments[*].start.location.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.order.fulfillments[*].start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_34","attr":"$.message.order.fulfillments[*].start.location.address.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING","attr":"$.message.order.fulfillments[*].start.location.address.building","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY","attr":"$.message.order.fulfillments[*].start.location.address.locality","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY","attr":"$.message.order.fulfillments[*].start.location.address.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_38","attr":"$.message.order.fulfillments[*].start.location.address.state","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNTRY","attr":"$.message.order.fulfillments[*].start.location.address.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.order.fulfillments[*].start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.order.fulfillments[*].start.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.order.fulfillments[*].start.contact.email","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION_43","attr":"$.message.order.fulfillments[*].start.time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_START","attr":"$.message.order.fulfillments[*].start.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_END","attr":"$.message.order.fulfillments[*].start.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_46","attr":"$.message.order.fulfillments[*].end.person.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_GPS_47","attr":"$.message.order.fulfillments[*].end.location.gps","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_48","attr":"$.message.order.fulfillments[*].end.location.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING_49","attr":"$.message.order.fulfillments[*].end.location.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY_50","attr":"$.message.order.fulfillments[*].end.location.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY_51","attr":"$.message.order.fulfillments[*].end.location.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_52","attr":"$.message.order.fulfillments[*].end.location.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNTRY_53","attr":"$.message.order.fulfillments[*].end.location.address.country","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_54","attr":"$.message.order.fulfillments[*].end.location.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE_55","attr":"$.message.order.fulfillments[*].end.contact.phone","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_START_56","attr":"$.message.order.fulfillments[*].end.time.range.start","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_END_57","attr":"$.message.order.fulfillments[*].end.time.range.end","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Delivery"],"_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_58","attr":"$.message.order.billing.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_59","attr":"$.message.order.billing.address.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING_60","attr":"$.message.order.billing.address.building","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY_61","attr":"$.message.order.billing.address.locality","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY_62","attr":"$.message.order.billing.address.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_63","attr":"$.message.order.billing.address.state","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNTRY_64","attr":"$.message.order.billing.address.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_65","attr":"$.message.order.billing.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TAX_NUMBER","attr":"$.message.order.billing.tax_number","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE_67","attr":"$.message.order.billing.phone","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_EMAIL_68","attr":"$.message.order.billing.email","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.order.billing.created_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.order.billing.updated_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COLLECTED_BY","attr":"$.message.order.payment.collected_by","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE_72","attr":"$.message.order.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]},{"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID_73","attr":"$.message.order['@ondc/org/linked_order'].items[*].category_id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_74","attr":"$.message.order['@ondc/org/linked_order'].items[*].descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_COUNT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.count","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_77","attr":"$.message.order['@ondc/org/linked_order'].items[*].quantity.measure.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY_78","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.currency","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_79","attr":"$.message.order['@ondc/org/linked_order'].items[*].price.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_80","attr":"$.message.order['@ondc/org/linked_order'].provider.descriptor.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_81","attr":"$.message.order['@ondc/org/linked_order'].provider.address.name","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_BUILDING_82","attr":"$.message.order['@ondc/org/linked_order'].provider.address.building","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LOCALITY_83","attr":"$.message.order['@ondc/org/linked_order'].provider.address.locality","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CITY_84","attr":"$.message.order['@ondc/org/linked_order'].provider.address.city","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATE_85","attr":"$.message.order['@ondc/org/linked_order'].provider.address.state","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_86","attr":"$.message.order['@ondc/org/linked_order'].provider.address.area_code","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_87","attr":"$.message.order['@ondc/org/linked_order'].order.id","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_88","attr":"$.message.order['@ondc/org/linked_order'].order.weight.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_89","attr":"$.message.order['@ondc/org/linked_order'].order.weight.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_90","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_91","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.length.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_92","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_93","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.breadth.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_94","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.unit","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_95","attr":"$.message.order['@ondc/org/linked_order'].order.dimensions.height.value","fulfillmentType":"$.message.order.fulfillments[*].type","fulType":["Batch"],"_CONTINUE_":"(fulfillmentType any in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_96","attr":"$.message.order.updated_at","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_STATE","enumList":["Created","Accepted","In-progress","Completed","Cancelled"],"enumPath":"$.message.order.state","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.order.items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.order.fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.order.fulfillments[*].start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["OTP"],"enumPath":"$.message.order.fulfillments[*].end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_8","enumList":["1","2","3","5"],"enumPath":"$.message.order.fulfillments[*].end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_9","enumList":["Pending","Cancelled","Order-picked-up","RTO","RTO-Initiated","RTO-Delivered","RTO-Disposed","Out-for-pickup","At-destination-hub","In-transit","At-pickup","Out-for-delivery","At-delivery","Searching-for-Agent","Agent-assigned","Pickup-failed","Pickup-rescheduled","Delivery-failed","Delivery-rescheduled","Order-delivered"],"enumPath":"$.message.order.fulfillments[*].state.descriptor.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_10","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.order.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_SETTLEMENT_COUNTERPARTY","enumList":["lbnp","lsp"],"enumPath":"$.message.order.payment['@ondc/org/settlement_details'][*].settlement_counterparty","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_BREAKUPONDCORGTITLE_TYPE","enumList":["delivery","rto","tax","diff","tax_diff","discount","cod","surge"],"enumPath":"$.message.order.quote.breakup[*]['@ondc/org/title_type']","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"validate_tag_0","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].start.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_0_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].start.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1","validTags":["masked_contact"],"tagPath":"$.message.order.fulfillments[*].end.contact.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_1_masked_contact","_SCOPE_":"$.message.order.fulfillments[*].end.contact.tags[?(@.code=='masked_contact')]","subTags":"$.list[*].code","validValues":["type","setup","token"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2","validTags":["linked_provider","linked_order","linked_order_item","cod_settlement_detail","rto_verification","shipping_label","fulfill_request","ebn","fulfill_response","rider_details","fulfillment_delay","fulfillment_proof","linked_order_diff","linked_order_diff_proof","tracking"],"tagPath":"$.message.order.fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_2_linked_provider","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name","address","cred_code","cred_desc","tax_id"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_linked_order","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["id","prep_time","cod_order","collection_amount","currency","declared_value","weight_unit","weight_value","dim_unit","length","breadth","height","shipment_type"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_linked_order_item","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_item')]","subTags":"$.list[*].code","validValues":["category","name","currency","value","quantity","weight_unit","weight_value","hsn_code","ebn_exempt"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_ebn_on_update","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='ebn')]","subTags":"$.list[*].code","validValues":["id","expiry_date"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_cod_settlement_detail","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='cod_settlement_detail')]","subTags":"$.list[*].code","validValues":["settlement_window","settlement_type","beneficiary_name","upi_address","bank_account_no","ifsc_code","bank_name","branch_name"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_rto_verification","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rto_verification')]","subTags":"$.list[*].code","validValues":["code","short_desc"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_shipping_label","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='shipping_label')]","subTags":"$.list[*].code","validValues":["type","url"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_fulfill_request","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_fulfill_response","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","diff_value"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_rider_details","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='rider_details')]","subTags":"$.list[*].code","validValues":["name","phone","vehicle_registration"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_fulfillment_delay","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_delay')]","subTags":"$.list[*].code","validValues":["state","reason_id","timestamp","attempt"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_fulfillment_proof","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='fulfillment_proof')]","subTags":"$.list[*].code","validValues":["state","type","url"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_linked_order_diff","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff')]","subTags":"$.list[*].code","validValues":["id","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2_linked_order_diff_proof","_SCOPE_":"$.message.order.fulfillments[*].tags[?(@.code=='linked_order_diff_proof')]","subTags":"$.list[*].code","validValues":["type","url"],"_RETURN_":"subTags all in validValues"}]}
"""
    }}] + sub_results

def on_update(input_data):
    total_results = on_update_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "on_update_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
