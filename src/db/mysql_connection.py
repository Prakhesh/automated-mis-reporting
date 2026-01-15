import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pr@khu7440",
        database="mis_db"
    )
