from iqoptionapi.stable_api import IQ_Option
import time
from configobj import ConfigObj
import sys
from datetime import datetime
from tabulate import tabulate


def catag(API):

    ### CRIANDO ARQUIVO DE CONFIGURAÇÃO ####
    config = ConfigObj('config.txt')
    

    pares_abertos = []

    all_asset = API.get_all_open_time()

    for par in all_asset['digital']:
        if all_asset['digital'][par]['open']:
            pares_abertos.append(par)

    for par in all_asset['turbo']:
        if all_asset['turbo'][par]['open']:
            if par not in pares_abertos:
                pares_abertos.append(par)
            

    timeframe = 60
    qnt_velas  = 120
    resultado = []

    for par in pares_abertos:
        velas = API.get_candles(par, timeframe,qnt_velas, time.time())
        doji = 0
        win = 0
        loss = 0
        gale1 = 0
        gale2 = 0

        for i in range(len(velas)):
            minutos = float(datetime.fromtimestamp(velas[i]['from']).strftime('%M')[1:])

            if minutos == 5 or minutos== 0:
                try:
                    if i <2:
                        pass
                    else:

                        vela1 = 'Verde' if velas[i-3]['open'] < velas[i-3]['close'] else 'Vermelha' if velas[i-3]['open'] > velas[i-3]['close'] else 'Doji'
                        vela2 = 'Verde' if velas[i-2]['open'] < velas[i-2]['close'] else 'Vermelha' if velas[i-2]['open'] > velas[i-2]['close'] else 'Doji'
                        vela3 = 'Verde' if velas[i-1]['open'] < velas[i-1]['close'] else 'Vermelha' if velas[i-1]['open'] > velas[i-1]['close'] else 'Doji'

                        entrada1 = 'Verde' if velas[i]['open'] < velas[i]['close'] else 'Vermelha' if velas[i]['open'] > velas[i]['close'] else 'Doji'
                        entrada2 = 'Verde' if velas[i+1]['open'] < velas[i+1]['close'] else 'Vermelha' if velas[i+1]['open'] > velas[i+1]['close'] else 'Doji'
                        entrada3 ='Verde' if velas[i+2]['open'] < velas[i+2]['close'] else 'Vermelha' if velas[i+2]['open'] > velas[i+2]['close'] else 'Doji'

                        cores = vela1,vela2,vela3

                        if cores.count('Verde') > cores.count('Vermelha') and cores.count('Doji') == 0 : dir = 'Vermelha'
                    
                        if cores.count('Vermelha') > cores.count('Verde') and cores.count('Doji') == 0 : dir = 'Verde'

                        if cores.count('Doji') >0:
                            doji += 1
                        else:
                            if entrada1 == dir:
                                win +=1
                            else:
                                if entrada2 == dir:
                                    gale1 +=1
                                else:
                                    if entrada3 == dir:
                                        gale2 +=1

                                    else:
                                        loss +=1
                except:
                    pass

        total_entrada = win + gale1 + gale2 + loss
        qnt_win = win
        qnt_gale1 = win + gale1
        qnt_gale2 = win + gale1 + gale2

        win = round(qnt_win/(total_entrada)*100,2)
        gale1 = round(qnt_gale1/(total_entrada)*100,2)
        gale2 = round(qnt_gale2/(total_entrada)*100,2)

        resultado.append([par]+ [win] +[gale1] + [gale2])



    if config['MARTINGALE']['usar_martingale'] == 'S':
        if int(config['MARTINGALE']['niveis_martingale']) == 0:
            linha = 1
        if int(config['MARTINGALE']['niveis_martingale']) == 1:
            linha = 2
        if int(config['MARTINGALE']['niveis_martingale']) >= 2:
            linha = 3
    else:
        linha = 1

    lista_catalog = sorted(resultado, key = lambda x: x[linha], reverse = True)

    return lista_catalog, linha
