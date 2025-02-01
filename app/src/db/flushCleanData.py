from db.getConn import getConn

def flushCostOfLifeData(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        description = row['description']
        value = row['value']
        unitValue = row['unitValue']
        sql = "INSERT INTO clean_data_cost_of_life (country, description, price, unitPrice) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (country, description, value, unitValue))

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_cost_of_life.")

def flushCrimeData(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        description = row['description']
        value = row['value']
        unit = row['unit']
        sql = "INSERT INTO clean_data_crime (country, description, value, unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (country, description, value, unit))

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_crime.")

def flushHealthCareData(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        description = row['description']
        value = row['value']
        unit = row['unit']
        sql = "INSERT INTO clean_data_health_care (country, description, value, unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (country, description, value, unit))

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_health_care.")

def flushPollutionData(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        description = row['description']
        value = row['value']
        unit = row['unit']
        sql = "INSERT INTO clean_data_pollution (country, description, value, unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (country, description, value, unit))

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_pollution.")

def flushQualityOfLifeData(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        description = row['description']
        value = row['value']
        unit = row['unit']
        sql = "INSERT INTO clean_data_quality_of_life (country, description, value, unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (country, description, value, unit))

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_quality_of_life.")