from ..utils.json_path_utils import payload_utils
from ..utils.validation_utils import validation_utils

def issue_validations(input_data):
    scope = payload_utils["get_json_path"](input_data["payload"], "$")
    sub_results = []
    valid = True

    for issue_validations_obj in scope:
        issue_validations_obj["_EXTERNAL"] = input_data["external_data"]

        def REQUIRED_MESSAGE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_obj in scope:
                REQUIRED_MESSAGE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_obj, "$.message.issue.id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID**: $.message.issue.id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.issue.id","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.issue.id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_STATUS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_STATUS_obj in scope:
                REQUIRED_MESSAGE_STATUS_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_STATUS_obj, "$.message.issue.status")
                enumList = ["OPEN","CLOSED","PROCESSING","RESOLVED","NEED_MORE_INFO","INFO_PROVIDED"]

                validate = ((validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))) and (validation_utils["are_unique"](attr))

                if not validate:
                    del REQUIRED_MESSAGE_STATUS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_STATUS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_STATUS**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_STATUS.1**: all of the following sub conditions must be met:

            - **condition REQUIRED_MESSAGE_STATUS.1.1**: $.message.issue.status must be present in the payload
            - **condition REQUIRED_MESSAGE_STATUS.1.2**: every element of $.message.issue.status must be in ["OPEN", "CLOSED", "PROCESSING", "RESOLVED", "NEED_MORE_INFO", "INFO_PROVIDED"]
          - **condition REQUIRED_MESSAGE_STATUS.2**: all values of $.message.issue.status must be unique""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATUS","attr":"$.message.issue.status","_RETURN_":"attr are present && attr all in enumList && attr are unique","enumList":["OPEN","CLOSED","PROCESSING","RESOLVED","NEED_MORE_INFO","INFO_PROVIDED"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_STATUS_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_STATUS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_STATUS","attr":"$.message.issue.status","_RETURN_":"attr are present && attr all in enumList && attr are unique","enumList":["OPEN","CLOSED","PROCESSING","RESOLVED","NEED_MORE_INFO","INFO_PROVIDED"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LEVEL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LEVEL_obj in scope:
                REQUIRED_MESSAGE_LEVEL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LEVEL_obj, "$.message.issue.level")
                enumList = ["ISSUE","GREVIENCE","DISPUTE"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_LEVEL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LEVEL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LEVEL**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_LEVEL.1**: $.message.issue.level must be present in the payload
          - **condition REQUIRED_MESSAGE_LEVEL.2**: every element of $.message.issue.level must be in ["ISSUE", "GREVIENCE", "DISPUTE"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LEVEL","attr":"$.message.issue.level","_RETURN_":"attr are present && attr all in enumList","enumList":["ISSUE","GREVIENCE","DISPUTE"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LEVEL_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LEVEL",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LEVEL","attr":"$.message.issue.level","_RETURN_":"attr are present && attr all in enumList","enumList":["ISSUE","GREVIENCE","DISPUTE"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CREATED_AT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CREATED_AT_obj in scope:
                REQUIRED_MESSAGE_CREATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CREATED_AT_obj, "$.message.issue.created_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CREATED_AT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CREATED_AT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CREATED_AT**: $.message.issue.created_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.issue.created_at","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.issue.created_at","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UPDATED_AT(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATED_AT_obj in scope:
                REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATED_AT_obj, "$.message.issue.updated_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATED_AT_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATED_AT",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATED_AT**: $.message.issue.updated_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.issue.updated_at","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.issue.updated_at","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DURATION(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_obj in scope:
                REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_obj, "$.message.issue.expected_response_time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION**: $.message.issue.expected_response_time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.issue.expected_response_time.duration","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.issue.expected_response_time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_DURATION_7(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_DURATION_7_obj in scope:
                REQUIRED_MESSAGE_DURATION_7_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_DURATION_7_obj, "$.message.issue.expected_resolution_time.duration")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_DURATION_7_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_DURATION_7",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_DURATION_7**: $.message.issue.expected_resolution_time.duration must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION_7","attr":"$.message.issue.expected_resolution_time.duration","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_DURATION_7_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_DURATION_7",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_DURATION_7","attr":"$.message.issue.expected_resolution_time.duration","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_REF_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_REF_ID_obj in scope:
                REQUIRED_MESSAGE_REF_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_REF_ID_obj, "$.message.issue.refs[*].ref_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_REF_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_REF_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_REF_ID**: $.message.issue.refs[*].ref_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_REF_ID","attr":"$.message.issue.refs[*].ref_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_REF_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_REF_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_REF_ID","attr":"$.message.issue.refs[*].ref_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_REF_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_REF_TYPE_obj in scope:
                REQUIRED_MESSAGE_REF_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_REF_TYPE_obj, "$.message.issue.refs[*].ref_type")
                enumList = ["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_REF_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_REF_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_REF_TYPE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_REF_TYPE.1**: $.message.issue.refs[*].ref_type must be present in the payload
          - **condition REQUIRED_MESSAGE_REF_TYPE.2**: every element of $.message.issue.refs[*].ref_type must be in ["ORDER", "ITEM", "FULFILLMENT", "TRANSACTION_ID", "MESSAGE_ID", "PROVIDER", "COMPLAINT", "ACTION", "PAYMENT", "CUSTOMER", "AGENT"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_REF_TYPE","attr":"$.message.issue.refs[*].ref_type","_RETURN_":"attr are present && attr all in enumList","enumList":["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"]}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_REF_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_REF_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_REF_TYPE","attr":"$.message.issue.refs[*].ref_type","_RETURN_":"attr are present && attr all in enumList","enumList":["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_10(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_10_obj in scope:
                REQUIRED_MESSAGE_ID_10_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_10_obj, "$.message.issue.actors[*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_10_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_10",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_10**: $.message.issue.actors[*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_10","attr":"$.message.issue.actors[*].id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_10_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_10",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_10","attr":"$.message.issue.actors[*].id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_TYPE_obj in scope:
                REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_TYPE_obj, "$.message.issue.actors[*].type")
                enumList = ["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"]

                validate = (validation_utils["are_present"](attr)) and (validation_utils["all_in"](attr, enumList))

                if not validate:
                    del REQUIRED_MESSAGE_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_TYPE**: all of the following sub conditions must be met:

          - **condition REQUIRED_MESSAGE_TYPE.1**: $.message.issue.actors[*].type must be present in the payload
          - **condition REQUIRED_MESSAGE_TYPE.2**: every element of $.message.issue.actors[*].type must be in ["INTERFACING_NP", "COUNTERPARTY_NP", "CASCADED_NP", "PROVIDER", "AGENT", "CUSTOMER", "INTERFACING_NP_GRO", "COUNTERPARTY_NP_GRO", "CASCADED_NP_GRO", "CONSUMER"]""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.issue.actors[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"]}
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
        {"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.issue.actors[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"]}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_obj in scope:
                REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_obj, "$.message.issue.actors[*].info.person.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME**: $.message.issue.actors[*].info.person.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.issue.actors[*].info.person.name","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.issue.actors[*].info.person.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_NAME_13(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_NAME_13_obj in scope:
                REQUIRED_MESSAGE_NAME_13_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_NAME_13_obj, "$.message.issue.actors[*].info.person.name")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_NAME_13_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_NAME_13",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_NAME_13**: $.message.issue.actors[*].info.person.name must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_13","attr":"$.message.issue.actors[*].info.person.name","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_NAME_13_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_NAME_13",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_NAME_13","attr":"$.message.issue.actors[*].info.person.name","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_PHONE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_PHONE_obj in scope:
                REQUIRED_MESSAGE_PHONE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_PHONE_obj, "$.message.issue.actors[*].info.contact.phone")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_PHONE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_PHONE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_PHONE**: $.message.issue.actors[*].info.contact.phone must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.issue.actors[*].info.contact.phone","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.issue.actors[*].info.contact.phone","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_EMAIL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_EMAIL_obj in scope:
                REQUIRED_MESSAGE_EMAIL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_EMAIL_obj, "$.message.issue.actors[*].info.contact.email")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_EMAIL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_EMAIL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_EMAIL**: $.message.issue.actors[*].info.contact.email must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.issue.actors[*].info.contact.email","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.issue.actors[*].info.contact.email","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_SOURCE_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_SOURCE_ID_obj in scope:
                REQUIRED_MESSAGE_SOURCE_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_SOURCE_ID_obj, "$.message.issue.source_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_SOURCE_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_SOURCE_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_SOURCE_ID**: $.message.issue.source_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SOURCE_ID","attr":"$.message.issue.source_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_SOURCE_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_SOURCE_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SOURCE_ID","attr":"$.message.issue.source_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CODE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CODE_obj in scope:
                REQUIRED_MESSAGE_CODE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CODE_obj, "$.message.issue.descriptor.code")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CODE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CODE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CODE**: $.message.issue.descriptor.code must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CODE","attr":"$.message.issue.descriptor.code","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_CODE","attr":"$.message.issue.descriptor.code","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_SHORT_DESC(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_SHORT_DESC_obj in scope:
                REQUIRED_MESSAGE_SHORT_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_SHORT_DESC_obj, "$.message.issue.descriptor.short_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_SHORT_DESC_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_SHORT_DESC",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_SHORT_DESC**: $.message.issue.descriptor.short_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC","attr":"$.message.issue.descriptor.short_desc","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC","attr":"$.message.issue.descriptor.short_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LONG_DESC(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LONG_DESC_obj in scope:
                REQUIRED_MESSAGE_LONG_DESC_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LONG_DESC_obj, "$.message.issue.descriptor.long_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LONG_DESC_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LONG_DESC",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LONG_DESC**: $.message.issue.descriptor.long_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LONG_DESC","attr":"$.message.issue.descriptor.long_desc","_RETURN_":"attr are present"}
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
        {"_NAME_":"REQUIRED_MESSAGE_LONG_DESC","attr":"$.message.issue.descriptor.long_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_URL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_URL_obj in scope:
                REQUIRED_MESSAGE_URL_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_URL_obj, "$.message.issue.descriptor.additional_desc.url")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_URL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_URL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_URL**: $.message.issue.descriptor.additional_desc.url must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_URL","attr":"$.message.issue.descriptor.additional_desc.url","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_URL_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_URL",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_URL","attr":"$.message.issue.descriptor.additional_desc.url","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CONTENT_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CONTENT_TYPE_obj in scope:
                REQUIRED_MESSAGE_CONTENT_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CONTENT_TYPE_obj, "$.message.issue.descriptor.additional_desc.content_type")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CONTENT_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CONTENT_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CONTENT_TYPE**: $.message.issue.descriptor.additional_desc.content_type must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CONTENT_TYPE","attr":"$.message.issue.descriptor.additional_desc.content_type","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CONTENT_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CONTENT_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CONTENT_TYPE","attr":"$.message.issue.descriptor.additional_desc.content_type","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_LAST_ACTION_ID(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_LAST_ACTION_ID_obj in scope:
                REQUIRED_MESSAGE_LAST_ACTION_ID_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_LAST_ACTION_ID_obj, "$.message.issue.last_action_id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_LAST_ACTION_ID_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_LAST_ACTION_ID",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_LAST_ACTION_ID**: $.message.issue.last_action_id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LAST_ACTION_ID","attr":"$.message.issue.last_action_id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_LAST_ACTION_ID_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_LAST_ACTION_ID",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_LAST_ACTION_ID","attr":"$.message.issue.last_action_id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ID_25(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ID_25_obj in scope:
                REQUIRED_MESSAGE_ID_25_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ID_25_obj, "$.message.issue.actions[*].id")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ID_25_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ID_25",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ID_25**: $.message.issue.actions[*].id must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_25","attr":"$.message.issue.actions[*].id","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ID_25_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ID_25",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ID_25","attr":"$.message.issue.actions[*].id","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_CODE_26(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_CODE_26_obj in scope:
                REQUIRED_MESSAGE_CODE_26_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_CODE_26_obj, "$.message.issue.actions[*].descriptor.code")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_CODE_26_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_CODE_26",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_CODE_26**: $.message.issue.actions[*].descriptor.code must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CODE_26","attr":"$.message.issue.actions[*].descriptor.code","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_CODE_26_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_CODE_26",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_CODE_26","attr":"$.message.issue.actions[*].descriptor.code","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_SHORT_DESC_27(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_SHORT_DESC_27_obj in scope:
                REQUIRED_MESSAGE_SHORT_DESC_27_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_SHORT_DESC_27_obj, "$.message.issue.actions[*].descriptor.short_desc")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_SHORT_DESC_27_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_SHORT_DESC_27",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_SHORT_DESC_27**: $.message.issue.actions[*].descriptor.short_desc must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC_27","attr":"$.message.issue.actions[*].descriptor.short_desc","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_SHORT_DESC_27_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_SHORT_DESC_27",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC_27","attr":"$.message.issue.actions[*].descriptor.short_desc","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_UPDATED_AT_28(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_UPDATED_AT_28_obj in scope:
                REQUIRED_MESSAGE_UPDATED_AT_28_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_UPDATED_AT_28_obj, "$.message.issue.actions[*].updated_at")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_UPDATED_AT_28_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_UPDATED_AT_28",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_UPDATED_AT_28**: $.message.issue.actions[*].updated_at must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_28","attr":"$.message.issue.actions[*].updated_at","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_UPDATED_AT_28_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_UPDATED_AT_28",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_28","attr":"$.message.issue.actions[*].updated_at","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def REQUIRED_MESSAGE_ACTION_BY(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for REQUIRED_MESSAGE_ACTION_BY_obj in scope:
                REQUIRED_MESSAGE_ACTION_BY_obj["_EXTERNAL"] = input_data["external_data"]
                attr = payload_utils["get_json_path"](REQUIRED_MESSAGE_ACTION_BY_obj, "$.message.issue.actions[*].action_by")

                validate = validation_utils["are_present"](attr)

                if not validate:
                    del REQUIRED_MESSAGE_ACTION_BY_obj["_EXTERNAL"]
                    return [{
                        "test_name": "REQUIRED_MESSAGE_ACTION_BY",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition REQUIRED_MESSAGE_ACTION_BY**: $.message.issue.actions[*].action_by must be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ACTION_BY","attr":"$.message.issue.actions[*].action_by","_RETURN_":"attr are present"}
        """
                        }
                    }]

                # del REQUIRED_MESSAGE_ACTION_BY_obj["_EXTERNAL"]

            return [{
                "test_name": "REQUIRED_MESSAGE_ACTION_BY",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"REQUIRED_MESSAGE_ACTION_BY","attr":"$.message.issue.actions[*].action_by","_RETURN_":"attr are present"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_STATUS(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_STATUS_obj in scope:
                VALID_ENUM_MESSAGE_STATUS_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["OPEN","CLOSED","PROCESSING","RESOLVED"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_STATUS_obj, "$.message.issue.status")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_STATUS_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_STATUS",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_STATUS**: every element of $.message.issue.status must be in ["OPEN", "CLOSED", "PROCESSING", "RESOLVED"]

        	> Note: **Condition VALID_ENUM_MESSAGE_STATUS** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.issue.status must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_STATUS","enumList":["OPEN","CLOSED","PROCESSING","RESOLVED"],"enumPath":"$.message.issue.status","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_STATUS_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_STATUS",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_STATUS","enumList":["OPEN","CLOSED","PROCESSING","RESOLVED"],"enumPath":"$.message.issue.status","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_LEVEL(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_LEVEL_obj in scope:
                VALID_ENUM_MESSAGE_LEVEL_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["ISSUE","GREVIENCE","DISPUTE"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_LEVEL_obj, "$.message.issue.level")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_LEVEL_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_LEVEL",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_LEVEL**: every element of $.message.issue.level must be in ["ISSUE", "GREVIENCE", "DISPUTE"]

        	> Note: **Condition VALID_ENUM_MESSAGE_LEVEL** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.issue.level must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_LEVEL","enumList":["ISSUE","GREVIENCE","DISPUTE"],"enumPath":"$.message.issue.level","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_LEVEL_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_LEVEL",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_LEVEL","enumList":["ISSUE","GREVIENCE","DISPUTE"],"enumPath":"$.message.issue.level","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_REF_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_REF_TYPE_obj in scope:
                VALID_ENUM_MESSAGE_REF_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_REF_TYPE_obj, "$.message.issue.refs[*].ref_type")

                skip_check = not (validation_utils["are_present"](enumPath))
                if skip_check:
                    continue

                validate = validation_utils["all_in"](enumPath, enumList)

                if not validate:
                    del VALID_ENUM_MESSAGE_REF_TYPE_obj["_EXTERNAL"]
                    return [{
                        "test_name": "VALID_ENUM_MESSAGE_REF_TYPE",
                        "valid": False,
                        "code": 30000,
                        "description": r"""- **condition VALID_ENUM_MESSAGE_REF_TYPE**: every element of $.message.issue.refs[*].ref_type must be in ["ORDER", "ITEM", "FULFILLMENT", "TRANSACTION_ID", "MESSAGE_ID", "PROVIDER", "COMPLAINT", "ACTION", "PAYMENT", "CUSTOMER", "AGENT"]

        	> Note: **Condition VALID_ENUM_MESSAGE_REF_TYPE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.issue.refs[*].ref_type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_REF_TYPE","enumList":["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"],"enumPath":"$.message.issue.refs[*].ref_type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
                        }
                    }]

                # del VALID_ENUM_MESSAGE_REF_TYPE_obj["_EXTERNAL"]

            return [{
                "test_name": "VALID_ENUM_MESSAGE_REF_TYPE",
                "valid": valid,
                "code": 200 if valid else 30000, 
                "_debug_info": {
                    "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_REF_TYPE","enumList":["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"],"enumPath":"$.message.issue.refs[*].ref_type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        def VALID_ENUM_MESSAGE_TYPE(input_data):
            scope = payload_utils["get_json_path"](input_data["payload"], "$")
            sub_results = []
            valid = True

            for VALID_ENUM_MESSAGE_TYPE_obj in scope:
                VALID_ENUM_MESSAGE_TYPE_obj["_EXTERNAL"] = input_data["external_data"]
                enumList = ["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"]
                enumPath = payload_utils["get_json_path"](VALID_ENUM_MESSAGE_TYPE_obj, "$.message.issue.actors[*].type")

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
                        "description": r"""- **condition VALID_ENUM_MESSAGE_TYPE**: every element of $.message.issue.actors[*].type must be in ["INTERFACING_NP", "COUNTERPARTY_NP", "CASCADED_NP", "PROVIDER", "AGENT", "CUSTOMER", "INTERFACING_NP_GRO", "COUNTERPARTY_NP_GRO", "CASCADED_NP_GRO", "CONSUMER"]

        	> Note: **Condition VALID_ENUM_MESSAGE_TYPE** can be skipped if the following conditions are met:
        	>
        	> - **condition B**: $.message.issue.actors[*].type must **not** be present in the payload""",
                        "_debug_info": {
                            "fed_config": r"""
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"],"enumPath":"$.message.issue.actors[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
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
        {"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"],"enumPath":"$.message.issue.actors[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}
        """
            }}] + sub_results

        test_functions = [
            REQUIRED_MESSAGE_ID,
            REQUIRED_MESSAGE_STATUS,
            REQUIRED_MESSAGE_LEVEL,
            REQUIRED_MESSAGE_CREATED_AT,
            REQUIRED_MESSAGE_UPDATED_AT,
            REQUIRED_MESSAGE_DURATION,
            REQUIRED_MESSAGE_DURATION_7,
            REQUIRED_MESSAGE_REF_ID,
            REQUIRED_MESSAGE_REF_TYPE,
            REQUIRED_MESSAGE_ID_10,
            REQUIRED_MESSAGE_TYPE,
            REQUIRED_MESSAGE_NAME,
            REQUIRED_MESSAGE_NAME_13,
            REQUIRED_MESSAGE_PHONE,
            REQUIRED_MESSAGE_EMAIL,
            REQUIRED_MESSAGE_SOURCE_ID,
            REQUIRED_MESSAGE_CODE,
            REQUIRED_MESSAGE_SHORT_DESC,
            REQUIRED_MESSAGE_LONG_DESC,
            REQUIRED_MESSAGE_URL,
            REQUIRED_MESSAGE_CONTENT_TYPE,
            REQUIRED_MESSAGE_LAST_ACTION_ID,
            REQUIRED_MESSAGE_ID_25,
            REQUIRED_MESSAGE_CODE_26,
            REQUIRED_MESSAGE_SHORT_DESC_27,
            REQUIRED_MESSAGE_UPDATED_AT_28,
            REQUIRED_MESSAGE_ACTION_BY,
            VALID_ENUM_MESSAGE_STATUS,
            VALID_ENUM_MESSAGE_LEVEL,
            VALID_ENUM_MESSAGE_REF_TYPE,
            VALID_ENUM_MESSAGE_TYPE,
        ]

        all_results = []
        for fn in test_functions:
            sub_result = fn(input_data)
            all_results.extend(sub_result)

        sub_results = all_results
        valid = all(r["valid"] for r in sub_results)

        # del issue_validations_obj["_EXTERNAL"]

    return [{
        "test_name": "issue_validations",
        "valid": valid,
        "code": 200 if valid else 30000, 
        "_debug_info": {
            "fed_config": r"""
{"_NAME_":"issue_validations","_RETURN_":[{"_NAME_":"REQUIRED_MESSAGE_ID","attr":"$.message.issue.id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_STATUS","attr":"$.message.issue.status","_RETURN_":"attr are present && attr all in enumList && attr are unique","enumList":["OPEN","CLOSED","PROCESSING","RESOLVED","NEED_MORE_INFO","INFO_PROVIDED"]},{"_NAME_":"REQUIRED_MESSAGE_LEVEL","attr":"$.message.issue.level","_RETURN_":"attr are present && attr all in enumList","enumList":["ISSUE","GREVIENCE","DISPUTE"]},{"_NAME_":"REQUIRED_MESSAGE_CREATED_AT","attr":"$.message.issue.created_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT","attr":"$.message.issue.updated_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION","attr":"$.message.issue.expected_response_time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_DURATION_7","attr":"$.message.issue.expected_resolution_time.duration","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_REF_ID","attr":"$.message.issue.refs[*].ref_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_REF_TYPE","attr":"$.message.issue.refs[*].ref_type","_RETURN_":"attr are present && attr all in enumList","enumList":["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"]},{"_NAME_":"REQUIRED_MESSAGE_ID_10","attr":"$.message.issue.actors[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_TYPE","attr":"$.message.issue.actors[*].type","_RETURN_":"attr are present && attr all in enumList","enumList":["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"]},{"_NAME_":"REQUIRED_MESSAGE_NAME","attr":"$.message.issue.actors[*].info.person.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_NAME_13","attr":"$.message.issue.actors[*].info.person.name","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_PHONE","attr":"$.message.issue.actors[*].info.contact.phone","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_EMAIL","attr":"$.message.issue.actors[*].info.contact.email","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_SOURCE_ID","attr":"$.message.issue.source_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CODE","attr":"$.message.issue.descriptor.code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC","attr":"$.message.issue.descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LONG_DESC","attr":"$.message.issue.descriptor.long_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_URL","attr":"$.message.issue.descriptor.additional_desc.url","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CONTENT_TYPE","attr":"$.message.issue.descriptor.additional_desc.content_type","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_LAST_ACTION_ID","attr":"$.message.issue.last_action_id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ID_25","attr":"$.message.issue.actions[*].id","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_CODE_26","attr":"$.message.issue.actions[*].descriptor.code","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_SHORT_DESC_27","attr":"$.message.issue.actions[*].descriptor.short_desc","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_UPDATED_AT_28","attr":"$.message.issue.actions[*].updated_at","_RETURN_":"attr are present"},{"_NAME_":"REQUIRED_MESSAGE_ACTION_BY","attr":"$.message.issue.actions[*].action_by","_RETURN_":"attr are present"},{"_NAME_":"VALID_ENUM_MESSAGE_STATUS","enumList":["OPEN","CLOSED","PROCESSING","RESOLVED"],"enumPath":"$.message.issue.status","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_LEVEL","enumList":["ISSUE","GREVIENCE","DISPUTE"],"enumPath":"$.message.issue.level","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_REF_TYPE","enumList":["ORDER","ITEM","FULFILLMENT","TRANSACTION_ID","MESSAGE_ID","PROVIDER","COMPLAINT","ACTION","PAYMENT","CUSTOMER","AGENT"],"enumPath":"$.message.issue.refs[*].ref_type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"},{"_NAME_":"VALID_ENUM_MESSAGE_TYPE","enumList":["INTERFACING_NP","COUNTERPARTY_NP","CASCADED_NP","PROVIDER","AGENT","CUSTOMER","INTERFACING_NP_GRO","COUNTERPARTY_NP_GRO","CASCADED_NP_GRO","CONSUMER"],"enumPath":"$.message.issue.actors[*].type","_CONTINUE_":"!(enumPath are present)","_RETURN_":"enumPath all in enumList"}]}
"""
    }}] + sub_results

def issue(input_data):
    total_results = issue_validations(input_data)

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
            target_success = next((r for r in total_results if r["test_name"] == "issue_validations"), None)
            if not target_success:
                raise Exception("Critical: Overall test result not found")
            return [target_success]
        return res

    return total_results
