import customtkinter as ctk

app = ctk.CTk()
app.geometry("800x600")

items = ["item 1", "item 2", "item 3", "item 4", "item 5"]

#NOTE - Funções
def gerar_pedido():
    print("Gerando pedido de venda...")

#NOTE - Texto
label = ctk.CTkLabel(app, text="Quantidade de produtos não retornados:")
label.place(relx=0.3, rely=0.1, anchor=ctk.NW)

#NOTE - Lista
textbox = ctk.CTkTextbox(
app,
width=600,
height=400,
border_width=2,
corner_radius=10,
)
textbox.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
for item in items:
    textbox.insert("end", item + "\n")

#NOTE - Rodapé
gerar_pedido_button = ctk.CTkButton(app, text="Gerar pedido de venda", command=gerar_pedido)
gerar_pedido_button.place(relx=0.5, rely=0.9, anchor=ctk.S)

app.mainloop()




