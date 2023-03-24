import customtkinter as ctk
import tkinter

def sub_janela_alerta_acesso_bloqueado_func():
    #NOTE - sub_janela_alerta_acesso_bloqueado
    sub_janela_alerta_acesso_bloqueado = ctk.CTk()
    sub_janela_alerta_acesso_bloqueado.title("Acesso Bloqueado")
    sub_janela_alerta_acesso_bloqueado.geometry("300x300")
    sub_janela_alerta_acesso_bloqueado.update_idletasks()
    sub_janela_alerta_acesso_bloqueado.attributes("-topmost", True)
    x = (sub_janela_alerta_acesso_bloqueado.winfo_screenwidth() // 2) - (sub_janela_alerta_acesso_bloqueado.winfo_width() // 2)
    y = (sub_janela_alerta_acesso_bloqueado.winfo_screenheight() // 2) - (sub_janela_alerta_acesso_bloqueado.winfo_height() // 2)
    sub_janela_alerta_acesso_bloqueado.geometry(f"+{x}+{y}")
    

    #SECTION - Funções Confirmar
    def ok_btn_func():
        #NOTE - ok_btn_func
        sub_janela_alerta_acesso_bloqueado.destroy()
    #!SECTION

    #NOTE - frame_confirmar
    frame_confirmar = ctk.CTkFrame(
        master=sub_janela_alerta_acesso_bloqueado,
        width=250,
        height=250
    )
    frame_confirmar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    label_confirmar = ctk.CTkLabel(
        master=sub_janela_alerta_acesso_bloqueado,
        text="Acesso Bloqueado!",
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

    sub_janela_alerta_acesso_bloqueado.mainloop()