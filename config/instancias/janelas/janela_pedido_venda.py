import customtkinter as ctk
import tkinter
import datetime
from unidecode import unidecode
from PIL import Image
import json
import requests
import random
from config.instancias.apis.apis_vendas import incluir_pedido_venda
from config.instancias.apis.apis_cliente import get_cod_cliente
from config.instancias.apis.apis_projetos import get_cod_projeto
from config.instancias.apis.apis_produtos import pesquisar_produto_nome_func

'''app_key = "2999342667321"
app_secret = "337f2cb08516d060a37c47243b91d20f"
codigo_conta_corrente: "6873271998"
def incluir_pedido_venda(codigo_produto, codigo_cliente, data_previsao, cfop, descricao, ncm, unidade, valor_produto, quantidade_diferenca, codigo_projeto):
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
    data = datetime.datetime.now()
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
                                                "codigo_conta_corrente": "6873271998",
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
def pesquisar_produto_nome_func(nome_produto):
    #NOTE - pesquisar_produto_nome_func
    """
    Função para pesquisar um produto em específico a partir de seu código.

    Essa função faz uso de uma requisição à API do Omie, passando como parâmetro\
    um código de pesquisa. A partir da resposta da requisição, é feito o tratamento\
    dos dados e retornado os seguintes valores: CFOP, código do produto, descrição,\
    NCM, unidade e valor unitário.

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
        if descricao == nome_produto:
            break
    return cfop, codigo_produto, descricao, ncm, unidade, valor_unitario
def get_cod_projeto(nome_produto):
    #NOTE - get_cod_projeto
    """Busca o código do projeto
    
    param:
        - str: nome_produto
    
    retun:
        - str: codigo_projeto"""
    nome_produto = nome_produto.replace(" ", "")
    nome_produto = unidecode(nome_produto).upper()
    total_de_paginas = 1
    pagina = 1
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/projetos/"
        payload = json.dumps({
                                "call": "ListarProjetos",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        total_de_paginas = int(response["total_de_paginas"])
        cadastro = response["cadastro"]
        for projeto in cadastro:
            nome = projeto["nome"]
            nome = nome.replace(" ", "")
            if unidecode(nome).upper() == nome_produto:
                codigo = projeto["codigo"]
                break
        pagina += 1
        
    return codigo
def get_cod_cliente(nome_cliente):
    #NOTE - get_cod_cliente
    """
    Retorna o código do cliente a partir do nome fornecido.
    Parâmetros:
    nome_cliente (str): Nome do cliente aser buscado.
    Retorna:
    str: Código do cliente correspondente ao nome fornecido. Se o cliente não for encontrado, retorna uma string vazia.
    """

    nome_cliente = unidecode(nome_cliente).lower()
    pagina = 1
    total_de_paginas = 1
    codigo_cliente_omie = ""
    while pagina <= total_de_paginas:
        url = "https://app.omie.com.br/api/v1/geral/clientes/"
        payload = json.dumps({
                                "call": "ListarClientes",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "apenas_importado_api": "N"
                                            }
                                        ]
                            })
        headers ={
                    "Content-Type": "application/json"
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        total_de_paginas = response["total_de_paginas"]
        clientes_cadastro = response["clientes_cadastro"]
        for cliente in clientes_cadastro:
            razao_social = unidecode(cliente["razao_social"]).lower()
            if razao_social == nome_cliente:
                codigo_cliente_omie = cliente["codigo_cliente_omie"]
                break
        if codigo_cliente_omie != "":
            break
        pagina += 1
    
    return codigo_cliente_omie
'''

with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
    lista_produtos = arquivo.readlines()
lista_pedidos_venda = []

