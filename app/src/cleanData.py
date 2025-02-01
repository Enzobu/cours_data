import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import mysql.connector

if __name__ == '__main__':


    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["id", "city", "description", "price"])

    df = df.dropna()
    df = df.drop_duplicates()

    # df_bis = df[~df["price"].str.contains(r"(\d+\.\d+)\s+[^\s]+", na=False)]

    df = df[df["price"].str.contains(r"(\d+\.\d+)\s+[^\s]+", na=False)]

    def extract_price_and_currency(price):
        match = re.search(r"(\d+\.\d+)\s+([^\s]+)", price)
        if match:
            numeric_price = float(match.group(1))
            currency = match.group(2)
            return numeric_price, currency
        return -1, -1

    df[["price", "unitPrice"]] = df["price"].apply(
        lambda p: pd.Series(extract_price_and_currency(p))
    )

    for index, row in df.iterrows():
        city = row['city']
        description = row['description']
        price = row['price']
        unitPrice = row['unitPrice']
        sql = "INSERT INTO cleanData (city, description, price, unitPrice) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (city, description, price, unitPrice))

    conn.commit()
    cursor.close()
    conn.close()

    print("Les données ont été nettoyées et insérées dans la table cleanData.")
    # print(f"longueur de df bis {len(df_bis)}")
