import json
import requests
import random
from datetime import datetime

app_key = "2999342667321"
app_secret =  "337f2cb08516d060a37c47243b91d20f"

def incluir_pedido_venda(lista_dat, codigo_cliente, data_previsao, codigo_projeto):
    """
    Função para incluir um pedido através da API Omie.
    
    Args:
        codigo_produto (str): Código do produto
        codigo_cliente (str): Código do cliente
        data_previsao (str): Data de previsão de entrega no formato "dd/mm/yyyy"
        cfop (str): Código Fiscal de Operações e Prestações
        descricao (str): Descrição do produto
        ncm (str): Código Nacional de Mercadorias
        unidade (str): Unidade de medida do produto
        valor_produto (float): Valor do produto
        quantidade_diferenca (int): Quantidade de diferença
        codigo_conta_corrente (str): Código da conta corrente
        codigo_projeto (str): Código do projeto
        
    Returns:
        Tuple: (descricao_status (str), codigo_pedido (str), numero_pedido (str))
    """
    randomlist = random.sample(range(1, 12), 8)
    randomlist = str(randomlist)
    aleatorio = randomlist.replace(",","")
    aleatorio = aleatorio.replace(" ","")
    aleatorio = aleatorio.replace("[","")
    codigo_pedido_integracao = aleatorio.replace("]","")
    data = datetime.now()
    data = data.strftime("%d/%m/%Y")
    url = "https://app.omie.com.br/api/v1/produtos/pedido/"
    payload = json.dumps({
                            "call": "IncluirPedido",
                            "app_key": app_key,
                            "app_secret": app_secret,
                            "param":[
                                        {
                                            "cabecalho": {
                                                "codigo_cliente": codigo_cliente,
                                                "codigo_pedido_integracao": codigo_pedido_integracao,
                                                "data_previsao": data_previsao,
                                                "etapa": "10"
                                            },
                                            "det": lista_det,

                                            "informacoes_adicionais": {
                                                "codigo_categoria": "1.01.01",
                                                "codigo_conta_corrente": 6873271998,
                                                "consumidor_final": "",
                                                "enviar_email": "N",
                                                "codProj": codigo_projeto
                                            }
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(f"IncluirPedido: {response}")

lista_det = [
        {
        "ide": {
            "codigo_item_integracao": "4422421"
        },
        "produto": {
            "cfop": "5.102",
            "codigo_produto": "6873272180",
            "descricao": "descricao",
            "ncm": "",
            "quantidade": "1",
            "unidade": "UN",
            "valor_unitario": "1"
        }
        },

        {
        "ide": {
            "codigo_item_integracao": "4422421"
        },
        "produto": {
            "cfop": "5.102",
            "codigo_produto": "6873272180",
            "descricao": "descricao",
            "ncm": "",
            "quantidade": "2",
            "unidade": "UN",
            "valor_unitario": "2"
        }
        }
]
incluir_pedido_venda(lista_det, "6873272007", "20/02/2023", "6893342043")