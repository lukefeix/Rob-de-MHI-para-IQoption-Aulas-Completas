"""Module for IQ option websocket."""
import iqoptionapi.constants as OP_code

def commission_changed(api, message):
    if message["name"] == "commission-changed":
        instrument_type = message["msg"]["instrument_type"]
        active_id = message["msg"]["active_id"]
        Active_name = list(OP_code.ACTIVES.keys())[list(
            OP_code.ACTIVES.values()).index(active_id)]
        commission = message["msg"]["commission"]["value"]
        api.subscribe_commission_changed_data[instrument_type][Active_name][api.timesync.server_timestamp] = int(
            commission)