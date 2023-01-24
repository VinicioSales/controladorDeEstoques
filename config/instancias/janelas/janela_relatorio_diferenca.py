import customtkinter as ctk
import tkinter
from datetime import date
from config.instancias.apis.apis_estoque import diferenca_quantidade_estoque_produto
from config.instancias.apis.apis_vendas import incluir_pedido_venda
from config.instancias.apis.apis_produtos import pesquisar_produto_nome_func

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
    def sub_janela_relatorio_func(produtos_nao_retornados_text, produtos_nao_retornados):
        #NOTE - sub_janela_relatorio_func
        """Mostra o relatório de produtos não retornados
        
        params:
            - string: produtos_nao_retornados
            
        return:
            - None"""
        sub_janela_relatorio = ctk.CTkToplevel()
        sub_janela_relatorio.geometry("800x600")
        sub_janela_relatorio.title("Relatório")

        #SECTION - Funcoes Sub        
        def criar_pedido_venda_btn_func():
            #NOTE - criar_pedido_venda_btn_func
            for linha in quant_diferenca_estoque:
                linha = linha.split("*")
                nome_produto = linha[0]
                quantidade_prod = linha[1]
                quantidade_prod = quantidade_prod.replace(" ", "")
                quantidade_prod = quantidade_prod.replace("\n", "")
                #================ TESTE =================#
                codigo_cliente = "6873272007"
                data_previsao = date.today()
                data_previsao = data_previsao.strftime("%d/%m/%Y")
                #================ TESTE =================#
                cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_nome_func(nome_produto)
                
                incluir_pedido_venda(codigo_produto, codigo_cliente, data_previsao, cfop, descricao , ncm ,unidade, valor_unitario, quantidade_prod)
        #!SECTION
        #NOTE - Texto
        label = ctk.CTkLabel(sub_janela_relatorio, text="Quantidade de produtos não retornados:")
        label.place(relx=0.3, rely=0.1, anchor=ctk.NW)
        #NOTE - produtos_nao_retornados
        textbox = ctk.CTkTextbox(
        master=sub_janela_relatorio,
        width=600,
        height=5,
        border_width=2,
        corner_radius=10,
        )
        textbox.insert("0.0", produtos_nao_retornados_text)
        textbox.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        #NOTE - quant_diferenca_estoque
        with open(f"config/arquivos/quant_diferenca_estoque.txt", "r") as arquivo:
            quant_diferenca_estoque = arquivo.readlines()
        textbox_relatorio = ctk.CTkTextbox(
        master=sub_janela_relatorio,
        width=600,
        height=200,
        border_width=2,
        corner_radius=10,
        )
        textbox_relatorio.insert("0.0", quant_diferenca_estoque)
        textbox_relatorio.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        #NOTE - Rodapé
        criar_pedido_venda_btn = ctk.CTkButton(master=sub_janela_relatorio, text="Criar pedido de venda", command=criar_pedido_venda_btn_func)
        criar_pedido_venda_btn.place(relx=0.4, rely=0.9, anchor=ctk.S)
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
                    estoque = estoque.split("*")
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
        produtos_nao_retornados = diferenca_quantidade_estoque_produto(codigo_local_estoque)
        produtos_nao_retornados_text = f"Total não retornados: {produtos_nao_retornados}"
        sub_janela_relatorio = sub_janela_relatorio_func(produtos_nao_retornados_text, produtos_nao_retornados)
        janela_relatorio_diferenca.destroy()
    
    #!SECTION
    
    #================== Puxando lista de estoques ===================#
    with open("config/arquivos/lista_estoques.txt", "r") as arquivo:
        lista_estoques = arquivo.readlines()
        lista_estoques_aux = []
        for estoque in lista_estoques:
            estoque = estoque.split("*")
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