import json
import requests

def pesquisar_produto_func(nome_produto):
    """
    Função para pesquisar um produto em específico a partir de seu código.

    Essa função faz uso de uma requisição à API do Omie, passando como parâmetro um código de pesquisa. A partir da resposta da requisição, é feito o tratamento dos dados e retornado os seguintes valores: CFOP, código do produto, descrição, NCM, unidade e valor unitário.

    Parâmetros:
    nome_produto (str): Nome do produto a ser pesquisado

    Retorna:
    Tuple (cfop: str, codigo_produto: str, descricao: str, ncm: str, unidade: str, valor_unitario: float)
    """   
    #=============== Listas =================#
    nome_produto = nome_produto.replace(" ", "")
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
                            "app_key": "2999342667321",
                            "app_secret": "337f2cb08516d060a37c47243b91d20f",
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
        print(f"nome_produto: {nome_produto} - descricao: {descricao}")
        if descricao == nome_produto:
            break
    return cfop, codigo_produto, descricao, ncm, unidade, valor_unitario

cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_func("Milho")