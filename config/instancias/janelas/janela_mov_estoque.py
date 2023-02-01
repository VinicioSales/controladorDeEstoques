import customtkinter as ctk
import tkinter
from PIL import Image
from unidecode import unidecode
from config.instancias.apis.apis_estoque import incluir_ajuste_estoque
from config.instancias.apis.apis_produtos import pesquisar_produto_cod_func
from config.instancias.apis.apis_projetos import get_cod_projeto
from config.styles import estilo_janelas_func
from config.instancias.janelas.janela_produtos import janela_produtos_func
from config.instancias.janelas.janela_inicial import janela_inicial_func


#SECTION - janela_produtos


def janela_produtos_func(janela_mov_estoque, tipo):
    #NOTE - janela_produtos_func
    """Cria a janela inicial"""
    janela_produtos = ctk.CTk()
    janela_produtos.title("CustomTkinter simple_example.py")
    janela_produtos.state("zoomed")
    
    font_texto = "arial"
    font_btn = "arial"
    cor_frame_meio = "#3b3b3b"

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
        janela_produtos.destroy()
        janela_mov_estoque = janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo)
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
        width=750,
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
    btn_voltar.place(relx=0.30, rely=0.1)
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
        font=("Arial", 12)
        )
    text_prod_selecionados.place(relx=0.85, rely=0.48, anchor=tkinter.CENTER)
    text_prod_selecionados.configure(state="disabled")
    #!SECTION

    janela_produtos.mainloop()
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

