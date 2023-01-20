import json
import requests
from datetime import datetime
from datetime import date
from config.credenciais import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]

#NOTE - incluir_ajuste_estoque
def incluir_ajuste_estoque(codigo_projeto, quantidade_itens, tipo, valor_unitario, obs, codigo_local_estoque):
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

#NOTE - pesquisar_produto
def pesquisar_produto(codigo_pesquisa):
    """Pesquisa o produto pelo codigo
    
    params:
        - codigo_pesquisa
        
    return:
        - cfop
        - codigo_produto
        - descricao
        - ncm
        - unidade
        - valor_unitario"""
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

#NOTE - diferenca_quantidade
def diferenca_quantidade():
    """Busca a diferença de itens na movimentação de estoque
    
    param:
        - none
    
    return:
        - list: lista_nCodProd
        - list: lista_quant_diferenca"""
    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m/%Y")
    total_de_paginas = 1
    pagina = 1
    lista_nCodProd = []
    lista_quant_diferenca = []
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/estoque/movestoque/"
        payload = json.dumps({
                                "call": "ListarMovimentos",
                                "app_key": "2999342667321",
                                "app_secret": "337f2cb08516d060a37c47243b91d20f",
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "codigo_local_estoque": 0,
                                                "data_inicial": data_atual,
                                                "data_final": data_atual,
                                                "apenas_importado_api": "S"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        cadastros = response["cadastros"]
        for cadastro in cadastros:
            nCodProd = cadastro["nCodProd"]
            lista_nCodProd.append(nCodProd)
            movimentos = cadastro["movimentos"]  
            movimento = movimentos[0]
            nQtdeSaidas = int(movimento["nQtdeSaidas"])
            nQtdeEntradas = int(movimento["nQtdeEntradas"])
            quant_diferenca = nQtdeSaidas - nQtdeEntradas
            lista_quant_diferenca.append(quant_diferenca)
        pagina += 1
    return lista_nCodProd, lista_quant_diferenca

def diferenca_quantidade_estoque(codigo_local_estoque):
    """Busca os ajuste de um estoque específico
    
    param:
        - string: codigo_local_estoque
    
    return:
        - list: produtos_nao_retornados
    """
    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m/%Y")
    total_de_paginas = 1
    pagina = 1
    lista_cod_produtos = []
    lista_quantidade = []
    lista_tipo = []
    produtos_nao_retornados = 0
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/estoque/ajuste/"
        payload = json.dumps({
                                "call": "ListarAjusteEstoque",
                                "app_key": "2999342667321",
                                "app_secret": "337f2cb08516d060a37c47243b91d20f",
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "codigo_local_estoque": codigo_local_estoque,
                                                "data_movimento_de": data_atual,
                                                "data_movimento_ate": data_atual,
                                                "apenas_importado_api": "S"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        ajuste_estoque_lista = response["ajuste_estoque_lista"]
        for ajuste in ajuste_estoque_lista:            
            lista_cod_produtos.append(ajuste["id_prod"])
            lista_tipo.append(ajuste["tipo"])
            quantidade = ajuste["quantidade"]
            if ajuste["tipo"] == "SAI":
                quantidade = f"-{quantidade}"
            lista_quantidade.append(quantidade)
            produtos_nao_retornados += int(quantidade) 
            relatorio = f"{codigo_local_estoque} * {quantidade}" 
            with open("config/arquivos/relatorio_caminhao.txt", "r") as arquivo:
                relatorio_caminhao = arquivo.readlines()
                relatorio_caminhao.append(f"{relatorio}\n")
            with open("config/arquivos/relatorio_caminhao.txt", "w") as arquivo:
                arquivo.writelines(relatorio_caminhao)       
        pagina += 1
        with open("config/arquivos/relatorio_caminhao.txt", "r") as arquivo:
            relatorio_caminhao = arquivo.readlines()
            relatorio_caminhao.append(f"produtos_nao_retornados * {produtos_nao_retornados}\n")
        with open("config/arquivos/relatorio_caminhao.txt", "w") as arquivo:
            arquivo.writelines(relatorio_caminhao)
    return produtos_nao_retornados

