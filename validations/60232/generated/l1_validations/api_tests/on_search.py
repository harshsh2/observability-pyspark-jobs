from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def on_search_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for on_search_validations_obj in scope:
        on_search_validations_obj["_EXTERNAL"] = input_data["external_data"]

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

        def REQUIRED_MESSAGE_NAME(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_obj in scope:
                REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_obj, "$.message.catalog['bpp/descriptor'].name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME**: $.message.catalog['bpp/descriptor'].name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_obj in scope:
                REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_obj, "$.message.catalog['bpp/providers'][*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID**: $.message.catalog['bpp/providers'][*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_15(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_15_obj in scope:
                REQUIRED_MESSAGE_NAME_15_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_15_obj, "$.message.catalog['bpp/providers'][*].descriptor.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_15_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_15",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_15**: $.message.catalog['bpp/providers'][*].descriptor.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_15","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_15_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_15",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_15","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_SHORT_DESC(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_SHORT_DESC_obj in scope:
                REQUIRED_MESSAGE_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_SHORT_DESC_obj, "$.message.catalog['bpp/providers'][*].descriptor.short_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_SHORT_DESC_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_SHORT_DESC",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_SHORT_DESC**: $.message.catalog['bpp/providers'][*].descriptor.short_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_SHORT_DESC_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_SHORT_DESC",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LONG_DESC(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LONG_DESC_obj in scope:
                REQUIRED_MESSAGE_LONG_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LONG_DESC_obj, "$.message.catalog['bpp/providers'][*].descriptor.long_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LONG_DESC_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LONG_DESC",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LONG_DESC**: $.message.catalog['bpp/providers'][*].descriptor.long_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LONG_DESC_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LONG_DESC",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_18(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_18_obj in scope:
                REQUIRED_MESSAGE_ID_18_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_18_obj, "$.message.catalog['bpp/providers'][*].categories[*].id")
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_ID_18_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_18",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_18**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_ID_18.1**: $.message.catalog['bpp/providers'][*].categories[*].id must be present in the payload
          - **condition REQUIRED_MESSAGE_ID_18.2**: every element of $.message.catalog['bpp/providers'][*].categories[*].id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_18","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_18_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_18",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_18","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LABEL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LABEL_obj in scope:
                REQUIRED_MESSAGE_LABEL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LABEL_obj, "$.message.catalog['bpp/providers'][*].categories[*].time.label")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LABEL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LABEL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LABEL**: $.message.catalog['bpp/providers'][*].categories[*].time.label must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.label","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.label","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DURATION(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_obj in scope:
                REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_obj, "$.message.catalog['bpp/providers'][*].categories[*].time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION**: $.message.catalog['bpp/providers'][*].categories[*].time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.duration","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TIMESTAMP(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TIMESTAMP_obj in scope:
                REQUIRED_MESSAGE_TIMESTAMP_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TIMESTAMP_obj, "$.message.catalog['bpp/providers'][*].categories[*].time.timestamp")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_TIMESTAMP_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TIMESTAMP",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TIMESTAMP**: $.message.catalog['bpp/providers'][*].categories[*].time.timestamp must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.timestamp","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.timestamp","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_22(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_22_obj in scope:
                REQUIRED_MESSAGE_ID_22_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_22_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_22_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_22",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_22**: $.message.catalog['bpp/providers'][*].fulfillments[*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_22","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_22_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_22",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_22","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_obj in scope:
                REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].type")
                enumList = ["Delivery","Return","Batch","RTO"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE.1**: $.message.catalog['bpp/providers'][*].fulfillments[*].type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE.2**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].type must be in ["Delivery", "Return", "Batch", "RTO"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]}
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
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_24(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_24_obj in scope:
                REQUIRED_MESSAGE_ID_24_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_24_obj, "$.message.catalog['bpp/providers'][*].items[*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_24_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_24",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_24**: $.message.catalog['bpp/providers'][*].items[*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_24","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_24_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_24",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_24","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_PARENT_ITEM_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PARENT_ITEM_ID_obj in scope:
                REQUIRED_MESSAGE_PARENT_ITEM_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PARENT_ITEM_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].parent_item_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PARENT_ITEM_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PARENT_ITEM_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PARENT_ITEM_ID**: $.message.catalog['bpp/providers'][*].items[*].parent_item_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PARENT_ITEM_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].parent_item_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_PARENT_ITEM_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_PARENT_ITEM_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PARENT_ITEM_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].parent_item_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CATEGORY_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CATEGORY_ID_obj in scope:
                REQUIRED_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CATEGORY_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_CATEGORY_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CATEGORY_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CATEGORY_ID**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_CATEGORY_ID.1**: $.message.catalog['bpp/providers'][*].items[*].category_id must be present in the payload
          - **condition REQUIRED_MESSAGE_CATEGORY_ID.2**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
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
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_FULFILLMENT_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_FULFILLMENT_ID_obj in scope:
                REQUIRED_MESSAGE_FULFILLMENT_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_FULFILLMENT_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].fulfillment_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_FULFILLMENT_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_FULFILLMENT_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_FULFILLMENT_ID**: $.message.catalog['bpp/providers'][*].items[*].fulfillment_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_FULFILLMENT_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_FULFILLMENT_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_28(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_28_obj in scope:
                REQUIRED_MESSAGE_NAME_28_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_28_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_28_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_28",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_28**: $.message.catalog['bpp/providers'][*].items[*].descriptor.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_28","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_28_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_28",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_28","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_SHORT_DESC_29(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_SHORT_DESC_29_obj in scope:
                REQUIRED_MESSAGE_SHORT_DESC_29_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_SHORT_DESC_29_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_SHORT_DESC_29_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_SHORT_DESC_29",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_SHORT_DESC_29**: $.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC_29","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_SHORT_DESC_29_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_SHORT_DESC_29",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC_29","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LONG_DESC_30(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LONG_DESC_30_obj in scope:
                REQUIRED_MESSAGE_LONG_DESC_30_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LONG_DESC_30_obj, "$.message.catalog['bpp/providers'][*].items[*].descriptor.long_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LONG_DESC_30_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LONG_DESC_30",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LONG_DESC_30**: $.message.catalog['bpp/providers'][*].items[*].descriptor.long_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LONG_DESC_30","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.long_desc","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LONG_DESC_30_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LONG_DESC_30",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LONG_DESC_30","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.long_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CURRENCY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CURRENCY_obj in scope:
                REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_obj, "$.message.catalog['bpp/providers'][*].items[*].price.currency")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CURRENCY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CURRENCY**: $.message.catalog['bpp/providers'][*].items[*].price.currency must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_obj in scope:
                REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_obj, "$.message.catalog['bpp/providers'][*].items[*].price.value")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE**: $.message.catalog['bpp/providers'][*].items[*].price.value must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"}
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
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CATEGORY_ID_obj, "$.message.catalog['bpp/providers'][*].items[*].category_id")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CATEGORY_ID**: every element of $.message.catalog['bpp/providers'][*].items[*].category_id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CATEGORY_ID** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].category_id must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_ID_obj in scope:
                VALID_ENUM_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_ID_obj, "$.message.catalog['bpp/providers'][*].categories[*].id")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_ID**: every element of $.message.catalog['bpp/providers'][*].categories[*].id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]

        	> Note: **Condition VALID_ENUM_MESSAGE_ID** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/providers'][*].categories[*].id must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.catalog['bpp/providers'][*].categories[*].id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.catalog['bpp/providers'][*].categories[*].id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Delivery","Return","Batch","RTO"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].type")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].type must be in ["Delivery", "Return", "Batch", "RTO"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/providers'][*].fulfillments[*].type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def validate_tag_0(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_0_obj in scope:
                validate_tag_0_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["bpp_terms"]
                tagPath = payload_utils["get_json_path"](validate_tag_0_obj, "$.message.catalog['bpp/descriptor'].tags[*].code")

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
                        "description": r"""- **condition validate_tag_0**: every element of $.message.catalog['bpp/descriptor'].tags[*].code must be in ["bpp_terms"]

        	> Note: **Condition validate_tag_0** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/descriptor'].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0","validTags":["bpp_terms"],"tagPath":"$.message.catalog['bpp/descriptor'].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_0","validTags":["bpp_terms"],"tagPath":"$.message.catalog['bpp/descriptor'].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_0_bpp_terms(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')]")
            sub_results = []
            valid = True

            for validate_tag_0_bpp_terms_obj in scope:
                validate_tag_0_bpp_terms_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_bpp_terms_obj, "$.list[*].code")
                validValues = ["static_terms","static_terms_new","effective_date","np_tax_type","max_liability","max_liability_cap","mandatory_arbitration","court_jurisdiction","delay_interest"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_bpp_terms_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_bpp_terms",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_bpp_terms**: every element of $.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[*].code must be in ["static_terms", "static_terms_new", "effective_date", "np_tax_type", "max_liability", "max_liability_cap", "mandatory_arbitration", "court_jurisdiction", "delay_interest"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_bpp_terms","_SCOPE_":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')]","subTags":"$.list[*].code","validValues":["static_terms","static_terms_new","effective_date","np_tax_type","max_liability","max_liability_cap","mandatory_arbitration","court_jurisdiction","delay_interest"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_0_bpp_terms_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_0_bpp_terms",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_0_bpp_terms","_SCOPE_":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')]","subTags":"$.list[*].code","validValues":["static_terms","static_terms_new","effective_date","np_tax_type","max_liability","max_liability_cap","mandatory_arbitration","court_jurisdiction","delay_interest"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_1_obj in scope:
                validate_tag_1_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["distance","fulfill_request","linked_provider","fulfill_response","motorable_distance"]
                tagPath = payload_utils["get_json_path"](validate_tag_1_obj, "$.message.catalog['bpp/providers'][*].fulfillments[*].tags[*].code")

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
                        "description": r"""- **condition validate_tag_1**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].tags[*].code must be in ["distance", "fulfill_request", "linked_provider", "fulfill_response", "motorable_distance"]

        	> Note: **Condition validate_tag_1** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/providers'][*].fulfillments[*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1","validTags":["distance","fulfill_request","linked_provider","fulfill_response","motorable_distance"],"tagPath":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_1","validTags":["distance","fulfill_request","linked_provider","fulfill_response","motorable_distance"],"tagPath":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_1_distance(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='distance')]")
            sub_results = []
            valid = True

            for validate_tag_1_distance_obj in scope:
                validate_tag_1_distance_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_distance_obj, "$.list[*].code")
                validValues = ["motorable_distance_type","motorable_distance"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_distance_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_distance",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_distance**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='distance')].list[*].code must be in ["motorable_distance_type", "motorable_distance"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_distance","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='distance')]","subTags":"$.list[*].code","validValues":["motorable_distance_type","motorable_distance"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_distance_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_distance",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_distance","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='distance')]","subTags":"$.list[*].code","validValues":["motorable_distance_type","motorable_distance"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1_motorable_distance(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='motorable_distance')]")
            sub_results = []
            valid = True

            for validate_tag_1_motorable_distance_obj in scope:
                validate_tag_1_motorable_distance_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_motorable_distance_obj, "$.list[*].code")
                validValues = ["unit","lower","upper"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_motorable_distance_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_motorable_distance",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_motorable_distance**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='motorable_distance')].list[*].code must be in ["unit", "lower", "upper"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_motorable_distance","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='motorable_distance')]","subTags":"$.list[*].code","validValues":["unit","lower","upper"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_motorable_distance_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_motorable_distance",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_motorable_distance","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='motorable_distance')]","subTags":"$.list[*].code","validValues":["unit","lower","upper"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1_fulfill_request(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_request')]")
            sub_results = []
            valid = True

            for validate_tag_1_fulfill_request_obj in scope:
                validate_tag_1_fulfill_request_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_fulfill_request_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_fulfill_request_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_fulfill_request",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_fulfill_request**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_request')].list[*].code must be in ["rider_count", "order_count", "rate_basis", "motorable_distance", "pickup_slot_start", "pickup_slot_end", "delivery_slot_start", "delivery_slot_end"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_fulfill_request","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_fulfill_request_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_fulfill_request",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_fulfill_request","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1_linked_provider(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='linked_provider')]")
            sub_results = []
            valid = True

            for validate_tag_1_linked_provider_obj in scope:
                validate_tag_1_linked_provider_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_linked_provider_obj, "$.list[*].code")
                validValues = ["id","name"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_linked_provider_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_linked_provider",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_linked_provider**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='linked_provider')].list[*].code must be in ["id", "name"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_linked_provider","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_linked_provider_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_linked_provider",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_linked_provider","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1_fulfill_response(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_response')]")
            sub_results = []
            valid = True

            for validate_tag_1_fulfill_response_obj in scope:
                validate_tag_1_fulfill_response_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_fulfill_response_obj, "$.list[*].code")
                validValues = ["rider_count","order_count","rate_basis"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_fulfill_response_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_fulfill_response",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_fulfill_response**: every element of $.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_response')].list[*].code must be in ["rider_count", "order_count", "rate_basis"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_fulfill_response","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_fulfill_response_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_fulfill_response",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_fulfill_response","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_2(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_2_obj in scope:
                validate_tag_2_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["type"]
                tagPath = payload_utils["get_json_path"](validate_tag_2_obj, "$.message.catalog['bpp/providers'][*].items[*].tags[*].code")

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
                        "description": r"""- **condition validate_tag_2**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[*].code must be in ["type"]

        	> Note: **Condition validate_tag_2** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/providers'][*].items[*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2","validTags":["type"],"tagPath":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_2","validTags":["type"],"tagPath":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_2_type(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='type')]")
            sub_results = []
            valid = True

            for validate_tag_2_type_obj in scope:
                validate_tag_2_type_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_2_type_obj, "$.list[*].code")
                validValues = ["type","unit"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_2_type_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_2_type",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_2_type**: every element of $.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='type')].list[*].code must be in ["type", "unit"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_2_type","_SCOPE_":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='type')]","subTags":"$.list[*].code","validValues":["type","unit"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_2_type_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_2_type",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_2_type","_SCOPE_":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='type')]","subTags":"$.list[*].code","validValues":["type","unit"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_3_obj in scope:
                validate_tag_3_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["lsp_features","special_req"]
                tagPath = payload_utils["get_json_path"](validate_tag_3_obj, "$.message.catalog['bpp/providers'][*].tags[*].code")

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
                        "description": r"""- **condition validate_tag_3**: every element of $.message.catalog['bpp/providers'][*].tags[*].code must be in ["lsp_features", "special_req"]

        	> Note: **Condition validate_tag_3** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.catalog['bpp/providers'][*].tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3","validTags":["lsp_features","special_req"],"tagPath":"$.message.catalog['bpp/providers'][*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_3","validTags":["lsp_features","special_req"],"tagPath":"$.message.catalog['bpp/providers'][*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_3_lsp_features(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].tags[?(@.code=='lsp_features')]")
            sub_results = []
            valid = True

            for validate_tag_3_lsp_features_obj in scope:
                validate_tag_3_lsp_features_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_lsp_features_obj, "$.list[*].code")
                validValues = ["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_lsp_features_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_lsp_features",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_lsp_features**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='lsp_features')].list[*].code must be in ["00B", "00E", "01D", "005", "009", "00C", "000", "001", "002", "003", "004", "006", "007", "008", "00A", "00D", "00F", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "01A", "01B", "01C", "01D", "01E", "01F", "020", "021"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_lsp_features","_SCOPE_":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='lsp_features')]","subTags":"$.list[*].code","validValues":["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_lsp_features_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_lsp_features",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_lsp_features","_SCOPE_":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='lsp_features')]","subTags":"$.list[*].code","validValues":["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_3_special_req(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.catalog['bpp/providers'][*].tags[?(@.code=='special_req')]")
            sub_results = []
            valid = True

            for validate_tag_3_special_req_obj in scope:
                validate_tag_3_special_req_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_3_special_req_obj, "$.list[*].code")
                validValues = ["dangerous_goods","cold_storage","open_box_delivery","fragile_handling","cod_order"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_3_special_req_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_3_special_req",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_3_special_req**: every element of $.message.catalog['bpp/providers'][*].tags[?(@.code=='special_req')].list[*].code must be in ["dangerous_goods", "cold_storage", "open_box_delivery", "fragile_handling", "cod_order"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_3_special_req","_SCOPE_":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='special_req')]","subTags":"$.list[*].code","validValues":["dangerous_goods","cold_storage","open_box_delivery","fragile_handling","cod_order"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_3_special_req_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_3_special_req",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_3_special_req","_SCOPE_":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='special_req')]","subTags":"$.list[*].code","validValues":["dangerous_goods","cold_storage","open_box_delivery","fragile_handling","cod_order"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_static_terms(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_static_terms_obj in scope:
                validate_static_terms_obj["_EXTERNAL"] = input_data["external_data"]
                staticTerms = payload_utils["get_json_path"](validate_static_terms_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms')].value")
                staticTermsNew = payload_utils["get_json_path"](validate_static_terms_obj, "$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms_new')].value")

                validate = (validation_utils["are_present"](staticTermsNew)) or (validation_utils["are_present"](staticTerms))

                if not validate:
                    del validate_static_terms_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_static_terms",
                        "valid": False,
                        "code": 30000,
                        "description": r"""Static terms should be sent inside bpp/descriptor/tags""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_static_terms","_DESCRIPTION_":"Static terms should be sent inside bpp/descriptor/tags","staticTerms":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms')].value","staticTermsNew":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms_new')].value","_RETURN_":"staticTermsNew are present || staticTerms are present"}
        """
                        }
                    }]

                # del validate_static_terms_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_static_terms",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_static_terms","_DESCRIPTION_":"Static terms should be sent inside bpp/descriptor/tags","staticTerms":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms')].value","staticTermsNew":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms_new')].value","_RETURN_":"staticTermsNew are present || staticTerms are present"}
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
            REQUIRED_MESSAGE_NAME,
            REQUIRED_MESSAGE_ID,
            REQUIRED_MESSAGE_NAME_15,
            REQUIRED_MESSAGE_SHORT_DESC,
            REQUIRED_MESSAGE_LONG_DESC,
            REQUIRED_MESSAGE_ID_18,
            REQUIRED_MESSAGE_LABEL,
            REQUIRED_MESSAGE_DURATION,
            REQUIRED_MESSAGE_TIMESTAMP,
            REQUIRED_MESSAGE_ID_22,
            REQUIRED_MESSAGE_TYPE,
            REQUIRED_MESSAGE_ID_24,
            REQUIRED_MESSAGE_PARENT_ITEM_ID,
            REQUIRED_MESSAGE_CATEGORY_ID,
            REQUIRED_MESSAGE_FULFILLMENT_ID,
            REQUIRED_MESSAGE_NAME_28,
            REQUIRED_MESSAGE_SHORT_DESC_29,
            REQUIRED_MESSAGE_LONG_DESC_30,
            REQUIRED_MESSAGE_CURRENCY,
            REQUIRED_MESSAGE_VALUE,
            VALID_ENUM_CONTEXT_DOMAIN,
            VALID_ENUM_MESSAGE_CATEGORY_ID,
            VALID_ENUM_MESSAGE_ID,
            VALID_ENUM_MESSAGE_TYPE,
            validate_tag_0,
            validate_tag_0_bpp_terms,
            validate_tag_1,
            validate_tag_1_distance,
            validate_tag_1_motorable_distance,
            validate_tag_1_fulfill_request,
            validate_tag_1_linked_provider,
            validate_tag_1_fulfill_response,
            validate_tag_2,
            validate_tag_2_type,
            validate_tag_3,
            validate_tag_3_lsp_features,
            validate_tag_3_special_req,
            validate_static_terms,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del on_search_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "on_search_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"on_search_validations","_RETURN_":[{"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]},{"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_ID","attr":"$.context.bpp_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BPP_URI","attr":"$.context.bpp_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.catalog['bpp/descriptor'].name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.catalog['bpp/providers'][*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_15","attr":"$.message.catalog['bpp/providers'][*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LONG_DESC","attr":"$.message.catalog['bpp/providers'][*].descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_18","attr":"$.message.catalog['bpp/providers'][*].categories[*].id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]},{"_NAME_":"REQUIRED_MESSAGE_LABEL","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.label","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TIMESTAMP","attr":"$.message.catalog['bpp/providers'][*].categories[*].time.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_22","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]},{"_NAME_":"REQUIRED_MESSAGE_ID_24","attr":"$.message.catalog['bpp/providers'][*].items[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PARENT_ITEM_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].parent_item_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CATEGORY_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].category_id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]},{"_NAME_":"REQUIRED_MESSAGE_FULFILLMENT_ID","attr":"$.message.catalog['bpp/providers'][*].items[*].fulfillment_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_28","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC_29","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LONG_DESC_30","attr":"$.message.catalog['bpp/providers'][*].items[*].descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY","attr":"$.message.catalog['bpp/providers'][*].items[*].price.currency","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE","attr":"$.message.catalog['bpp/providers'][*].items[*].price.value","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CATEGORY_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.catalog['bpp/providers'][*].items[*].category_id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.catalog['bpp/providers'][*].categories[*].id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.catalog['bpp/providers'][*].fulfillments[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"validate_tag_0","validTags":["bpp_terms"],"tagPath":"$.message.catalog['bpp/descriptor'].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_0_bpp_terms","_SCOPE_":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')]","subTags":"$.list[*].code","validValues":["static_terms","static_terms_new","effective_date","np_tax_type","max_liability","max_liability_cap","mandatory_arbitration","court_jurisdiction","delay_interest"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1","validTags":["distance","fulfill_request","linked_provider","fulfill_response","motorable_distance"],"tagPath":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_1_distance","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='distance')]","subTags":"$.list[*].code","validValues":["motorable_distance_type","motorable_distance"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1_motorable_distance","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='motorable_distance')]","subTags":"$.list[*].code","validValues":["unit","lower","upper"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1_fulfill_request","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1_linked_provider","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1_fulfill_response","_SCOPE_":"$.message.catalog['bpp/providers'][*].fulfillments[*].tags[?(@.code=='fulfill_response')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_2","validTags":["type"],"tagPath":"$.message.catalog['bpp/providers'][*].items[*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_2_type","_SCOPE_":"$.message.catalog['bpp/providers'][*].items[*].tags[?(@.code=='type')]","subTags":"$.list[*].code","validValues":["type","unit"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3","validTags":["lsp_features","special_req"],"tagPath":"$.message.catalog['bpp/providers'][*].tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_3_lsp_features","_SCOPE_":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='lsp_features')]","subTags":"$.list[*].code","validValues":["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_3_special_req","_SCOPE_":"$.message.catalog['bpp/providers'][*].tags[?(@.code=='special_req')]","subTags":"$.list[*].code","validValues":["dangerous_goods","cold_storage","open_box_delivery","fragile_handling","cod_order"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_static_terms","_DESCRIPTION_":"Static terms should be sent inside bpp/descriptor/tags","staticTerms":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms')].value","staticTermsNew":"$.message.catalog['bpp/descriptor'].tags[?(@.code=='bpp_terms')].list[?(@.code=='static_terms_new')].value","_RETURN_":"staticTermsNew are present || staticTerms are present"}]}
"""
    }}] + sub_results

def on_search(input_data):
    total_results = on_search_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "on_search_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
