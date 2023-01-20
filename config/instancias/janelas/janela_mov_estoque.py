import customtkinter as ctk
import tkinter
from config.instancias.apis.apis_estoque import incluir_ajuste_estoque
from config.instancias.apis.apis_produtos import pesquisar_produto_func
from config.styles import estilo_janelas_func


estilo_janela = estilo_janelas_func()
dimensao = estilo_janela["dimensao"]
#SECTION - Abrindo arquivos
with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
    lista_produtos = arquivo.readlines()
    lista_projetos_aux = []
    for produto in lista_produtos:
        produto = produto.split("-")
        del produto[0]
        produto = str(produto)
        produto = produto.replace("[", "")
        produto = produto.replace("]", "")
        produto = produto.replace("'", "")
        produto = produto.replace("\\n", "")
        produto = produto.replace(" ", "")
        lista_projetos_aux.append(produto)
    lista_produtos = lista_projetos_aux
with open("config/arquivos/lista_estoques.txt", "r") as arquivo:
    lista_estoques = arquivo.readlines()
    lista_estoques_aux = []
    for estoque in lista_estoques:
        estoque = estoque.split("-")
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
        projeto = projeto.split("-")
        del projeto[1]
        projeto = str(projeto)
        projeto = projeto.replace("[", "")
        projeto = projeto.replace("]", "")
        projeto = projeto.replace("'", "")
        projeto = projeto.replace("\\n", "")
        lista_projetos_aux.append(projeto)
    lista_projetos = lista_projetos_aux

#!SECTION

