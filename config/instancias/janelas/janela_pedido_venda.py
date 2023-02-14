import customtkinter as ctk
import os
import tkinter
import datetime
from unidecode import unidecode
from PIL import Image
import ast
from config.instancias.apis.apis_vendas import incluir_pedido_venda
from config.instancias.apis.apis_vendas import incluir_pedido_venda_lot
from config.instancias.apis.apis_cliente import get_cod_cliente
from config.instancias.apis.apis_projetos import get_cod_projeto
from config.instancias.apis.apis_produtos import pesquisar_produto_nome_func


with open("config/arquivos/lista_clientes.txt", "r") as arquivo:
    lista_clientes = arquivo.readlines()
    lista_clientes_aux = []
    for cliente in lista_clientes:
        cliente = cliente.split(" | ")
        del cliente[0]
        cliente = str(cliente)
        cliente = cliente.replace("[", "")
        cliente = cliente.replace("]", "")
        cliente = cliente.replace("'", "")
        cliente = cliente.replace("\\n", "")
        lista_clientes_aux.append(cliente)
    lista_clientes = lista_clientes_aux

#SECTION - sub_janela_alerta_sucesso
def sub_janela_alerta_sucesso():
    #NOTE - sub_janela_alerta_sucesso
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
        text="Sucesso!",
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
def janela_pedido_venda_func(sub_janela_relatorio, produtos_estoque, text_relatorio):
    #NOTE - janela_pedido_venda_func
    janela_pedido_venda = ctk.CTk()
    janela_pedido_venda.title("Pedido de venda")
    janela_pedido_venda.state("zoomed")
    
    font_texto = "arial"
    font_btn = "arial"
    cor_frame_meio = "#3b3b3b"

    #SECTION - Funções
    def atualizar_func():
        #NOTE - atualizar_func
        with open("config/arquivos/codigo_local_estoque_aux.txt", "r") as arquivo:
            codigo_local_estoque_aux = arquivo.read()
        codigo_local_estoque_aux = codigo_local_estoque_aux.strip()
        with open("config/arquivos/produtos_venda.txt", "r") as arquivo:
            produtos_venda = arquivo.readlines()
        with open(f"config/arquivos/quant_diferenca_estoque.txt", "r") as arquivo:
            quant_diferenca_estoque = arquivo.readlines()
        for prods_venda in produtos_venda:
            codigo_local_estoque_venda = prods_venda.split(" | ")[0].strip()
            nome_produto_venda = prods_venda.split(" | ")[1].strip()
            quant_venda = float(prods_venda.split(" | ")[2].strip())
            for i, prods_dif in enumerate(quant_diferenca_estoque):
                nome_produto_diferenca = prods_dif.split(" | ")[1].strip()
                quant_diferenca = float(prods_dif.split(" | ")[2].strip())
                codigo_local_estoque = prods_dif.split(" | ")[0].strip()
                if codigo_local_estoque == codigo_local_estoque_venda:
                    if nome_produto_venda in nome_produto_diferenca:
                        quant_sub = quant_diferenca - quant_venda
                        quant_diferenca_estoque[i] = f"{codigo_local_estoque} | {nome_produto_diferenca} | {quant_sub}\n"
        text_relatorio.configure(state="normal")
        text_relatorio.delete("0.0", "end")
        linha = 0
        for prod_estoque in quant_diferenca_estoque:
            prod_estoque = prod_estoque.split(" | ")
            prod_estoque.pop(0)
            text_relatorio.insert(f"{linha}.0", f"{prod_estoque[0]} | {prod_estoque[1]}")
            linha += 1
        text_relatorio.configure(state="disabled")
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
            try:
                quantidade = quantidade.replace(",", ".")
            except:
                pass
            try:
                valor = valor.replace(",", ".")
            except:
                pass
            try:
                quantidade = float(quantidade)
                valor = float(valor)
                text_prod_selecionados.configure(state="normal")
                prods_quant_selecionados = text_prod_selecionados.get("0.0", "end").strip()
                if prods_quant_selecionados == "":
                    text_prod_selecionados.insert("0.0", f"\n\n{produto} | {quantidade} | {valor}")
                else:
                    text_prod_selecionados.insert("3.0", f"{produto} | {quantidade} | {valor}\n")
                text_prod_selecionados.configure(state="disabled")
                combo_pesquisar_prod.configure(state="normal")
                entry_quantidade.delete("0", "end")
                entry_valor.delete("0", "end")
            except ValueError:
                sub_janela_alerta_digite_numeros()
    def adicionar_prod_btn_event_func(event):
        #NOTE - adicionar_prod_btn_event_func
        produto = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        valor = entry_valor.get()
        if produto == "" or quantidade == "" or valor == "":
            sub_janela_alerta_preencher_dados()
        elif produto != "" and quantidade != "" and valor != "":
            try:
                quantidade = quantidade.replace(",", ".")
            except:
                pass
            try:
                valor = valor.replace(",", ".")
            except:
                pass
            try:
                quantidade = float(quantidade)
                valor = float(valor)
                text_prod_selecionados.configure(state="normal")
                prods_quant_selecionados = text_prod_selecionados.get("0.0", "end").strip()
                if prods_quant_selecionados == "":
                    text_prod_selecionados.insert("0.0", f"\n\n{produto} | {quantidade} | {valor}")
                else:
                    text_prod_selecionados.insert("3.0", f"{produto} | {quantidade} | {valor}\n")
                text_prod_selecionados.configure(state="disabled")
                combo_pesquisar_prod.configure(state="normal")
                entry_quantidade.delete("0", "end")
                entry_valor.delete("0", "end")
            except ValueError:
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
        prods_selecionados = text_prod_selecionados.get("1.0", "end").split("\n")       
        
        for index, item in enumerate(prods_selecionados):
            if item == "":
                del prods_selecionados[index]
        if prods_selecionados[-1] == "":
            prods_selecionados.pop(-1)
        prods_selecionados.pop(1)
        
        text_prod_selecionados.delete("0.0", "end") 
        text_prod_selecionados.insert("0.0", "\n\n")
        prods_selecionados = list(reversed(prods_selecionados))
        for item in prods_selecionados:        
            text_prod_selecionados.insert("2.0", f"{item}\n")
        text_prod_selecionados.configure(state="disabled")
    def limpar_prods_selecionados():
        #NOTE - limpar_prods_selecionados
        text_prod_selecionados.configure(state="normal")
        text_prod_selecionados.delete("0.0", "end")
        text_prod_selecionados.configure(state="disabled")
    def concluir_cliente_func():
        #NOTE - concluir_cliente_func
        lista_det = []
        data = entry_data.get()
        verificar_data = verificar_data_func(data)
        if verificar_data == False:
            sub_janela_alerta_data_invalida()
        else:            
            prods_selecionados = text_prod_selecionados.get("0.0", "end").split("\n")
            for i, item in enumerate(prods_selecionados):
                if item == "":
                    prods_selecionados.pop(i)
            if prods_selecionados[0] == "":
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
                lista_nome_produtos_selecionados = []
                lista_valor_selecionados = []
                lista_quantidade_selecionados = []
                lista_codigo_produtos_selecionados = []
                lista_unidade_selecionados = []
                lista_projeto_selecionados = []
                lista_ncm_selecionados = []
                lista_cfop_selecionados = []
                lista_pedidos_venda = []
                dict_pedido_venda = {}
                
                for linha in prods_selecionados:                            
                    linha = linha.split(" | ")
                    nome_produto = linha[0]
                    quantidade_prod = float(linha[1].strip())
                    valor = linha[2].strip()
                    valor = float(valor.replace("\n", ""))
                    cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_nome_func(nome_produto)
                    codigo_projeto = get_cod_projeto(nome_produto)
                    dict_det = {
                        "ide": {
                                "codigo_item_integracao": "4422421"
                        },
                        "produto": {
                                "cfop": cfop,
                                "codigo_produto": codigo_produto,
                                "descricao": descricao,
                                "ncm": ncm,
                                "quantidade": quantidade_prod,
                                "unidade": unidade,
                                "valor_unitario": valor
                            }
                    }
                    
                    lista_det.append(dict_det)
                    
                    lista_nome_produtos_selecionados.append(nome_produto)
                    lista_codigo_produtos_selecionados.append(codigo_produto)
                    lista_quantidade_selecionados.append(quantidade_prod)
                    lista_valor_selecionados.append(valor)
                    lista_cfop_selecionados.append(cfop)
                    lista_ncm_selecionados.append(ncm)
                    lista_projeto_selecionados.append(codigo_projeto)
                    lista_unidade_selecionados.append(unidade)
                with open(f"config/arquivos/temp_lista_det_{codigo_cliente_omie}.txt", "w") as arquivo:
                    arquivo.write(str(lista_det))
                dict_pedido_venda = {
                    "valor": lista_valor_selecionados,
                    "razao_social": razao_social,
                    "codigo_produto": lista_codigo_produtos_selecionados,
                    "codigo_cliente_omie": codigo_cliente_omie,
                    "data_vencimento": data_vencimento,
                    "cfop": lista_cfop_selecionados,
                    "descricao": lista_nome_produtos_selecionados,
                    "ncm": lista_ncm_selecionados,
                    "unidade": lista_unidade_selecionados,                        
                    "quantidade_prod": lista_quantidade_selecionados,                    
                    "codigo_projeto": lista_projeto_selecionados
                }
                with open("config/arquivos/lista_det.txt", "w") as arquivo:
                    arquivo.write(str(lista_det))
                lista_titulos = ["valor", "razao_social"]
                lista_pedidos_venda.append(dict_pedido_venda)
                with open("config/arquivos/dados_venda.txt", "w") as arquivo:
                    arquivo.write(f"{codigo_cliente_omie} | {data_vencimento}")
                text_venda.configure(state="normal")                
                for dict_pedido_venda in lista_pedidos_venda:
                    for chave, valor in dict_pedido_venda.items():                        
                        for titulo in lista_titulos:
                            if chave == titulo:
                                if chave == "razao_social":                              
                                    text_venda.insert(f"0.0", f"Cliente: {valor}\n")
                                if chave == "valor":
                                    lista_quantidade = dict_pedido_venda["quantidade_prod"]
                                    lista_preco = dict_pedido_venda["valor"]
                                    total = 0
                                    for quantidade, preco in zip(lista_quantidade, lista_preco):
                                        total += quantidade * preco
                                    text_venda.insert(f"1.0", f"Valor: R$ {total}\n\n")
                                break
                text_venda.configure(state="disabled")
                limpar_prods_selecionados()
    def voltar_prod_func():
        #NOTE - voltar_prod_func
        janela_pedido_venda.destroy()
        sub_janela_relatorio.deiconify()
        sub_janela_relatorio.state("zoomed")
    def inicio_prod_func():
        #NOTE - inicio_prod_func
        janela_pedido_venda.destroy()
        sub_janela_relatorio.destroy()
    def btn_pedido_venda_func():
        #NOTE - btn_pedido_venda_func
        with open("config/arquivos/codigo_local_estoque_aux.txt", "r") as arquivo:
            codigo_local_estoque = arquivo.read()
        codigo_local_estoque = codigo_local_estoque.strip()
        with open("config/arquivos/produtos_venda.txt", "r") as arquivo:
            produtos_venda = arquivo.readlines()        
        with open("config/arquivos/lista_det.txt", "r") as arquivo:
            lista_det = arquivo.read()
        lista_det = ast.literal_eval(lista_det)
        with open("config/arquivos/dados_venda.txt", "r") as arquivo:
            dados_venda = arquivo.read()
        data_vencimento = dados_venda.split(" | ")[1].strip()
        arquivos = os.listdir("config/arquivos")
        for arquivo_dir in arquivos:
            if "temp_lista_det_" in arquivo_dir:
                codigo_cliente_omie = arquivo_dir.split("_")[3]
                codigo_cliente_omie = codigo_cliente_omie.split(".")[0]
                with open(f"config/arquivos/{arquivo_dir}") as arquivo:
                    temp_det = arquivo.read()
                temp_det = ast.literal_eval(temp_det)
                with open("config/arquivos/lista_departamentos.txt", "r") as arquivo:
                    lista_departamentos = arquivo.readlines()
                departamentos = []
                for dict_det in temp_det:
                    produtos = dict_det["produto"]
                    descricao = produtos["descricao"]
                    for departamento in lista_departamentos:
                        nome_departamento = departamento.split(" | ")[1].strip()
                        if nome_departamento == descricao:
                            codigo_departamento = departamento.split(" | ")[0].strip()
                            dict_departamentos = {
                                "cCodDepto": codigo_departamento,
                                "nPerc": 50,
                                "nValor": 1,
                                "nValorFixo": "S"
                            }
                            departamentos.append(dict_departamentos)                            
                incluir_pedido_venda_lot(temp_det, codigo_cliente_omie, data_vencimento, departamentos)
                os.remove(f"config/arquivos/{arquivo_dir}")        
                for dict_det in temp_det:
                    produtos = dict_det["produto"]
                    descricao = produtos["descricao"]
                    quantidade = produtos["quantidade"]
                    produtos_venda.append(f"{codigo_local_estoque} | {descricao} | {quantidade}\n")        
        with open("config/arquivos/produtos_venda.txt", "w") as arquivo:
            arquivo.writelines(produtos_venda)
        sub_janela_alerta_sucesso()
        janela_pedido_venda.destroy()
        sub_janela_relatorio.deiconify()
        sub_janela_relatorio.state("zoomed")
        atualizar_func()
    #!SECTION
    

    #SECTION - Centro
    #NOTE - frame_meio
    frame_meio = ctk.CTkFrame(
        master=janela_pedido_venda,
        width=1300,
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
    btn_voltar.place(relx=0.39, rely=0.08)
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
    btn_inicio.place(relx=0.44, rely=0.08)

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
    label_pesquisar_prod.place(relx=0.43, rely=0.30, anchor=tkinter.CENTER)    
    
    #NOTE - combo_pesquisar_prod
    with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
        lista_produtos = arquivo.readlines()
    for i, produto in enumerate(lista_produtos):
        lista_produtos[i] = str((produto.split(" | "))[1]).replace("\n","")
    combo_pesquisar_prod = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_produtos,
        width=150,
        height=25,        
        )
    combo_pesquisar_prod.place(relx=0.53, rely=0.30, anchor=tkinter.CENTER)
    combo_pesquisar_prod.bind("<Return>", pesquisar_prod_func)

    #NOTE - label_quantidade 
    label_quantidade = ctk.CTkLabel(
        master=frame_meio,
        text="Quantidade",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_quantidade.place(relx=0.43, rely=0.36, anchor=tkinter.CENTER)    

    #NOTE - entry_quantidade
    entry_quantidade = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_quantidade.place(relx=0.53, rely=0.36, anchor=tkinter.CENTER)

    #NOTE - label_valor 
    label_valor = ctk.CTkLabel(
        master=frame_meio,
        text="Valor Un.",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_valor.place(relx=0.43, rely=0.42, anchor=tkinter.CENTER)    

    #NOTE - entry_valor
    entry_valor = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_valor.place(relx=0.53, rely=0.42, anchor=tkinter.CENTER)
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
    btn_adicionar_produto.place(relx=0.53, rely=0.50, anchor=ctk.CENTER)
    #NOTE - btn_remover_ultimo
    btn_remover_ultimo = ctk.CTkButton(
        master=frame_meio,
        width=125,
        height=25,
        text="Remover último produto",
        font=(font_btn, 13),
        command = remover_ultimo_btn_func)
    btn_remover_ultimo.place(relx=0.53, rely=0.56, anchor=ctk.CENTER)
    #NOTE - btn_limpar 
    btn_limpar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Limpar",
        font=(font_btn, 15),
        command = limpar_prods_selecionados)
    btn_limpar.place(relx=0.53, rely=0.62, anchor=ctk.CENTER)
    
    #NOTE - label_clientes
    label_clientes = ctk.CTkLabel(
        master=frame_meio,
        text="Cliente",
        fg_color=cor_frame_meio,
        font= (font_texto, 13, "bold"),
    )
    label_clientes.place(relx=0.43, rely=0.68, anchor=tkinter.CENTER)

    #NOTE - combo_cliente
    #lista_clientes = ["vinicio", "Victor", "Amanda", "Papelaria e Livraria Rápida Ltda", "Indústria de Malhas"]

    combo_cliente = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_clientes,
        width=150,
        height=25,
    )
    combo_cliente.place(relx=0.53, rely=0.68, anchor=tkinter.CENTER)
    combo_cliente.bind("<Return>", pesquisar_cliente_func)

    #NOTE - label_data 
    label_data = ctk.CTkLabel(
        master=frame_meio,
        text="Data",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_data.place(relx=0.43, rely=0.74, anchor=tkinter.CENTER)    

    #NOTE - entry_data
    entry_data = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_data.place(relx=0.53, rely=0.74, anchor=tkinter.CENTER)

    

    #NOTE - label_prazo 
    label_prazo = ctk.CTkLabel(
        master=frame_meio,
        text="Prazo",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_prazo.place(relx=0.43, rely=0.80, anchor=tkinter.CENTER)    

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
    combo_prazo.place(relx=0.53, rely=0.80, anchor=tkinter.CENTER)

    #NOTE - btn_concluir_cliente
    btn_concluir_cliente = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Concluir Cliente",
        font=(font_btn, 15),
        command=concluir_cliente_func
    )
    btn_concluir_cliente.place(relx=0.53, rely=0.87, anchor=tkinter.CENTER)

    #NOTE - btn_gerar_pedido_venda
    btn_gerar_pedido_venda = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Gerar pedido de venda",
        font=(font_btn, 15),
        fg_color="#00993D",
        hover_color=("#007830"),
        command=btn_pedido_venda_func
    )
    btn_gerar_pedido_venda.place(relx=0.53, rely=0.95, anchor=tkinter.CENTER)
    #!SECTION

    #SECTION - Direita
    
    #NOTE - text_prod_selecionados
    text_prod_selecionados = ctk.CTkTextbox(
        master=frame_meio,
        width=300,
        height=230,
        font=("Arial", 12)
        )
    text_prod_selecionados.place(relx=0.74, rely=0.27, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")

    #NOTE - label_prod_selecionados
    label_prod_selecionados = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold"),
        fg_color=cor_frame_meio
        )
    label_prod_selecionados.place(relx=0.74, rely=0.07, anchor=tkinter.CENTER)

    #NOTE - text_venda
    text_venda = ctk.CTkTextbox(
        master=frame_meio,
        width=300,
        height=230,
        font=("Arial", 12)
        )
    text_venda.place(relx=0.74, rely=0.75, anchor=tkinter.CENTER)
    text_venda.configure(state="disabled")

    #NOTE - label_venda
    """label_venda = ctk.CTkLabel(
        master=frame_meio,
        text="Adicionados para Venda",
        font=("Arial", 15, "bold"),
        fg_color=cor_frame_meio
        )
    label_venda.place(relx=0.85, rely=0.55, anchor=tkinter.CENTER)"""
    #!SECTION

    janela_pedido_venda.mainloop()
#!SECTION

