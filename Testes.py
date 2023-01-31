import customtkinter as ctk
from PIL import Image
import tkinter
from unidecode import unidecode
#from config.styles import estilo_janelas_func

#estilo_janela = estilo_janelas_func()
#dimensao = estilo_janela["dimensao"]
font_texto = "arial"
font_btn = "arial"

lista_produtos_adicionados=[]
lista_produtos = ["banana", "pera", "abacate", "Cebola", "Cenoura", "Milho"]

def janela_produtos_func():
    #NOTE - janela_produtos_func
    """Cria a janela inicial"""
    janela_produtos = ctk.CTk()
    janela_produtos.geometry("1100x580")
    janela_produtos.title("CustomTkinter simple_example.py")
    janela_produtos._set_appearance_mode("dark")
    janela_produtos.state("zoomed")

    #SECTION - Funções
    def adicionar_prod_btn_func():
        #NOTE - adicionar_prod_btn_func
        prod_selecionado = entry_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        if prod_selecionado != "" and quantidade != "":
            text_prod_selecionados.configure(state="normal")
            text_prod_selecionados.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
            text_prod_selecionados.configure(state="disabled")
            entry_pesquisar_prod.configure(state="normal")
            entry_pesquisar_prod.delete("0", "end")
            entry_quantidade.delete("0", "end")
    def adicionar_prod_func(event):
        #NOTE - adicionar_prod_func
        prod_selecionado = entry_pesquisar_prod.get()
        quantidade = entry_quantidade.get()        
        if prod_selecionado != "" and quantidade != "":
            filtered_items = [item for item in lista_produtos if unidecode(prod_selecionado).upper() in unidecode(item).upper()]
            for produto in lista_produtos:
                print(f"prod_selecionado: {prod_selecionado} - produto: {produto}")
                if unidecode(prod_selecionado).upper() == unidecode(produto).upper():                  
                    text_prod_selecionados.configure(state="normal")
                    text_prod_selecionados.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
                    text_prod_selecionados.configure(state="disabled")
                    entry_pesquisar_prod.configure(state="normal")   
                    entry_pesquisar_prod.delete("0", "end")
                    entry_quantidade.delete("0", "end")
                    break
    def pesquisar_prod_func(event):
        #NOTE - pesquisaar_prod
        produto_pesquisado = entry_pesquisar_prod.get()
        text_prod.configure(state="normal")
        if str(produto_pesquisado) == "":
            text_prod.delete("1.0", "end")
            '''for item in lista_produtos:                
                text_prod.insert("0.0", f"{item}\n")'''
        elif str(produto_pesquisado) != "":            
            filtered_items = [item for item in lista_produtos if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]        
            text_prod.delete("1.0", "end")
            for item in filtered_items:
                text_prod.insert("0.0", f"{item}\n")
        text_prod.configure(state="disabled")
    def pesquisar_prod_btn_func():
        #NOTE - pesquisar_prod_btn_func
        produto_pesquisado = entry_pesquisar_prod.get()
        text_prod.configure(state="normal")
        if str(produto_pesquisado) == "":
            text_prod.delete("1.0", "end")
            '''for item in lista_produtos:                
                text_prod.insert("0.0", f"{item}\n")'''
        elif str(produto_pesquisado) != "":            
            filtered_items = [item for item in lista_produtos if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]        
            text_prod.delete("1.0", "end")
            for item in filtered_items:
                text_prod.insert("0.0", f"{item}\n")
        text_prod.configure(state="disabled")
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
        for index, item in enumerate(prods_selecionados):
            if item == "":
                del prods_selecionados[index]
        if prods_selecionados[-1] == "":
            prods_selecionados.pop()
        janela_produtos.withdraw()
    #!SECTION


    #SECTION - Centro
    #NOTE - Cabeçalho
    img_voltar = ctk.CTkImage(light_image=Image.open("config/arquivos/img/voltar.png"), size=(30,30))
    btn_voltar = ctk.CTkButton(
        master=janela_produtos,
        width=15,
        height=15,
        text="",
        font=(font_btn, 15),
        image=img_voltar,
        fg_color="transparent"
    )
    btn_voltar.place(relx=0.39, rely=0.2)
    img_home = ctk.CTkImage(light_image=Image.open("config/arquivos/img/home.png"), size=(30,30))
    btn_inicio = ctk.CTkButton(
        master=janela_produtos,
        width=15,
        height=15,
        text="",
        font=(font_btn, 15),
        image=img_home,
        fg_color="transparent"
    )
    btn_inicio.place(relx=0.43, rely=0.2)

    #NOTE - frame_central
    frame_central = ctk.CTkFrame(
        master=janela_produtos,
        width=300,
        height=326,
        fg_color= ("#3b3b3b")
    )
    frame_central.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    label_pesquisar_prod = ctk.CTkLabel(
        master=janela_produtos,
        text="Produtos",
        font= (font_texto, 18),
        fg_color= ("#3b3b3b")
    )
    label_pesquisar_prod.place(relx=0.50, rely=0.32, anchor=tkinter.CENTER)
    entry_pesquisar_prod = ctk.CTkEntry(
        master=janela_produtos,
        width=150,
        height=25,
        fg_color= ("#3b3b3b"))
    entry_pesquisar_prod.place(relx=0.50, rely=0.36, anchor=tkinter.CENTER)
    #entry_pesquisar_prod.bind("<Return>", pesquisar_prod_func)
    img_lupa = ctk.CTkImage(light_image=Image.open("config/arquivos/img/lupa.png"))
    btn_lupa = ctk.CTkButton(
        master=janela_produtos,
        image=img_lupa,
        text="",
        width=8,
        height=8,
        fg_color="transparent",
        hover=False,
        bg_color=("#3b3b3b")
    )
    btn_lupa.place(relx=0.57, rely=0.36, anchor=tkinter.CENTER)
    label_quantidade = ctk.CTkLabel(
        master=janela_produtos,
        text="Quantidade",
        font=(font_texto, 18),
        fg_color= ("#3b3b3b")
    )
    label_quantidade.place(relx=0.50, rely=0.40, anchor=tkinter.CENTER)
    entry_quantidade = ctk.CTkEntry(
        master=janela_produtos,
        width=150,
        height=25,)
    entry_quantidade.place(relx=0.50, rely=0.44, anchor=tkinter.CENTER)
    entry_quantidade.bind("<Return>", adicionar_prod_func)
    btn_adicionar_produto = ctk.CTkButton(
        master=janela_produtos,
        width=150,
        height=25,
        text="Adicionar Produto",
        font=(font_btn, 15),
        border_width=0,
        command = adicionar_prod_btn_func)
    btn_adicionar_produto.place(relx=0.50, rely=0.50, anchor=ctk.CENTER)
    
    #NOTE - Produtos Selecionados
    btn_remover_ultimo = ctk.CTkButton(
        master=janela_produtos,
        width=125,
        height=25,
        text="Remover último produto",
        font=(font_btn, 13),
        command = remover_ultimo_btn_func)
    btn_remover_ultimo.place(relx=0.50, rely=0.55, anchor=ctk.CENTER)
    btn_limpar = ctk.CTkButton(
        master=janela_produtos,
        width=150,
        height=25,
        text="Limpar",
        font=(font_btn, 15),
        command = limpar_prods_selecionados)
    btn_limpar.place(relx=0.50, rely=0.60, anchor=ctk.CENTER)
    btn_confirmar = ctk.CTkButton(
        master=janela_produtos,
        width=150,
        height=25,
        text="Confirmar",
        font=(font_btn, 15),
        fg_color="#00993D",
        hover_color=("#007830"),
        command=confirmar_btn_func
    )
    btn_confirmar.place(relx=0.50, rely=0.67, anchor=tkinter.CENTER)
    #!SECTION

    #SECTION - Direita
    #NOTE - Produtos Selecionados
    label_prod_selecionados = ctk.CTkLabel(
        master=janela_produtos,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold")
        )
    label_prod_selecionados.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
    text_prod_selecionados = ctk.CTkTextbox(
        master=janela_produtos,
        width=200,
        height=400,
        font=("Arial", 18)
        )
    text_prod_selecionados.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")
    #!SECTION

    janela_produtos.mainloop()

    return janela_produtos

janela_produtos_func()