"""Module for IQ option websocket."""

def position_closed(api, message):
    if message["name"] == "position-closed":
        api.close_position_data = message
        api.sold_digital_options_respond = message