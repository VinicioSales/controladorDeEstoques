import json
import requests
#from config.credenciais.database import database_infos_func
from unidecode import unidecode

"""database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]"""
app_key = "3167947832049"
app_secret = "1d8e4d03c432a464ef95cc920ae34026"

def get_cod_projeto(nome_produto):
    #NOTE - get_cod_projeto
    """Busca o código do projeto
    
    param:
        - str: nome_produto
    
    retun:
        - str: codigo_projeto"""
    nome_produto = nome_produto.replace(" ", "")
    nome_produto = unidecode(nome_produto).upper()
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
                                                "registros_por_pagina": 500
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        total_de_paginas = int(response["total_de_paginas"])
        cadastro = response["cadastro"]
        for projeto in cadastro:
            nome = projeto["nome"]
            nome = nome.replace(" ", "")
            if unidecode(nome).upper() == nome_produto:
                codigo = projeto["codigo"]
                break
        pagina += 1
        
    return codigo
