import customtkinter as ctk

def pesquisar_item_combobox(event):
    search_text = combobox.get()
    filtered_items = [item for item in lista if search_text in item]
    combobox.configure(values=filtered_items)

janela = ctk.CTk()
lista = ['Tomate', 'Tomilho', 'Cebola']
combobox = ctk.CTkComboBox(janela, values=lista)
combobox.bind('<Return>', pesquisar_item_combobox)
combobox.pack()

janela.mainloop()
