import json
import requests
from config.credenciais.database import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]

#NOTE - pesquisar_produto
def pesquisar_produto_func(codigo_pesquisa):    
    #=============== Listas =================#
    codigo_lista = []
    cfop_lista = []
    codigo_produto_lista = []
    descricao_lista = []
    ncm_lista = []
    unidade_lista = []
    valor_unitario_lista = []
    url = "https://app.omie.com.br/api/v1/geral/produtos/"
    payload = json.dumps({
                            "call": "ListarProdutos",
                            "app_key": app_key,
                            "app_secret": app_secret,
                            "param":[
                                        {
                                            "pagina": 1,
                                            "registros_por_pagina": 500,
                                            "apenas_importado_api": "N",
                                            "filtrar_apenas_omiepdv": "N"
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()  
    #==================== COLETANDO DADOS ==================#      
    produto_servico_cadastro = response["produto_servico_cadastro"]
    for produto in produto_servico_cadastro:
        codigo_lista.append(produto["codigo"])            
        cfop_lista.append(produto["cfop"])
        codigo_produto_lista.append(produto["codigo_produto"])
        descricao_lista.append(produto["descricao"])
        ncm_lista.append(produto["ncm"])
        unidade_lista.append(produto["unidade"])
        valor_unitario_lista.append(produto["valor_unitario"])
    for codigo, cfop, codigo_produto, descricao, ncm, unidade, valor_unitario in zip(codigo_lista,\
        cfop_lista, codigo_produto_lista, descricao_lista, ncm_lista, unidade_lista, valor_unitario_lista):
        if codigo == codigo_pesquisa:
            break
    return cfop, codigo_produto, descricao, ncm, unidade, valor_unitario

#NOTE - listar_produtos
def listar_produtos():
    """List todos os produtos da base

    params:
        - None
        
    return:
        - codigo_descricao"""
    #=============== Listas =================#
    codigo_descricao = []
    total_de_paginas = 1
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/produtos/"
        payload = json.dumps({
                                "call": "ListarProdutos",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "apenas_importado_api": "N",
                                                "filtrar_apenas_omiepdv": "N"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()            
        total_de_paginas = int(response['total_de_paginas'])
        produto_servico_cadastro = response["produto_servico_cadastro"]
        for produto in produto_servico_cadastro:
            codigo_descricao.append(f'{produto["codigo"]} - {produto["descricao"]}')
        pagina += 1
    return codigo_descricao

#NOTE - listar_produtos_codigo_produto
def listar_produtos_codigo_produto():
    """List todos os produtos da base. Coleta a tag "codigo_produto"

    params:
        - None
        
    return:
        - list: codigo_descricao"""
    #=============== Listas =================#
    codigo_descricao = []
    total_de_paginas = 1
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/produtos/"
        payload = json.dumps({
                                "call": "ListarProdutos",
                                "app_key": "2999342667321",
                                "app_secret": "337f2cb08516d060a37c47243b91d20f",
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "apenas_importado_api": "N",
                                                "filtrar_apenas_omiepdv": "N"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()            
        total_de_paginas = int(response['total_de_paginas'])
        produto_servico_cadastro = response["produto_servico_cadastro"]
        for produto in produto_servico_cadastro:
            codigo_descricao.append(f'{produto["codigo_produto"]} * {produto["descricao"]}')
        pagina += 1
    return codigo_descricao

#NOTE - relatorio_quant_diferenca_func
def relatorio_quant_diferenca_func(lista_nCodProd, lista_quant_diferenca):
    """Busca a o nome do produto pelo codigo do produto
    
    param:
        - list: lista_nCodProd
        - list: lista_quant_diferenca
    
    return:
        - list: relatorio_quant_diferenca"""
    relatorio_quant_diferenca = []
    codigo_descricao = listar_produtos_codigo_produto()
    for codigo_produto, quant_diferenca in zip(lista_nCodProd, lista_quant_diferenca):
        for codigo_descricao_item in codigo_descricao:
            if str(codigo_produto) in str(codigo_descricao_item):
                codigo_descricao_item = codigo_descricao_item.split("*")
                nome_produto = codigo_descricao_item[1]
                relatorio_quant_diferenca.append(f"{nome_produto} * {quant_diferenca}")
    return relatorio_quant_diferenca
