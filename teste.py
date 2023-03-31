import json
import requests
from datetime import datetime
import random

def incluir_pedido_venda_lot(lista_det, codigo_cliente, data_vencimento, departamentos):
    """
    Função para incluir um pedido através da API Omie.
    
    Args:
        lista_det (list)
        codigo_cliente (str): Código do cliente
        data_vencimento (str): Data de previsão de entrega no formato "dd/mm/yyyy"
        
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
                            "app_key": '3332558667438',
                            "app_secret": '016c1a606262cd6e6a308c2dc44a885d ',
                            "param":[
                                        {
                                            "cabecalho": {
                                                "codigo_cliente": codigo_cliente,
                                                "codigo_pedido_integracao": codigo_pedido_integracao,
                                                "data_previsao": data_vencimento,
                                                "etapa": "10"
                                            },
                                            "det": lista_det,

                                            "informacoes_adicionais": {
                                                "codigo_categoria": "1.01.01",
                                                "codigo_conta_corrente": 4572119672,
                                                "consumidor_final": "",
                                                "enviar_email": "N"
                                            },
                                            "departamentos": departamentos
                                        }
                                    ]
                        })
    headers ={
                "Content-Type": "application/json"
            }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(response)

dict_det = {
                        "ide": {
                                "codigo_item_integracao": "4422421"
                        },
                        "produto": {
                                "cfop": '',
                                "codigo_produto": 4572119846,
                                "descricao": 'Game Resident Evil 6 - PS3',
                                "ncm": '9504.10.99',
                                "quantidade": 2,
                                "unidade": "UN",
                                "valor_unitario": "1",
                                "codigo_local_estoque": "4572176967"
                            }
                    }
lista_det = []
lista_det.append(dict_det)

incluir_pedido_venda_lot(lista_det, 4572119681, '20/02/2023', "departamentos")