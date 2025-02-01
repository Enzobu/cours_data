import pandas as pd # type: ignore
import re

from db.getDataFromDb import getDataFromDb
from db.flushCleanData import flushHealthCareData

def getHealthCareCleanData():
    data = getDataFromDb('data_health_care')

    df = pd.DataFrame(data, columns=["id", "country", "description", "value", "unit"])

    df = df.dropna()
    df = df.drop_duplicates()
    # Supprimer les ligne pour lesquelles il y a '?' dans une des colonnes
    df = df[~df.applymap(lambda x: '?' in str(x)).any(axis=1)]
    # Supprimer les ligne pour lesquelles la colonne 'value' n'est pas un nombre
    df = df[pd.to_numeric(df['value'], errors='coerce').notna()]

    flushHealthCareData(df)
