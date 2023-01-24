import json
import requests
import random
from datetime import datetime
from config.credenciais.database import database_infos_func

database_infos = database_infos_func()
app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]
codigo_conta_corrente = database_infos["codigo_conta_corrente"]

def incluir_pedido_venda(codigo_produto, codigo_cliente, data_previsao, cfop, descricao, ncm, unidade, valor_produto, quantidade_diferenca):
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
                                            "det": [
                                                {
                                                "ide": {
                                                    "codigo_item_integracao": "4422421"
                                                },
                                                "produto": {
                                                    "cfop": cfop,
                                                    "codigo_produto": codigo_produto,
                                                    "descricao": descricao,
                                                    "ncm": ncm,
                                                    "quantidade": quantidade_diferenca,
                                                    "unidade": unidade,
                                                    "valor_unitario": valor_produto
                                                }
                                                }
                                            ],
                                            "informacoes_adicionais": {
                                                "codigo_categoria": "1.01.01",
                                                "codigo_conta_corrente": codigo_conta_corrente,
                                                "consumidor_final": "",
                                                "enviar_email": "N"
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
    #================== COLETANDO DADOS ====================#
    if "descricao_status" in str(response):
        descricao_status = response["descricao_status"]
        codigo_pedido = response["codigo_pedido"]
        numero_pedido = response["numero_pedido"]
    if "faultstring" in str(response):
        descricao_status = response['faultstring']
        codigo_pedido = ''
        numero_pedido = ''
    return descricao_status, codigo_pedido, numero_pedido
