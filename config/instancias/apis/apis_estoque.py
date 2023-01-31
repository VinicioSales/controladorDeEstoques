import json
import requests
from datetime import datetime
from datetime import date
from config.credenciais import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]

#NOTE - incluir_ajuste_estoque
def incluir_ajuste_estoque(codigo_produto, quantidade_itens, tipo, valor_unitario, obs, codigo_local_estoque):
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
                                            "id_prod": codigo_produto,
                                            "data": data,
                                            "quan": quantidade_itens,
                                            "origem": "AJU",
                                            "tipo": tipo,
                                            "motivo": "INV",
                                            "valor": valor_unitario,
                                            "obs": obs
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
            locais_estoque.append(f"{descricao} | {codigo_local_estoque}")
        pagina += 1
        total_de_paginas = int(response["nPagina"])
    return locais_estoque

def diferenca_quantidade_estoque_produto(codigo_local_estoque):
    #NOTE - diferenca_quantidade_estoque_produto
    """Busca os movimentos um estoque específico
    
    param:
        - string: codigo_local_estoque
    
    return:
        - int: total_estoque
    """
    with open(f"config/arquivos/quant_diferenca_estoque.txt", "w") as arquivo:
        arquivo.write("")
    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m/%Y")
    total_de_paginas = 1
    pagina = 1
    lista_produtos = []
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/estoque/movestoque/"
        payload = json.dumps({
                                "call": "ListarMovimentos",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 20,
                                                "codigo_local_estoque": codigo_local_estoque,
                                                "apenas_importado_api": "S",
                                                "data_inicial": data_atual,
                                                "data_final": data_atual,
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
            cCodigo = cadastro["cCodigo"]
            movimentos = cadastro["movimentos"]            
            for movimento in movimentos:                
                entradas = int(movimento["nQtdeEntradas"])
                saidas = int(movimento["nQtdeSaidas"])
                quant_nao_retornados = entradas - saidas                
                with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
                    lista_produtos = arquivo.readlines()
                for linha_lista_produtos in lista_produtos:
                    linha_lista_produtos = linha_lista_produtos.split("|")
                    cod_produto = linha_lista_produtos[0]
                    try:
                        cod_produto = cod_produto.replace(" ", "")
                    except:
                        pass
                    if cCodigo == cod_produto:
                        nome_produto = linha_lista_produtos[1]
                        nome_produto_aux = nome_produto.replace(" ", "")
                        nome_produto_aux = nome_produto_aux.replace("\n", "")
                        with open(f"config/arquivos/lista_produtos_ceasa.txt", "r") as arquivo:
                            lista_produtos_ceasa = arquivo.readlines()
                        for linha_lista_ceasa in lista_produtos_ceasa:
                            linha_lista_ceasa = linha_lista_ceasa.split("|")
                            nome_produto_ceasa = linha_lista_ceasa[0]
                            nome_produto_ceasa = nome_produto_ceasa.replace(" ", "")
                            if nome_produto_ceasa == nome_produto_aux:
                                quant_ceasa = linha_lista_ceasa[2]
                                quant_ceasa = quant_ceasa.replace(" ", "")
                                quant_ceasa = int(quant_ceasa.replace("\n", ""))
                                quant_nao_retornados = quant_nao_retornados - quant_ceasa
                        with open("config/arquivos/quant_diferenca_estoque.txt", "r") as arquivo:
                            quant_diferenca_estoque = arquivo.readlines()
                            nome_produto = nome_produto.replace("\n", "")
                            print(f"nome_produto: {nome_produto} - quant_nao_retornados: {quant_nao_retornados}")
                        quant_diferenca_estoque.append(f"{nome_produto} | {quant_nao_retornados}\n")
                        with open("config/arquivos/quant_diferenca_estoque.txt", "w") as arquivo:
                            arquivo.writelines(quant_diferenca_estoque)         
        pagina += 1
        total_de_paginas = int(response["total_de_paginas"])
    total_estoque = 0
    with open("config/arquivos/quant_diferenca_estoque.txt", "r") as arquivo:
        quant_diferenca_estoque = arquivo.readlines()
    for linha_dif_estoque in quant_diferenca_estoque:
        linha_dif_estoque = linha_dif_estoque.split("|")
        quant_dif_estoque = int(linha_dif_estoque[1])
        total_estoque += quant_dif_estoque
    return total_estoque

