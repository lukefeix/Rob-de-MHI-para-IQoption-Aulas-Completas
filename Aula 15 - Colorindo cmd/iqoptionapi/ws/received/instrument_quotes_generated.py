"""Module for IQ option websocket."""
import iqoptionapi.constants as OP_code

def instrument_quotes_generated(api, message):
    if message["name"] == "instrument-quotes-generated":

        Active_name = list(OP_code.ACTIVES.keys())[list(OP_code.ACTIVES.values()).index(message["msg"]["active"])]
        period = message["msg"]["expiration"]["period"]
        ans = {}
        for data in message["msg"]["quotes"]:
            # FROM IQ OPTION SOURCE CODE
            if data["price"]["ask"] == None:
                ProfitPercent = None
            else:
                askPrice = (float)(data["price"]["ask"])
                ProfitPercent = ((100-askPrice)*100)/askPrice

            for symble in data["symbols"]:
                try:
                    """
                    ID SAMPLE:doUSDJPY-OTC201811111204PT1MC11350481
                    """

                    """
                    dict ID-prodit:{ID:profit}
                    """

                    ans[symble] = ProfitPercent
                except:
                    pass
        api.instrument_quites_generated_timestamp[Active_name][
            period] = message["msg"]["expiration"]["timestamp"]
        api.instrument_quites_generated_data[Active_name][period] = ans

        api.instrument_quotes_generated_raw_data[Active_name][period] = message