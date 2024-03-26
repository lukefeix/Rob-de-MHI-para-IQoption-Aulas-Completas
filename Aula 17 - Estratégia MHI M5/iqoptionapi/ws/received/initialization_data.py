"""Module for IQ option websocket."""

def initialization_data(api, message):
    if message["name"] == "initialization-data":
        api.api_option_init_all_result_v2 = message["msg"]