#NOTE - Instancia Janela
def janela_mov_estoque_func(tipo):
    """Instancia a janela de saida de caminhões
    params:
        - string: tipo
        
    return:
        - None"""
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    janela_saida_caminhao.title("Saida de caminhões")
    master = janela_saida_caminhao

    #SECTION - Funcoes
    def get_codigo(nome_produto):
        #NOTE - get_codigo
        """Pega o codigo do produto na lista de produtos
        
        param:
            - string: nome_produto
            
        return:
            - string: codigo"""
        with open("config/arquivos/lista_produtos.txt", "r") as arquivo:
            lista_produtos = arquivo.readlines()
            for produto in lista_produtos:
                if nome_produto in produto:
                    produto = produto.split("-")
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
            for estoque in lista_estoques:
                if nome_estoque in estoque:
                    estoque = estoque.split("-")
                    codigo_local_estoque = estoque[1]
                    codigo_local_estoque = codigo_local_estoque.replace(" ", "")
                    break
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
                    projeto = projeto.split("-")
                    codigo_projeto = projeto[1]
                    codigo_projeto = codigo_projeto.replace(" ", "")
                    break
        return codigo_projeto
    def procurar_produto():
        #NOTE - procurar_produto
        """Procura o produto na lista de produtos

        param:
            - None
        
        return:
            - None"""
        search_text = pesquisar_produto.get()
        filtered_items = [item for item in lista_produtos if search_text in item]
        combo_produtos.configure(values=filtered_items)
    def procurar_estoque_interno():
        #NOTE - procurar_estoque_interno
        """Procura o estoque na lista de estoques

        param:
            - None
        
        return:
            - None"""
        search_text = pesquisar_estoque_interno.get()
        filtered_items = [item for item in lista_estoques if search_text in item]
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
        combo_estoque_caminhao.configure(values=filtered_items)
    def procurar_projeto():
        #NOTE - procurar_projeto
        """Procura o projeto pesquisado
        
        params:
            - None
        
        return:
            - None"""
        search_text = pesquisar_projeto.get()
        filtered_items = [item for item in lista_projetos if search_text in item]
        combo_projeto.configure(values=filtered_items)    
    def ajustar_estoque_func():
        #NOTE - ajustar_estoque_func
        """Lança um ajuste de movimento de estoque

        param:
            - None
        
        return:
            - None"""
        # Pegando variaveis
        nome_produto = combo_produtos.get()
        quantidade_itens = quantidade_itens_entry.get()
        nome_estoque_interno = combo_estoque_interno.get()
        nome_estoque_caminhao = combo_estoque_caminhao.get()
        nome_projeto = combo_projeto.get()
        nota = nota_entry.get()
        if tipo == "SAI":
            mov_obg = "saida"
        if tipo == "ENT":
            mov_obg = "entrada"
        obs = f"{nota},\n\n{mov_obg}"        
        codigo = get_codigo(nome_produto)

        
        codigo_local_estoque = get_codigo_local_estoque(nome_estoque=nome_estoque_interno)
        codigo_estoque_caminhao = get_codigo_local_estoque(nome_estoque=nome_estoque_caminhao)
        codigo_projeto = get_codigo_projeto(nome_projeto=nome_projeto)
        cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_func(codigo)
        if tipo == "SAI":
            #descricao_status, id_movest, id_ajuste = incluir_ajuste_estoque(codigo_produto, quantidade_itens, tipo, valor_unitario, obs, codigo_local_estoque, codigo_estoque_caminhao)
            descricao_status, id_movest, id_ajuste = incluir_ajuste_estoque(codigo_produto, quantidade_itens, "SAI", valor_unitario, obs, codigo_local_estoque)
            descricao_status, id_movest, id_ajuste = incluir_ajuste_estoque(codigo_produto, quantidade_itens, "ENT", valor_unitario, obs, codigo_estoque_caminhao)
        elif tipo == "ENT":
            produtos_ceasa = produtos_ceasa_entry.get()
            if produtos_ceasa == "":
                produtos_ceasa = "0"
            relatorio_ceasa = f"{nome_produto} * {codigo_produto} * {produtos_ceasa}"
            with open("config/arquivos/lista_produtos_ceasa.txt", "r") as arquivo:
                lista_produtos_ceasa = arquivo.readlines()
                lista_produtos_ceasa.append(f"{relatorio_ceasa}\n")
            with open("config/arquivos/lista_produtos_ceasa.txt", "w") as arquivo:
                arquivo.writelines(lista_produtos_ceasa)
                #descricao_status, id_movest, id_ajuste = incluir_ajuste_estoque(codigo_produto, quantidade_itens, tipo, valor_unitario, obs, codigo_estoque_caminhao, codigo_local_estoque)
                descricao_status, id_movest, id_ajuste = incluir_ajuste_estoque(codigo_produto, quantidade_itens, "ENT", valor_unitario, obs, codigo_local_estoque)
                descricao_status, id_movest, id_ajuste = incluir_ajuste_estoque(codigo_produto, quantidade_itens, "SAI", valor_unitario, obs, codigo_estoque_caminhao)
        
    def inicio_func():
        janela_saida_caminhao.destroy()
    #!SECTION

    #NOTE - Produtos
    #============= Produtos ================#
    produtos_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    produtos_text.place(relx=0.3, rely=0.1, anchor=tkinter.CENTER)
    produtos_text.insert("0.0", "Selecione o produto")
    produtos_text.configure(state="disabled")
    combo_produtos = ctk.CTkComboBox(master, values=lista_produtos)
    combo_produtos.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    pesquisar_produto = ctk.StringVar()
    filtrar_produto_entry = ctk.CTkEntry(master, textvariable=pesquisar_produto)
    filtrar_produto_entry.place(relx=0.7, rely=0.1, anchor=ctk.CENTER)
    filtrar_produto_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_produto)
    filtrar_produto_btn.place(relx=0.8, rely=0.1, anchor=ctk.CENTER)

    #NOTE - Itens
    #============= Itens ================#
    quantidade_itens_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    quantidade_itens_text.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
    quantidade_itens_text.insert("0.0", "Quantidade de itens")
    quantidade_itens_text.configure(state="disabled")
    quantidade_itens_entry = ctk.CTkEntry(
        master=master,
        width=150,
        height=25)
    quantidade_itens_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    if tipo == "ENT":
        produtos_ceasa_text = ctk.CTkTextbox(
            master,
            width=150,
            height=25
            )
        produtos_ceasa_text.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)
        produtos_ceasa_text.insert("0.0", "Produtos na Ceasa")
        produtos_ceasa_text.configure(state="disabled")
        produtos_ceasa_entry = ctk.CTkEntry(
            master=master,
            width=150,
            height=25)
        produtos_ceasa_entry.place(relx=0.9, rely=0.2, anchor=tkinter.CENTER)     

    #NOTE - Estoque
    #============= Estoque ===============#
    estoques_interno_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    estoques_interno_text.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
    estoques_interno_text.insert("0.0", "Estoque interno:")
    estoques_interno_text.configure(state="disabled")
    combo_estoque_interno = ctk.CTkComboBox(master, values=lista_estoques)
    combo_estoque_interno.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)    
    pesquisar_estoque_interno = ctk.StringVar()
    filtrar_estoque_interno_entry = ctk.CTkEntry(master, textvariable=pesquisar_estoque_interno)
    filtrar_estoque_interno_entry.place(relx=0.7, rely=0.3, anchor=ctk.CENTER)
    filtrar_interno_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_estoque_interno)
    filtrar_interno_btn.place(relx=0.8, rely=0.3, anchor=ctk.CENTER)
    estoques_caminhao_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    estoques_caminhao_text.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
    estoques_caminhao_text.insert("0.0", "Estoque caminhao:")
    estoques_caminhao_text.configure(state="disabled")
    combo_estoque_caminhao = ctk.CTkComboBox(master, values=lista_estoques)
    combo_estoque_caminhao.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)    
    pesquisar_estoque_caminhao = ctk.StringVar()
    filtrar_estoque_caminhao_entry = ctk.CTkEntry(master, textvariable=pesquisar_estoque_caminhao)
    filtrar_estoque_caminhao_entry.place(relx=0.7, rely=0.4, anchor=ctk.CENTER)
    filtrar_caminhao_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_estoque_caminhao)
    filtrar_caminhao_btn.place(relx=0.8, rely=0.4, anchor=ctk.CENTER)


    #NOTE - Projeto
    #============== Projeto ==============#
    projeto_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    projeto_text.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)
    projeto_text.insert("0.0", "Selecione o projeto:")
    projeto_text.configure(state="disabled")
    combo_projeto = ctk.CTkComboBox(master, values=lista_projetos)
    combo_projeto.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    pesquisar_projeto = ctk.StringVar()
    projeto_entry = ctk.CTkEntry(master, textvariable=pesquisar_projeto)
    projeto_entry.place(relx=0.7, rely=0.5, anchor=ctk.CENTER)
    filtrar_projeto_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_projeto)
    filtrar_projeto_btn.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)

    #NOTE - Numero Nota
    #============== Numero Nota ==============#
    nota_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    nota_text.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
    nota_text.insert("0.0", "Adicione código da nota:")
    nota_text.configure(state="disabled")
    nota_entry = ctk.CTkEntry(master)
    nota_entry.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

    #NOTE - Rodapé
    inicio_btn = ctk.CTkButton(master, text="início", command=inicio_func)
    inicio_btn.place(relx=0.6, rely=0.8, anchor=ctk.CENTER)
    enviar_btn = ctk.CTkButton(master, text="Enviar", command=ajustar_estoque_func)
    enviar_btn.place(relx=0.8, rely=0.8, anchor=ctk.CENTER)

    janela_saida_caminhao.mainloop()

