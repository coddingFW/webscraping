import tkinter as tk
from tkinter import ttk
import webbrowser
import urllib.parse

def search():
    query = entry.get()
    # Aqui você pode adicionar a lógica para executar a busca com o texto inserido no Entry
    print("Buscando por:", query)

    def pesquisar_no_google(query):
        base_url = "https://pt.wikipedia.org/wiki/"
        query_formatada = urllib.parse.quote(query)
        url_completa = base_url  + query_formatada
        webbrowser.open(url_completa)

    # Consulta de pesquisa que você deseja fazer
    consulta = query

    # Chama a função para pesquisar no Google
    pesquisar_no_google(consulta)
# Criação da janela principal
root = tk.Tk()
root.title("Busca")

# Função para executar a busca quando o botão da lupa for clicado
button_search = tk.PhotoImage(file="lupa.png")
search_button = ttk.Button(root, image=button_search, command=search)
search_button.grid(row=0, column=1, padx=5)

# Campo de entrada
entry = ttk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()