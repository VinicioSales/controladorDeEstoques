import customtkinter as ctk
import tkinter
import datetime
from unidecode import unidecode
from PIL import Image
#from config.credenciais.database import database_infos_func

with open(f"config/arquivos/lista_produtos.txt", "r") as arquivo:
    lista_produtos = arquivo.readlines()

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
def janela_pedido_venda_func(janela_mov_estoque, tipo):
    #NOTE - janela_pedido_venda_func
    janela_pedido_venda = ctk.CTk()
    janela_pedido_venda.title("Pedido de venda")
    janela_pedido_venda.state("zoomed")
    
    font_texto = "arial"
    font_btn = "arial"
    cor_frame_meio = "#3b3b3b"

    #SECTION - Funções
    def verificar_data_func(date_string):
        #NOTE - verificar_data_func
        try:
            datetime.datetime.strptime(date_string, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    def adicionar_prod_btn_func():
        #NOTE - adicionar_prod_btn_func
        cliente = combo_cliente.get()
        produto = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        valor = entry_valor.get()

        if cliente == "" or produto == "" or quantidade == "" or valor == "":
            sub_janela_alerta_preencher_dados()
        elif cliente != "" and produto != "" and quantidade != "" and valor != "": 
            if quantidade.isnumeric() and valor.isnumeric():
                text_prod_selecionados.configure(state="normal")
                text_prod_selecionados.insert("0.0", f"{produto} | {quantidade}\n")
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
            filtered_items = [item for item in lista_produtos if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]
            if len(filtered_items) <= 0:
                sub_janela_alerta_prod_nao_encontrado()
            combo_pesquisar_prod.configure(values=filtered_items)
        elif str(produto_pesquisado) == "":
            combo_pesquisar_prod.configure(values=lista_produtos)
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
    def confirmar_btn_func():
        #NOTE - confirmar_btn_func
        data = entry_data.get()
        verificar_data = verificar_data_func(data)
        print(f"verificar_data: {verificar_data}")
        if verificar_data == False:
            sub_janela_alerta_data_invalida()
        else:
            prazo = combo_prazo.get()            
            prods_selecionados = text_prod_selecionados.get("0.0", "end").split("\n")
            print(f"prods_selecionados: {prods_selecionados}")        
    def voltar_prod_func():
        #NOTE - voltar_prod_func
        janela_pedido_venda.destroy()
        janela_mov_estoque.deiconify()
        janela_mov_estoque.state("zoomed")
    def inicio_prod_func():
        #NOTE - inicio_prod_func
        janela_pedido_venda.destroy()
        janela_mov_estoque.destroy()
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
        text="Selecionar Produtos",
        font=("arial", 18, "bold")
    )
    label_titulo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

    
    
    #NOTE - label_clientes
    label_clientes = ctk.CTkLabel(
        master=frame_meio,
        text="Cliente",
        fg_color=cor_frame_meio,
        font= (font_texto, 13, "bold"),
    )
    label_clientes.place(relx=0.37, rely=0.30, anchor=tkinter.CENTER)

    #NOTE - combo_cliente
    lista_clientes = ["vinicio", "Victor", "Amanda"]
    combo_cliente = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_clientes,
        width=150,
        height=25,
    )
    combo_cliente.place(relx=0.55, rely=0.30, anchor=tkinter.CENTER)
    combo_cliente.bind("<Return>", pesquisar_cliente_func)

    #NOTE - label_pesquisar_prod
    label_pesquisar_prod = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos",
        font= (font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_pesquisar_prod.place(relx=0.37, rely=0.36, anchor=tkinter.CENTER)    
    
    #NOTE - combo_pesquisar_prod
    for i, produto in enumerate(lista_produtos):
        lista_produtos[i] = str((produto.split(" | "))[1]).replace("\n","")
    combo_pesquisar_prod = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_produtos,
        width=150,
        height=25,        
        )
    combo_pesquisar_prod.place(relx=0.55, rely=0.36, anchor=tkinter.CENTER)
    combo_pesquisar_prod.bind("<Return>", pesquisar_prod_func)

    #NOTE - label_quantidade 
    label_quantidade = ctk.CTkLabel(
        master=frame_meio,
        text="Quantidade",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_quantidade.place(relx=0.37, rely=0.42, anchor=tkinter.CENTER)    

    #NOTE - entry_quantidade
    entry_quantidade = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_quantidade.place(relx=0.55, rely=0.42, anchor=tkinter.CENTER)

    #NOTE - label_valor 
    label_valor = ctk.CTkLabel(
        master=frame_meio,
        text="Valor Un.",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_valor.place(relx=0.37, rely=0.48, anchor=tkinter.CENTER)    

    #NOTE - entry_valor
    entry_valor = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_valor.place(relx=0.55, rely=0.48, anchor=tkinter.CENTER)

    #NOTE - label_data 
    label_data = ctk.CTkLabel(
        master=frame_meio,
        text="Data",
        font=(font_texto, 13, "bold"),
        fg_color=cor_frame_meio
    )
    label_data.place(relx=0.37, rely=0.75, anchor=tkinter.CENTER)    

    #NOTE - entry_data
    entry_data = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_data.place(relx=0.55, rely=0.75, anchor=tkinter.CENTER)

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
    
    """#NOTE - btn_lupa
    img_lupa = ctk.CTkImage(light_image=Image.open("config/arquivos/img/lupa.png"))
    btn_lupa = ctk.CTkButton(
        master=frame_meio,
        #image=img_lupa,
        text="",
        width=8,
        height=8,
        hover=False,
        fg_color=cor_frame_meio
    )
    btn_lupa.place(relx=0.62, rely=0.36, anchor=tkinter.CENTER)"""
    
    
    #NOTE - btn_adicionar_produto
    btn_adicionar_produto = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Adicionar Produto",
        font=(font_btn, 15),
        border_width=0,
        command = adicionar_prod_btn_func)
    btn_adicionar_produto.place(relx=0.55, rely=0.56, anchor=ctk.CENTER)
    #NOTE - btn_remover_ultimo
    btn_remover_ultimo = ctk.CTkButton(
        master=frame_meio,
        width=125,
        height=25,
        text="Remover último produto",
        font=(font_btn, 13),
        command = remover_ultimo_btn_func)
    btn_remover_ultimo.place(relx=0.55, rely=0.62, anchor=ctk.CENTER)
    #NOTE - btn_limpar 
    btn_limpar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Limpar",
        font=(font_btn, 15),
        command = limpar_prods_selecionados)
    btn_limpar.place(relx=0.55, rely=0.68, anchor=ctk.CENTER)
    #NOTE - btn_confirmar
    btn_confirmar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Confirmar",
        font=(font_btn, 15),
        fg_color="#00993D",
        hover_color=("#007830"),
        command=confirmar_btn_func
    )
    btn_confirmar.place(relx=0.55, rely=0.87, anchor=tkinter.CENTER)
    #!SECTION

    #SECTION - Direita
    #NOTE - label_prod_selecionados
    label_prod_selecionados = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold")
        )
    label_prod_selecionados.place(relx=0.85, rely=0.02, anchor=tkinter.CENTER)
    #NOTE - text_prod_selecionados
    text_prod_selecionados = ctk.CTkTextbox(
        master=frame_meio,
        width=200,
        height=434,
        font=("Arial", 12)
        )
    text_prod_selecionados.place(relx=0.85, rely=0.48, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")
    #!SECTION

    janela_pedido_venda.mainloop()
#!SECTION

janela_pedido_venda_func("janela_mov_estoque", "tipo")