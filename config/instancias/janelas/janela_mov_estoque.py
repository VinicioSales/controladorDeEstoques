import customtkinter as ctk
import tkinter
from PIL import Image
from unidecode import unidecode
from config.instancias.apis.apis_estoque import incluir_ajuste_estoque
from config.instancias.apis.apis_produtos import pesquisar_produto_cod_func
from config.credenciais.database import database_infos_func

database_infos = database_infos_func()
estoque_box = database_infos["estoque_box"]

#SECTION - sub_janela_alerta_sucesso
def sub_janela_alerta_sucesso():
    #NOTE - sub_janela_alerta_sucesso
    sub_janela_alerta_sucesso = ctk.CTkToplevel()
    sub_janela_alerta_sucesso.title("Sucesso")
    sub_janela_alerta_sucesso.geometry("300x300")
    sub_janela_alerta_sucesso.update_idletasks()
    sub_janela_alerta_sucesso.attributes("-topmost", True)
    x = (sub_janela_alerta_sucesso.winfo_screenwidth() // 2) - (sub_janela_alerta_sucesso.winfo_width() // 2)
    y = (sub_janela_alerta_sucesso.winfo_screenheight() // 2) - (sub_janela_alerta_sucesso.winfo_height() // 2)
    sub_janela_alerta_sucesso.geometry(f"+{x}+{y}")
    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_alerta_sucesso.destroy()
    def ok_btn_event_func(event):
        #NOTE - ok_btn_func
        sub_janela_alerta_sucesso.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_alerta_sucesso,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_alerta_sucesso,
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

#SECTION - sub_janela_confirmar_ceasa_func
def sub_janela_confirmar_ceasa_func(text_prod_selecionados, janela_produtos, tipo, janela_mov_estoque, prods_selecionados):
    """Cria uma subjanela "sub_janela_confirmar_ceasa", centraliza a janela na tela,
    e apresenta uma pergunta "Há algum produto na Ceasa?" com uma entrada para a
    quantidade e dois botões "Ok" e "Cancelar".
    """
    sub_janela_confirmar_ceasa = ctk.CTkToplevel()
    sub_janela_confirmar_ceasa.geometry("500x200")
    sub_janela_confirmar_ceasa.title("")
    sub_janela_confirmar_ceasa.update_idletasks()
    x = (sub_janela_confirmar_ceasa.winfo_screenwidth() // 2) - (sub_janela_confirmar_ceasa.winfo_width() // 2)
    y = (sub_janela_confirmar_ceasa.winfo_screenheight() // 2) - (sub_janela_confirmar_ceasa.winfo_height() // 2)
    sub_janela_confirmar_ceasa.geometry(f"+{x}+{y}")

    #SECTION - Funções confirmar Ceasa
    def btn_confimar_ceasa_1_func():
        sub_janela_confirmar_ceasa.destroy()
        janela_produtos.destroy()        
        sub_janela_ceasa = sub_janela_ceasa_func(janela_mov_estoque, tipo, janela_produtos, prods_selecionados)
    def btn_confimar_ceasa_2_func():
        """
        Esta função fecha a sub-janela "sub_janela_confirmar_ceasa".
        """
        sub_janela_confirmar_ceasa.destroy()
        janela_produtos.destroy()
        prods_ceasa = ""
        janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo, prods_ceasa)
    #!SECTION

    #NOTE - frame_confirmar_ceasa
    frame_confirmar_ceasa = ctk.CTkFrame(
        master=sub_janela_confirmar_ceasa,
        width=470,
        height=270
    )
    frame_confirmar_ceasa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    #NOTE - label_confirmar_ceasa_1
    label_confirmar_ceasa_1 = ctk.CTkLabel(
        master=frame_confirmar_ceasa,
        text="Há algum produto na Ceasa?",
        font=("arial", 20, "bold")
    )
    label_confirmar_ceasa_1.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)

    #NOTE - btn_confimar_ceasa_1
    btn_confimar_ceasa_1 = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Sim",
        command=btn_confimar_ceasa_1_func
    )
    btn_confimar_ceasa_1.place(relx=0.35, rely=0.60, anchor=tkinter.CENTER)
    
    #NOTE - btn_confimar_ceasa_2
    btn_confimar_ceasa_2 = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Não",
        command=btn_confimar_ceasa_2_func
    )
    btn_confimar_ceasa_2.place(relx=0.65, rely=0.60, anchor=tkinter.CENTER)
#!SECTION

#SECTION - sub_janela_confirmar_produtos
def sub_janela_confirmar_produtos_func():
    #NOTE - sub_janela_confirmar_produtos_func
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
        text="Adicione um produto",
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

#SECTION - sub_janela_alerta_estoque_não_encontrado
def sub_janela_alerta_estoque_não_encontrado():
    #NOTE - sub_janela_alerta_estoque_não_encontrado
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
        text="Estoque não encontrado!",
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
        text="Digite Apenas Números!",
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

