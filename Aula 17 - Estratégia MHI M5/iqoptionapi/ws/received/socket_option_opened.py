"""Module for IQ option websocket."""

def socket_option_opened(api, message):
    if message["name"] == "socket-option-opened":
        id = message["msg"]["id"]
        api.socket_option_opened[id] = message