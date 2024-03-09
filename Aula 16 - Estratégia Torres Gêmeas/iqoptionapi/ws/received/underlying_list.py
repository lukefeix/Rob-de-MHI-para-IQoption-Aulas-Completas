"""Module for IQ option websocket."""

def underlying_list(api, message):
    if message["name"] == "underlying-list":
        api.underlying_list_data = message["msg"]
