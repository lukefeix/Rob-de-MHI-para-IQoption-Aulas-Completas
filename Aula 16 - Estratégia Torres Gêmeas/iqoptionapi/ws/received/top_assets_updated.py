"""Module for IQ option websocket."""

def top_assets_updated(api, message):
    if message["name"] == "top-assets-updated":
        api.top_assets_updated_data[str(message["msg"]["instrument_type"])] = message["msg"]["data"]