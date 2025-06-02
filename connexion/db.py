####conn
import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="fastapiexamen",
        user="user",
        password="pass",
        host="localhost",
        port="3456"
    )
    print("Connexió establerta correctament")

    return conn


