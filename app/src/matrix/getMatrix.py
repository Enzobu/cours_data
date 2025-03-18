import pandas as pd  # type: ignore
import json

from db.getDataFromDb import getDataFromDb
from db.flushMatrix import flushMatrix

def getMatrix():
    data = getDataFromDb('clean_data_cost_of_life')
    data_crime_index = getDataFromDb('data_crime_index')

    df = pd.DataFrame(data, columns=['id', 'country', 'description', 'price', 'unitPrice'])
    print("Données brutes :")
    print(df.head())

    df_crime_index = pd.DataFrame(data_crime_index, columns=['id', 'country', 'crime_index'])
    print("Données crime index :")
    print(df_crime_index.head())

    with open("src/matrix/mappedColumn.json", "r") as f:
        column_mapping = json.load(f)

    column_mapping = {key.strip().lower(): value for key, value in column_mapping.items()}

    df["description"] = df["description"].str.strip().str.lower()

    df["column_name"] = df["description"].map(column_mapping)

    unmapped_descriptions = df[df["column_name"].isnull()]["description"].unique()
    if len(unmapped_descriptions) > 0:
        print("Descriptions non mappées :")
        print(unmapped_descriptions)

    df = df.dropna(subset=["column_name"])

    if df.duplicated(subset=["country", "column_name"]).any():
        print("Des doublons ont été trouvés, résolution par agrégation...")
        df = df.groupby(["country", "column_name"], as_index=False)["price"].mean()

    matrix = df.pivot(index="country", columns="column_name", values="price").reset_index()

    matrix = matrix.fillna(0)

    matrix = matrix.merge(df_crime_index[['country', 'crime_index']], on='country', how='left')

    matrix['crime_index'] = matrix['crime_index'].fillna(0)

    matrix['crime_index'] = pd.to_numeric(matrix['crime_index'], errors='coerce')

    matrix['crime_index'] = matrix['crime_index'].fillna(0)

    matrix['crime_index'] = matrix['crime_index'] / 100

    numeric_columns = matrix.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        min_value = matrix[col].min()
        max_value = matrix[col].max()
        if max_value > min_value:
            matrix[col] = (matrix[col] - min_value) / (max_value - min_value)
        else:
            matrix[col] = 0

    print("Matrice finale normalisée :")
    print(matrix)

    flushMatrix(matrix)
