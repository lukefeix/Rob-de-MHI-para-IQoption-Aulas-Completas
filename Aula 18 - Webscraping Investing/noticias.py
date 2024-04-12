import urllib
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
from tabulate import tabulate


def get_noticias():
    url = 'https://br.investing.com/economic-calendar/'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
    result = []

    try:
        response = urllib.request.urlopen(req)
        html = response.read()

        soup = BeautifulSoup(html, "html.parser")
        t = soup.find('table', {"id": "economicCalendarData"})
        tabela = t.find("tbody")
        linhas = tabela.findAll('tr' , {"class": "js-event-item"})

        for tr in linhas:
            data = tr.attrs['data-event-datetime']
            data2 = datetime.strptime(data, '%Y/%m/%d %H:%M:%S')
            hora = data2.strftime("%H:%M")
            timestamp = int(datetime.timestamp(data2))

            cols = tr.find('td', {"class": "flagCur"})
            par = cols.text.strip()

            impact = tr.find('td', {"class": "sentiment"})
            bull = impact.findAll("i", {"class": "grayFullBullishIcon"})

            result.append([hora, len(bull), par])
        
        return result
        
    except HTTPError as error:
        print ("Ocorreu um erro." + error.code)


noticias = get_noticias()

print(tabulate(noticias, headers=['HORA',"TOUROS", "PAR"], tablefmt= "pretty"))