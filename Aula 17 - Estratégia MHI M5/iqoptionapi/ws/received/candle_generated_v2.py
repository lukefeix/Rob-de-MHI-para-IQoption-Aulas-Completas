import iqoptionapi.constants as OP_code

def candle_generated_v2(api, message, dict_queue_add):
    if message["name"] == "candles-generated":
        Active_name = list(OP_code.ACTIVES.keys())[list(
                OP_code.ACTIVES.values()).index(message["msg"]["active_id"])]
        active = str(Active_name)
        for k, v in message["msg"]["candles"].items():
            v["active_id"] = message["msg"]["active_id"]
            v["at"] = message["msg"]["at"]
            v["ask"] = message["msg"]["ask"]
            v["bid"] = message["msg"]["bid"]
            v["close"] = message["msg"]["value"]
            v["size"] = int(k)
            size = int(v["size"])
            from_ = int(v["from"])
            maxdict = api.real_time_candles_maxdict_table[Active_name][size]
            msg = v
            dict_queue_add(api.real_time_candles, maxdict, active, size, from_, msg)

        api.candle_generated_all_size_check[active] = True