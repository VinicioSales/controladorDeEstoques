import customtkinter as ctk
import tkinter

def sub_janela_confirmar_produtos_func():
    #NOTE - sub_janela_confirmar_produtos_func
    """
    Cria uma sub-janela para confirmar a adição de um produto.
    Esta sub-janela é centralizada na tela e tem um label e um botão "Ok".
    Ao clicar no botão "Ok", a sub-janela é fechada.
    """
    sub_janela_confirmar_produtos = ctk.CTkToplevel()
    sub_janela_confirmar_produtos.geometry("300x300")
    sub_janela_confirmar_produtos.update_idletasks()
    x = (sub_janela_confirmar_produtos.winfo_screenwidth() // 2) - (sub_janela_confirmar_produtos.winfo_width() // 2)
    y = (sub_janela_confirmar_produtos.winfo_screenheight() // 2) - (sub_janela_confirmar_produtos.winfo_height() // 2)
    sub_janela_confirmar_produtos.geometry(f"+{x}+{y}")
    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_confirmar_produtos.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_confirmar_produtos,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_confirmar_produtos,
        text="Adicione um produto",
        text_color = "#F04A29",
        bg_color="#2b2b2b",
        font=("arial", 18, "bold")
    )
    label_confirmar.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    btn_ok = ctk.CTkButton(
        master=frame_confirmar,
        text="Ok",
        command=ok_btn_func
    )
    btn_ok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    sub_janela_confirmar_produtos.mainloop()

sub_janela_confirmar_produtos_func()