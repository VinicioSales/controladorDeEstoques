import json
import requests
#from config.credenciais.database import database_infos_func
from unidecode import unidecode
from datetime import datetime

"""database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]"""
app_key = "3167947832049"
app_secret = "1d8e4d03c432a464ef95cc920ae34026"

def incluir_ajuste_estoque_lote(codigo_projeto, quantidade_itens, tipo, valor_unitario, obs, codigo_local_estoque):
    #NOTE - incluir_ajuste_estoque_lote
    """Inclui um ajuste de estoque

    param:
        - string: codigo_projeto
        - int: quan
        - string: tipo
        - float: valor_unitario
        - string: obs
        - string: codigo_local_estoque
        - string: estoque_destino
    
    retun:
        - string: descricao_status
        - string: id_movest
        - string: id_ajuste
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
                                            "id_prod": codigo_projeto,
                                            "data": data,
                                            "quan": quantidade_itens,
                                            "origem": "AJU",
                                            "tipo": tipo,
                                            "motivo": "INV",
                                            "valor": valor_unitario,
                                            "obs": obs
                                            #"codigo_local_estoque_destino": estoque_destino
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(f"incluir_ajuste_estoque: {response}")
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