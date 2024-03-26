"""Module for IQ option websocket."""

def digital_option_placed(api, message, api_dict_clean):
    if message["name"] == "digital-option-placed":
        if message["msg"].get("id") != None:
            api_dict_clean(api.digital_option_placed_id)
            api.digital_option_placed_id[message["request_id"]
                                                ] = message["msg"]["id"]
        else:
            api.digital_option_placed_id[message["request_id"]] = {
                "code": "error_place_digital_order",
                "message": message["msg"]["message"]
            }