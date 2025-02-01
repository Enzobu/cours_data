from db.getConn import getConn

def getLinksFromDb():
    conn = getConn()
    cursor = conn.cursor()

    urls = []

    try:
        cursor.execute("SELECT country_link FROM links")
        data = cursor.fetchall()
        for row in data:
            urls.append(row[0])
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
    finally:
        cursor.close()
        conn.close()

    return urls