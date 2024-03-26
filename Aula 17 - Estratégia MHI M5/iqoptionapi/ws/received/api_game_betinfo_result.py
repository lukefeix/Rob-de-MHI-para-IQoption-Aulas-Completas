"""Module for IQ option websocket."""

def api_game_betinfo_result(api, message):
    if message["name"] == "api_game_betinfo_result":
        try:
            api.game_betinfo.isSuccessful = message["msg"]["isSuccessful"]
            api.game_betinfo.dict = message["msg"]
        except:
            pass