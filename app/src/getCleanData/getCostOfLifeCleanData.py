import pandas as pd # type: ignore
import re

from db.getDataFromDb import getDataFromDb
from db.flushCleanData import flushCostOfLifeData

def getCostOfLifeCleanData():
    data = getDataFromDb('data_cost_of_life')

    df = pd.DataFrame(data, columns=["id", "country", "description", "value", "unit"])

    df = df.dropna()
    df = df.drop_duplicates()

    df = df[df["value"].str.contains(r"(\d+\.\d+)\s+[^\s]+", na=False)]

    def extract_value_and_currency(value):
        match = re.search(r"(\d+\.\d+)\s+([^\s]+)", value)
        if match:
            numeric_value = float(match.group(1))
            currency = match.group(2)
            return numeric_value, currency
        return -1, -1

    df[["value", "unitValue"]] = df["value"].apply(
        lambda p: pd.Series(extract_value_and_currency(p))
    )

    return df
