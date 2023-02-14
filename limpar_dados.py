import json
import requests

app_key = "2999342667321"
app_secret = "337f2cb08516d060a37c47243b91d20f"

def excluir_ajuste_estoque(id_ajuste):
    """List todos os produtos da base. Coleta a tag "codigo_produto"

    params:
        - None
        
    return:
        - list: codigo_descricao"""
    #=============== Listas =================#
    url = "https://app.omie.com.br/api/v1/estoque/ajuste/"
    payload = json.dumps({
                            "call": "ExcluirAjusteEstoque",
                            "app_key": app_key,
                            "app_secret": app_secret,
                            "param":[
                                        {
                                            "id_ajuste": id_ajuste
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(f"excluir_ajuste_estoque: {response}")


def listar_ajuste_estoque():
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
        url = "https://app.omie.com.br/api/v1/estoque/ajuste/"
        payload = json.dumps({
                                "call": "ListarAjusteEstoque",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
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
        print(len(ajuste_estoque_lista))
        for ajuste in ajuste_estoque_lista:            
            id_ajuste =  ajuste["id_ajuste"]
            print(f"id_ajuste: {id_ajuste}")
            excluir_ajuste_estoque(id_ajuste)
        pagina += 1
        total_de_paginas = response["total_de_paginas"]

def excluir_pedido_venda(codigo_pedido):
    """Exlui os pedidos de venda da base

    params:
        - string: codigo_pedido
        
    return:
        - None"""       

    url = "https://app.omie.com.br/api/v1/produtos/pedido/"
    payload = json.dumps({
                            "call": "ExcluirPedido",
                            "app_key": app_key,
                            "app_secret": app_secret,
                            "param":[
                                        {
                                            "codigo_pedido": codigo_pedido
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(f"excluir_pedido_venda: {response}")

def listar_pedido_vendas():
    """List todos os pedidos de venda da base.

    params:
        - None
        
    return:
        - None"""
    total_de_paginas = 1
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/produtos/pedido/"
        payload = json.dumps({
                                "call": "ListarPedidos",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "apenas_importado_api": "S"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        pedido_venda_produto = response["pedido_venda_produto"]
        print(len(pedido_venda_produto))
        for pedido in pedido_venda_produto:
            cabecalho = pedido["cabecalho"]
            codigo_pedido = cabecalho["codigo_pedido"]
            excluir_pedido_venda(codigo_pedido)
        pagina += 1
        total_de_paginas = int(response["total_de_paginas"])

#listar_ajuste_estoque()
listar_pedido_vendas()
