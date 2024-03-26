"""Module for IQ option websocket."""

def strike_list(api, message):
    if message["name"] == "strike-list":
        api.strike_list = message