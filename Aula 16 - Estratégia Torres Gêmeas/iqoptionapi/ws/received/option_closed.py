"""Module for IQ option websocket."""

def option_closed(api, message):
    if message["name"] == "option-closed":
        api.order_async[int(message["msg"]["option_id"])][message["name"]] = message
        if message["microserviceName"] == "binary-options":
            api.order_binary[message["msg"]["option_id"]] = message['msg']