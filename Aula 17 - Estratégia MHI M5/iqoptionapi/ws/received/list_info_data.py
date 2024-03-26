"""Module for IQ option websocket."""

def list_info_data(api, message):
    if message["name"] == "listInfoData":
        for get_m in message["msg"]:
            api.listinfodata.set(get_m["win"], get_m["game_state"], get_m["id"])