from db.getConn import getConn

def flush(dict):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in dict["df"].iterrows():
        table = dict["table"]

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
