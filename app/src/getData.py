import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import mysql.connector
import time

if __name__ == '__main__':

    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='cours_data',
        port=3306
    )
    cursor = conn.cursor()

    urls = []

    cursor.execute("SELECT country_link FROM links")
    data = cursor.fetchall()
    for row in data:
        urls.append(row[0])

    col0 = []
    col1 = []
    col2 = []

    n = 1

    for url in urls:
        ville = re.search(r"country=([^&]+)", url).group(1)

        print(f"Récupération pour {ville}. No = {n}")

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.select('table.data_wide_table')[0]
        trList = table.select('tr')

        for tr in trList:
            if tr.select('td'):
                td_desc = tr.select('td')[0].text
                price = tr.select('td.priceValue')[0].text
                col0.append(ville)
                col1.append(td_desc)
                col2.append(price)
        time.sleep(0.5)
        n+=1

    result = {
        "city": col0,
        "description": col1,
        "price": col2
    }

    df = pd.DataFrame(result)

    for index, row in df.iterrows():
        city = row['city']
        description = row['description']
        price = row['price']

        sql = "INSERT INTO data (city, description, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (city, description, price))

    conn.commit()

    cursor.close()
    conn.close()

    print("Les données ont été insérées avec succès.")
