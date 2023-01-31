import customtkinter as ctk
from PIL import Image
import tkinter
from unidecode import unidecode
#from config.styles import estilo_janelas_func

#estilo_janela = estilo_janelas_func()
#dimensao = estilo_janela["dimensao"]
font_texto = "arial"
font_btn = "arial"
cor_frame_meio = "#3b3b3b"

lista_produtos_adicionados=[]
#lista_produtos = ["banana", "pera", "abacate", "Cebola", "Cenoura", "Milho"]

def janela_produtos_func(janela_mov_estoque, tipo):
    #NOTE - janela_produtos_func
    """Cria a janela inicial"""
    janela_produtos = ctk.CTk()
    janela_produtos.geometry("1100x580")
    janela_produtos.title("CustomTkinter simple_example.py")
    janela_produtos.state("zoomed")
    

    #SECTION - Funções
    def adicionar_prod_btn_func():
        #NOTE - adicionar_prod_btn_func
        prod_selecionado = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()
        if prod_selecionado != "" and quantidade != "":
            text_prod_selecionados.configure(state="normal")
            text_prod_selecionados.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
            text_prod_selecionados.configure(state="disabled")
            combo_pesquisar_prod.configure(state="normal")
            entry_quantidade.delete("0", "end")
    def adicionar_prod_func(event):
        #NOTE - adicionar_prod_func
        prod_selecionado = combo_pesquisar_prod.get()
        quantidade = entry_quantidade.get()        
        if prod_selecionado != "" and quantidade != "":
            filtered_items = [item for item in lista_produtos if unidecode(prod_selecionado).upper() in unidecode(item).upper()]
            for produto in lista_produtos:
                if unidecode(prod_selecionado).upper() == unidecode(produto).upper():                  
                    text_prod_selecionados.configure(state="normal")
                    text_prod_selecionados.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
                    text_prod_selecionados.configure(state="disabled")
                    combo_pesquisar_prod.configure(state="normal")
                    entry_quantidade.delete("0", "end")
                    break
    def pesquisar_prod_func(event):
        #NOTE - pesquisaar_prod
        produto_pesquisado = combo_pesquisar_prod.get()
        print(f"produto_pesquisado: {produto_pesquisado}")
        #text_prod.configure(state="normal")
        if str(produto_pesquisado) != "":            
            filtered_items = [item for item in lista_produtos if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]
            print(f"filtered_items: {filtered_items}")
            combo_pesquisar_prod.configure(values=filtered_items)
        elif str(produto_pesquisado) == "":
            combo_pesquisar_prod.configure(values=lista_produtos)
    def pesquisar_prod_btn_func():
        #NOTE - pesquisar_prod_btn_func
        produto_pesquisado = combo_pesquisar_prod.get()
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
        janela_mov_estoque = janela_mov_estoque_func(janela_produtos, tipo)
        return prods_selecionados
    #!SECTION


    #SECTION - Centro
    #NOTE - frame_meio
    frame_meio = ctk.CTkFrame(
        master=janela_produtos,
        width=750,
        height=500,
        fg_color="transparent"
        )
    frame_meio.place(relx=0.3, rely=0.3)
    #NOTE - Cabeçalho
    img_voltar = ctk.CTkImage(light_image=Image.open("config/arquivos/img/voltar.png"), size=(30,30))
    btn_voltar = ctk.CTkButton(
        master=frame_meio,
        width=15,
        height=15,
        text="Voltar",
        font=(font_btn, 15),
        #image=img_voltar,
        fg_color="transparent",
    )
    btn_voltar.place(relx=0.30, rely=0.1)
    img_home = ctk.CTkImage(light_image=Image.open("config/arquivos/img/home.png"), size=(30,30))
    btn_inicio = ctk.CTkButton(
        master=frame_meio,
        width=15,
        height=15,
        text="Início",
        font=(font_btn, 15),
        #image=img_home,
        fg_color="transparent"
    )
    btn_inicio.place(relx=0.38, rely=0.1)

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
    btn_lupa.place(relx=0.62, rely=0.36, anchor=tkinter.CENTER)
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
    label_prod_selecionados.place(relx=0.85, rely=0.05, anchor=tkinter.CENTER)
    text_prod_selecionados = ctk.CTkTextbox(
        master=frame_meio,
        width=200,
        height=400,
        font=("Arial", 18)
        )
    text_prod_selecionados.place(relx=0.85, rely=0.48, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")
    #!SECTION

    janela_produtos.mainloop()

#janela_produtos_func()