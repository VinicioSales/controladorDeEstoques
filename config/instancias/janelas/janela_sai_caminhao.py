import customtkinter as ctk
import tkinter

#NOTE - Abrindo arquivos
with open("config/arquivos/lista_estoques.txt", "r") as arquivo:
    lista_estoques = arquivo.readlines()

with open("config/arquivos/lista_projetos.txt", "r") as arquivo:
    lista_projetos = arquivo.readlines()

#NOTE - Instancia Janela
dimensao = "1100x580"
def janela_saida_caminhoes_func():    
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    janela_saida_caminhao.title("Saida de caminhões")
    master = janela_saida_caminhao

    #NOTE - Funcoes
    def procurar_estoque():
        search_text = pesquisar_estoque.get()
        filtered_items = [item for item in lista_estoque if search_text in item]
        combo_estoque.configure(values=filtered_items)
    def procurar_projeto():
        search_text = pesquisar_projeto.get()
        filtered_items = [item for item in lista_projetos if search_text in item]
        combo_projeto.configure(values=filtered_items)
    def ajustar_estoque_func():
        quantidade_itens = quantidade_itens_entry.get()
        nome_estoque = combo_estoque.get()
        nome_projeto = combo_projeto.get()
        print(f"quantidade_itens: {quantidade_itens}")
        print(f"variavel: {nome_estoque}")
        print(f"nome_projeto: {nome_projeto}")
        #incluir_ajuste_estoque(codigo_pesquisa, quan, tipo, valor, obs, codigo_local_estoque)
    
    #NOTE - Itens
    #============= Itens ================#
    quantidade_itens_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        #border_width=2,
        #corner_radius=10,
        )
    quantidade_itens_text.place(relx=0.3, rely=0.1, anchor=tkinter.CENTER)
    quantidade_itens_text.insert("0.0", "Quantidade de itens")
    quantidade_itens_text.configure(state="disabled")
    quantidade_itens_entry = ctk.CTkEntry(
        master=master,
        width=200,
        height=25)
    quantidade_itens_entry.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    #NOTE - Estoque
    #============= Estoque ===============#
    estoques_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    estoques_text.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
    estoques_text.insert("0.0", "Selecione o estoque:")
    estoques_text.configure(state="disabled")
    combo_estoque = ctk.CTkComboBox(master, values=lista_estoques)
    combo_estoque.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)    
    pesquisar_estoque = ctk.StringVar()
    filtrar_estoque_entry = ctk.CTkEntry(master, textvariable=pesquisar_estoque)
    filtrar_estoque_entry.place(relx=0.7, rely=0.2, anchor=ctk.CENTER)
    filtrar_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_estoque)
    filtrar_btn.place(relx=0.8, rely=0.2, anchor=ctk.CENTER)

    #NOTE - Projeto
    #============== Projeto ==============#
    projeto_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        #border_width=2,
        #corner_radius=10,
        )
    projeto_text.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
    projeto_text.insert("0.0", "Selecione o projeto:")
    projeto_text.configure(state="disabled")
    combo_projeto = ctk.CTkComboBox(master, values=lista_projetos)
    combo_projeto.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
    pesquisar_projeto = ctk.StringVar()
    projeto_entry = ctk.CTkEntry(master, textvariable=pesquisar_projeto)
    projeto_entry.place(relx=0.7, rely=0.3, anchor=ctk.CENTER)
    filtrar_projeto_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_projeto)
    filtrar_projeto_btn.place(relx=0.8, rely=0.3, anchor=ctk.CENTER)

    #NOTE - Rodapé
    enviar_btn = ctk.CTkButton(master, text="Enviar", command=ajustar_estoque_func)
    enviar_btn.place(relx=0.8, rely=0.4, anchor=ctk.CENTER)

    janela_saida_caminhao.mainloop()

