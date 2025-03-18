import requests
from bs4 import BeautifulSoup  # type: ignore
import pandas as pd  # type: ignore
import re
import time

url = "https://www.numbeo.com/crime/rankings_by_country.jsp"

def getCrimeIndex():
    col0 = []  # Country
    col1 = []  # Crime Index

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Sélectionner le tableau
        table = soup.select('table.stripe')[0]
        tbody = table.find('tbody')  # Utilisez find au lieu de select
        trList = tbody.find_all('tr')  # Utilisez find_all pour récupérer tous les tr

        # Parcourir chaque ligne de tr
        for tr in trList:
            try:
                td_country = tr.select('td')[1].text.strip()  # Ajout de strip pour nettoyer les espaces
                td_crime_index = tr.select('td')[2].text.strip()  # Idem
                col0.append(td_country)
                col1.append(td_crime_index)
            except Exception as e:
                col0.append("Erreur")
                col1.append("Erreur")
                print(f"Erreur lors d'une boucle: {e}")

    except Exception as e:
        col0.append("Erreur")
        col1.append("Erreur")
        print(f"Erreur lors de la récupération: {e}")

    result = {
        "country": col0,
        "crime_index": col1,
    }

    df = pd.DataFrame(result)

    return df

if __name__ == "__main__":  # Correction ici : "__main__" au lieu de "main"
    df = getCrimeIndex()
    print(df)
