"""Module for IQ option websocket."""

def available_leverages(api, message):
    if message["name"] == "available-leverages":
        api.available_leverages = message