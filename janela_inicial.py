#NOTE - Imports
import tkinter
import customtkinter as ctk
from datetime import date
import os
from config.instancias import janela_inicial_func
from config.instancias import janela_mov_estoque_func
from config.instancias import janela_relatorio_diferenca_func
from config.styles.styles import estilo_janelas_func
from config.instancias.apis import listar_local_estoque
from config.instancias.apis import listar_projetos
from config.instancias.apis import listar_produtos
from config.instancias.apis import listar_clientes
from config.instancias.apis import listar_departamentos
from config.instancias.janelas import sub_janela_alerta_acesso_bloqueado_func
from config.instancias.apis import consultar_cliente_inativo

#NOTE - Liberação de acesso
inativo = consultar_cliente_inativo()
if inativo == "S":
    sub_janela_alerta_acesso_bloqueado = sub_janela_alerta_acesso_bloqueado_func()
elif inativo == "N":
    #SECTION - Puxando listas
    #NOTE - listar_local_estoque
    data_atual = date.today()
    data_atual = data_atual.strftime("%d/%m/%Y")
    with open("config/arquivos/data_anterior.txt", "r") as arquivo:
        data_anterior = arquivo.read()
        
    if str(data_atual) != str(data_anterior):
        with open("config/arquivos/lista_produtos_ceasa.txt", "w") as arquivo:
            arquivo.write("")
        with open("config/arquivos/produtos_venda.txt", "w") as arquivo:
            arquivo.write("")
        with open("config/arquivos/lista_pedidos_venda.txt", "w") as arquivo:
            arquivo.write("")
        arquivos = os.listdir("config/arquivos")
        for arquivo in arquivos:
            if "temp_lista_det_" in arquivo:
                os.remove(f"config/arquivos/{arquivo}")

    with open("config/arquivos/data_anterior.txt", "w") as arquivo:
        arquivo.write(data_atual)

    lista_estoque = listar_local_estoque()
    with open(f"config/arquivos/lista_estoques.txt", "r") as arquivo:
        lista_estoques_arquivo = arquivo.readlines()
    lista_estoques_arquivo = []
    for item in lista_estoque:
        lista_estoques_arquivo.append(f"{item}\n")
    with open("config/arquivos/lista_estoques.txt", "w") as arquivo:
        arquivo.writelines(lista_estoques_arquivo)

    #NOTE - listar_projetos
    lista_projetos = listar_projetos()
    with open(f"config/arquivos/lista_projetos.txt", "r") as arquivo:
        lista_projetos_arquivo = arquivo.readlines()
    lista_projetos_arquivo = []
    for item in lista_projetos:
        lista_projetos_arquivo.append(f"{item}\n")
    with open("config/arquivos/lista_projetos.txt", "w") as arquivo:
        arquivo.writelines(lista_projetos_arquivo)

    lista_produtos = listar_produtos()
    with open(f"config/arquivos/lista_produtos.txt", "r") as arquivo:
        lista_produtos_arquivo = arquivo.readlines()
    lista_produtos_arquivo = []
    for item in lista_produtos:
        lista_produtos_arquivo.append(f"{item}\n")
    with open("config/arquivos/lista_produtos.txt", "w") as arquivo:
        arquivo.writelines(lista_produtos_arquivo)

    lista_clientes = listar_clientes()
    with open("config/arquivos/lista_clientes.txt", "w") as arquivo:
        arquivo.writelines(lista_clientes)

    lista_departamentos = listar_departamentos()
    with open("config/arquivos/lista_departamentos.txt", "w") as arquivo:
        arquivo.writelines(lista_departamentos)
    #!SECTION

    #SECTION - janela_configurações
    def janela_configurações_func():
        janela_configurações = ctk.CTk()
        janela_configurações = ctk.CTkToplevel()
        janela_configurações.title("Configurações")
        janela_configurações.geometry("300x300")
        janela_configurações.update_idletasks()
        janela_configurações.attributes("-topmost", True)
        x = (janela_configurações.winfo_screenwidth() // 2) - (janela_configurações.winfo_width() // 2)
        y = (janela_configurações.winfo_screenheight() // 2) - (janela_configurações.winfo_height() // 2)
        janela_configurações.geometry(f"+{x}+{y}")

        #SECTION - FUNÇÔES
        #NOTE - mudar_tamnho_escala
        def mudar_tamnho_escala(new_scaling: str):
            #NOTE - mudar_tamnho_escala
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            ctk.set_widget_scaling(new_scaling_float)
        def ok_func():
            janela_configurações.destroy()
        #!SECTION

        #NOTE - frame_configuracao
        frame_configuracao = ctk.CTkFrame(master=janela_configurações)
        frame_configuracao.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #NOTE - menu_escala
        menu_escala = ctk.CTkOptionMenu(
            frame_configuracao,
            values=["80%", "90%", "100%", "110%", "120%", "130%", "140%", "150%"],
            command=mudar_tamnho_escala)
        menu_escala.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        #NOTE - btn_ok
        btn_ok = ctk.CTkButton(
            master=frame_configuracao,
            width=100,
            height=25,
            text="Ok",
            font=("Arial", 12),
            hover_color = "#AA0",
            command=ok_func
        )
        btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    #NOTE - JANELA INICIO
    janela_inicio = janela_inicial_func()   
    estilo_janelas = estilo_janelas_func()
    tema_janela = estilo_janelas["tema_janela"]
    janela_inicio.state("zoomed")
    ctk.set_appearance_mode(tema_janela)

    #SECTION - INICIO
    #====================== FRAMES ===================#

    frame_1_inicio = ctk.CTkFrame(
        master=janela_inicio,
        width=500,
        height=500
        )
    frame_1_inicio.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    prods_selecionados = ""

    #=============== FUNCAO BOTAO ==================#
    quant_produtos_ceasa = ""
    prods_ceasa = ""
    def btn_saida_caminhao_func():
        #//NOTE - btn_mov_estoque_func
        """Abre a janela de movimento de estoque
        params:
            - None

        return:
            - None
        """
        #janela_inicio.withdraw()
        janela_sai_caminhoes = janela_mov_estoque_func(janela_inicio, prods_selecionados, "SAI", prods_ceasa)
    def btn_entrada_caminhao_func():
        #//NOTE - btn_entrada_caminhao_func
        """Abre a janela de movimento de estoque
        params:
            - None

        return:
            - None
        """
        janela_sai_caminhoes = janela_mov_estoque_func(janela_inicio, prods_selecionados, "ENT", prods_ceasa)
    def btn_relatorio_func():
        #//NOTE - btn_relatorio_func
        """Abre a janela de relatorio de diferença de quantidade
        params:
            - None

        return:
            - None
        """
        #janela_inicio.withdraw()
        janela_relatorio_diferenca = janela_relatorio_diferenca_func(janela_inicio)
    def btn_configuracoes_func():
        janela_configurações_func()

    #==================== PAGINA INICIAL ================#
    #========= BOTOES ===========#
    btn_sai_estoque = ctk.CTkButton(
        master=frame_1_inicio,
        text="Saída de estoque",
        hover_color = "#AA0",
        width=200,
        height=50,
        font=("Arial", 20, "bold"),
        command=btn_saida_caminhao_func
    )
    btn_sai_estoque.place(relx=0.5, rely=0.39, anchor=tkinter.CENTER)

    btn_ent_estoque = ctk.CTkButton(
        master=frame_1_inicio,
        text="Entrada de estoque",
        hover_color = "#AA0",
        width=200,
        height=50,
        font=("Arial", 20, "bold"),
        command=btn_entrada_caminhao_func
    )
    btn_ent_estoque.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    btn_relatorio = ctk.CTkButton(
        master=frame_1_inicio,
        text="Relatório",
        font=("Arial", 20, "bold"),
        hover_color = "#AA0",
        command=btn_relatorio_func
    )
    btn_relatorio.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    btn_configuracoes = ctk.CTkButton(
        master=frame_1_inicio,
        text="Configurações",
        font=("Arial", 20, "bold"),
        hover_color = "#AA0",
        command=btn_configuracoes_func
    )
    btn_configuracoes.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)
    #!SECTION

    janela_inicio.mainloop()