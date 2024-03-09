"""Module for IQ option websocket."""

def buy_complete(api, message):
    if message['name'] == 'buyComplete':
        try:
            api.buy_successful = message["msg"]["isSuccessful"]
            api.buy_id = message["msg"]["result"]["id"]
        except:
            pass