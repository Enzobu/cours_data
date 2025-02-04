import requests
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
import re
import time

from db.getLinksFromDb import getLinksFromDb


def getQualityOfLifeData(urls, base_url, sleep = .2):
    col0 = []
    col1 = []
    col2 = []
    col3 = []

    url_count = len(urls)

    n = 1

    for url in urls:
        country = re.search(r"country=([^&]+)", url).group(1)

        part = re.search(r"(?<=https://www\.numbeo\.com/)([^/]+)", base_url).group(1)
        print(f"{round((n/url_count*100), 2):.2f}% --- N° = {n:03d}/{url_count} ---- {part} ---- Récupération pour {country}.")

        try:
            response = requests.get(base_url + url)
            soup = BeautifulSoup(response.content, 'html.parser')

            table = soup.select('table')[2]
            trList = table.select('tr')
            
            for tr in trList:
                try:
                    if tr.select('a.discreet_link') and not tr.select('a.hide_smaller_than_600'):
                        td_description = tr.select('a.discreet_link')[0].text
                        td_value = tr.select('td')[1].text
                        col0.append(td_description)
                        col1.append(td_value)
                        col2.append("%")
                        col3.append(country)
                except:
                    col0.append("Erreur")
                    col1.append("Erreur")
                    col2.append("Erreur")
                    col3.append(country)
                    print(f"Erreur lors d'une boucle pour {country}...")

        except:
            col0.append("Erreur")
            col1.append("Erreur")
            col2.append("Erreur")
            col3.append(country)
            print(f"Erreur lors de la récupération pour {country}...")

        time.sleep(sleep)
        n+=1

    result = {
        "country": col3,
        "description": col0,
        "value": col1,
        "unit": col2
    }

    df = pd.DataFrame(result)

    return df

if __name__ == "main":
    urls = getLinksFromDb()
    base_url = "https://www.numbeo.com/quality-of-life/"
    getQualityOfLifeData(urls, base_url)
