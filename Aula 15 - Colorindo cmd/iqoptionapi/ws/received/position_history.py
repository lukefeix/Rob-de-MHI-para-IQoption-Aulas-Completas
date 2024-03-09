"""Module for IQ option websocket."""

def position_history(api, message):
    if message["name"] == "position-history":
        api.position_history = message