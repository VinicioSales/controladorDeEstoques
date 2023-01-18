import json
import requests
from config.credenciais.database import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]

def listar_projetos():
    """
    Lista os projetos
    param: - None
    return: - list: lista_projetos
    """

    lista_projetos = []
    total_de_paginas = 1   
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/projetos/"        
        payload = json.dumps({
                                "call": "ListarProjetos",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "apenas_importado_api": "N"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        cadastro = response["cadastro"]
        for projeto in cadastro:
            nome = projeto["nome"]
            codigo = projeto["codigo"]
            lista_projetos.append(f"{nome} - {codigo}")
        pagina += 1
        return lista_projetos