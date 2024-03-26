"""Module for IQ option websocket."""
import iqoptionapi.constants as OP_code
from threading import Thread

def live_deal_binary_option_placed(api, message):
    if message["name"] == "live-deal-binary-option-placed":
        # name = message["name"]
        active_id = message["msg"]["active_id"]
        active = list(OP_code.ACTIVES.keys())[
            list(OP_code.ACTIVES.values()).index(active_id)]
        _type = message["msg"]["option_type"]
        try:
            # self.api.live_deal_data[name][active][_type].appendleft(
            #     message["msg"])
            if hasattr(api.binary_live_deal_cb, '__call__'):
                cb_data = {
                    "active": active,
                    **message["msg"]
                }
                realbinary = Thread(target=api.binary_live_deal_cb,
                                    kwargs=(cb_data))
                realbinary.daemon = True
                realbinary.start()
        except:
            pass