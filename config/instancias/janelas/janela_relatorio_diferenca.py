import customtkinter as ctk
import tkinter
import datetime
from PIL import Image
from config.instancias.apis.apis_estoque import diferenca_quantidade_estoque_produto
from config.instancias.apis.apis_vendas import incluir_pedido_venda
from config.instancias.apis.apis_produtos import pesquisar_produto_nome_func
from config.styles import estilo_janelas_func

#estilo_janelas = estilo_janelas_func()
#dimensao = estilo_janelas["dimensao"]
def janela_relatorio_diferenca_func(janela_inicio):
    """Mostra a diferença de quantidade de itens não retornados
    
    params:
        - ctk: janela_inicio
        
    retun:
        - None"""
    ctk.set_appearance_mode("dark")
    janela_relatorio_diferenca = ctk.CTk()
    #janela_relatorio_diferenca.geometry(dimensao)
    janela_relatorio_diferenca.state("zoomed")
    master = janela_relatorio_diferenca

    #SECTION - sub_janela_relatorio_func
    def sub_janela_relatorio_func(produtos_nao_retornados_text):
        #NOTE - sub_janela_relatorio_func
        """Mostra o relatório de produtos não retornados
        
        params:
            - string: produtos_nao_retornados
            
        return:
            - None"""
        sub_janela_relatorio = ctk.CTkToplevel()
        sub_janela_relatorio.title("Relatório")
        sub_janela_relatorio.state("zoomed")

        #SECTION - Funcoes Sub 
        
        def inicio_func():
            #NOTE - inicio_func
            """
            Função que destrói a janela de relatórios
            """
            sub_janela_relatorio.withdraw()
            janela_inicio.deiconify()
        def criar_pedido_venda_btn_func():
            #NOTE - criar_pedido_venda_btn_func
            """
            Função que cria um pedido de venda a partir de uma lista de produtos e quantidades.
            """
            
            for linha in quant_diferenca_estoque:
                
                linha = linha.split("|")
                nome_produto = linha[0]
                quantidade_prod = linha[1]
                quantidade_prod = quantidade_prod.replace(" ", "")
                quantidade_prod = quantidade_prod.replace("\n", "")
                #================ TESTE =================#
                codigo_cliente = "5646179802"
                #================ TESTE =================#
                cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_nome_func(nome_produto)
                sub_janela_data_vencimento = sub_janela_data_vencimento_func(codigo_produto, codigo_cliente, cfop, descricao, ncm, unidade, valor_unitario, quantidade_prod)              
                #incluir_pedido_venda(codigo_produto, codigo_cliente, data_previsao, cfop, descricao, ncm ,unidade, valor_unitario, quantidade_prod)
        def inicio_sub_func():
            #NOTE - inicio_sub_func
            """
            Função que fecha a sub-janela de relatório e reabre a janela principal de relatório de diferença de estoque.
            """
            #NOTE - inicio_sub_func
            sub_janela_relatorio.withdraw()
            janela_inicio.deiconify()
        def estoques_sub_tbn_func():
            #NOTE - estoques_sub_tbn_func
            sub_janela_relatorio.withdraw()
            janela_relatorio_diferenca.deiconify()
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
        font=("arial", 14, "bold")
        )
        textbox.insert("0.0", produtos_nao_retornados_text)
        textbox.configure(state="disabled")
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
        textbox_relatorio.configure(state="disabled")

        #NOTE - Rodapé
        criar_pedido_venda_btn = ctk.CTkButton(master=sub_janela_relatorio, text="Criar pedido de venda", command=criar_pedido_venda_btn_func)
        criar_pedido_venda_btn.place(relx=0.4, rely=0.9, anchor=ctk.S)
        estoques_btn = ctk.CTkButton(master=sub_janela_relatorio, text="Estoques", command=estoques_sub_tbn_func)
        estoques_btn.place(relx=0.6, rely=0.9, anchor=ctk.S)
        inicio_sub_btn = ctk.CTkButton(master=sub_janela_relatorio, text="Início", command=inicio_func)
        inicio_sub_btn.place(relx=0.8, rely=0.9, anchor=ctk.S)
    #!SECTION
    #SECTION - sub_janela_data_vencimento_func
    def sub_janela_data_vencimento_func(codigo_produto, codigo_cliente, cfop, descricao, ncm, unidade, valor_unitario, quantidade_prod):
        #NOTE - sub_janela_data_vencimento_func
        #=========== Instanciando Janea ================#
        sub_janela_data_vencimento = ctk.CTkToplevel()
        sub_janela_data_vencimento.title("Data Vencimento")

        #SECTION - funções
        def somar_dias_uteis(dias_a_somar):
            #NOTE - somar_dias_uteis
            """
            Esta função soma dias úteis a partir de uma data inicial.

            param:
            - int: dias_a_somar (número de dias úteis a serem somados)

            return:
            - datetime.date: data_atual (data somada com os dias úteis)
            """
            dias_uteis = 0
            data_atual = datetime.date.today()

            while dias_uteis < dias_a_somar:
                data_atual += datetime.timedelta(days=1)
                if data_atual.weekday() not in (5, 6):
                    dias_uteis += 1

            data_vencimento = data_atual
            return data_vencimento
        def confirmar_venda_btn_func():
            #NOTE - confirmar_venda_btn_func
            dias_uteis_combo = data_vencimento_combo.get()
            dias_uteis_entry = data_vencimento_entry.get()
            if dias_uteis_entry == "":
                dias_uteis = dias_uteis_combo
                if dias_uteis == "A vista":
                    dias_uteis = 1
                else:
                    dias_uteis = dias_uteis.split(" ")
                    dias_uteis = dias_uteis[0]
            elif dias_uteis_entry != "":
                dias_uteis = dias_uteis_entry
                dias_uteis = dias_uteis.replace(" ", "")
            dias_uteis = int(dias_uteis)
            data_vencimento = somar_dias_uteis(dias_uteis)
            data_vencimento = data_vencimento.strftime("%d/%m/%Y")
            incluir_pedido_venda(codigo_produto, codigo_cliente, data_vencimento, cfop, descricao, ncm ,unidade, valor_unitario, quantidade_prod)

        #NOTE - Body
        lista_data_vencimento = ["A vista",
                                "7 dias",
                                "14 Dias",
                                "21 Dias",
                                "30 Dias",
                                "45 Dias",
                                "60 Dias"]
        data_vencimento_text = ctk.CTkTextbox(
            master=sub_janela_data_vencimento,
            width=300,
            height=25)
        data_vencimento_text.insert("0.0", "Selecione os dias para a data de vencimento")
        data_vencimento_text.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)
        data_vencimento_text.configure(state="disabled")
        data_vencimento_combo = ctk.CTkComboBox(master=sub_janela_data_vencimento, values=lista_data_vencimento)
        data_vencimento_combo.place(relx=0.7, rely=0.3, anchor=tkinter.CENTER)
        data_vencimento_text_2 = ctk.CTkTextbox(
            master=sub_janela_data_vencimento,
            width=200,
            height=2)
        data_vencimento_text_2.insert("0.0", "Ou digite os dias")
        data_vencimento_text_2.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)
        data_vencimento_text_2.configure(state="disabled")
        data_vencimento_entry = ctk.CTkEntry(master=sub_janela_data_vencimento)
        data_vencimento_entry.place(relx=0.7, rely=0.4, anchor=tkinter.CENTER)

        #NOTE - Rodapé
        confirmar_venda_btn = ctk.CTkButton(
            master=sub_janela_data_vencimento,
            text="Confirmar e gerar venda",
            command=confirmar_venda_btn_func
        )
        confirmar_venda_btn.place(relx=0.4, rely=0.8, anchor=tkinter.CENTER)
        

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
                    estoque = estoque.split("|")
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
    def selecionar_estoque_func():
        #NOTE - selecionar_estoque_func
        """Cofirma o estoque escolhido
        
        params:
            - None
            
        return:
            - None"""
        nome_estoque = combo_estoque.get()
        codigo_local_estoque = get_codigo_local_estoque(nome_estoque=nome_estoque)
        produtos_nao_retornados = diferenca_quantidade_estoque_produto(codigo_local_estoque)
        produtos_nao_retornados_text = f"Total não retornados: {produtos_nao_retornados}"
        sub_janela_relatorio = sub_janela_relatorio_func(produtos_nao_retornados_text)
        janela_relatorio_diferenca.withdraw()
    def inicio_rel_func():
        """
        inicio_rel_func():
        Função para destruir a janela de relatório de diferença
        """
        #NOTE - inicio_rel_func
        janela_relatorio_diferenca.withdraw()
        janela_inicio.deiconify()
    def voltar_btn_func():
        #NOTE - voltar_btn_func
        janela_relatorio_diferenca.destroy()
        janela_inicio.deiconify()
        janela_inicio.state("zoomed")
    #!SECTION
    
    #================== Puxando lista de estoques ===================#
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

    #NOTE - Frames
    frame_principal = ctk.CTkFrame(
        master=janela_relatorio_diferenca,
        width=500,
        height=500
    )
    frame_principal.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    img_voltar = ctk.CTkImage(light_image=Image.open("config/arquivos/img/voltar.png"), size=(30,30))
    btn_voltar = ctk.CTkButton(
        master=frame_principal,
        width=50,
        height=30,
        text="Voltar",
        #image=img_voltar,
        command=voltar_btn_func
    )
    btn_voltar.place(relx=0.1, rely=0.05)
    label_estoque = ctk.CTkLabel(
        master=frame_principal,
        text="Selecione o Estoque",
        width=200,
        height=25,
        font=("arial", 19, "bold")
        )
    label_estoque.place(relx=0.5, rely=0.23, anchor=tkinter.CENTER)
    combo_estoque = ctk.CTkComboBox(
        master=frame_principal,
        width=200,
        height=35,
        values=lista_estoques)
    combo_estoque.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
    btn_selecionar = ctk.CTkButton(
        master=frame_principal,
        width=200,
        height=35,
        text="Selecionar",
        command=selecionar_estoque_func)
    btn_selecionar.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
    inicio_rel_btn = ctk.CTkButton(
        master=frame_principal,
        text="Início",
        command=inicio_rel_func)
    inicio_rel_btn.place(relx=0.5, rely=0.48, anchor=ctk.CENTER)
    
    

    #SECTION - Funções
    def inicio():
        janela_relatorio_diferenca.withdraw()

    janela_relatorio_diferenca.mainloop()
#janela_relatorio_diferenca_func("ok")