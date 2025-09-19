import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change to your MySQL username
        password="1234", # change to your MySQL password
        database="test_db"   # change to your DB name
    )