#SECTION - janela_produtos
def janela_produtos_func(janela_mov_estoque, tipo):
    #NOTE - janela_produtos_func
    """Cria a janela inicial"""
    janela_produtos = ctk.CTk()
    janela_produtos.title("Produtos")
    janela_produtos.state("zoomed")
    
    font_texto = "arial"
    font_btn = "arial"
    cor_frame_meio = "#3b3b3b"

    #SECTION - Funções
    def adicionar_prod_btn_func():
        #NOTE - adicionar_prod_btn_func
        prod_selecionado = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        if prod_selecionado == "" or quantidade == "":
            sub_janela_alerta_preencher_dados()
        elif prod_selecionado != "" and quantidade != "" and quantidade.isnumeric():
            text_prod_selecionados.configure(state="normal")
            text_prod_selecionados.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
            text_prod_selecionados.configure(state="disabled")
            combo_pesquisar_prod.configure(state="normal")
            entry_quantidade.delete("0", "end")
        elif not quantidade.isnumeric():
            sub_janela_alerta_digite_numeros()
    def adicionar_prod_func(event):
        #NOTE - adicionar_prod_func
        prod_selecionado = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        if prod_selecionado == "" or quantidade == "":
            sub_janela_alerta_preencher_dados()
        if prod_selecionado != "" and quantidade != "" and quantidade.isnumeric():
            #filtered_items = [item for item in lista_produtos if unidecode(prod_selecionado).upper() in unidecode(item).upper()]
            for produto in lista_produtos:
                if unidecode(prod_selecionado).upper() == unidecode(produto).upper():                  
                    text_prod_selecionados.configure(state="normal")
                    text_prod_selecionados.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
                    text_prod_selecionados.configure(state="disabled")
                    combo_pesquisar_prod.configure(state="normal")
                    entry_quantidade.delete("0", "end")
                    break
        elif not quantidade.isnumeric():
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
        prods_selecionados = text_prod_selecionados.get("0.0", "end").split("\n")  
        if len(prods_selecionados) <= 2:
            sub_janela_confirmar_produtos_func()
        elif len(prods_selecionados) > 2 and tipo == "ENT":
            sub_janela_confirmar_ceasa_func(text_prod_selecionados, janela_produtos, tipo, janela_mov_estoque, prods_selecionados)
        elif len(prods_selecionados) > 2 and tipo == "SAI":
            janela_produtos.destroy()
            prods_ceasa = ""
            janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo, prods_ceasa)
    def voltar_prod_func():
        #NOTE - voltar_prod_func
        janela_produtos.destroy()
        janela_mov_estoque.deiconify()
        janela_mov_estoque.state("zoomed")
    def inicio_prod_func():
        #NOTE - inicio_prod_func
        janela_produtos.destroy()
        janela_mov_estoque.destroy()
    #!SECTION


    #SECTION - Centro
    #NOTE - frame_meio
    frame_meio = ctk.CTkFrame(
        master=janela_produtos,
        width=1300,
        height=500,
        fg_color="transparent"
        )
    frame_meio.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    #NOTE - Cabeçalho
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
    btn_voltar.place(relx=0.39, rely=0.1)
    img_home = ctk.CTkImage(light_image=Image.open("config/arquivos/img/home.png"), size=(30,30))
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
    btn_inicio.place(relx=0.44, rely=0.1)

    #NOTE - label_titulo
    label_titulo = ctk.CTkLabel(
        master=frame_meio,
        text="Selecionar Produtos",
        font=("arial", 18, "bold")
    )
    label_titulo.place(relx=0.5, rely=0.19, anchor=tkinter.CENTER)

    #NOTE - frame_central
    frame_central = ctk.CTkFrame(
            master=frame_meio,
            width=300,
            height=326,
            fg_color= ("#3b3b3b")
        )
    frame_central.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    
    label_pesquisar_prod = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos",
        font= (font_texto, 18),
        fg_color=cor_frame_meio
    )
    label_pesquisar_prod.place(relx=0.50, rely=0.31, anchor=tkinter.CENTER)
    combo_pesquisar_prod = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_produtos,
        width=150,
        height=25,        
        )
    combo_pesquisar_prod.place(relx=0.50, rely=0.36, anchor=tkinter.CENTER)
    combo_pesquisar_prod.bind("<Return>", pesquisar_prod_func)
    
    label_quantidade = ctk.CTkLabel(
        master=frame_meio,
        text="Quantidade",
        font=(font_texto, 18),
        fg_color=cor_frame_meio
    )
    label_quantidade.place(relx=0.50, rely=0.41, anchor=tkinter.CENTER)
    entry_quantidade = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_quantidade.place(relx=0.50, rely=0.46, anchor=tkinter.CENTER)
    entry_quantidade.bind("<Return>", adicionar_prod_func)
    btn_adicionar_produto = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Adicionar Produto",
        font=(font_btn, 15),
        border_width=0,
        command = adicionar_prod_btn_func)
    btn_adicionar_produto.place(relx=0.50, rely=0.56, anchor=ctk.CENTER)
    btn_remover_ultimo = ctk.CTkButton(
        master=frame_meio,
        width=125,
        height=25,
        text="Remover último produto",
        font=(font_btn, 13),
        command = remover_ultimo_btn_func)
    btn_remover_ultimo.place(relx=0.50, rely=0.62, anchor=ctk.CENTER)
    btn_limpar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Limpar",
        font=(font_btn, 15),
        command = limpar_prods_selecionados)
    btn_limpar.place(relx=0.50, rely=0.68, anchor=ctk.CENTER)
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
    btn_confirmar.place(relx=0.50, rely=0.80, anchor=tkinter.CENTER)
    #!SECTION

    #SECTION - Direita
    #NOTE - Produtos Selecionados
    label_prod_selecionados = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold")
        )
    label_prod_selecionados.place(relx=0.75, rely=0.05, anchor=tkinter.CENTER)
    text_prod_selecionados = ctk.CTkTextbox(
        master=frame_meio,
        width=300,
        height=400,
        font=("Arial", 12)
        )
    text_prod_selecionados.place(relx=0.75, rely=0.48, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")
    #!SECTION

    janela_produtos.mainloop()
#!SECTION


#SECTION - sub_janela_ceasa_func
def sub_janela_ceasa_func(janela_mov_estoque, tipo, janela_produtos, prods_selecionados):    
    #NOTE - sub_janela_ceasa_func
    """Cria a janela inicial"""
    sub_janela_ceasa = ctk.CTk()
    sub_janela_ceasa.title("Produtos Ceasa")
    sub_janela_ceasa.state("zoomed")    
    font_texto = "arial"
    font_btn = "arial"
    cor_frame_meio = "#3b3b3b"    

    #SECTION - Funções
    def adicionar_prod_btn_func():
        #NOTE - adicionar_prod_btn_func
        prod_selecionado = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        if prod_selecionado == "" or quantidade == "":
            sub_janela_alerta_preencher_dados()
        elif prod_selecionado != "" and quantidade != "" and quantidade.isnumeric():
            text_prod_ceasa.configure(state="normal")
            text_prod_ceasa.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
            text_prod_ceasa.configure(state="disabled")
            combo_pesquisar_prod.configure(state="normal")
            entry_quantidade.delete("0", "end")
        elif not quantidade.isnumeric():
            sub_janela_alerta_digite_numeros()
    def adicionar_prod_func(event):
        #NOTE - adicionar_prod_func
        prod_selecionado = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        if prod_selecionado == "" or quantidade == "":
            sub_janela_alerta_preencher_dados()      
        if prod_selecionado != "" and quantidade != "" and quantidade.isnumeric():
            for produto in lista_produtos:
                if unidecode(prod_selecionado).upper() == unidecode(produto).upper():                  
                    text_prod_ceasa.configure(state="normal")
                    text_prod_ceasa.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
                    text_prod_ceasa.configure(state="disabled")
                    combo_pesquisar_prod.configure(state="normal")
                    entry_quantidade.delete("0", "end")
                    break
        elif not quantidade.isnumeric():
            sub_janela_alerta_digite_numeros()
    def pesquisar_prod_func(event):
        #NOTE - pesquisaar_prod
        produto_pesquisado = combo_pesquisar_prod.get()
        if str(produto_pesquisado) != "":            
            filtered_items = [item for item in lista_produtos if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]
            sub_janela_alerta_prod_nao_encontrado()
            combo_pesquisar_prod.configure(values=filtered_items)
        elif str(produto_pesquisado) == "":
            combo_pesquisar_prod.configure(values=lista_produtos)
    def remover_ultimo_btn_func():
        #NOTE - remover_ultimo_btn_func
        text_prod_ceasa.configure(state="normal")
        text_prod_ceasa.delete("1.0", "1.1000")
        prods_ceasa = text_prod_ceasa.get("1.0", "end").split("\n")
        text_prod_ceasa.delete("1.0", "end")        
        for index, item in enumerate(prods_ceasa):
            if item == "":
                del prods_ceasa[index]
        prods_ceasa.pop()
        for item in prods_ceasa:
            text_prod_ceasa.insert("1.0", f"{item}\n")
        text_prod_ceasa.configure(state="disabled")
    def limpar_prods_selecionados():
        #NOTE - limpar_prods_selecionados
        text_prod_ceasa.configure(state="normal")
        text_prod_ceasa.delete("0.0", "end")
        text_prod_ceasa.configure(state="disabled")
    def get_codigo(nome_produto):
        #NOTE - get_codigo
        """Pega o codigo do produto na lista de produtos
        
        param:
            - string: nome_produto
            
        return:
            - string: codigo"""
        with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
            lista_produtos = arquivo.readlines()
        nome_produto_aux= nome_produto.replace(" ", "")
        for produto in lista_produtos:                
            produto = produto.split("|")
            nome = produto[1]
            nome_aux = nome.replace(" ", "")
            if str(nome_produto_aux) in str(nome_aux):
                codigo = produto[0]
                codigo = codigo.replace(" ", "")
                break
        return codigo
    def get_codigo_local_estoque(nome_estoque):
        #NOTE - get_codigo_local_estoque
        """Pega o codigo do estoque na lista de estoques
        
        param:
            - string: nome_estoque
            
        return:
            - string: codigo_local_estoque"""        
        with open("config/arquivos/lista_estoques.txt", "r") as arquivo:
            lista_estoques = arquivo.readlines()
            try:
                for estoque in lista_estoques:
                    if nome_estoque in estoque:
                        estoque = estoque.split("|")
                        codigo_local_estoque = estoque[1]
                        codigo_local_estoque = codigo_local_estoque.replace(" ", "")
                        break
            except:
                codigo_local_estoque = ""
        return codigo_local_estoque
    def btn_confirmar_func():
        #NOTE - btn_confirmar_func
        prods_ceasa = text_prod_ceasa.get("0.0", "end").split("\n")
        prods_ceasa.pop()
        prods_ceasa.pop()
        if len(prods_ceasa) <= 0:
            sub_janela_alerta_prod_nao_encontrado()
        else:            
            estoque_origem = combo_estoque_ceasa_origem.get()
            #estoque_destino = combo_estoque_ceasa_destino.get()
            nota = entry_nota.get()
            obs_ent = f"{nota}\n\nDe: {estoque_origem}"
            obs_sai = f"{nota}\n\nPara: Box"
            codigo_estoque_origem = get_codigo_local_estoque(nome_estoque=estoque_origem)
            #codigo_estoque_destino = get_codigo_local_estoque(nome_estoque=estoque_destino)  
            lista_nome_produto = []
            lista_cod_produto = []
            lista_quantidade_produto = []
            for item in prods_ceasa:
                item = item.split("|")
                nome_produto = item[0]
                codigo = get_codigo(nome_produto)
                quantidade_produto = item[1]
                lista_nome_produto.append(nome_produto)
                lista_cod_produto.append(codigo)
                lista_quantidade_produto.append(quantidade_produto)
            for nome_produto, cod_produto, quantidade_produto in zip(lista_nome_produto, lista_cod_produto, lista_quantidade_produto):
                cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_cod_func(cod_produto)
                incluir_ajuste_estoque(codigo_produto, quantidade_produto, "SAI", valor_unitario, obs_sai, codigo_estoque_origem)
                incluir_ajuste_estoque(codigo_produto, quantidade_produto, "ENT", valor_unitario, obs_ent, estoque_box)        
            
            # Preenchendo lista_produtos_ceasa
            with open("config/arquivos/lista_produtos_ceasa.txt", "r") as arquivo:
                lista_produtos_ceasa = arquivo.readlines()      
            for item in prods_ceasa:
                item = item.split("|")
                nome_produto = item[0]
                codigo = get_codigo(nome_produto)
                quantidade_produto = item[1]
                codigo_estoque_origem = codigo_estoque_origem.strip()
                nome_produto = nome_produto.strip()
                quantidade_produto = quantidade_produto.strip()
                lista_produtos_ceasa.append(f"{codigo_estoque_origem} | {nome_produto} | {quantidade_produto}\n")
            with open("config/arquivos/lista_produtos_ceasa.txt", "w") as arquivo:
                arquivo.writelines(lista_produtos_ceasa)        
            sub_janela_ceasa.destroy()   
            sub_janela_alerta_sucesso()     
            janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo, prods_ceasa)
    def voltar_prod_func():
        #NOTE - voltar_prod_func
        sub_janela_ceasa.destroy()
        janela_mov_estoque.deiconify()
        janela_mov_estoque.state("zoomed")
    def inicio_prod_func():
        #NOTE - inicio_prod_func
        sub_janela_ceasa.destroy()
        janela_mov_estoque.destroy()
    def procurar_estoque_interno(event):
        #NOTE - procurar_estoque_interno
        """Procura o estoque na lista de estoques

        param:
            - None
        
        return:
            - None"""
        search_text = combo_estoque_ceasa_origem.get()
        filtered_items = [item for item in lista_estoques if search_text in item]
        if len(filtered_items) <= 0:
            sub_janela_alerta_estoque_não_encontrado()
        combo_estoque_ceasa_origem.configure(values=filtered_items)
    def procurar_estoque_caminhao(event):
        #NOTE - procurar_estoque_caminhao
        """Procura o estoque na lista de estoques

        param:
            - None
        
        return:
            - None"""
        search_text = combo_estoque_ceasa_destino.get()
        filtered_items = [item for item in lista_estoques if search_text in item]
        if len(filtered_items) <= 0:
            sub_janela_alerta_estoque_não_encontrado()
        combo_estoque_ceasa_destino.configure(values=filtered_items)
    #!SECTION

    #SECTION - Centro
    #NOTE - frame_meio
    frame_meio = ctk.CTkFrame(
        master=sub_janela_ceasa,
        width=1300,
        height=500,
        fg_color="transparent"
        )
    frame_meio.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    #frame_meio.pack()
    #NOTE - Cabeçalho
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
    #btn_voltar.place(relx=0.30, rely=0.1)
    btn_voltar.place(relx=0.39, rely=0.1)
    img_home = ctk.CTkImage(light_image=Image.open("config/arquivos/img/home.png"), size=(30,30))
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
    #btn_inicio.place(relx=0.38, rely=0.1)
    btn_inicio.place(relx=0.44, rely=0.1)

    #NOTE - label_titulo
    label_titulo = ctk.CTkLabel(
        master=frame_meio,
        text="Estoque Box",
        font=("arial", 18, "bold")
    )
    label_titulo.place(relx=0.5, rely=0.19, anchor=tkinter.CENTER)
    #NOTE - frame_central
    frame_central = ctk.CTkFrame(
            master=frame_meio,
            width=300,
            height=326,
            fg_color= ("#3b3b3b")
        )
    frame_central.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    
    label_pesquisar_prod = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos",
        font= (font_texto, 18),
        fg_color=cor_frame_meio
    )
    label_pesquisar_prod.place(relx=0.50, rely=0.31, anchor=tkinter.CENTER)
    combo_pesquisar_prod = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_produtos,
        width=150,
        height=25,        
        )
    combo_pesquisar_prod.place(relx=0.50, rely=0.36, anchor=tkinter.CENTER)
    combo_pesquisar_prod.bind("<Return>", pesquisar_prod_func)
    label_quantidade = ctk.CTkLabel(
        master=frame_meio,
        text="Quantidade",
        font=(font_texto, 18),
        fg_color=cor_frame_meio
    )
    label_quantidade.place(relx=0.50, rely=0.41, anchor=tkinter.CENTER)
    entry_quantidade = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_quantidade.place(relx=0.50, rely=0.46, anchor=tkinter.CENTER)
    entry_quantidade.bind("<Return>", adicionar_prod_func)
    btn_adicionar_produto = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Adicionar Produto",
        font=(font_btn, 15),
        border_width=0,
        command = adicionar_prod_btn_func)
    btn_adicionar_produto.place(relx=0.50, rely=0.53, anchor=ctk.CENTER)
    btn_remover_ultimo = ctk.CTkButton(
        master=frame_meio,
        width=125,
        height=25,
        text="Remover último produto",
        font=(font_btn, 13),
        command = remover_ultimo_btn_func)
    btn_remover_ultimo.place(relx=0.50, rely=0.59, anchor=ctk.CENTER)
    btn_limpar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Limpar",
        font=(font_btn, 15),
        command = limpar_prods_selecionados)
    btn_limpar.place(relx=0.50, rely=0.65, anchor=ctk.CENTER)
    label_estoque_origem = ctk.CTkLabel(
        master=frame_meio,
        text="Origem:",
        font=("arial", 12, "bold"),
        bg_color="#3b3b3b",
    ) 
    label_estoque_origem.place(relx=0.42, rely=0.71, anchor=tkinter.CENTER)
    combo_estoque_ceasa_origem = ctk.CTkComboBox(
        master=frame_meio,
        values=lista_estoques,
        width=150,
        height=25,
    )
    combo_estoque_ceasa_origem.bind("<Return>", procurar_estoque_interno)
    combo_estoque_ceasa_origem.place(relx=0.5, rely=0.71, anchor=tkinter.CENTER)
    
    #NOTE - label_nota
    label_nota = ctk.CTkLabel(
        master=frame_meio,
        text="Nota:",
        font=("arial", 12, "bold"),
        bg_color="#3b3b3b",
    )
    label_nota.place(relx=0.42, rely=0.77, anchor=tkinter.CENTER)

    #NOTE - entry_nota
    entry_nota = ctk.CTkEntry(
        master=frame_meio,
        width=150,
        height=25,)
    entry_nota.place(relx=0.5, rely=0.77, anchor=tkinter.CENTER)

    btn_confirmar = ctk.CTkButton(
        master=frame_meio,
        width=150,
        height=25,
        text="Movimentar Estoque",
        font=(font_btn, 15),
        fg_color="#00993D",
        hover_color=("#007830"),
        command=btn_confirmar_func
    )
    btn_confirmar.place(relx=0.50, rely=0.84, anchor=tkinter.CENTER)
    #!SECTION

    #SECTION - Direita
    #NOTE - Produtos Adicionados
    label_prod_selecionados = ctk.CTkLabel(
        master=frame_meio,
        text="Produtos Adicionados",
        font=("Arial", 15, "bold")
        )
    label_prod_selecionados.place(relx=0.75, rely=0.05, anchor=tkinter.CENTER)
    text_prod_ceasa = ctk.CTkTextbox(
        master=frame_meio,
        width=300,
        height=400,
        font=("Arial", 12)
        )
    text_prod_ceasa.place(relx=0.75, rely=0.48, anchor=tkinter.CENTER)
    text_prod_ceasa.configure(state="disabled")
    #!SECTION
    sub_janela_ceasa.mainloop()
