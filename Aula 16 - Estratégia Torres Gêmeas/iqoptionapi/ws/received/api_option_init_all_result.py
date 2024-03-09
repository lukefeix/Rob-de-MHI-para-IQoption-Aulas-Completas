"""Module for IQ option websocket."""

def api_option_init_all_result(api, message):
    if message["name"] == "api_option_init_all_result":
        api.api_option_init_all_result = message["msg"]