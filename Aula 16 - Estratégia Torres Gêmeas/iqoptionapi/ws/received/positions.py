"""Module for IQ option websocket."""

def positions(api, message):
    if message["name"] == "positions":
        api.positions = message
