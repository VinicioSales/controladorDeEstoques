import json
import requests
from datetime import datetime
from config.credenciais import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]

#NOTE - incluir_ajuste_estoque
def incluir_ajuste_estoque(codigo_pesquisa, quan, tipo, valor, obs, codigo_local_estoque):
    """Inclui um ajuste de estoque

    param:
        - string: codigo_pesquisa
        - int: quan
        - string: tipo
        - float: valor
        - string: obs
        - string: codigo_local_estoque
    """
    data = datetime.now()
    data = data.strftime("%d/%m/%Y")    
    url = "https://app.omie.com.br/api/v1/estoque/ajuste/"
    payload = json.dumps({
                            "call": "IncluirAjusteEstoque",
                            "app_key": app_key,
                            "app_secret": app_secret,
                            "param":[
                                        {
                                            "codigo_local_estoque": codigo_local_estoque,
                                            "id_prod": codigo_pesquisa,
                                            "data": data,
                                            "quan": quan,
                                            "origem": "AJU",
                                            "tipo": tipo,
                                            "motivo": "INV",
                                            "valor": valor,
                                            "obs": obs
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(f"IncluirAjusteEstoque: {response}")
    if "descricao_status" in str(response):
        descricao_status = response["descricao_status"]
    if "faultstring" in str(response):
        descricao_status = response['faultstring']
    if "id_movest" in str(response):
        id_movest = response["id_movest"]
    else:
        id_movest = "ERRO"
    if "id_ajuste" in str(response):
        id_ajuste = response["id_ajuste"]
    else:
        id_ajuste = "ERRO"
    return descricao_status, id_movest, id_ajuste

#NOTE - listar_local_estoque
def listar_local_estoque():
    """Lista todos os locais de estoque
    
    param:
        - none"""
    locais_estoque = []
    total_de_paginas = 1
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/estoque/local/"
        payload = json.dumps({
                                "call": "ListarLocaisEstoque",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "nPagina": pagina,
                                                "nRegPorPagina": 500
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        locaisEncontrados = response["locaisEncontrados"]
        for estoque in locaisEncontrados:
            codigo_local_estoque = estoque["codigo_local_estoque"]
            descricao = estoque["descricao"]
            locais_estoque.append(f"{descricao} - {codigo_local_estoque}")
        pagina += 1
    return locais_estoque