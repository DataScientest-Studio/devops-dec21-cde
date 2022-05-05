from fastapi import FastAPI

api = FastAPI(title="Mon API pour les DEC21 CDE")

# method: GET, POST, DELETE, PUT, PATCH, HEAD, OPTIONS, ...
# GET /users
# GET /users/{user_id}
# POST /users
# PUT /users/{user_id}
# DELETE /users/{user_id}

# url : http(s):// + mon_domaine.com + /mon/point/de/terminaison


@api.get("/")
def get_index():
    return {
        "hello": "world"
    }


@api.delete("/mon_delete")
def ma_fonction():
    """Cette fonction ne fait rien du tout. C'est juste un exemple
    """
    return {
        "Ceci est": "un delete un peu différent"
    }


@api.post("/mon_post")
def post_mon_post():
    return {
        "mon_nombre": 123
    }


# VSCode, Pycharms CE, Spyder


@api.get("/status")
def get_status():
    return {
        "status": 1
    }
