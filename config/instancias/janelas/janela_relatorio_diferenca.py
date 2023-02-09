
import customtkinter as ctk
import tkinter
import datetime
from PIL import Image
from config.instancias.apis.apis_estoque import diferenca_quantidade_estoque_produto
from config.instancias.apis.apis_vendas import incluir_pedido_venda
from config.instancias.apis.apis_produtos import pesquisar_produto_nome_func
from config.instancias.apis.apis_projetos import get_cod_projeto
from config.styles import estilo_janelas_func
from config.credenciais.database import database_infos_func
from config.instancias.janelas.janela_pedido_venda import janela_pedido_venda_func



#SECTION - janela_relatorio_diferenca_func
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
        def atualizar_func():
            #NOTE - atualizar_func
            with open("config/arquivos/produtos_venda.txt", "r") as arquivo:
                produtos_venda = arquivo.readlines()
            with open(f"config/arquivos/quant_diferenca_estoque.txt", "r") as arquivo:
                quant_diferenca_estoque = arquivo.readlines()
            for prods_venda in produtos_venda:
                nome_produto_venda = prods_venda.split(" | ")[0].strip()
                quant_venda = float(prods_venda.split(" | ")[1].strip())
                for i, prods_dif in enumerate(quant_diferenca_estoque):
                    nome_produto_diferenca = prods_dif.split(" | ")[0].strip()
                    quant_diferenca = float(prods_dif.split(" | ")[1].strip())
                    if nome_produto_venda in nome_produto_diferenca:
                        quant_sub = quant_diferenca - quant_venda
                        quant_diferenca_estoque[i] = f"{nome_produto_diferenca} | {quant_sub}\n"
            text_relatorio.configure(state="normal")
            text_relatorio.delete("0.0", "end")
            linha = 0
            for prod_estoque in quant_diferenca_estoque:                
                text_relatorio.insert(f"{linha}.0", prod_estoque)
                linha += 1
            text_relatorio.configure(state="disabled")
        def inicio_func():
            #NOTE - inicio_func
            """
            Função que destrói a janela de relatórios
            """
            sub_janela_relatorio.withdraw()
            janela_inicio.deiconify()
            janela_inicio.state("zoomed")
        def criar_pedido_venda_btn_func():
            #NOTE - criar_pedido_venda_btn_func
            """
            Função que cria um pedido de venda a partir de uma lista de produtos e quantidades.
            """
            produtos_estoque = text_relatorio.get("0.0", "end").split("\n")
            sub_janela_relatorio.withdraw()
            janela_pedido_venda_func(sub_janela_relatorio, produtos_estoque, text_relatorio)
            
            #sub_janela_data_vencimento = sub_janela_data_vencimento_func(quant_diferenca_estoque)
        def estoques_sub_tbn_func():
            #NOTE - estoques_sub_tbn_func
            sub_janela_relatorio.withdraw()
            janela_relatorio_diferenca.deiconify()
            janela_relatorio_diferenca.state("zoomed")
        #!SECTION

        
        
            
        #NOTE - Frame
        frame_principal = ctk.CTkFrame(
            master=sub_janela_relatorio,
            width=500,
            height=350
        )
        frame_principal.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        #NOTE - Texto
        label = ctk.CTkLabel(
            master=frame_principal,
            text="Quantidade de produtos no estoque:",
            font=("arial", 16, "bold")
            )
        label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        #NOTE - quant_diferenca_estoque
        with open(f"config/arquivos/quant_diferenca_estoque.txt", "r") as arquivo:
            quant_diferenca_estoque = arquivo.readlines()
        with open(f"config/arquivos/lista_produtos_ceasa.txt", "r") as arquivo:
            lista_produtos_ceasa = arquivo.readlines()
        
        lista_relatorio = []
        for produto_ceasa in lista_produtos_ceasa:
            codigo_local_estoque, nome_produto_ceasa, quant_ceasa = produto_ceasa.split(" | ")
            nome_produto_ceasa = nome_produto_ceasa.strip()
            quant_ceasa = int(quant_ceasa.strip())
            for diferenca_estoque in quant_diferenca_estoque:
                nome_difenca, quant_diferenca = diferenca_estoque.split(" | ")
                quant_diferenca = int(quant_diferenca.strip())
                nome_difenca = nome_difenca.strip()
                if nome_produto_ceasa == nome_difenca:
                    resultado = quant_diferenca - quant_ceasa
                    lista_relatorio.append(f"{nome_difenca} | {resultado}\n")
        with open(f"config/arquivos/quant_diferenca_estoque.txt", "w") as arquivo:
            arquivo.writelines(quant_diferenca_estoque)
            #quant_diferenca_estoque = arquivo.readlines()

        text_relatorio = ctk.CTkTextbox(
        master=frame_principal,
        width=500,
        height=200,
        border_width=2,
        corner_radius=10,
        )
        linha = 0
        for prod_estoque in quant_diferenca_estoque:
            text_relatorio.insert(f"{linha}.0", prod_estoque)
            linha += 1
        text_relatorio.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        text_relatorio.configure(state="disabled")

        #NOTE - Rodapé
        criar_pedido_venda_btn = ctk.CTkButton(
            master=frame_principal,
            text="Criar pedido de venda",
            fg_color="#00993D",
            hover_color=("#007830"),
            command=criar_pedido_venda_btn_func)
        criar_pedido_venda_btn.place(relx=0.8, rely=0.9, anchor=ctk.S)
        estoques_btn = ctk.CTkButton(
            master=frame_principal,
            text="Estoques",
            command=estoques_sub_tbn_func)
        estoques_btn.place(relx=0.5, rely=0.9, anchor=ctk.S)
        
        #NOTE - inicio_sub_btn
        inicio_sub_btn = ctk.CTkButton(
            master=frame_principal,
            text="Início",
            width=50,
            command=inicio_func)
        inicio_sub_btn.place(relx=0.15, rely=0.1, anchor=ctk.S)

        #NOTE - btn_atualizar
        btn_atualizar = ctk.CTkButton(master=frame_principal,
        text="Atualizar",
        command=atualizar_func)
        btn_atualizar.place(relx=0.19, rely=0.9, anchor=ctk.S)
    #!SECTION
    #SECTION - sub_janela_data_vencimento_func
    def sub_janela_data_vencimento_func(quant_diferenca_estoque):
        #NOTE - sub_janela_data_vencimento_func
        sub_janela_data_vencimento = ctk.CTkToplevel()
        sub_janela_data_vencimento.title("")
        sub_janela_data_vencimento.update_idletasks()
        x = (sub_janela_data_vencimento.winfo_screenwidth() // 2) - (sub_janela_data_vencimento.winfo_width() // 2)
        y = (sub_janela_data_vencimento.winfo_screenheight() // 2) - (sub_janela_data_vencimento.winfo_height() // 2)
        sub_janela_data_vencimento.geometry(f"+{x}+{y}")

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
            for linha in quant_diferenca_estoque:                
                linha = linha.split("|")
                nome_produto = linha[0]
                quantidade_prod = linha[1]
                quantidade_prod = quantidade_prod.replace(" ", "")
                quantidade_prod = quantidade_prod.replace("\n", "")                
                cfop, codigo_produto, descricao, ncm, unidade, valor_unitario = pesquisar_produto_nome_func(nome_produto)
                codigo_projeto = get_cod_projeto(nome_produto)
                incluir_pedido_venda(codigo_produto, codigo_cliente, data_vencimento, cfop, descricao, ncm ,unidade, valor_unitario, quantidade_prod, codigo_projeto)
            sub_janela_data_vencimento.destroy()

        #NOTE - Frame
        frame_principal_data = ctk.CTkFrame(
            master=sub_janela_data_vencimento,
            width=350,
            height=250
        )
        frame_principal_data.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        #NOTE - Body
        lista_data_vencimento = ["A vista",
                                "7 dias",
                                "14 Dias",
                                "21 Dias",
                                "30 Dias",
                                "45 Dias",
                                "60 Dias"]
        data_vencimento_text = ctk.CTkTextbox(
            master=frame_principal_data,
            width=300,
            height=25,
            font=("arial", 12, "bold"))
        data_vencimento_text.insert("0.0", "                  Selecione a data de vencimento")
        data_vencimento_text.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
        data_vencimento_text.configure(state="disabled")
        data_vencimento_combo = ctk.CTkComboBox(master=frame_principal_data, values=lista_data_vencimento)
        data_vencimento_combo.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
        data_vencimento_text_2 = ctk.CTkTextbox(
            master=frame_principal_data,
            width=210,
            height=2,
            font=("arial", 12, "bold")
            )
        data_vencimento_text_2.insert("0.0", "                Ou digite os dias")
        data_vencimento_text_2.place(relx=0.5, rely=0.50, anchor=tkinter.CENTER)
        data_vencimento_text_2.configure(state="disabled")
        data_vencimento_entry = ctk.CTkEntry(master=frame_principal_data)
        data_vencimento_entry.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
        confirmar_venda_btn = ctk.CTkButton(
            master=frame_principal_data,
            text="Confirmar e gerar venda",
            fg_color="#00993D",
            hover_color=("#007830"),
            command=confirmar_venda_btn_func
        )
        confirmar_venda_btn.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)
        

    #!SECTION

    #SECTION - FUNÇÔES
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
        janela_inicio.state("zoomed")
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
    
    #NOTE - inicio_rel_btn
    inicio_rel_btn = ctk.CTkButton(
        master=frame_principal,
        text="Início",
        command=inicio_rel_func)
    inicio_rel_btn.place(relx=0.5, rely=0.48, anchor=ctk.CENTER)

    janela_relatorio_diferenca.mainloop()
#!SECTION

