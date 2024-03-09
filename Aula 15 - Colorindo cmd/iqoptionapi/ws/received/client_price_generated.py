"""Module for IQ option websocket."""

def client_price_generated(api, message):
    if message["name"] == "client-price-generated":
        ask_price = [d for d in message["msg"]["prices"] if d['strike'] == 'SPT'][0]['call']['ask']
        api.digital_payout = int(((100-ask_price)*100)/ask_price)
        api.client_price_generated = message["msg"]
    else:
        pass