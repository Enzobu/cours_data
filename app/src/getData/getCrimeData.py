import requests
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
import re
import time


def getCrimeData(urls, base_url, sleep):
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

            table = soup.select('table.table_builder_with_value_explanation')[0]
            trList = table.select('tr')

            for tr in trList:
                try:
                    if tr.select('td'):
                        td_description = tr.select('td.columnWithName')[0].text
                        td_value = re.sub(r'\n.*', '', tr.select('td.indexValueTd')[0].text)
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