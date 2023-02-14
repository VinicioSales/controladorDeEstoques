import json
import requests
from config.credenciais.database import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]

#NOTE - listar_departamentos
def listar_departamentos():
    """List todos os produtos da base

    params:
        - None
        
    return:
        - lista_departamentos"""
    #=============== Listas =================#
    lista_departamentos = []
    total_de_paginas = 1
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/departamentos/"
        payload = json.dumps({
                                "call": "ListarDepartamentos",
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
        total_de_paginas = int(response['total_de_paginas'])
        departamentos = response["departamentos"]
        for departamento in departamentos:
            lista_departamentos.append(f'{departamento["codigo"]} | {departamento["descricao"]}\n')
        pagina += 1
    return lista_departamentos