
def user_schema(user) -> dict:
    response = {
        "id":user[0],
        "nom":user[1],
        "cognom":user[2],
        "email":user[3],
        "descripcio":user[4],
        "curs":user[5],
        "ano":user[6],
        "calle":user[7],
        "cp":user[8],
        "password":user[9]
    }
    return response

def users_schema(users) -> list[dict]:
    response = [user_schema(user) for user in users]
    return response
