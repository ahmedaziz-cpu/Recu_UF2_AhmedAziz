import connexion.db


def delete_user(user_id: int) -> bool:
    conn = connexion.db.connection_db()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM users WHERE id = %s RETURNING id"
        cursor.execute(sql, (user_id,))
        deleted = cursor.fetchone()
        if deleted:
            conn.commit()
            return True
        else:
            conn.rollback()
            return False
    finally:
        cursor.close()
        conn.close()

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


def update_user(user_id: int, cognom: str, calle: str) -> dict | None:
    conn = connexion.db.connection_db()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE users
            SET nom = %s, email = %s
            WHERE id = %s
            RETURNING id, nom, email
        """

        cursor.execute(sql, (cognom, calle, user_id))
        updated_row = cursor.fetchone()
        if updated_row:
            conn.commit()
            return user_schema(updated_row)

        else:
            return None
    finally:
        cursor.close()
        conn.close()
