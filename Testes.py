import json
import requests
import time
app_key = "2999342667321",
app_secret =  "337f2cb08516d060a37c47243b91d20f"

def diferenca_quantidade():
    """Busca a diferença de itens na movimentação de estoque
    
    param:
        - none
    
    return:
        - list: lista_nCodProd
        - list: lista_quant_diferenca"""
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
                                                "data_inicial": "19/01/2023",
                                                "data_final": "19/01/2023"
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
    print(f"lista_nCodProd: {lista_nCodProd}")
    print(f"lista_quant_diferenca: {lista_quant_diferenca}")
    return lista_nCodProd, lista_quant_diferenca

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
            codigo_descricao.append(f'{produto["codigo_produto"]} - {produto["descricao"]}')
        pagina += 1
    return codigo_descricao

def relatorio_quant_diferenca_func(lista_nCodProd, lista_quant_diferenca):
    """Busca a o nome do produto pelo codigo do produto
    
    param:
        - list: lista_nCodProd
        - list: lista_quant_diferenca
    
    return:
        - None"""
    relatorio_quant_diferenca = []
    codigo_descricao = listar_produtos_codigo_produto()
    for codigo_produto, quant_diferenca in zip(lista_nCodProd, lista_quant_diferenca):
        for codigo_descricao_item in codigo_descricao:
            if str(codigo_produto) in str(codigo_descricao_item):
                codigo_descricao_item = codigo_descricao_item.split("-")
                nome_produto = codigo_descricao_item[1]
                relatorio_quant_diferenca.append(f"{nome_produto} - {quant_diferenca}")


lista_nCodProd, lista_quant_diferenca = diferenca_quantidade()
relatorio_quant_diferenca_func(lista_nCodProd, lista_quant_diferenca)
