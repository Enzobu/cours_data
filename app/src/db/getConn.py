import mysql.connector # type: ignore

def getConn():
    return mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='cours_data',
        port=3306
    )