#!SECTION

dimensao = "20x20"
#SECTION - Abrindo arquivos
with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
    lista_produtos = arquivo.readlines()
    lista_projetos_aux = []
    for produto in lista_produtos:
        produto = produto.split("|")
        del produto[0]
        produto = str(produto)
        produto = produto.replace("[", "")
        produto = produto.replace("]", "")
        produto = produto.replace("'", "")
        produto = produto.replace("\\n", "")
        lista_projetos_aux.append(produto)
    lista_produtos = lista_projetos_aux
with open("config/arquivos/lista_estoques.txt", "r") as arquivo:
    lista_estoques = arquivo.readlines()
    lista_estoques_aux = []
    for estoque in lista_estoques:
        estoque = estoque.split("|")
        del estoque[1]
        estoque = str(estoque)
        estoque = estoque.replace("[", "")
        estoque = estoque.replace("]", "")
        estoque = estoque.replace("'", "")
        estoque = estoque.replace("\\n", "")
        lista_estoques_aux.append(estoque)
    lista_estoques = lista_estoques_aux
with open("config/arquivos/lista_projetos.txt", "r") as arquivo:
    lista_projetos = arquivo.readlines()
    lista_projetos_aux = []
    for projeto in lista_projetos:
        projeto = projeto.split("|")
        del projeto[1]
        projeto = str(projeto)
        projeto = projeto.replace("[", "")
        projeto = projeto.replace("]", "")
        projeto = projeto.replace("'", "")
        projeto = projeto.replace("\\n", "")
        lista_projetos_aux.append(projeto)
    lista_projetos = lista_projetos_aux

