import json
import requests
from datetime import datetime
from datetime import date
from config.credenciais import database_infos_func
from unidecode import unidecode

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]
app_key_parceiro = database_infos["app_key_parceiro"]
app_secret_parceiro = database_infos["app_secret_parceiro"]

def get_cod_cliente(nome_cliente):
    #NOTE - get_cod_cliente
    """
    Retorna o código do cliente a partir do nome fornecido.
    Parâmetros:
    nome_cliente (str): Nome do cliente aser buscado.
    Retorna:
    str: codigo_cliente_omie
    str: razao_social
    """

    nome_cliente = unidecode(nome_cliente).lower()
    pagina = 1
    total_de_paginas = 1
    codigo_cliente_omie = ""
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/clientes/"
        payload = json.dumps({
                                "call": "ListarClientes",
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
        total_de_paginas = response["total_de_paginas"]
        clientes_cadastro = response["clientes_cadastro"]
        for cliente in clientes_cadastro:
            razao_social = unidecode(cliente["razao_social"]).lower()
            nome_fantasia = unidecode(cliente["nome_fantasia"]).lower()
            if razao_social == nome_cliente or nome_fantasia == nome_cliente:
                codigo_cliente_omie = cliente["codigo_cliente_omie"]
                break
        if codigo_cliente_omie != "":
            break
        pagina += 1
    
    return codigo_cliente_omie, razao_social

def listar_clientes():
    #NOTE - get_cod_cliente
    """
    Retorna uma lista de todos os clientes.
    Retorna:
    str: lista_clientes
    """
    lista_clientes = []
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/clientes/"
        payload = json.dumps({
                                "call": "ListarClientes",
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
        clientes_cadastro = response["clientes_cadastro"]
        for cliente in clientes_cadastro:
            codigo_cliente_omie = cliente["codigo_cliente_omie"]
            razao_social = cliente["razao_social"]
            lista_clientes.append(f"{codigo_cliente_omie} | {razao_social}\n")
        return lista_clientes

def consultar_cliente_inativo():
    #NOTE - consultar_cliente_inativo
    """
    Consulta o status de inatividade de um cliente na API Omie.

    Returns:
        Um valor booleano indicando se o cliente está inativo ou não.
    """
    url = "https://app.omie.com.br/api/v1/geral/clientes/"
    payload = json.dumps({
                            "call": "ConsultarCliente",
                            "app_key": app_key_parceiro,
                            "app_secret": app_secret_parceiro,
                            "param":[
                                        {
                                            "codigo_cliente_omie": "7311700214"
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    inativo = response["inativo"]

    return inativo