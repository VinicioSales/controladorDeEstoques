import customtkinter as ctk
import tkinter

dimensao = "1100x580"

def janela_saida_caminhoes_func():
    #NOTE - Instancia Janela
    janela_saida_caminhao = ctk.CTkToplevel()
    janela_saida_caminhao.geometry(dimensao)
    master = janela_saida_caminhao

    #NOTE - Entradas
    fechar_button = ctk.CTkButton(master, text="Fechar", command=janela_saida_caminhao.destroy)

    textbox = ctk.CTkTextbox(
        master,
        width=200,
        height=25
        #border_width=2,
        #corner_radius=10,
        )
    textbox.place(relx=0.4, rely=0.1, anchor=tkinter.CENTER)
    textbox.insert("0.0", "Quantidade de itens")  # insert at line 0 character 0
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    textbox.configure(state="disabled")  # configure textbox to be read-only

    quantidade = ctk.CTkEntry(master=master,
                                    placeholder_text="CTkEntry",
                                    width=120,
                                    height=25,
                                    border_width=1,
                                    corner_radius=5)
    quantidade.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)

    fechar_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    janela_saida_caminhao.mainloop()
