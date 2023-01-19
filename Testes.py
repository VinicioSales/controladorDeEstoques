import customtkinter as ctk
import tkinter

app = ctk.CTk()
app.geometry("400x300")


def minha_funcao():
    variavel_local = combo_produtos.get()
    variavel_global = variavel_local
    return variavel_global
    
def funcao():
    a = minha_funcao()
    print(f"a: {a}")

botao = ctk.CTkButton(app, text="Clique aqui", command=minha_funcao)
botao.pack()
lista_produtos = ["a", "b", "c"]
combo_produtos = ctk.CTkComboBox(app, values=lista_produtos)
combo_produtos.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

botao = ctk.CTkButton(app, text="Clique aqui", command=funcao)
botao.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)




app.mainloop()
