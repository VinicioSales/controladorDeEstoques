import os
from dotenv import load_dotenv

load_dotenv()

def database_infos_func():
    database_infos = {
        "app_key": "app_key",
        "app_secret": "33app_secret7f2cb08516d060a37c47243b91d20f",
        "codigo_conta_corrente": "codigo_conta_corrente",
        "estoque_box": "estoque_box",
        "codigo_local_estoque_galpao": "codigo_local_estoque_galpao",
        "app_key_parceiro": os.getenv("APP_KEY_PARCEIRO"),
        "app_secret_parceiro": os.getenv("APP_SECRET_PARCEIRO")
    }
    return database_infos