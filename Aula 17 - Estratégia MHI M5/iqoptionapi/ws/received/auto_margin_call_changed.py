"""Module for IQ option websocket."""

def auto_margin_call_changed(api, message):
    if message["name"] == "auto-margin-call-changed":
        api.auto_margin_call_changed_respond = message