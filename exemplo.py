import customtkinter as ctk
import tkinter

def sub_janela_confirmar_ceasa_func():
    """Cria uma subjanela "sub_janela_confirmar_ceasa", centraliza a janela na tela,
    e apresenta uma pergunta "Há algum produto na Ceasa?" com uma entrada para a
    quantidade e dois botões "Ok" e "Cancelar".
    """
    sub_janela_confirmar_ceasa = ctk.CTkToplevel()
    sub_janela_confirmar_ceasa.geometry("500x200")
    sub_janela_confirmar_ceasa.title("")
    sub_janela_confirmar_ceasa.update_idletasks()
    x = (sub_janela_confirmar_ceasa.winfo_screenwidth() // 2) - (sub_janela_confirmar_ceasa.winfo_width() // 2)
    y = (sub_janela_confirmar_ceasa.winfo_screenheight() // 2) - (sub_janela_confirmar_ceasa.winfo_height() // 2)
    sub_janela_confirmar_ceasa.geometry(f"+{x}+{y}")

    #SECTION - Funções confirmar Ceasa
    def btn_confimar_ceasa_1_func():
        """Função que pega o conteúdo digitado em uma entrada e fecha uma subjanela"""
        #NOTE - btn_confimar_ceasa_1_func
        produtos_ceasa = entry_confirmar_ceasa_1.get()
        sub_janela_confirmar_ceasa.destroy()
    def btn_confimar_ceasa_2_func():
        """
        Esta função fecha a sub-janela "sub_janela_confirmar_ceasa".
        """
        sub_janela_confirmar_ceasa.destroy()
    #!SECTION
    #NOTE - frame_confirmar_ceasa
    frame_confirmar_ceasa = ctk.CTkFrame(
        master=sub_janela_confirmar_ceasa,
        width=470,
        height=270
    )
    frame_confirmar_ceasa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    #NOTE - label_confirmar_ceasa_1
    label_confirmar_ceasa_1 = ctk.CTkLabel(
        master=frame_confirmar_ceasa,
        text="Há algum produto na Ceasa?",
        font=("arial", 20, "bold")
    )
    label_confirmar_ceasa_1.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
    
    #NOTE - label_confirmar_ceasa_2
    label_confirmar_ceasa_2 = ctk.CTkLabel(
        master=frame_confirmar_ceasa,
        text="Quantidade:",
        font=("arial", 14)
    )
    label_confirmar_ceasa_2.place(relx=0.2, rely=0.40, anchor=tkinter.CENTER)

    #NOTE - entry_confirmar_ceasa_1
    entry_confirmar_ceasa_1 = ctk.CTkEntry(
        master=frame_confirmar_ceasa,
    )
    entry_confirmar_ceasa_1.place(relx=0.5, rely=0.40, anchor=tkinter.CENTER)

    #NOTE - btn_confimar_ceasa_1
    btn_confimar_ceasa_1 = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Ok",
        command=btn_confimar_ceasa_1_func
    )
    btn_confimar_ceasa_1.place(relx=0.35, rely=0.60, anchor=tkinter.CENTER)
    
    #NOTE - btn_confimar_ceasa_2
    btn_confimar_ceasa_2 = ctk.CTkButton(
        master=frame_confirmar_ceasa,
        text="Cancelar",
        command=btn_confimar_ceasa_2_func
    )
    btn_confimar_ceasa_2.place(relx=0.65, rely=0.60, anchor=tkinter.CENTER)
    sub_janela_confirmar_ceasa.mainloop()

sub_janela_confirmar_ceasa_func()