"""Module for IQ option websocket."""

def traders_mood_changed(api, message):
    if message["name"] == "traders-mood-changed":
        api.traders_mood[message["msg"]["asset_id"]] = message["msg"]["value"]