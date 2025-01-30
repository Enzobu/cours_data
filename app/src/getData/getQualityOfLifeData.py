import requests
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
import re
import time


def getQualityOfLifeData(urls, base_url):
    col0 = []
    col1 = []
    col2 = []
    col3 = []

    n = 1

    for url in urls:
        country = re.search(r"country=([^&]+)", url).group(1)

        print(f"Récupération pour {country}. No = {n}")

        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.select('table')[2]
        trList = table.select('tr')
        for tr in trList:
            # print(True if tr.select('a.discreet_link') and not tr.select('a.hide_smaller_than_600') else False)
            if tr.select('a.discreet_link') and not tr.select('a.hide_smaller_than_600'):
                td_description = tr.select('a.discreet_link')[0].text
                td_value = tr.select('td')[1].text
                col0.append(td_description)
                col1.append(td_value)
                col2.append("%")
                col3.append(country)
        time.sleep(0.5)
        n+=1

    result = {
        "country": col3,
        "description": col0,
        "value": col1,
        "unit": col2
    }

    df = pd.DataFrame(result)

    return df