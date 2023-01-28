import customtkinter as ctk
import tkinter
from unidecode import unidecode
#from config.styles import estilo_janelas_func

#estilo_janela = estilo_janelas_func()
#dimensao = estilo_janela["dimensao"]

lista_produtos_adicionados=[]

def janela_produtos_func():
    #NOTE - janela_produtos_func
    """Cria a janela inicial"""
    janela_produtos = ctk.CTk()
    janela_produtos.geometry("1100x580")
    janela_produtos.title("CustomTkinter simple_example.py")
    janela_produtos._set_appearance_mode("dark")
    janela_produtos.state("zoomed")

    #SECTION - Funções
    def selecionar_prod_func(event):
        #NOTE - selecionar_prod_func
        prod_selecionado = box_prod.get("0.0", "1.1000")
        box_prod_selecionados.configure(state="normal")
        box_prod_selecionados.insert("0.0", f"{prod_selecionado}\n")
        box_prod_selecionados.configure(state="disabled")
    def selecionar_prod_btn_func():
        #NOTE - selecionar_prod_func
        prod_selecionado = box_prod.get("0.0", "1.1000")
        box_prod_selecionados.configure(state="normal")
        box_prod_selecionados.insert("0.0", f"{prod_selecionado}\n")
        box_prod_selecionados.configure(state="disabled")
    def pesquisar_prod_func(event):
        #NOTE - pesquisaar_prod
        produto_pesquisado = entry_pesquisar.get()
        box_prod.configure(state="normal")
        if str(produto_pesquisado) == "":
            box_prod.delete("1.0", "end")
            for item in lista_teste:                
                box_prod.insert("0.0", f"{item}\n")
                print(f"item: {item}")
        elif str(produto_pesquisado) != "":            
            filtered_items = [item for item in lista_teste if unidecode(produto_pesquisado).upper() in unidecode(item).upper()]        
            box_prod.delete("1.0", "end")
            for item in filtered_items:
                box_prod.insert("0.0", f"{item}\n")
        box_prod.configure(state="disabled")
    #!SECTION


    #SECTION - BODY
    #NOTE - Quantidade
    text_quantidade = ctk.CTkTextbox(
        master=janela_produtos,
        width=150,
        height=25
    )
    text_quantidade.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    text_quantidade.insert("0.0", "Quantidade")
    text_quantidade.configure(state="disabled")
    entry_quantidade = ctk.CTkEntry(master=janela_produtos)
    entry_quantidade.place(relx=0.35, rely=0.3, anchor=tkinter.CENTER)

    #NOTE - Produtos
    entry_pesquisar = ctk.CTkEntry(master=janela_produtos)
    entry_pesquisar.place(relx=0.64, rely=0.1, anchor=tkinter.CENTER)
    entry_pesquisar.bind("<Return>", pesquisar_prod_func)
    btn_adicionar_produto = ctk.CTkButton(
        master=janela_produtos,
        width=150,
        height=25,
        text="Adicionar Produto",
        command = selecionar_prod_btn_func)
    btn_adicionar_produto.place(relx=0.72, rely=0.1, anchor=ctk.CENTER)
    box_prod = ctk.CTkTextbox(
        master=janela_produtos,
        width=300,
        height=400
        )
    box_prod.place(relx=0.68, rely=0.32, anchor=tkinter.CENTER)
    lista_teste = ["banana", "pera", "pero"]
    #NOTE - Preenchendo Box produtos
    for item in lista_teste:
        box_prod.insert("0.0", f"{item}\n")
    box_prod.configure(state="disabled")
    box_prod.bind("<Button-1>", selecionar_prod_func)
    
    #NOTE - Produtos Selecionados
    text_prod_selecionados = ctk.CTkTextbox(
        master=janela_produtos,
        width=300,
        height=25
        )
    text_prod_selecionados.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER)
    text_prod_selecionados.insert("0.0", "Produtos Selecionados")
    text_prod_selecionados.configure(state="disabled")
    box_prod_selecionados = ctk.CTkTextbox(
        master=janela_produtos,
        width=300,
        height=400
        )
    box_prod_selecionados.place(relx=0.85, rely=0.32, anchor=tkinter.CENTER)
    box_prod_selecionados.configure(state="disabled")
    box_prod_selecionados.bind("<Button-1>", selecionar_prod_func)
    #!SECTION

    
    #SECTION - Rodapé
    btn_confirmar = ctk.CTkButton(
        master=janela_produtos,
        text="Confirmar"
    )
    btn_confirmar.place(relx=0.4, rely=0.8)

    janela_produtos.mainloop()

    return janela_produtos

janela_produtos_func()