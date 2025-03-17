import pandas as pd # type: ignore
import re

from db.getDataFromDb import getDataFromDb
from db.flushCleanData import flushCrimeData

def getCrimeCleanData():
    data = getDataFromDb('data_crime')

    df = pd.DataFrame(data, columns=["id", "country", "description", "value", "unit"])

    df = df.dropna()
    df = df.drop_duplicates()
    df = df[~df.applymap(lambda x: '?' in str(x)).any(axis=1)]
    df = df[pd.to_numeric(df['value'], errors='coerce').notna()]

    return df
