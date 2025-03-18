import pandas as pd # type: ignore
import re

from db.getDataFromDb import getDataFromDb

def getCostOfLifeCleanData():
    # Récupération des données
    data = getDataFromDb('data_cost_of_life')

    # Création du DataFrame
    df = pd.DataFrame(data, columns=["id", "country", "description", "value", "unit"])

    # Nettoyage des données
    df = df.dropna()
    df = df.drop_duplicates()

    # Filtrage avec str.contains corrigé (sans groupes de capture)
    df = df[df["value"].str.contains(r"\d+\.\d+\s+\S+", na=False, regex=True)]

    # Extraction des valeurs et unités
    def extract_value_and_currency(value):
        match = re.search(r"(\d+\.\d+)\s+(\S+)", value)
        if match:
            numeric_value = float(match.group(1))
            currency = match.group(2)
            return numeric_value, currency
        return -1, -1

    # Appliquer la transformation
    df[["value", "unitValue"]] = df["value"].apply(
        lambda p: pd.Series(extract_value_and_currency(p))
    )

    return df
