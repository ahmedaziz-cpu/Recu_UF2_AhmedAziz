import connexion.db
from schemas.user_sch import users_schema, user_schema

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