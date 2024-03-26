"""Module for IQ option websocket."""

def socket_option_closed(api, message):
    if message["name"] == "socket-option-closed":
        id = message["msg"]["id"]
        api.socket_option_closed[id] = message