#NOTE - Instancia Janela
def janela_mov_estoque_func(janela_inicio, prods_selecionados, tipo):
    """Instancia a janela de saida de caminhões
    params:
        - ctk: janela_inicio
        - string: tipo
        
    return:
        - None"""
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    janela_saida_caminhao.title("Saida de caminhões")
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
            print(f"nome_produto: {nome_produto} - nome: {nome}")
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
            for estoque in lista_estoques:
                if nome_estoque in estoque:
                    estoque = estoque.split("|")
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
                    projeto = projeto.split("|")
                    codigo_projeto = projeto[1]
                    codigo_projeto = codigo_projeto.replace(" ", "")
                    break
        return codigo_projeto
    '''def procurar_produto():
        #NOTE - procurar_produto
        """Procura o produto na lista de produtos

        param:
            - None
        
        return:
            - None"""
        search_text = pesquisar_produto.get()
        filtered_items = [item for item in lista_produtos if search_text in item]
        combo_produtos.configure(values=filtered_items)'''
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
    def ajustar_estoque_func():
        #NOTE - ajustar_estoque_func
        """Lança um ajuste de movimento de estoque

        param:
            - None
        
        return:
            - None"""
        # Pegando variaveis
        #barra_proresso = ctk.CTkProgressBar(master=frame_1)
        #barra_proresso.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        #barra_proresso.place(relx=0.5, rely=0.8)
        #barra_proresso.configure(mode="indeterminnate")
        #barra_proresso.start()
        

        lista_nome_produto = []
        lista_cod_produto = []
        lista_quantidade_produto = []
        for item in prods_selecionados:
            item = item.split("|")
            nome_produto = item[0]
            codigo = get_codigo(nome_produto)
            quantidade_produto = item[1]
            lista_nome_produto.append(nome_produto)
            lista_cod_produto.append(codigo)
            lista_quantidade_produto.append(quantidade_produto)            

        nome_estoque_interno = combo_estoque_interno.get()
        nome_estoque_caminhao = combo_estoque_caminhao.get()
        #nome_projeto = combo_projeto.get()
        nota = nota_entry.get()
        obs_ent = f"{nota},\n\nentrada"
        obs_sai = f"{nota},\n\nsaida"        
        codigo_local_estoque = get_codigo_local_estoque(nome_estoque=nome_estoque_interno)
        codigo_estoque_caminhao = get_codigo_local_estoque(nome_estoque=nome_estoque_caminhao)        
        for nome_produto, cod_produto, quantidade_produto in zip(lista_nome_produto, lista_cod_produto, lista_quantidade_produto):
            cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_cod_func(cod_produto)
            incluir_ajuste_estoque(codigo_produto, quantidade_produto, "SAI", valor_unitario, obs_ent, codigo_local_estoque)
            incluir_ajuste_estoque(codigo_produto, quantidade_produto, "ENT", valor_unitario, obs_sai, codigo_estoque_caminhao)
    def inicio_func():
        #NOTE - inicio_func 
        janela_saida_caminhao.destroy()
    def procurar_estoque_interno(event):
        #NOTE - procurar_estoque_interno
        estoque_interno = combo_estoque_interno.get()
        if estoque_interno != "":
            filtered_items = [item for item in lista_estoques if unidecode(estoque_interno).upper() in unidecode(item).upper()]
            combo_estoque_interno.configure(values=filtered_items)
        elif estoque_interno == "":
            combo_estoque_interno.configure(values=lista_estoques)
    def procurar_estoque_caminhao(event):
        #NOTE - procurar_estoque_caminhao
        estoque_caminhao = combo_estoque_caminhao.get()
        if estoque_caminhao != "":
            filtered_items = [item for item in lista_estoques if unidecode(estoque_caminhao).upper() in unidecode(item).upper()]
            combo_estoque_caminhao.configure(values=filtered_items)
        elif estoque_caminhao == "":
            combo_estoque_caminhao.configure(values=lista_estoques)
    def selecionar_prod_btn_func():
        #NOTE - selecionar_prod_btn_func
        janela_saida_caminhao.withdraw()
        janela_produtos_func(janela_saida_caminhao, tipo)

    #!SECTION

    #NOTE - Produtos    
    
    #NOTE - Frame
    frame_1 = ctk.CTkFrame(
        master=janela_saida_caminhao,
        width=1300,
        height=700
    )
    frame_1.pack()
    frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #NOTE - Cabeçalho
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

    #NOTE - text_produtos
    label_prods_selecionados = ctk.CTkLabel(
        master=frame_1,
        text="Produtos Selecionados",
        font=("Arial", 15, "bold")
    )
    label_prods_selecionados.place(relx=0.68, rely=0.18, anchor=tkinter.CENTER)
    text_produtos = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=350,
        font=("arial", 12)
    )
    text_produtos.place(relx=0.68, rely=0.45, anchor=tkinter.CENTER)
    for item in prods_selecionados:
        text_produtos.insert("0.0", f"{item}\n")
    text_produtos.configure(state="disabled")
    
    #NOTE - Selecionar Produtos
    btn_produtos = ctk.CTkButton(
        master=frame_1,
        text="Selecionar Produtos",
        width=200,
        command=selecionar_prod_btn_func
    )
    btn_produtos.place(relx=0.35, rely=0.52, anchor=tkinter.CENTER)

    #NOTE - Estoque
    #============= Estoque ===============#
    estoques_interno_text = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=25
        )
    estoques_interno_text.place(relx=0.35, rely=0.61, anchor=tkinter.CENTER)
    estoques_interno_text.insert("0.0", "Estoque Origem:")
    estoques_interno_text.configure(state="disabled")
    combo_estoque_interno = ctk.CTkComboBox(master=frame_1, values=lista_estoques)
    combo_estoque_interno.place(relx=0.5, rely=0.61, anchor=ctk.CENTER)
    combo_estoque_interno.bind("<Return>", procurar_estoque_interno)
    pesquisar_estoque_interno = ctk.StringVar()
    estoques_caminhao_text = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=25
        )
    estoques_caminhao_text.place(relx=0.35, rely=0.68, anchor=tkinter.CENTER)
    estoques_caminhao_text.insert("0.0", "Estoque Destino:")
    estoques_caminhao_text.configure(state="disabled")
    combo_estoque_caminhao = ctk.CTkComboBox(master=frame_1, values=lista_estoques)
    combo_estoque_caminhao.place(relx=0.5, rely=0.68, anchor=ctk.CENTER)
    combo_estoque_caminhao.bind("<Return>", procurar_estoque_caminhao)
    pesquisar_estoque_caminhao = ctk.StringVar()
    
    nota_text = ctk.CTkTextbox(
        master=frame_1,
        width=200,
        height=25
        )
    nota_text.place(relx=0.35, rely=0.75, anchor=tkinter.CENTER)
    nota_text.insert("0.0", "Adicione código da nota:")
    nota_text.configure(state="disabled")
    nota_entry = ctk.CTkEntry(master=frame_1)
    nota_entry.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

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

prods_selecionados = ""
#janela_mov_estoque_func("janela_inicio", prods_selecionados, "SAI")