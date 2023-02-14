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
                            "app_key": "2999342667321",
                            "app_secret": "337f2cb08516d060a37c47243b91d20f",
                            "param":[
                                        {
                                            "cabecalho": {
                                                "codigo_cliente": 6873272014,
                                                "codigo_pedido_integracao": codigo_pedido_integracao,
                                                "data_previsao": "20/02/2023",
                                                "etapa": "10"
                                            },
                                            #"det": lista_det,

                                            "informacoes_adicionais": {
                                                "codigo_categoria": "1.01.01",
                                                "codigo_conta_corrente": 6873271998,
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

departamentos = [
        
            {
                "cCodDepto": 6873271996,
                "nPerc": 50,
                "nValor": 50,
                "nValorFixo": "S"
                
            
        },
        
            {
                "cCodDepto": 6873271995,
                "nPerc": 50,
                "nValor": 50,
                "nValorFixo": "S"
                
            
        }

    ]
incluir_pedido_venda_lot("lista_det", "codigo_cliente", "data_vencimento", departamentos)
