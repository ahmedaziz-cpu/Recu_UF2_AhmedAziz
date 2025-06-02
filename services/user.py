import connexion.db
from schemas.user_sch import  user_schema
from connexion.db import connection_db


def get_user_by_id(user_id: int) -> dict | None:
    conn = connexion.db.connection_db()
    cursor = conn.cursor()
    try:
        sql = "SELECT id, nom, cognom, email, curs, ano, calle FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()
        return user_schema(row) if row else None
    finally:
        cursor.close()
        conn.close()

from connexion.db import connection_db
from schemas.user_sch import user_schema


def create_user(nom: str, email: str, cognom: str, descripcio: str, curs: str, ano: int, calle: str, cp: int, password: str) -> dict:
    conn = connection_db()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO users (nom, cognom, email, descripcio, curs, ano, calle, cp, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id, nom, email"
        cursor.execute(sql, (nom, cognom, email, descripcio, curs, ano, calle, cp, password))
        new_row = cursor.fetchone()
        conn.commit()
        return user_schema(new_row)
    finally:
        cursor.close()
        conn.close()

