"""Module for IQ option websocket."""
import iqoptionapi.constants as OP_code
import iqoptionapi.global_value as global_value

def candle_generated_realtime(api, message, dict_queue_add):
    if message["name"] == "candle-generated":
        Active_name = list(OP_code.ACTIVES.keys())[list(
            OP_code.ACTIVES.values()).index(message["msg"]["active_id"])]

        active = str(Active_name)
        size = int(message["msg"]["size"])
        from_ = int(message["msg"]["from"])
        msg = message["msg"]
        maxdict = api.real_time_candles_maxdict_table[Active_name][size]

        dict_queue_add(api.real_time_candles,
                            maxdict, active, size, from_, msg)
        api.candle_generated_check[active][size] = True