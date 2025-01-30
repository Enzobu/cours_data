import mysql.connector # type: ignore
import pandas as pd # type: ignore

from getData.getCostOfLifeData import getCostOfLifeData

from getData.getCrimeData import getCrimeData
from getData.getHealthCareData import getHealthCareData
from getData.getPollutionData import getPollutionData
from getData.getQualityOfLifeData import getQualityOfLifeData

conn = mysql.connector.connect(
    host='mysql',
    user='root',
    password='root',
    database='cours_data',
    port=3306
)
cursor = conn.cursor()

base_urls = {
    "costOfLife": "https://www.numbeo.com/cost-of-living/",
    "crime": "https://www.numbeo.com/crime/",
    "healthCare": "https://www.numbeo.com/health-care/",
    "pollution": "https://www.numbeo.com/pollution/",
    "qualityOfLife": "https://www.numbeo.com/quality-of-life/",
}

urls = []

cursor.execute("SELECT country_link FROM links")
data = cursor.fetchall()
for row in data:
    urls.append(row[0])

dfs = []

print("=============================================")
df_costOfLife = getCostOfLifeData(urls, base_urls['costOfLife'])
dfs.append({
    "table": "cost_of_life_data",
    "df": df_costOfLife,
})

print("=============================================")
df_crime = getCrimeData(urls, base_urls['crime'])
dfs.append({
    "table": "crime_data",
    "df": df_crime,
})

print("=============================================")
df_healthCare = getHealthCareData(urls, base_urls['healthCare'])
dfs.append({
    "table": "health_care_data",
    "df": df_healthCare,
})

print("=============================================")
df_pollution = getPollutionData(urls, base_urls['pollution'])
dfs.append({
    "table": "pollution_data",
    "df": df_pollution,
})

print("=============================================")
df_qualityOfLife = getQualityOfLifeData(urls, base_urls['qualityOfLife'])
dfs.append({
    "table": "quality_of_life_data",
    "df": df_qualityOfLife,
})


for df in dfs:
    for index, row in df["df"].iterrows():
        table = df["table"]

        country = row['country']
        description = row['description']
        value = row['value']
        unit = row['unit']
        

        sql = f"INSERT INTO {table} (country, description, value, unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (country, description,value, unit))

    print(f"Les données ont été insérées avec succès dans la table {table}")
    conn.commit()

cursor.close()
conn.close()

print("Processus terminé avec succès.")