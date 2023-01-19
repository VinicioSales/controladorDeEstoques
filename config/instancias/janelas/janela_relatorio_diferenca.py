import customtkinter as ctk
from config.instancias.apis.apis_estoque import diferenca_quantidade
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
    lista_nCodProd, lista_quant_diferenca = diferenca_quantidade()
    relatorio_quant_diferenca = relatorio_quant_diferenca_func(lista_nCodProd, lista_quant_diferenca)
    with open("config/arquivos/lista_produtos_ceasa.txt", "r") as arquivo:
        lista_produtos_ceasa = arquivo.readlines()
    for index, item in enumerate(relatorio_quant_diferenca):
        for produto_ceasa in lista_produtos_ceasa:            
            produto_ceasa = produto_ceasa.split("*")
            nome_produto = produto_ceasa[0]
            quant_ceasa = int(produto_ceasa[2])
            if str(nome_produto) in str(item):
                item = item.split("*")
                quant_diferenca = int(item[1])
                quant_diferenca_soma = quant_diferenca + quant_ceasa
                item_resultado = f"{item[0]} * {quant_diferenca_soma}"
                relatorio_quant_diferenca[index] = item_resultado

    #SECTION - Funções
    #NOTE - gerar_pedido
    def gerar_pedido():
        """Gera pedidos de venda de todos os produtos exibidos
        
        params:
            - None
            
        return:
            - None"""
        print("Gerando pedido de venda...")
    def inicio():
        janela_relatorio_diferenca.destroy()
    #!SECTION

    #NOTE - Texto
    label = ctk.CTkLabel(janela_relatorio_diferenca, text="Quantidade de produtos não retornados:")
    label.place(relx=0.3, rely=0.1, anchor=ctk.NW)

    #NOTE - Lista
    textbox = ctk.CTkTextbox(
    janela_relatorio_diferenca,
    width=600,
    height=400,
    border_width=2,
    corner_radius=10,
    )
    textbox.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    for item in relatorio_quant_diferenca:
        textbox.insert("end", item + "\n")

    #NOTE - Rodapé
    gerar_pedido_button = ctk.CTkButton(janela_relatorio_diferenca, text="Gerar pedido de venda", command=gerar_pedido)
    gerar_pedido_button.place(relx=0.6, rely=0.9, anchor=ctk.S)
    inicio_btn = ctk.CTkButton(janela_relatorio_diferenca, text="Início", command=inicio)
    inicio_btn.place(relx=0.4, rely=0.9, anchor=ctk.S)

    janela_relatorio_diferenca.mainloop()