import customtkinter as ctk
import tkinter
from config.instancias.apis.apis_estoque import diferenca_quantidade
from config.instancias.apis.apis_estoque import diferenca_quantidade_estoque
from config.instancias.apis.apis_produtos import listar_produtos_codigo_produto
from config.instancias.apis.apis_produtos import relatorio_quant_diferenca_func

def janela_relatorio_diferenca_func():
    """Mostra a diferença de quantidade de itens não retornados
    
    params:
        - None
        
    retun:
        - None"""
    janela_relatorio_diferenca = ctk.CTk()
    janela_relatorio_diferenca.geometry("800x600")
    master = janela_relatorio_diferenca

    #SECTION - Sub_janelas
    def sub_janela_relatorio_func(produtos_nao_retornados):
        #NOTE - sub_janela_relatorio_func
        """Mostra o relatório de produtos não retornados
        
        params:
            - string: produtos_nao_retornados
            
        return:
            - None"""
        sub_janela_relatorio = ctk.CTkToplevel()
        sub_janela_relatorio.geometry("800x600")
        sub_janela_relatorio.title("Relatório")
        #=============== ABRINDO relatorio_caminhao ===============#
        #with open("config/arquivos/relatorio_caminhao.txt", "r") as arquivo:
            #relatorio_caminhao = arquivo.readlines()

        #NOTE - Texto
        label = ctk.CTkLabel(sub_janela_relatorio, text="Quantidade de produtos não retornados:")
        label.place(relx=0.3, rely=0.1, anchor=ctk.NW)
        #NOTE - Lista
        textbox = ctk.CTkTextbox(
        master=sub_janela_relatorio,
        width=600,
        height=400,
        border_width=2,
        corner_radius=10,
        )
        textbox.insert("0.0", produtos_nao_retornados)
        textbox.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        #for item_relatorio in relatorio_quant_diferenca:
        #    textbox.insert("end", item_relatorio + "\n")
    #!SECTION

    #SECTION - Funções
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
    def procurar_estoque():
        #NOTE - procurar_estoque
        """Procura o estoque na lista de estoques

        param:
            - None
        
        return:
            - None"""
        search_text = pesquisar_estoque.get()
        filtered_items = [item for item in lista_estoques if search_text in item]
        combo_estoque.configure(values=filtered_items)
    def confirmar_estoque_func():
        #NOTE - confirmar_estoque_func
        """Cofirma o estoque escolhido
        
        params:
            - None
            
        return:
            - None"""
        nome_estoque = combo_estoque.get()
        codigo_local_estoque = get_codigo_local_estoque(nome_estoque=nome_estoque)
        produtos_nao_retornados = diferenca_quantidade_estoque(codigo_local_estoque)
        produtos_nao_retornados = f"Quantidade: {produtos_nao_retornados}"
        sub_janela_relatorio = sub_janela_relatorio_func(produtos_nao_retornados)
        janela_relatorio_diferenca.destroy()

        criar_pedido_venda_btn = ctk.CTkButton(master=sub_janela_relatorio, text="Criar pedido de venda")
        criar_pedido_venda_btn.place(relx=0.4, rely=0.9, anchor=ctk.S)

    #!SECTION
    
    #================== Puxando lista de estoques ===================#
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

    estoques_text = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        )
    estoques_text.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
    estoques_text.insert("0.0", "Estoque interno:")
    estoques_text.configure(state="disabled")
    combo_estoque = ctk.CTkComboBox(master, values=lista_estoques)
    combo_estoque.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)    
    pesquisar_estoque = ctk.StringVar()
    filtrar_estoque_entry = ctk.CTkEntry(master, textvariable=pesquisar_estoque)
    filtrar_estoque_entry.place(relx=0.7, rely=0.3, anchor=ctk.CENTER)
    filtrar_btn = ctk.CTkButton(master, text="Filtrar", command=procurar_estoque)
    filtrar_btn.place(relx=0.8, rely=0.3, anchor=ctk.CENTER)

    selecionar_estoque_btn = ctk.CTkButton(master=janela_relatorio_diferenca, text="Selecionar", command=confirmar_estoque_func)
    selecionar_estoque_btn.place(relx=0.8, rely=0.4, anchor=ctk.CENTER)
    
    

    #SECTION - Funções
    def inicio():
        janela_relatorio_diferenca.destroy()

    janela_relatorio_diferenca.mainloop()