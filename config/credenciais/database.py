import os
from dotenv import load_dotenv

load_dotenv()

def database_infos_func():
    database_infos = {
        "app_key": "2999342667321",
        "app_secret": "337f2cb08516d060a37c47243b91d20f",
        "codigo_conta_corrente": "6873271998",
        "estoque_box": "6900976395",
        "codigo_local_estoque_galpao": "6873272006",
        "app_key_parceiro": os.getenv("APP_KEY_PARCEIRO"),
        "app_secret_parceiro": os.getenv("APP_SECRET_PARCEIRO")
    }
    return database_infos