"""Module for IQ option websocket."""
import iqoptionapi.constants as OP_code
from threading import Thread

def live_deal_digital_option(api, message):
    if message["name"] == "live-deal-digital-option":
        # name = message["name"]
        active_id = message["msg"]["instrument_active_id"]
        active = list(OP_code.ACTIVES.keys())[
            list(OP_code.ACTIVES.values()).index(active_id)]
        _type = message["msg"]["expiration_type"]
        try:
            # self.api.live_deal_data[name][active][_type].appendleft(
            #     message["msg"])
            if hasattr(api.digital_live_deal_cb, '__call__'):
                cb_data = {
                    "active": active,
                    **message["msg"]
                }
                realdigital = Thread(target=api.digital_live_deal_cb,
                                        kwargs=(cb_data))
                realdigital.daemon = True
                realdigital.start()
        except:
            pass