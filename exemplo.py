import customtkinter as ctk
import tkinter

lista_produtos = ["a", "B"]
def sub_janela_confirmar_ceasa_func(text_prod_selecionados, janela_produtos, tipo):
    """Cria uma subjanela "sub_janela_confirmar_ceasa", centraliza a janela na tela,
    e apresenta uma pergunta "Há algum produto na Ceasa?" com uma entrada para a
    quantidade e dois botões "Ok" e "Cancelar".
    """
    sub_janela_confirmar_ceasa = ctk.CTkToplevel()
    sub_janela_confirmar_ceasa.state("zoomed")
    sub_janela_confirmar_ceasa.title("")
    """sub_janela_confirmar_ceasa.update_idletasks()
    x = (sub_janela_confirmar_ceasa.winfo_screenwidth() // 2) - (sub_janela_confirmar_ceasa.winfo_width() // 2)
    y = (sub_janela_confirmar_ceasa.winfo_screenheight() // 2) - (sub_janela_confirmar_ceasa.winfo_height() // 2)
    sub_janela_confirmar_ceasa.geometry(f"+{x}+{y}")"""

    #SECTION - Funções confirmar Ceasa
    def btn_confimar_ceasa_1_func():
        """Função que pega o conteúdo digitado em uma entrada e fecha uma subjanela"""
        #NOTE - btn_confimar_ceasa_1_func
        quant_produtos_ceasa = entry_prod_ceasa.get()
        sub_janela_confirmar_ceasa.destroy()
        prods_selecionados = text_prod_selecionados.get("0.0", "end").split("\n")
        if len(prods_selecionados) <= 2:
            sub_janela_confirmar_produtos_func()
        else:
            for index, item in enumerate(prods_selecionados):
                if item == "":
                    del prods_selecionados[index]
            if prods_selecionados[-1] == "":
                prods_selecionados.pop()
            janela_produtos.destroy()
            janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo, quant_produtos_ceasa)
    def btn_confimar_ceasa_1_event_func(event):
        """Função que pega o conteúdo digitado em uma entrada e fecha uma subjanela"""
        #NOTE - btn_confimar_ceasa_1_event_func
        quant_produtos_ceasa = entry_prod_ceasa.get()
        sub_janela_confirmar_ceasa.destroy()
        prods_selecionados = text_prod_selecionados.get("0.0", "end").split("\n")
        if len(prods_selecionados) <= 2:
            sub_janela_confirmar_produtos_func()
        else:
            for index, item in enumerate(prods_selecionados):
                if item == "":
                    del prods_selecionados[index]
            if prods_selecionados[-1] == "":
                prods_selecionados.pop()
            janela_produtos.destroy()
            janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo, quant_produtos_ceasa)
    def btn_confimar_ceasa_2_func():
        """
        Esta função fecha a sub-janela "sub_janela_confirmar_ceasa".
        """
        sub_janela_confirmar_ceasa.destroy()
        janela_produtos.destroy()
        quant_produtos_ceasa = ""
        janela_mov_estoque_func(janela_produtos, prods_selecionados, tipo, quant_produtos_ceasa)
    def btn_adicionar_func():
        produto_selecionado = combo_produto_1.get()
        if produto_selecionado != "":
            text_quant_produtos_ceasa.configure(state="normal")
            text_quant_produtos_ceasa.insert("0.0", f"{prod_selecionado} | {quantidade}\n")
            text_quant_produtos_ceasa.configure(state="disabled")
            combo_pesquisar_prod.configure(state="normal")
    #!SECTION


    #NOTE - frame_confirmar_ceasa
    frame_confirmar_ceasa = ctk.CTkFrame(
        master=sub_janela_confirmar_ceasa,
        width=900,
        height=600
    )
    frame_confirmar_ceasa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    #NOTE - label_confirmar_ceasa_1
    label_confirmar_ceasa_1 = ctk.CTkLabel(
        master=frame_confirmar_ceasa,
        text="Produtos na Ceasa",
        font=("arial", 20, "bold")
    )
    label_confirmar_ceasa_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    #NOTE - label_produto_ceasa
    label_produto_ceasa = ctk.CTkLabel(
        master=frame_confirmar_ceasa,
        text="Produto:"
    )
    label_produto_ceasa.place(relx=0.43, rely=0.23, anchor=tkinter.CENTER)

    #NOTE - btn_adicionar
    btn_adicionar = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Adicionar",
    )
    btn_adicionar.place(relx=0.56, rely=0.35, anchor=tkinter.CENTER)

    #NOTE - combo_produto_1
    combo_produto_1 = ctk.CTkComboBox(
        master=frame_confirmar_ceasa,
        values=lista_produtos
    )
    combo_produto_1.place(relx=0.56, rely=0.23, anchor=tkinter.CENTER)
    
    #NOTE - label_quantidade_ceasa
    label_quantidade_ceasa = ctk.CTkLabel(
        master=frame_confirmar_ceasa,
        text="Quantidade:",
        font=("arial", 14)
    )
    label_quantidade_ceasa.place(relx=0.43, rely=0.29, anchor=tkinter.CENTER)

    #NOTE - entry_prod_ceasa
    entry_prod_ceasa = ctk.CTkEntry(
        master=frame_confirmar_ceasa,
    )
    entry_prod_ceasa.bind("<Return>", btn_confimar_ceasa_1_event_func)
    entry_prod_ceasa.place(relx=0.56, rely=0.29, anchor=tkinter.CENTER)

    #NOTE - text_quant_produtos_ceasa
    text_quant_produtos_ceasa = ctk.CTkTextbox(
        master=frame_confirmar_ceasa,
        width=250,
        height=350
    )
    text_quant_produtos_ceasa.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

    #NOTE - btn_ceasa_concluir
    btn_ceasa_concluir = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Concluir",
        fg_color="#00993D",
        hover_color=("#007830"),
    )
    btn_ceasa_concluir.place(relx=0.40, rely=0.77, anchor=tkinter.CENTER)

    #NOTE - btn_ceasa_cancelar
    btn_ceasa_cancelar = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Cancelar"
    )
    btn_ceasa_cancelar.place(relx=0.56, rely=0.77, anchor=tkinter.CENTER)

    '''#NOTE - btn_confimar_ceasa_1
    btn_confimar_ceasa_1 = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Sim, enviar",
        command=btn_confimar_ceasa_1_func
    )
    btn_confimar_ceasa_1.place(relx=0.35, rely=0.70, anchor=tkinter.CENTER)
    
    #NOTE - btn_confimar_ceasa_2
    btn_confimar_ceasa_2 = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Não",
        command=btn_confimar_ceasa_2_func
    )
    btn_confimar_ceasa_2.place(relx=0.65, rely=0.70, anchor=tkinter.CENTER)'''
    
    sub_janela_confirmar_ceasa.mainloop()

sub_janela_confirmar_ceasa_func("text_prod_selecionados", "janela_produtos", "tipo")