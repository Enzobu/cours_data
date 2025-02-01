import pandas as pd # type: ignore

from getData.getCostOfLifeData import getCostOfLifeData
from getData.getCrimeData import getCrimeData
from getData.getHealthCareData import getHealthCareData
from getData.getPollutionData import getPollutionData
from getData.getQualityOfLifeData import getQualityOfLifeData

from getLinksFromDb import getLinksFromDb
from flush import flush

base_urls = {
    "costOfLife": "https://www.numbeo.com/cost-of-living/",
    "crime": "https://www.numbeo.com/crime/",
    "healthCare": "https://www.numbeo.com/health-care/",
    "pollution": "https://www.numbeo.com/pollution/",
    "qualityOfLife": "https://www.numbeo.com/quality-of-life/",
}

urls = getLinksFromDb()

sleep = 2

print(" ========== Début de la récupération des datas relative à \"costOfLife\" ========== ")
df_costOfLife = getCostOfLifeData(urls, base_urls['costOfLife'], sleep)
flush({
    "table": "cost_of_life_data",
    "df": df_costOfLife,
})

print(" ========== Début de la récupération des datas relative à \"crime\" ========== ")
df_crime = getCrimeData(urls, base_urls['crime'], sleep)
flush({
    "table": "crime_data",
    "df": df_crime,
})

print(" ========== Début de la récupération des datas relative à \"healthCare\" ========== ")
df_healthCare = getHealthCareData(urls, base_urls['healthCare'], sleep)
flush({
    "table": "health_care_data",
    "df": df_healthCare,
})

print(" ========== Début de la récupération des datas relative à \"pollution\" ========== ")
df_pollution = getPollutionData(urls, base_urls['pollution'], sleep)
flush({
    "table": "pollution_data",
    "df": df_pollution,
})

print(" ========== Début de la récupération des datas relative à \"qualityOfLife\" ========== ")
df_qualityOfLife = getQualityOfLifeData(urls, base_urls['qualityOfLife'], sleep)
flush({
    "table": "quality_of_life_data",
    "df": df_qualityOfLife,
})

print("Processus terminé avec succès.")