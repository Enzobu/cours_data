from db.getConn import getConn

def getDataFromDb(table):
    conn = getConn()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data