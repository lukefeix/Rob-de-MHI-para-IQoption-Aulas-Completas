"""Module for IQ option websocket."""

def technical_indicators(api, message, api_dict_clean):
    if message["name"] == "technical-indicators":
        if message["msg"].get("indicators") != None:
            api_dict_clean(api.technical_indicators)
            api.technical_indicators[message["request_id"]] = message["msg"]["indicators"]
        else:
            api.technical_indicators[message["request_id"]] = {
                "code": "no_technical_indicator_available",
                "message": message["msg"]["message"]
            }