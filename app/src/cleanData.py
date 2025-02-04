from getCleanData.getCostOfLifeCleanData import getCostOfLifeCleanData
from getCleanData.getCrimeCleanData import getCrimeCleanData
from getCleanData.getHealthCareCleanData import getHealthCareCleanData
from getCleanData.getPollutionCleanData import getPollutionCleanData
from getCleanData.getQualityOfLifeCleanData import getQualityOfLifeCleanData

from db.flushCleanData import *

print(" ========== Début de la récupération des datas relative à \"getCostOfLifeCleanData\" ========== ")
try:
    df = getCostOfLifeCleanData()
    flushCostOfLifeData(df)
except Exception as e:
    print(f"Erreur lors du traitement pour \"getCostOfLifeCleanData\" : {e}")

print("\n\n ========== Début de la récupération des datas relative à \"getCrimeCleanData\" ========== ")
try:
    df = getCrimeCleanData()
    flushCrimeData(df)
except Exception as e:
    print(f"Erreur lors du traitement pour \"getCrimeCleanData\" : {e}")

print("\n\n ========== Début de la récupération des datas relative à \"getHealthCareCleanData\" ========== ")
try:
    df = getHealthCareCleanData()
    flushHealthCareData(df)
except Exception as e:
    print(f"Erreur lors du traitement pour \"getHealthCareCleanData\" : {e}")

print("\n\n ========== Début de la récupération des datas relative à \"getPollutionCleanData\" ========== ")
try:
    df = getPollutionCleanData()
    flushPollutionData(df)
except Exception as e:
    print(f"Erreur lors du traitement pour \"getPollutionCleanData\" : {e}")

print("\n\n ========== Début de la récupération des datas relative à \"getQualityOfLifeCleanData\" ========== ")
try:
    df = getQualityOfLifeCleanData()
    flushQualityOfLifeData(df)
except Exception as e:
    print(f"Erreur lors du traitement pour \"getQualityOfLifeCleanData\" : {e}")

print("Processus terminé avec succès.")