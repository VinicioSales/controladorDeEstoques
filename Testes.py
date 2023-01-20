import json
import requests
from datetime import date

def diferenca_quantidade_estoque(codigo_local_estoque):
    """Busca os ajuste de um estoque específico
    
    param:
        - string: codigo_local_estoque
    
    return:
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
        
diferenca_quantidade_estoque("6891101179")