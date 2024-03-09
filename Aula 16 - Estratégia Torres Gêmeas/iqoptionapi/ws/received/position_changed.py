"""Module for IQ option websocket."""

def position_changed(api, message):
    if message["name"] == "position-changed":
        if message["microserviceName"] == "portfolio" and (message["msg"]["source"] == "digital-options") or message["msg"]["source"] == "trading":
            api.order_async[int(message["msg"]["raw_event"]["order_ids"][0])][message["name"]] = message
        elif message["microserviceName"] == "portfolio" and message["msg"]["source"] == "binary-options":
            api.order_async[int(message["msg"]["external_id"])][message["name"]] = message
        else:
            api.position_changed = message