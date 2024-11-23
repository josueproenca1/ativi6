import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gato import Gato
from cachorro import Cachorro

animais = []

def cadastrar_gato():
    nome = entry_nome.get()
    idade = entry_idade.get()
    raca = entry_info.get()
    if nome and idade and raca:
        try:
            idade = int(idade)
            gato = Gato(nome, idade, raca)
            animais.append(gato)
            messagebox.showinfo("Sucesso", "Gato cadastrado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")
def cadastrar_cachorro():
    nome = entry_nome.get()
    idade = entry_idade.get()
    porte = entry_info.get()
    if nome and idade and porte:
        try:
            idade = int(idade)
            cachorro = Cachorro(nome, idade, porte)
            animais.append(cachorro)
            messagebox.showinfo("Sucesso", "Cachorro cadastrado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def mostrar_lista():
    lista.delete(0, tk.END)
    for animal in animais:
        lista.insert(tk.END, animal.mostrar())

janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("500x400")

janelinha = ttk.Notebook(janela)
janelinha.pack(fill="both", expand=True)

tab1 = ttk.Frame(janelinha)
janelinha.add(tab1, text="Cadastro")

label_nome = tk.Label(tab1, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(tab1)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = tk.Label(tab1, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(tab1)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

label_info = tk.Label(tab1, text="Raça/Porte:")
label_info.grid(row=2, column=0, padx=10, pady=5)
entry_info = tk.Entry(tab1)
entry_info.grid(row=2, column=1, padx=10, pady=5)

btn_cadastrar_gato = tk.Button(tab1, text="Cadastrar Gato", command=cadastrar_gato)
btn_cadastrar_gato.grid(row=3, column=0, padx=10, pady=10)

btn_cadastrar_cachorro = tk.Button(tab1, text="Cadastrar Cachorro", command=cadastrar_cachorro)
btn_cadastrar_cachorro.grid(row=3, column=1, padx=10, pady=10)

tab2 = ttk.Frame(janelinha)
janelinha.add(tab2, text="Lista")

btn_mostrar = tk.Button(tab2, text="Mostrar Lista", command=mostrar_lista)
btn_mostrar.pack(pady=10)

lista = tk.Listbox(tab2)
lista.pack(fill="both", expand=True, padx=10, pady=10)

janela.mainloop()

#eu fiz umas auterações no codigo em relação ao do professor para ele ficar de um jeito que eu goste mais eu não sabia como fazer então pesquisei até descobrir se caso na hora da avaliação não tiver o vscode instalado click no main.py duas vezes
