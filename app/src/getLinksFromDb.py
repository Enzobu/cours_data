import mysql.connector # type: ignore

def getLinksFromDb():
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='cours_data',
        port=3306
    )
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