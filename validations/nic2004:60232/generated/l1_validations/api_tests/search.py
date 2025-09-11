from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def search_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for search_validations_obj in scope:
        search_validations_obj["_EXTERNAL"] = input_data["external_data"]

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
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_obj, "$.message.intent.category.id")
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_ID.1**: $.message.intent.category.id must be present in the payload
          - **condition REQUIRED_MESSAGE_ID.2**: every element of $.message.intent.category.id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.intent.category.id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
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
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.intent.category.id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DAYS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DAYS_obj in scope:
                REQUIRED_MESSAGE_DAYS_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DAYS_obj, "$.message.intent.provider.time.days")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DAYS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DAYS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DAYS**: $.message.intent.provider.time.days must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DAYS","attr":"$.message.intent.provider.time.days","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_DAYS_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_DAYS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DAYS","attr":"$.message.intent.provider.time.days","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_HOLIDAYS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_HOLIDAYS_obj in scope:
                REQUIRED_MESSAGE_HOLIDAYS_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_HOLIDAYS_obj, "$.message.intent.provider.time.schedule.holidays[*]")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_HOLIDAYS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_HOLIDAYS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_HOLIDAYS**: $.message.intent.provider.time.schedule.holidays[*] must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_HOLIDAYS","attr":"$.message.intent.provider.time.schedule.holidays[*]","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_HOLIDAYS_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_HOLIDAYS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_HOLIDAYS","attr":"$.message.intent.provider.time.schedule.holidays[*]","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DURATION(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_obj in scope:
                REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_obj, "$.message.intent.provider.time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION**: $.message.intent.provider.time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.intent.provider.time.duration","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.intent.provider.time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_START(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_START_obj in scope:
                REQUIRED_MESSAGE_START_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_START_obj, "$.message.intent.provider.time.range.start")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_START_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_START",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_START**: $.message.intent.provider.time.range.start must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_START","attr":"$.message.intent.provider.time.range.start","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_START","attr":"$.message.intent.provider.time.range.start","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_END(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_END_obj in scope:
                REQUIRED_MESSAGE_END_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_END_obj, "$.message.intent.provider.time.range.end")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_END_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_END",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_END**: $.message.intent.provider.time.range.end must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_END","attr":"$.message.intent.provider.time.range.end","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_END","attr":"$.message.intent.provider.time.range.end","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_obj in scope:
                REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_obj, "$.message.intent.fulfillment.type")
                enumList = ["Delivery","Return","Batch","RTO"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE.1**: $.message.intent.fulfillment.type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE.2**: every element of $.message.intent.fulfillment.type must be in ["Delivery", "Return", "Batch", "RTO"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.intent.fulfillment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]}
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
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.intent.fulfillment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_GPS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_GPS_obj in scope:
                REQUIRED_MESSAGE_GPS_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_obj, "$.message.intent.fulfillment.start.location.gps")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_GPS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_GPS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_GPS**: $.message.intent.fulfillment.start.location.gps must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.intent.fulfillment.start.location.gps","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.intent.fulfillment.start.location.gps","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_obj, "$.message.intent.fulfillment.start.location.address.area_code")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE**: $.message.intent.fulfillment.start.location.address.area_code must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.intent.fulfillment.start.location.address.area_code","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.intent.fulfillment.start.location.address.area_code","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_GPS_21(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_GPS_21_obj in scope:
                REQUIRED_MESSAGE_GPS_21_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_21_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_GPS_21_obj, "$.message.intent.fulfillment.end.location.gps")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_GPS_21_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_GPS_21",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_GPS_21**: $.message.intent.fulfillment.end.location.gps must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_GPS_21** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS_21","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_GPS_21_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_GPS_21",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_GPS_21","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_AREA_CODE_22(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_AREA_CODE_22_obj in scope:
                REQUIRED_MESSAGE_AREA_CODE_22_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_22_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_AREA_CODE_22_obj, "$.message.intent.fulfillment.end.location.address.area_code")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_AREA_CODE_22_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_AREA_CODE_22",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_AREA_CODE_22**: $.message.intent.fulfillment.end.location.address.area_code must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_AREA_CODE_22** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_22","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_AREA_CODE_22_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_AREA_CODE_22",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_22","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TYPE_23(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_23_obj in scope:
                REQUIRED_MESSAGE_TYPE_23_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_23_obj, "$.message.intent.payment.type")
                enumList = ["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_23_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE_23",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE_23**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE_23.1**: $.message.intent.payment.type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE_23.2**: every element of $.message.intent.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT", "POST-FULFILLMENT"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE_23","attr":"$.message.intent.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_TYPE_23_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_TYPE_23",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE_23","attr":"$.message.intent.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_obj in scope:
                REQUIRED_MESSAGE_UNIT_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_obj, "$.message.intent['@ondc/org/payload_details'].weight.unit")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT**: $.message.intent['@ondc/org/payload_details'].weight.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].weight.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_UNIT","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].weight.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_obj in scope:
                REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_obj, "$.message.intent['@ondc/org/payload_details'].weight.value")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE**: $.message.intent['@ondc/org/payload_details'].weight.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].weight.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_VALUE","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].weight.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_26(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_26_obj in scope:
                REQUIRED_MESSAGE_UNIT_26_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_26_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_26_obj, "$.message.intent['@ondc/org/payload_details'].dimensions.length.unit")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_26_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_26",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_26**: $.message.intent['@ondc/org/payload_details'].dimensions.length.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_26** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_26","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.length.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_26_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_26",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_26","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.length.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_27(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_27_obj in scope:
                REQUIRED_MESSAGE_VALUE_27_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_27_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_27_obj, "$.message.intent['@ondc/org/payload_details'].dimensions.length.value")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_27_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_27",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_27**: $.message.intent['@ondc/org/payload_details'].dimensions.length.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_27** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_27","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.length.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_27_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_27",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_27","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.length.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_28(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_28_obj in scope:
                REQUIRED_MESSAGE_UNIT_28_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_28_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_28_obj, "$.message.intent['@ondc/org/payload_details'].dimensions.breadth.unit")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_28_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_28",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_28**: $.message.intent['@ondc/org/payload_details'].dimensions.breadth.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_28** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_28","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.breadth.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_28_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_28",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_28","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.breadth.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_29(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_29_obj in scope:
                REQUIRED_MESSAGE_VALUE_29_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_29_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_29_obj, "$.message.intent['@ondc/org/payload_details'].dimensions.breadth.value")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_29_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_29",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_29**: $.message.intent['@ondc/org/payload_details'].dimensions.breadth.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_29** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_29","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.breadth.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_29_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_29",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_29","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.breadth.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UNIT_30(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UNIT_30_obj in scope:
                REQUIRED_MESSAGE_UNIT_30_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_30_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UNIT_30_obj, "$.message.intent['@ondc/org/payload_details'].dimensions.height.unit")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UNIT_30_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UNIT_30",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UNIT_30**: $.message.intent['@ondc/org/payload_details'].dimensions.height.unit must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_UNIT_30** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_30","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.height.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UNIT_30_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UNIT_30",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UNIT_30","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.height.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_31(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_31_obj in scope:
                REQUIRED_MESSAGE_VALUE_31_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_31_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_31_obj, "$.message.intent['@ondc/org/payload_details'].dimensions.height.value")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_31_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_31",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_31**: $.message.intent['@ondc/org/payload_details'].dimensions.height.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_31** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_31","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.height.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_31_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_31",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_31","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.height.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CATEGORY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CATEGORY_obj in scope:
                REQUIRED_MESSAGE_CATEGORY_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CATEGORY_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CATEGORY_obj, "$.message.intent['@ondc/org/payload_details'].category")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CATEGORY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CATEGORY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CATEGORY**: $.message.intent['@ondc/org/payload_details'].category must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CATEGORY** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].category","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CATEGORY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CATEGORY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CATEGORY","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].category","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CURRENCY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CURRENCY_obj in scope:
                REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CURRENCY_obj, "$.message.intent['@ondc/org/payload_details'].value.currency")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CURRENCY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CURRENCY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CURRENCY**: $.message.intent['@ondc/org/payload_details'].value.currency must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_CURRENCY** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].value.currency","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_CURRENCY","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].value.currency","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_VALUE_34(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_VALUE_34_obj in scope:
                REQUIRED_MESSAGE_VALUE_34_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_34_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_VALUE_34_obj, "$.message.intent['@ondc/org/payload_details'].value.value")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_VALUE_34_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_VALUE_34",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_VALUE_34**: $.message.intent['@ondc/org/payload_details'].value.value must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_VALUE_34** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_34","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].value.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_VALUE_34_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_VALUE_34",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_VALUE_34","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].value.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DANGEROUS_GOODS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DANGEROUS_GOODS_obj in scope:
                REQUIRED_MESSAGE_DANGEROUS_GOODS_obj["_EXTERNAL"] = input_data["external_data"]
                fulfillmentType = payload_utils["get_json_path"](REQUIRED_MESSAGE_DANGEROUS_GOODS_obj, "$.message.intent.fulfillment.type")
                fulType = ["Delivery"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DANGEROUS_GOODS_obj, "$.message.intent['@ondc/org/payload_details'].dangerous_goods")

                skip_check = not (validation_utils["all_in"](fulfillmentType, fulType))
                if skip_check:
                    continue

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DANGEROUS_GOODS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DANGEROUS_GOODS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DANGEROUS_GOODS**: $.message.intent['@ondc/org/payload_details'].dangerous_goods must be present in the payload

        	> Note: **Condition REQUIRED_MESSAGE_DANGEROUS_GOODS** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: every element of $.message.intent.fulfillment.type must **not** be in ["Delivery"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DANGEROUS_GOODS","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dangerous_goods","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_DANGEROUS_GOODS_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_DANGEROUS_GOODS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DANGEROUS_GOODS","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dangerous_goods","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"}
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

        def VALID_ENUM_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Delivery","Return","Batch","RTO"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_obj, "$.message.intent.fulfillment.type")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE**: every element of $.message.intent.fulfillment.type must be in ["Delivery", "Return", "Batch", "RTO"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.fulfillment.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.intent.fulfillment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.intent.fulfillment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE_3(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_3_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_3_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["OTP"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_3_obj, "$.message.intent.fulfillment.start.authorization.type")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_TYPE_3_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_TYPE_3",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE_3**: every element of $.message.intent.fulfillment.start.authorization.type must be in ["OTP"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE_3** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.fulfillment.start.authorization.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_3","enumList":["OTP"],"enumPath":"$.message.intent.fulfillment.start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_TYPE_3_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_TYPE_3",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_3","enumList":["OTP"],"enumPath":"$.message.intent.fulfillment.start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_CODE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_CODE_obj in scope:
                VALID_ENUM_MESSAGE_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["2","3","4","5"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CODE_obj, "$.message.intent.fulfillment.start.instructions.code")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CODE**: every element of $.message.intent.fulfillment.start.instructions.code must be in ["2", "3", "4", "5"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CODE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.fulfillment.start.instructions.code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.intent.fulfillment.start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.intent.fulfillment.start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE_5(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_5_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_5_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["OTP"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_5_obj, "$.message.intent.fulfillment.end.authorization.type")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE_5**: every element of $.message.intent.fulfillment.end.authorization.type must be in ["OTP"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE_5** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.fulfillment.end.authorization.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.intent.fulfillment.end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.intent.fulfillment.end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_CODE_6(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_CODE_6_obj in scope:
                VALID_ENUM_MESSAGE_CODE_6_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["1","2","3","5"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_CODE_6_obj, "$.message.intent.fulfillment.end.instructions.code")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_CODE_6_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_CODE_6",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_CODE_6**: every element of $.message.intent.fulfillment.end.instructions.code must be in ["1", "2", "3", "5"]

        	> Note: **Condition VALID_ENUM_MESSAGE_CODE_6** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.fulfillment.end.instructions.code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE_6","enumList":["1","2","3","5"],"enumPath":"$.message.intent.fulfillment.end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_CODE_6_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_CODE_6",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_CODE_6","enumList":["1","2","3","5"],"enumPath":"$.message.intent.fulfillment.end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE_7(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_7_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_7_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_7_obj, "$.message.intent.payment.type")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE_7**: every element of $.message.intent.payment.type must be in ["ON-ORDER", "ON-FULFILLMENT", "POST-FULFILLMENT"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE_7** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.payment.type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.intent.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.intent.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_ID_obj in scope:
                VALID_ENUM_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_ID_obj, "$.message.intent.category.id")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_ID**: every element of $.message.intent.category.id must be in ["Express Delivery", "Standard Delivery", "Immediate Delivery", "Next Day Delivery", "Same Day Delivery", "Instant Delivery"]

        	> Note: **Condition VALID_ENUM_MESSAGE_ID** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.category.id must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.intent.category.id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.intent.category.id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def validate_tag_0(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_0_obj in scope:
                validate_tag_0_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["linked_provider","linked_order","fulfill_request"]
                tagPath = payload_utils["get_json_path"](validate_tag_0_obj, "$.message.intent.fulfillment.tags[*].code")

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
                        "description": r"""- **condition validate_tag_0**: every element of $.message.intent.fulfillment.tags[*].code must be in ["linked_provider", "linked_order", "fulfill_request"]

        	> Note: **Condition validate_tag_0** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.fulfillment.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0","validTags":["linked_provider","linked_order","fulfill_request"],"tagPath":"$.message.intent.fulfillment.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_0","validTags":["linked_provider","linked_order","fulfill_request"],"tagPath":"$.message.intent.fulfillment.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_0_linked_provider(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.intent.fulfillment.tags[?(@.code=='linked_provider')]")
            sub_results = []
            valid = True

            for validate_tag_0_linked_provider_obj in scope:
                validate_tag_0_linked_provider_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_linked_provider_obj, "$.list[*].code")
                validValues = ["id","name"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_linked_provider_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_linked_provider",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_linked_provider**: every element of $.message.intent.fulfillment.tags[?(@.code=='linked_provider')].list[*].code must be in ["id", "name"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_provider","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name"],"_RETURN_":"subTags all in validValues"}
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
        {"_NAME_":"validate_tag_0_linked_provider","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_linked_order(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.intent.fulfillment.tags[?(@.code=='linked_order')]")
            sub_results = []
            valid = True

            for validate_tag_0_linked_order_obj in scope:
                validate_tag_0_linked_order_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_0_linked_order_obj, "$.list[*].code")
                validValues = ["cod_order","collection_amount","currency","declared_value","category","weight_unit","weight_value","dim_unit","length","breadth","height"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_0_linked_order_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_0_linked_order",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_0_linked_order**: every element of $.message.intent.fulfillment.tags[?(@.code=='linked_order')].list[*].code must be in ["cod_order", "collection_amount", "currency", "declared_value", "category", "weight_unit", "weight_value", "dim_unit", "length", "breadth", "height"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_linked_order","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["cod_order","collection_amount","currency","declared_value","category","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"}
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
        {"_NAME_":"validate_tag_0_linked_order","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["cod_order","collection_amount","currency","declared_value","category","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_0_fulfill_request(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.intent.fulfillment.tags[?(@.code=='fulfill_request')]")
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
                        "description": r"""- **condition validate_tag_0_fulfill_request**: every element of $.message.intent.fulfillment.tags[?(@.code=='fulfill_request')].list[*].code must be in ["rider_count", "order_count", "rate_basis", "motorable_distance", "pickup_slot_start", "pickup_slot_end", "delivery_slot_start", "delivery_slot_end"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_0_fulfill_request","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
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
        {"_NAME_":"validate_tag_0_fulfill_request","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for validate_tag_1_obj in scope:
                validate_tag_1_obj["_EXTERNAL"] = input_data["external_data"]
                validTags = ["lbnp_features","lbnp_sla_terms"]
                tagPath = payload_utils["get_json_path"](validate_tag_1_obj, "$.message.intent.tags[*].code")

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
                        "description": r"""- **condition validate_tag_1**: every element of $.message.intent.tags[*].code must be in ["lbnp_features", "lbnp_sla_terms"]

        	> Note: **Condition validate_tag_1** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.intent.tags[*].code must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1","validTags":["lbnp_features","lbnp_sla_terms"],"tagPath":"$.message.intent.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
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
        {"_NAME_":"validate_tag_1","validTags":["lbnp_features","lbnp_sla_terms"],"tagPath":"$.message.intent.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"}
        """
            }}] + sub_results

        def validate_tag_1_lbnp_features(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.intent.tags[?(@.code=='lbnp_features')]")
            sub_results = []
            valid = True

            for validate_tag_1_lbnp_features_obj in scope:
                validate_tag_1_lbnp_features_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_lbnp_features_obj, "$.list[*].code")
                validValues = ["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021","022"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_lbnp_features_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_lbnp_features",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_lbnp_features**: every element of $.message.intent.tags[?(@.code=='lbnp_features')].list[*].code must be in ["00B", "00E", "01D", "005", "009", "00C", "000", "001", "002", "003", "004", "006", "007", "008", "00A", "00D", "00F", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "01A", "01B", "01C", "01D", "01E", "01F", "020", "021", "022"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_lbnp_features","_SCOPE_":"$.message.intent.tags[?(@.code=='lbnp_features')]","subTags":"$.list[*].code","validValues":["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021","022"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_lbnp_features_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_lbnp_features",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_lbnp_features","_SCOPE_":"$.message.intent.tags[?(@.code=='lbnp_features')]","subTags":"$.list[*].code","validValues":["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021","022"],"_RETURN_":"subTags all in validValues"}
        """
            }}] + sub_results

        def validate_tag_1_lbnp_sla_terms(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$.message.intent.tags[?(@.code=='lbnp_sla_terms')]")
            sub_results = []
            valid = True

            for validate_tag_1_lbnp_sla_terms_obj in scope:
                validate_tag_1_lbnp_sla_terms_obj["_EXTERNAL"] = input_data["external_data"]
                subTags = payload_utils["get_json_path"](validate_tag_1_lbnp_sla_terms_obj, "$.list[*].code")
                validValues = ["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"]

                validate = validation_utils["all_in"](subTags, validValues)

                if not validate:
                    del validate_tag_1_lbnp_sla_terms_obj["_EXTERNAL"]
                    return [{
                        "test_name": "validate_tag_1_lbnp_sla_terms",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition validate_tag_1_lbnp_sla_terms**: every element of $.message.intent.tags[?(@.code=='lbnp_sla_terms')].list[*].code must be in ["metric", "base_unit", "base_min", "base_max", "penalty_min", "penalty_max", "penalty_unit", "penalty_value"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"validate_tag_1_lbnp_sla_terms","_SCOPE_":"$.message.intent.tags[?(@.code=='lbnp_sla_terms')]","subTags":"$.list[*].code","validValues":["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"],"_RETURN_":"subTags all in validValues"}
        """
                        }
                    }]

                # del validate_tag_1_lbnp_sla_terms_obj["_EXTERNAL"]

            return [{
                "test_name": "validate_tag_1_lbnp_sla_terms",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"validate_tag_1_lbnp_sla_terms","_SCOPE_":"$.message.intent.tags[?(@.code=='lbnp_sla_terms')]","subTags":"$.list[*].code","validValues":["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"],"_RETURN_":"subTags all in validValues"}
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
            REQUIRED_CONTEXT_TRANSACTION_ID,
            REQUIRED_CONTEXT_MESSAGE_ID,
            REQUIRED_CONTEXT_TIMESTAMP,
            REQUIRED_CONTEXT_TTL,
            REQUIRED_MESSAGE_ID,
            REQUIRED_MESSAGE_DAYS,
            REQUIRED_MESSAGE_HOLIDAYS,
            REQUIRED_MESSAGE_DURATION,
            REQUIRED_MESSAGE_START,
            REQUIRED_MESSAGE_END,
            REQUIRED_MESSAGE_TYPE,
            REQUIRED_MESSAGE_GPS,
            REQUIRED_MESSAGE_AREA_CODE,
            REQUIRED_MESSAGE_GPS_21,
            REQUIRED_MESSAGE_AREA_CODE_22,
            REQUIRED_MESSAGE_TYPE_23,
            REQUIRED_MESSAGE_UNIT,
            REQUIRED_MESSAGE_VALUE,
            REQUIRED_MESSAGE_UNIT_26,
            REQUIRED_MESSAGE_VALUE_27,
            REQUIRED_MESSAGE_UNIT_28,
            REQUIRED_MESSAGE_VALUE_29,
            REQUIRED_MESSAGE_UNIT_30,
            REQUIRED_MESSAGE_VALUE_31,
            REQUIRED_MESSAGE_CATEGORY,
            REQUIRED_MESSAGE_CURRENCY,
            REQUIRED_MESSAGE_VALUE_34,
            REQUIRED_MESSAGE_DANGEROUS_GOODS,
            VALID_ENUM_CONTEXT_DOMAIN,
            VALID_ENUM_MESSAGE_TYPE,
            VALID_ENUM_MESSAGE_TYPE_3,
            VALID_ENUM_MESSAGE_CODE,
            VALID_ENUM_MESSAGE_TYPE_5,
            VALID_ENUM_MESSAGE_CODE_6,
            VALID_ENUM_MESSAGE_TYPE_7,
            VALID_ENUM_MESSAGE_ID,
            validate_tag_0,
            validate_tag_0_linked_provider,
            validate_tag_0_linked_order,
            validate_tag_0_fulfill_request,
            validate_tag_1,
            validate_tag_1_lbnp_features,
            validate_tag_1_lbnp_sla_terms,
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
{"_NAME_":"search_validations","_RETURN_":[{"_NAME_":"REQUIRED_CONTEXT_DOMAIN","attr":"$.context.domain","_RETURN_":"attr are present && attr all in enumList","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"]},{"_NAME_":"REQUIRED_CONTEXT_COUNTRY","attr":"$.context.country","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CITY","attr":"$.context.city","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_ACTION","attr":"$.context.action","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_CORE_VERSION","attr":"$.context.core_version","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_ID","attr":"$.context.bap_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_BAP_URI","attr":"$.context.bap_uri","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TRANSACTION_ID","attr":"$.context.transaction_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_MESSAGE_ID","attr":"$.context.message_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TIMESTAMP","attr":"$.context.timestamp","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_CONTEXT_TTL","attr":"$.context.ttl","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.intent.category.id","_RETURN_":"attr are present && attr all in enumList","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"]},{"_NAME_":"REQUIRED_MESSAGE_DAYS","attr":"$.message.intent.provider.time.days","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_HOLIDAYS","attr":"$.message.intent.provider.time.schedule.holidays[*]","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.intent.provider.time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_START","attr":"$.message.intent.provider.time.range.start","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_END","attr":"$.message.intent.provider.time.range.end","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.intent.fulfillment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["Delivery","Return","Batch","RTO"]},{"_NAME_":"REQUIRED_MESSAGE_GPS","attr":"$.message.intent.fulfillment.start.location.gps","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE","attr":"$.message.intent.fulfillment.start.location.address.area_code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_GPS_21","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent.fulfillment.end.location.gps","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_AREA_CODE_22","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent.fulfillment.end.location.address.area_code","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE_23","attr":"$.message.intent.payment.type","_RETURN_":"attr are present && attr all in enumList","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"]},{"_NAME_":"REQUIRED_MESSAGE_UNIT","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].weight.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].weight.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_26","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.length.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_27","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.length.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_28","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.breadth.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_29","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.breadth.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UNIT_30","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.height.unit","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_31","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dimensions.height.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CATEGORY","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].category","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CURRENCY","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].value.currency","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_VALUE_34","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].value.value","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DANGEROUS_GOODS","fulfillmentType":"$.message.intent.fulfillment.type","fulType":["Delivery"],"attr":"$.message.intent['@ondc/org/payload_details'].dangerous_goods","_CONTINUE_":"!(fulfillmentType all in fulType)","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_CONTEXT_DOMAIN","enumList":["ONDC:LOG10","ONDC:LOG11","nic2004:60232"],"enumPath":"$.context.domain","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["Delivery","Return","Batch","RTO"],"enumPath":"$.message.intent.fulfillment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_3","enumList":["OTP"],"enumPath":"$.message.intent.fulfillment.start.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE","enumList":["2","3","4","5"],"enumPath":"$.message.intent.fulfillment.start.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_5","enumList":["OTP"],"enumPath":"$.message.intent.fulfillment.end.authorization.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_CODE_6","enumList":["1","2","3","5"],"enumPath":"$.message.intent.fulfillment.end.instructions.code","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE_7","enumList":["ON-ORDER","ON-FULFILLMENT","POST-FULFILLMENT"],"enumPath":"$.message.intent.payment.type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_ID","enumList":["Express Delivery","Standard Delivery","Immediate Delivery","Next Day Delivery","Same Day Delivery","Instant Delivery"],"enumPath":"$.message.intent.category.id","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"validate_tag_0","validTags":["linked_provider","linked_order","fulfill_request"],"tagPath":"$.message.intent.fulfillment.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_0_linked_provider","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='linked_provider')]","subTags":"$.list[*].code","validValues":["id","name"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_linked_order","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='linked_order')]","subTags":"$.list[*].code","validValues":["cod_order","collection_amount","currency","declared_value","category","weight_unit","weight_value","dim_unit","length","breadth","height"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_0_fulfill_request","_SCOPE_":"$.message.intent.fulfillment.tags[?(@.code=='fulfill_request')]","subTags":"$.list[*].code","validValues":["rider_count","order_count","rate_basis","motorable_distance","pickup_slot_start","pickup_slot_end","delivery_slot_start","delivery_slot_end"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1","validTags":["lbnp_features","lbnp_sla_terms"],"tagPath":"$.message.intent.tags[*].code","_CONTINUE_":"!(tagPath are present)","_RETURN_":"tagPath all in validTags"},{"_NAME_":"validate_tag_1_lbnp_features","_SCOPE_":"$.message.intent.tags[?(@.code=='lbnp_features')]","subTags":"$.list[*].code","validValues":["00B","00E","01D","005","009","00C","000","001","002","003","004","006","007","008","00A","00D","00F","010","011","012","013","014","015","016","017","018","019","01A","01B","01C","01D","01E","01F","020","021","022"],"_RETURN_":"subTags all in validValues"},{"_NAME_":"validate_tag_1_lbnp_sla_terms","_SCOPE_":"$.message.intent.tags[?(@.code=='lbnp_sla_terms')]","subTags":"$.list[*].code","validValues":["metric","base_unit","base_min","base_max","penalty_min","penalty_max","penalty_unit","penalty_value"],"_RETURN_":"subTags all in validValues"}]}
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
