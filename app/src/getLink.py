import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector

if __name__ == '__main__':
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='cours_data',
        port=3306
    )
    cursor = conn.cursor()

    urls = [
        "https://www.numbeo.com/cost-of-living/"
    ]

    col0 = []
    col1 = []

    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erreur lors de la requête vers {url}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        # Récupérer toutes les tables avec la classe `related_links`
        tables = soup.select('table.related_links')

        # Parcourir chaque table et extraire les données
        base_url = "https://www.numbeo.com/cost-of-living/"
        for table in tables:
            trList = table.select('a')  # Sélectionner tous les liens dans la table
            for tr in trList:
                country = tr.text.strip()
                country_link = base_url + tr['href']
                col0.append(country)
                col1.append(country_link)

    result = {
        "country": col0,
        "country_link": col1,
    }

    df = pd.DataFrame(result)

    # Insérer dans la base de données
    for index, row in df.iterrows():
        country = row['country']
        country_link = row['country_link']

        sql = "INSERT INTO links (country, country_link) VALUES (%s, %s)"
        cursor.execute(sql, (country, country_link))

    conn.commit()

    cursor.close()
    conn.close()

    print("Les données ont été insérées avec succès.")