#SECTION - sub_janela_alerta_preencher_dados
def sub_janela_alerta_preencher_dados():
    #NOTE - sub_janela_alerta_preencher_dados
    """
    Cria uma sub-janela para confirmar a adição de um produto.
    Esta sub-janela é centralizada na tela e tem um label e um botão "Ok".
    Ao clicar no botão "Ok", a sub-janela é fechada.
    """
    sub_janela_confirmar_produtos = ctk.CTkToplevel()
    sub_janela_confirmar_produtos.geometry("300x300")
    sub_janela_confirmar_produtos.update_idletasks()
    x = (sub_janela_confirmar_produtos.winfo_screenwidth() // 2) - (sub_janela_confirmar_produtos.winfo_width() // 2)
    y = (sub_janela_confirmar_produtos.winfo_screenheight() // 2) - (sub_janela_confirmar_produtos.winfo_height() // 2)
    sub_janela_confirmar_produtos.geometry(f"+{x}+{y}")
    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_confirmar_produtos.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_confirmar_produtos,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_confirmar_produtos,
        text="Preencha todos os dados",
        text_color = "#F04A29",
        bg_color="#2b2b2b",
        font=("arial", 18, "bold")
    )
    label_confirmar.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    btn_ok = ctk.CTkButton(
        master=frame_confirmar,
        text="Ok",
        command=ok_btn_func
    )
    btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
#!SECTION

#SECTION - sub_janela_alerta_prod_nao_encontrado
def sub_janela_alerta_prod_nao_encontrado():
    #NOTE - sub_janela_alerta_prod_nao_encontrado
    sub_janela_confirmar_produtos = ctk.CTkToplevel()
    sub_janela_confirmar_produtos.geometry("300x300")
    sub_janela_confirmar_produtos.update_idletasks()
    x = (sub_janela_confirmar_produtos.winfo_screenwidth() // 2) - (sub_janela_confirmar_produtos.winfo_width() // 2)
    y = (sub_janela_confirmar_produtos.winfo_screenheight() // 2) - (sub_janela_confirmar_produtos.winfo_height() // 2)
    sub_janela_confirmar_produtos.geometry(f"+{x}+{y}")    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_confirmar_produtos.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_confirmar_produtos,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_confirmar_produtos,
        text="Produto Não Encontrado!",
        text_color = "#F04A29",
        bg_color="#2b2b2b",
        font=("arial", 18, "bold")
    )
    label_confirmar.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    btn_ok = ctk.CTkButton(
        master=frame_confirmar,
        text="Ok",
        command=ok_btn_func
    )
    btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
#!SECTION

#SECTION - sub_janela_alerta_cliente_nao_encontrado
def sub_janela_alerta_cliente_nao_encontrado():
    #NOTE - sub_janela_alerta_cliente_nao_encontrado
    sub_janela_confirmar_cliente = ctk.CTkToplevel()
    sub_janela_confirmar_cliente.geometry("300x300")
    sub_janela_confirmar_cliente.update_idletasks()
    x = (sub_janela_confirmar_cliente.winfo_screenwidth() // 2) - (sub_janela_confirmar_cliente.winfo_width() // 2)
    y = (sub_janela_confirmar_cliente.winfo_screenheight() // 2) - (sub_janela_confirmar_cliente.winfo_height() // 2)
    sub_janela_confirmar_cliente.geometry(f"+{x}+{y}")    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_confirmar_cliente.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_confirmar_cliente,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_confirmar_cliente,
        text="Cliente Não Encontrado!",
        text_color = "#F04A29",
        bg_color="#2b2b2b",
        font=("arial", 18, "bold")
    )
    label_confirmar.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    btn_ok = ctk.CTkButton(
        master=frame_confirmar,
        text="Ok",
        command=ok_btn_func
    )
    btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
#!SECTION

#SECTION - sub_janela_alerta_digite_numeros
def sub_janela_alerta_digite_numeros():
    #NOTE - sub_janela_alerta_digite_numeros
    sub_janela_confirmar_produtos = ctk.CTkToplevel()
    sub_janela_confirmar_produtos.geometry("300x300")
    sub_janela_confirmar_produtos.update_idletasks()
    x = (sub_janela_confirmar_produtos.winfo_screenwidth() // 2) - (sub_janela_confirmar_produtos.winfo_width() // 2)
    y = (sub_janela_confirmar_produtos.winfo_screenheight() // 2) - (sub_janela_confirmar_produtos.winfo_height() // 2)
    sub_janela_confirmar_produtos.geometry(f"+{x}+{y}")
    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_confirmar_produtos.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_confirmar_produtos,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_confirmar_produtos,
        text="Dados Inválidos!",
        text_color = "#F04A29",
        bg_color="#2b2b2b",
        font=("arial", 18, "bold")
    )
    label_confirmar.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    btn_ok = ctk.CTkButton(
        master=frame_confirmar,
        text="Ok",
        command=ok_btn_func
    )
    btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
#!SECTION

#SECTION - sub_janela_alerta_data_invalida
def sub_janela_alerta_data_invalida():
    #NOTE - sub_janela_alerta_data_invalida
    sub_janela_confirmar_data = ctk.CTkToplevel()
    sub_janela_confirmar_data.geometry("300x300")
    sub_janela_confirmar_data.update_idletasks()
    x = (sub_janela_confirmar_data.winfo_screenwidth() // 2) - (sub_janela_confirmar_data.winfo_width() // 2)
    y = (sub_janela_confirmar_data.winfo_screenheight() // 2) - (sub_janela_confirmar_data.winfo_height() // 2)
    sub_janela_confirmar_data.geometry(f"+{x}+{y}")
    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_confirmar_data.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_confirmar_data,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_confirmar_data,
        text="Data Inválida!",
        text_color = "#F04A29",
        bg_color="#2b2b2b",
        font=("arial", 18, "bold")
    )
    label_confirmar.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    btn_ok = ctk.CTkButton(
        master=frame_confirmar,
        text="Ok",
        command=ok_btn_func
    )
    btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
#!SECTION

#SECTION - janela_pedido_venda_func
def janela_pedido_venda_func(sub_janela_relatorio, produtos_estoque):
    #NOTE - janela_pedido_venda_func
    janela_pedido_venda = ctk.CTk()
    janela_pedido_venda.title("Pedido de venda")
    janela_pedido_venda.state("zoomed")
    
    font_texto = "arial"
    font_btn = "arial"
    cor_frame_meio = "#3b3b3b"

    #SECTION - Funções
    def somar_dias_uteis(dias_a_somar):
        #NOTE - somar_dias_uteis
        """
        Esta função soma dias úteis a partir de uma data inicial.

        param:
        - int: dias_a_somar (número de dias úteis a serem somados)

        return:
        - datetime.date: data_atual (data somada com os dias úteis)
        """
        dias_uteis = 0
        data_atual = datetime.date.today()

        while dias_uteis < dias_a_somar:
            data_atual += datetime.timedelta(days=1)
            if data_atual.weekday() not in (5, 6):
                dias_uteis += 1

        data_vencimento = data_atual
        return data_vencimento
    def verificar_data_func(date_string):
        #NOTE - verificar_data_func
        try:
            datetime.datetime.strptime(date_string, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    def adicionar_prod_btn_func():
        #NOTE - adicionar_prod_btn_func
        produto = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        valor = entry_valor.get()

        if produto == "" or quantidade == "" or valor == "":
            sub_janela_alerta_preencher_dados()
        elif produto != "" and quantidade != "" and valor != "": 
            if quantidade.isnumeric() and valor.isnumeric():
                text_prod_selecionados.configure(state="normal")
                text_prod_selecionados.insert("0.0", f"\n\n{produto} | {quantidade} | {valor}")
                text_prod_selecionados.configure(state="disabled")
                combo_pesquisar_prod.configure(state="normal")
                entry_quantidade.delete("0", "end")
                entry_valor.delete("0", "end")
            elif not quantidade.isnumeric() or not valor.isnumeric():
                sub_janela_alerta_digite_numeros()
    def adicionar_prod_btn_event_func(event):
        #NOTE - adicionar_prod_btn_event_func
        produto = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        valor = entry_valor.get()

        if produto == "" or quantidade == "" or valor == "":
            sub_janela_alerta_preencher_dados()
        elif produto != "" and quantidade != "" and valor != "": 
            if quantidade.isnumeric() and valor.isnumeric():
                text_prod_selecionados.configure(state="normal")
                text_prod_selecionados.insert("0.0", f"\n\n{produto} | {quantidade} | {valor}")
                text_prod_selecionados.configure(state="disabled")
                combo_pesquisar_prod.configure(state="normal")
                entry_quantidade.delete("0", "end")
                entry_valor.delete("0", "end")
            elif not quantidade.isnumeric() or not valor.isnumeric():
                sub_janela_alerta_digite_numeros()
    def pesquisar_prod_func(event):
        #NOTE - pesquisaar_prod
        produto_pesquisado = combo_pesquisar_prod.get()
        if str(produto_pesquisado) != "":            
            filtered_items = [item for item in produtos_estoque if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]
            if len(filtered_items) <= 0:
                sub_janela_alerta_prod_nao_encontrado()
            combo_pesquisar_prod.configure(values=filtered_items)
        elif str(produto_pesquisado) == "":
            combo_pesquisar_prod.configure(values=produtos_estoque)
    def pesquisar_cliente_func(event):
        #NOTE - pesquisar_cliente_func
        cliente_pesquisado = combo_cliente.get()
        if str(cliente_pesquisado) != "":            
            filtered_items = [item for item in lista_clientes if unidecode(cliente_pesquisado).upper() in unidecode(item).upper()]
            if len(filtered_items) <= 0:
                sub_janela_alerta_cliente_nao_encontrado()
            combo_cliente.configure(values=filtered_items)
        elif str(cliente_pesquisado) == "":
            combo_cliente.configure(values=lista_clientes)
    def remover_ultimo_btn_func():
        #NOTE - remover_ultimo_btn_func
        text_prod_selecionados.configure(state="normal")
        text_prod_selecionados.delete("1.0", "1.1000")
        prods_selecionados = text_prod_selecionados.get("1.0", "end").split("\n")        
        text_prod_selecionados.delete("1.0", "end")        
        for index, item in enumerate(prods_selecionados):
            if item == "":
                del prods_selecionados[index]
        prods_selecionados.pop()
        for item in prods_selecionados:
            text_prod_selecionados.insert("1.0", f"{item}\n")
        text_prod_selecionados.configure(state="disabled")
    def limpar_prods_selecionados():
        #NOTE - limpar_prods_selecionados
        text_prod_selecionados.configure(state="normal")
        text_prod_selecionados.delete("0.0", "end")
        text_prod_selecionados.configure(state="disabled")
    def concluir_func():
        #NOTE - concluir_func
        data = entry_data.get()
        verificar_data = verificar_data_func(data)
        if verificar_data == False:
            sub_janela_alerta_data_invalida()
        else:
            prods_selecionados = text_prod_selecionados.get("0.0", "end").split("\n")
            prods_selecionados.pop()
            prods_selecionados.pop(0)
            prods_selecionados.pop(0)
            if len(prods_selecionados) > 0:
                nome_cliente = combo_cliente.get()
                data = entry_data.get()
                prazo = combo_prazo.get()
                if prazo == "A vista":
                    data_vencimento = datetime.date.today()
                    data_vencimento = data_vencimento.strftime("%d/%m/%Y")
                else:
                    prazo = prazo.split(" ")[0]
                    data_vencimento = somar_dias_uteis(data, prazo)
                codigo_cliente_omie, razao_social = get_cod_cliente(nome_cliente)                
                for linha in prods_selecionados:
                    for i, item in enumerate(prods_selecionados):
                        if item == "":
                            prods_selecionados.pop(i)        
                    linha = linha.split(" | ")
                    nome_produto = linha[0]
                    quantidade_prod = linha[1].strip()
                    valor = linha[2].strip()
                    valor = valor.replace("\n", "")
                    cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_nome_func(nome_produto)
                    codigo_projeto = get_cod_projeto(nome_produto)
                    dict_pedido_venda = {
                        "razao_social": razao_social,
                        "codigo_produto": codigo_produto,
                        "codigo_cliente_omie": codigo_cliente_omie,
                        "data_vencimento": data_vencimento,
                        "cfop": cfop,
                        "descricao": descricao,
                        "ncm": ncm,
                        "unidade": unidade,                        
                        "quantidade_prod": quantidade_prod,
                        "valor": valor,
                        "codigo_projeto": codigo_projeto
                    }
                    lista_pedidos_venda.append(dict_pedido_venda)
                text_venda.configure(state="normal")
                linha = 1
                
                for dict_pedido_venda in lista_pedidos_venda:
                    print(f"dict_pedido_venda: {dict_pedido_venda}")
                    for chave, valor in dict_pedido_venda.items():
                        if chave == "razao_social":
                            text_venda.insert(f"{linha}.0", f"Cliente: {valor}\n")
                        if chave == "descricao":
                            text_venda.insert(f"{linha}.0", f"Produto: {valor}\n")
                        if chave == "quantidade_prod":
                            text_venda.insert(f"{linha}.0", f"Quantidade: {valor}\n")
                        if chave == "valor":
                            text_venda.insert(f"{linha}.0", f"Valor: {valor}\n")
                        linha += 1
                    text_venda.insert(f"{linha}.0", f"__________________________\n")
                text_venda.configure(state="disabled")
                    
                    #incluir_pedido_venda(codigo_produto, codigo_cliente_omie, data_vencimento, cfop, descricao, ncm ,unidade, valor, quantidade_prod, codigo_projeto)
    def voltar_prod_func():
        #NOTE - voltar_prod_func
        janela_pedido_venda.destroy()
        sub_janela_relatorio.deiconify()
        sub_janela_relatorio.state("zoomed")
    def inicio_prod_func():
        #NOTE - inicio_prod_func
        janela_pedido_venda.destroy()
        sub_janela_relatorio.destroy()
    #!SECTION


    #SECTION - Centro
    #NOTE - frame_meio
    frame_meio = ctk.CTkFrame(
        master=janela_pedido_venda,
        width=750,
        height=500,
        fg_color="transparent"
        )
    frame_meio.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #NOTE - frame_central
    frame_central = ctk.CTkFrame(
            master=frame_meio,
            width=300,
            height=360,
            fg_color= ("#3b3b3b")
        )
    frame_central.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

    #NOTE - btn_voltar
    img_voltar = ctk.CTkImage(light_image=Image.open("config/arquivos/img/voltar.png"), size=(30,30))
    btn_voltar = ctk.CTkButton(
        master=frame_meio,
        width=15,
        height=15,
        text="Voltar",
        font=(font_btn, 15),
        #image=img_voltar,
        #fg_color="transparent",
        command=voltar_prod_func
    )
    btn_voltar.place(relx=0.30, rely=0.08)
    img_home = ctk.CTkImage(light_image=Image.open("config/arquivos/img/home.png"), size=(30,30))
    #NOTE - btn_inicio
    btn_inicio = ctk.CTkButton(
        master=frame_meio,
        width=15,
        height=15,
        text="Início",
        font=(font_btn, 15),
        #image=img_home,
        #fg_color="transparent",
        command=inicio_prod_func
    )
    btn_inicio.place(relx=0.38, rely=0.08)

    #NOTE - label_titulo
    label_titulo = ctk.CTkLabel(
        master=frame_meio,
        text="Criar Pedido de Venda",
        font=("arial", 18, "bold")
    )
    label_titulo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

    #NOTE - label_pesquisar_prod
    label_pesquisar_prod = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos",
        font= (font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_pesquisar_prod.place(relx=0.37, rely=0.30, anchor=tkinter.CENTER)    
    
    #NOTE - combo_pesquisar_prod
    for i, produto in enumerate(lista_produtos):
        lista_produtos[i] = str((produto.split(" | "))[1]).replace("\n","")
    combo_pesquisar_prod = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_produtos,
        width=150,
        height=25,        
        )
    combo_pesquisar_prod.place(relx=0.55, rely=0.30, anchor=tkinter.CENTER)
    combo_pesquisar_prod.bind("<Return>", pesquisar_prod_func)

    #NOTE - label_quantidade 
    label_quantidade = ctk.CTkLabel(
        master=frame_meio,
        text="Quantidade",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_quantidade.place(relx=0.37, rely=0.36, anchor=tkinter.CENTER)    

    #NOTE - entry_quantidade
    entry_quantidade = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_quantidade.place(relx=0.55, rely=0.36, anchor=tkinter.CENTER)

    #NOTE - label_valor 
    label_valor = ctk.CTkLabel(
        master=frame_meio,
        text="Valor Un.",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_valor.place(relx=0.37, rely=0.42, anchor=tkinter.CENTER)    

    #NOTE - entry_valor
    entry_valor = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_valor.place(relx=0.55, rely=0.42, anchor=tkinter.CENTER)
    entry_valor.bind("<Return>", adicionar_prod_btn_event_func)

    #NOTE - btn_adicionar_produto
    btn_adicionar_produto = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Adicionar Produto",
        font=(font_btn, 15),
        border_width=0,
        command = adicionar_prod_btn_func)
    btn_adicionar_produto.place(relx=0.55, rely=0.50, anchor=ctk.CENTER)
    #NOTE - btn_remover_ultimo
    btn_remover_ultimo = ctk.CTkButton(
        master=frame_meio,
        width=125,
        height=25,
        text="Remover último produto",
        font=(font_btn, 13),
        command = remover_ultimo_btn_func)
    btn_remover_ultimo.place(relx=0.55, rely=0.56, anchor=ctk.CENTER)
    #NOTE - btn_limpar 
    btn_limpar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Limpar",
        font=(font_btn, 15),
        command = limpar_prods_selecionados)
    btn_limpar.place(relx=0.55, rely=0.62, anchor=ctk.CENTER)
    
    #NOTE - label_clientes
    label_clientes = ctk.CTkLabel(
        master=frame_meio,
        text="Cliente",
        fg_color=cor_frame_meio,
        font= (font_texto, 13, "bold"),
    )
    label_clientes.place(relx=0.37, rely=0.68, anchor=tkinter.CENTER)

    #NOTE - combo_cliente
    lista_clientes = ["vinicio", "Victor", "Amanda", "Papelaria e Livraria Rápida Ltda"]
    combo_cliente = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_clientes,
        width=150,
        height=25,
    )
    combo_cliente.place(relx=0.55, rely=0.68, anchor=tkinter.CENTER)
    combo_cliente.bind("<Return>", pesquisar_cliente_func)

    #NOTE - label_data 
    label_data = ctk.CTkLabel(
        master=frame_meio,
        text="Data",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_data.place(relx=0.37, rely=0.74, anchor=tkinter.CENTER)    

    #NOTE - entry_data
    entry_data = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_data.place(relx=0.55, rely=0.74, anchor=tkinter.CENTER)

    

    #NOTE - label_prazo 
    label_prazo = ctk.CTkLabel(
        master=frame_meio,
        text="Prazo",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_prazo.place(relx=0.37, rely=0.80, anchor=tkinter.CENTER)    

    #NOTE - entry_prazo
    lista_prazo = ["A vista",
                                "7 dias",
                                "14 Dias",
                                "21 Dias",
                                "30 Dias",
                                "45 Dias",
                                "60 Dias"]
    combo_prazo = ctk.CTkComboBox(master=frame_meio,
    values=lista_prazo,
    width=150,
    height=25)
    combo_prazo.place(relx=0.55, rely=0.80, anchor=tkinter.CENTER)

    #NOTE - btn_gerar_pedido_venda
    btn_gerar_pedido_venda = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Concluir",
        font=(font_btn, 15),
        fg_color="#00993D",
        hover_color=("#007830"),
        command=concluir_func
    )
    btn_gerar_pedido_venda.place(relx=0.55, rely=0.87, anchor=tkinter.CENTER)
    #!SECTION

    #SECTION - Direita
    
    #NOTE - text_prod_selecionados
    text_prod_selecionados = ctk.CTkTextbox(
        master=frame_meio,
        width=200,
        height=230,
        font=("Arial", 12)
        )
    text_prod_selecionados.place(relx=0.85, rely=0.27, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")

    #NOTE - label_prod_selecionados
    label_prod_selecionados = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold"),
        fg_color=cor_frame_meio
        )
    label_prod_selecionados.place(relx=0.85, rely=0.07, anchor=tkinter.CENTER)

    #NOTE - text_venda
    text_venda = ctk.CTkTextbox(
        master=frame_meio,
        width=200,
        height=230,
        font=("Arial", 12)
        )
    text_venda.place(relx=0.85, rely=0.75, anchor=tkinter.CENTER)
    text_venda.configure(state="disabled")

    """#NOTE - label_venda
    label_venda = ctk.CTkLabel(
        master=frame_meio,
        text="Adicionados para Venda",
        font=("Arial", 15, "bold"),
        fg_color=cor_frame_meio
        )
    label_venda.place(relx=0.85, rely=0.55, anchor=tkinter.CENTER)"""
    #!SECTION

    janela_pedido_venda.mainloop()
#!SECTION