#!SECTION


#SECTION - janela_mov_estoque_func
#NOTE - Instancia Janela
def janela_mov_estoque_func(janela_inicio, prods_selecionados, tipo, prods_ceasa):
    """Instancia a janela de saida de caminhões
    params:
        - ctk: janela_inicio
        - string: tipo
        
    return:
        - None"""
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    janela_saida_caminhao.title("Movimento de estoques")
    janela_saida_caminhao.state("zoomed")
    ctk.set_appearance_mode("dark")

    #SECTION - Funcoes mov
    def get_codigo(nome_produto):
        #NOTE - get_codigo
        """Pega o codigo do produto na lista de produtos
        
        param:
            - string: nome_produto
            
        return:
            - string: codigo"""
        with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
            lista_produtos = arquivo.readlines()
        nome_produto_aux= nome_produto.replace(" ", "")
        for produto in lista_produtos:                
            produto = produto.split("|")
            nome = produto[1]
            nome_aux = nome.replace(" ", "")
            if str(nome_produto_aux) in str(nome_aux):
                codigo = produto[0]
                codigo = codigo.replace(" ", "")
                break
        return codigo
    def get_codigo_local_estoque(nome_estoque):
        #NOTE - get_codigo_local_estoque
        """Pega o codigo do estoque na lista de estoques
        
        param:
            - string: nome_estoque
            
        return:
            - string: codigo_local_estoque"""        
        with open("config/arquivos/lista_estoques.txt", "r") as arquivo:
            lista_estoques = arquivo.readlines()
        try:
            for estoque in lista_estoques:
                if nome_estoque in estoque:
                    estoque = estoque.split("|")
                    codigo_local_estoque = estoque[1]
                    codigo_local_estoque = codigo_local_estoque.replace(" ", "")
                    break
        except:
            codigo_local_estoque = ""
        return codigo_local_estoque
    def get_codigo_projeto(nome_projeto):
        #NOTE - get_codigo_projeto
        """Pega o codigo do projeto na lista de projetos
        
        param:
            - string: nome_projeto
            
        return:
            - string: codigo_projeto"""
        with open("config/arquivos/lista_projetos.txt", "r") as arquivo:
            lista_projetos = arquivo.readlines()
            for projeto in lista_projetos:
                if nome_projeto in projeto:
                    projeto = projeto.split("|")
                    codigo_projeto = projeto[1]
                    codigo_projeto = codigo_projeto.replace(" ", "")
                    break
        return codigo_projeto
    def procurar_estoque_interno():
        #NOTE - procurar_estoque_interno
        """Procura o estoque na lista de estoques

        param:
            - None
        
        return:
            - None"""
        search_text = pesquisar_estoque_interno.get()
        filtered_items = [item for item in lista_estoques if search_text in item]
        if len(filtered_items) <= 0:
            sub_janela_alerta_estoque_não_encontrado()
        combo_estoque_interno.configure(values=filtered_items)
    def procurar_estoque_caminhao():
        #NOTE - procurar_estoque_caminhao
        """Procura o estoque na lista de estoques

        param:
            - None
        
        return:
            - None"""
        search_text = pesquisar_estoque_caminhao.get()
        filtered_items = [item for item in lista_estoques if search_text in item]
        if len(filtered_items) <= 0:
            sub_janela_alerta_estoque_não_encontrado()
        combo_estoque_caminhao.configure(values=filtered_items) 
    def ajustar_estoque_func():
        #NOTE - ajustar_estoque_func
        """Lança um ajuste de movimento de estoque

        param:
            - None
        
        return:
            - None"""
        lista_nome_produto = []
        lista_cod_produto = []
        lista_quantidade_produto = []
        nome_estoque_interno = combo_estoque_interno.get()
        nome_estoque_caminhao = combo_estoque_caminhao.get()
        nota = nota_entry.get()
        produtos_selecionados = text_produtos.get("0.0", "end").strip()
        if produtos_selecionados != "":
            if prods_selecionados != "" and nome_estoque_interno != "" and nome_estoque_caminhao != "":
                for item in prods_selecionados:
                    item = item.split("|")
                    nome_produto = item[0]
                    codigo = get_codigo(nome_produto)
                    quantidade_produto = item[1]
                    lista_nome_produto.append(nome_produto)
                    lista_cod_produto.append(codigo)
                    lista_quantidade_produto.append(quantidade_produto)
                obs_ent = f"{nota}\n\nDe: {nome_estoque_interno}"
                obs_sai = f"{nota}\n\nPara: {nome_estoque_caminhao}"        
                codigo_local_estoque = get_codigo_local_estoque(nome_estoque=nome_estoque_interno)
                
                if codigo_local_estoque != "":
                    codigo_estoque_caminhao = get_codigo_local_estoque(nome_estoque=nome_estoque_caminhao)        
                    for nome_produto, cod_produto, quantidade_produto in zip(lista_nome_produto, lista_cod_produto, lista_quantidade_produto):
                        cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_cod_func(cod_produto)
                        incluir_ajuste_estoque(codigo_produto, quantidade_produto, "SAI", valor_unitario, obs_sai, codigo_local_estoque)
                        incluir_ajuste_estoque(codigo_produto, quantidade_produto, "ENT", valor_unitario, obs_ent, codigo_estoque_caminhao)
                        text_produtos.configure(state="normal")
                        text_produtos.delete("0.0", "end")
                        text_produtos.configure(state="disabled")
                        sub_janela_alerta_sucesso()
                else:
                    sub_janela_alerta_estoque_não_encontrado()
            elif prods_selecionados == "":
                sub_janela_confirmar_produtos_func()
            elif nome_estoque_interno == "" or nome_estoque_caminhao == "":
                sub_janela_alerta_preencher_dados()
        else:
            sub_janela_alerta_prod_nao_encontrado()
    def inicio_func():
        #NOTE - inicio_func 
        janela_saida_caminhao.destroy()
    def procurar_estoque_interno(event):
        #NOTE - procurar_estoque_interno
        estoque_interno = combo_estoque_interno.get()
        if estoque_interno != "":
            filtered_items = [item for item in lista_estoques if unidecode(estoque_interno).upper() in unidecode(item).upper()]
            combo_estoque_interno.configure(values=filtered_items)
            if len(filtered_items) <= 0:
                sub_janela_alerta_estoque_não_encontrado()
        elif estoque_interno == "":
            combo_estoque_interno.configure(values=lista_estoques)
    def procurar_estoque_caminhao(event):
        #NOTE - procurar_estoque_caminhao
        estoque_caminhao = combo_estoque_caminhao.get()
        if estoque_caminhao != "":
            filtered_items = [item for item in lista_estoques if unidecode(estoque_caminhao).upper() in unidecode(item).upper()]
            combo_estoque_caminhao.configure(values=filtered_items)
            if len(filtered_items) <= 0:
                sub_janela_alerta_estoque_não_encontrado()
        elif estoque_caminhao == "":
            combo_estoque_caminhao.configure(values=lista_estoques)
    def selecionar_prod_btn_func():
        #NOTE - selecionar_prod_btn_func
        janela_saida_caminhao.withdraw()
        janela_produtos_func(janela_saida_caminhao, tipo)

    #!SECTION

    #NOTE - Produtos    
    
    #NOTE - frame_1
    frame_1 = ctk.CTkFrame(
        master=janela_saida_caminhao,
        width=1300,
        height=700
    )
    frame_1.pack()
    frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #NOTE - btn_voltar_mov
    img_voltar = ctk.CTkImage(light_image=Image.open("config/arquivos/img/voltar.png"), size=(30,30))
    btn_voltar_mov = ctk.CTkButton(
        master=frame_1,
        width=15,
        height=15,
        text="",
        image=img_voltar,
        fg_color="transparent",
        command=inicio_func
    )
    btn_voltar_mov.place(relx=0.30, rely=0.20, anchor=tkinter.CENTER)

    #NOTE - label_prods_selecionados
    label_prods_selecionados = ctk.CTkLabel(
        master=frame_1,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold")
    )
    label_prods_selecionados.place(relx=0.68, rely=0.18, anchor=tkinter.CENTER)
    text_produtos = ctk.CTkTextbox(
        master=frame_1,
        width=300,
        height=350,
        font=("arial", 12)
    )
    #NOTE - text_produtos
    text_produtos.place(relx=0.68, rely=0.45, anchor=tkinter.CENTER)
    lista_quant_resultado = []
    try:
        prods_selecionados.pop()
        prods_selecionados.pop()
    except:
        pass
    """if len(prods_ceasa) > 0:
        for produto in prods_selecionados:
            nome, quant_selecionado = produto.split(" | ")
            quant_selecionado = int(quant_selecionado.strip())
            for produto_ceasa in prods_ceasa:
                nome_ceasa, quant_ceasa = produto_ceasa.split(" | ")
                quant_ceasa = int(quant_ceasa.strip())
                if nome == nome_ceasa:
                    resultado = quant_selecionado - quant_ceasa
                    lista_quant_resultado.append(f"{nome} | {resultado}")
                    break
        prods_selecionados = lista_quant_resultado"""
    for item in prods_selecionados:
        text_produtos.insert("0.0", f"{item}\n")
    text_produtos.configure(state="disabled")
    
    #NOTE - btn_produtos
    btn_produtos = ctk.CTkButton(
        master=frame_1,
        text="Selecionar Produtos",
        width=200,
        command=selecionar_prod_btn_func
    )
    btn_produtos.place(relx=0.35, rely=0.45, anchor=tkinter.CENTER)

    #NOTE - estoques_interno_text
    estoques_interno_text = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=25
        )
    estoques_interno_text.place(relx=0.35, rely=0.54, anchor=tkinter.CENTER)
    estoques_interno_text.insert("0.0", "Estoque Origem:")
    estoques_interno_text.configure(state="disabled")
    combo_estoque_interno = ctk.CTkComboBox(master=frame_1, values=lista_estoques)
    combo_estoque_interno.place(relx=0.5, rely=0.54, anchor=ctk.CENTER)
    combo_estoque_interno.bind("<Return>", procurar_estoque_interno)
    pesquisar_estoque_interno = ctk.StringVar()
    #NOTE - estoques_caminhao_text
    estoques_caminhao_text = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=25
        )
    estoques_caminhao_text.place(relx=0.35, rely=0.61, anchor=tkinter.CENTER)
    estoques_caminhao_text.insert("0.0", "Estoque Destino:")
    estoques_caminhao_text.configure(state="disabled")
    combo_estoque_caminhao = ctk.CTkComboBox(master=frame_1, values=lista_estoques)
    combo_estoque_caminhao.place(relx=0.5, rely=0.61, anchor=ctk.CENTER)
    combo_estoque_caminhao.bind("<Return>", procurar_estoque_caminhao)
    pesquisar_estoque_caminhao = ctk.StringVar()
    #NOTE - nota_text
    nota_text = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=25
        )
    nota_text.place(relx=0.35, rely=0.68, anchor=tkinter.CENTER)
    nota_text.insert("0.0", "Adicione código da nota:")
    nota_text.configure(state="disabled")
    #NOTE - nota_entry
    nota_entry = ctk.CTkEntry(master=frame_1)
    nota_entry.place(relx=0.5, rely=0.68, anchor=ctk.CENTER)

    #NOTE - btn_mov_estoque
    btn_mov_estoque = ctk.CTkButton(
        master=frame_1,
        text="Movimentar estoque",
        width=200,
        fg_color="#00993D",
        hover_color=("#007830"),
        command=ajustar_estoque_func
    )
    btn_mov_estoque.place(relx=0.68, rely=0.75, anchor=tkinter.CENTER)
    

    janela_saida_caminhao.mainloop()
#!SECTION

