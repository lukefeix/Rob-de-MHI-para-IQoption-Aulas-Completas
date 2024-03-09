"""Module for IQ option websocket."""
import iqoptionapi.constants as OP_code
from threading import Thread

def live_deal(api, message): 
    if message["name"] == "live-deal":
        # name = message["name"]
        active_id = message["msg"]["instrument_active_id"]
        active = list(OP_code.ACTIVES.keys())[
            list(OP_code.ACTIVES.values()).index(active_id)]
        _type = message["msg"]["instrument_type"]
        try:
            # api.live_deal_data[name][active][_type].appendleft(
            #     message["msg"])
            if hasattr(api.live_deal_cb, '__call__'):
                cb_data = {
                    "active": active,
                    **message["msg"]
                }
                livedeal = Thread(target=api.live_deal_cb,
                                kwargs=(cb_data))
                livedeal.daemon = True
                livedeal.start()
        except:
            pass