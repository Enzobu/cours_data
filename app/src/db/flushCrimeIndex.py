from db.getConn import getConn

def flushCrimeIndex(df):
    conn = getConn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        country = row['country']
        crime_index = row['crime_index']
        sql = "INSERT INTO data_crime_index (country, crime_index) VALUES (%s, %s)"
        cursor.execute(sql, (country, crime_index))

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Les données ont été nettoyées et insérées dans la table clean_data_cost_of_life.")