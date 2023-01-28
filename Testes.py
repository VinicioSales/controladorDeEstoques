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
    #janela_produtos.state("zoomed")

    #SECTION - Funções
    def procurar_produto_func(event):
        #NOTE - procurar_produto
        """Procura o produto na lista de produtos

        param:
            - None
        
        return:
            - None"""
        search_text = combo_produtos.get()
        filtered_items = [item for item in lista_produtos if search_text in item]
        
        combo_produtos.configure(values=filtered_items)
    def adicionar_produtos_func():
        #NOTE - adicionar_produtos_func
        """Adiciona um produto selecionado a uma lista e exibe na tela"""
        produto_selecionado = combo_produtos.get()
        quantidade_produto = entry_quantidade.get()
        produto_quantidade = f"{produto_selecionado} / {quantidade_produto}"
        lista_produtos_adicionados.append(produto_selecionado)
        if produto_selecionado != "" and quantidade_produto != "":
            box_prod_selecionados.configure(state="normal")
            box_prod_selecionados.insert("0.0", f"{produto_quantidade}\n")
            box_prod_selecionados.configure(state="disabled")
    def selecionar_prod_func(event):
        #NOTE - selecionar_prod_func
        prod_selecionado = box_prod.get("0.0", "1.1000")
        print(f'prod: {prod_selecionado}')
        box_prod_selecionados.configure(state="normal")
        box_prod_selecionados.insert("0.0", f"{prod_selecionado}\n")
        box_prod_selecionados.configure(state="disabled")

    def pesquisar_prod_func(event):
        #NOTE - pesquisaar_prod
        produto_pesquisado = entry_pesquisar_prod.get()
        print(f"produto_pesquisado: {produto_pesquisado}")
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


    lista_produtos = ["Banana", "Cebola", "Tomate"]
    #SECTION - BODY
    #SECTION - BLOCO 1
    frame_bloco_1 = ctk.CTkFrame(janela_produtos)
    frame_bloco_1.pack(side="left", anchor="n", padx=10, pady=10)
    frame_bloco_1.configure(width=500, height=300)
    produtos_text = ctk.CTkLabel(frame_bloco_1, text="Selecione o Produto e a Quantidade")
    produtos_text.pack()

    #NOTE - Linha 1.1
    '''produtos_text = ctk.CTkTextbox(
        master=janela_produtos,
        width=475,
        height=25
        )
    produtos_text.place(relx=0.35, rely=0.1, anchor=tkinter.CENTER)
    produtos_text.insert("0.0", "Selecione o Produto e a Quantidade")
    produtos_text.configure(state="disabled")'''

    #NOTE - Linha 1.2  
    '''text_produto = ctk.CTkTextbox(
    master=janela_produtos,
    width=150,
    height=25
    )
    text_produto.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
    text_produto.insert("0.0", "Produto")
    text_produto.configure(state="disabled")
    combo_produtos = ctk.CTkComboBox(master=janela_produtos, values=lista_produtos)
    combo_produtos.place(relx=0.35, rely=0.2, anchor=ctk.CENTER)
    combo_produtos.bind("<Return>", procurar_produto_func)'''
    #btn_pesquisar_prod_funcuto = ctk.CTkButton(master=janela_produtos, text="Pesquisar Produto", command=procurar_produto_func)
    #btn_pesquisar_prod_funcuto.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
    text_produto = ctk.CTkLabel(frame_bloco_1, text="Produto")
    text_produto.pack()
    combo_produtos = ctk.CTkComboBox(frame_bloco_1, values=lista_produtos)
    combo_produtos.pack()
    

    #NOTE - Linha 1.3
    '''text_quantidade = ctk.CTkTextbox(
        master=janela_produtos,
        width=150,
        height=25
    )
    text_quantidade.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    text_quantidade.insert("0.0", "Quantidade")
    text_quantidade.configure(state="disabled")
    entry_quantidade = ctk.CTkEntry(
        master=janela_produtos
    )
    entry_quantidade.place(relx=0.35, rely=0.3, anchor=tkinter.CENTER)'''
    text_quantidade = ctk.CTkLabel(frame_bloco_1, text="Quantidade")
    text_quantidade.pack()
    entry_quantidade = ctk.CTkEntry(frame_bloco_1)
    entry_quantidade.pack()

    #NOTE - Linha 1.4
    '''btn_adicionar_produto = ctk.CTkButton(
        master=janela_produtos,
        width=150,
        height=25,
        text="Adicionar Produto",
        command = adicionar_produtos_func)
    btn_adicionar_produto.place(relx=0.2, rely=0.4, anchor=ctk.CENTER)'''
    btn_adicionar_produto = ctk.CTkButton(frame_bloco_1, text="Adicionar Produto", command=adicionar_produtos_func)
    btn_adicionar_produto.pack()
    #!SECTION

    #SECTION - BLOCO 2
    #NOTE - Linha 2.1
    '''text_prod_selecionados = ctk.CTkTextbox(
        master=janela_produtos,
        width=300,
        height=25
        )
    text_prod_selecionados.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER)
    text_prod_selecionados.insert("0.0", "Produtos Selecionados")
    text_prod_selecionados.configure(state="disabled")
    text_prod_selecionados'''
    frame_bloco_2 = ctk.CTkFrame(janela_produtos)
    frame_bloco_2.pack(side="right", anchor="n", padx=10, pady=10)
    frame_bloco_2.configure(width=300, height=400)
    frame_bloco_2.place(relx=0.83, rely=0.09)
    
    frame_bloco_3 = ctk.CTkFrame(janela_produtos)
    #frame_bloco_3.pack(side="right", anchor="n", padx=10, pady=10)
    frame_bloco_3.configure(width=300, height=400)
    frame_bloco_3.place(relx=0.65, rely=0.09)

    text_prod_selecionados = ctk.CTkLabel(frame_bloco_2, text="Produtos Selecionados")
    #text_prod_selecionados.pack()

    #NOTE - Linha 2.2
    '''box_prod_selecionados = ctk.CTkTextbox(
        master=janela_produtos,
        width=300,
        height=300
        )
    box_prod_selecionados.place(relx=0.85, rely=0.30, anchor=tkinter.CENTER)
    box_prod_selecionados.configure(state="disabled")
    box_prod_selecionados.bind("<Button-1>", selecionar_prod_func)'''
    box_prod_selecionados = ctk.CTkTextbox(
        master=frame_bloco_2,
        width=300,
        height=400)
    box_prod_selecionados.pack()
    
    entry_pesquisar_prod = ctk.CTkEntry(
        master=janela_produtos
    )
    entry_pesquisar_prod.place(relx=0.35, rely=0.4, anchor=tkinter.CENTER)
    entry_pesquisar_prod.bind("<Return>", pesquisar_prod_func)
    
    box_prod = ctk.CTkTextbox(
        master=frame_bloco_3,
        width=300,
        height=400
        )
    box_prod.pack()
    #box_prod.place(relx=0.4, rely=0.30, anchor=tkinter.CENTER)
    lista_teste = ["banana", "pera", "pero"]
    for item in lista_teste:
        box_prod.insert("0.0", f"{item}\n")
    box_prod.configure(state="disabled")
    #box_prod.insert("0.0", f"{lista_teste}")
    box_prod.bind("<Button-1>", selecionar_prod_func)
    

    #box_prod_selecionados.bind("<Return>", printar)
    #!SECTION    
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