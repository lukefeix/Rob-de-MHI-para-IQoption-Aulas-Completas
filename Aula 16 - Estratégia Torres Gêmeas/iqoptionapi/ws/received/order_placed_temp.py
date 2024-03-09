"""Module for IQ option websocket."""

def order_placed_temp(api, message):
    if message["name"] == "order-placed-temp":
        api.buy_order_id = message["msg"]["id"]
