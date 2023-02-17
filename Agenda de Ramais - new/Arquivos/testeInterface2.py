# Importando Interface
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Importando Banco
import sqlite3

# Criando Listas e Variaveis
listaRamalDireta = []
listaNomeDireta = []
listaRamalInterna = []
listaNomeInterna = []
i = 0
menu = 1
ramal = 0
nome = ""

# --------------------- ADICIONAR INTERNO --------------------------------------        
    

# ------------------------- MENU ------------------------------
class Menu:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Ramais Copobras MG")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.adicionar = Button(self.quartoContainer)
        self.adicionar["text"] = "Adicionar"
        self.adicionar["font"] = ("Calibri", "8")
        self.adicionar["width"] = 12
        self.adicionar["command"] = self.Adicionar
        self.adicionar.pack()

    #def botaoAdicionar(self):
    #    menu = 2
    def Adicionar(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Adicionar Ramal")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.ramalLabel = Label(self.terceiroContainer, text="Ramal", font=self.fontePadrao)
        self.ramalLabel.pack(side=LEFT)

        self.ramal = Entry(self.terceiroContainer)
        self.ramal["width"] = 30
        self.ramal["font"] = self.fontePadrao
        #self.senha["show"] = "*"
        self.ramal.pack(side=LEFT)

        self.adicionar = Button(self.quartoContainer)
        self.adicionar["text"] = "Adicionar"
        self.adicionar["font"] = ("Calibri", "8")
        self.adicionar["width"] = 12
        self.adicionar["command"] = self.adicionarRamal
        self.adicionar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Adicionando ao Banco
    def adicionarRamal(self):
        # Interface
        nome = self.nome.get()
        ramal = self.ramal.get()
        if nome == "Andre" and ramal == "123":
            self.mensagem["text"] = "Ramal %s adicionado" %(ramal)
        else:
            self.mensagem["text"] = "Erro na autenticação"
        # Banco de dados
        print("Adicionando")

        adicionarRamalInterno = "INSERT INTO agendaInterna (nome, ramal) VALUES ('%s',%s)" %(nome,ramal)
        conexao = sqlite3.connect('agendaTeste.db')
        cursor = conexao.cursor()

        cursor.execute(adicionarRamalInterno)
        conexao.commit()

        print("Ramal adicionado!\n\n")


root = Tk()
Menu(root)
'''
while True:
    if (menu==1):
        Menu(root)
    if (menu==2):
        Menu(root)
    root.mainloop()
'''
root.mainloop()