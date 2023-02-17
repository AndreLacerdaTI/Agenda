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
menu = 0
ramal = 0
nome = ""
 
"""
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()

def main():
    master = Tk()
    master.grid()
    altura = master.winfo_screenmmheight()
    altura = int((altura*50)/100)
    largura = master.winfo_screenmmwidth()
    print("largura antes: ",largura)
    largura = int((largura*50)/100)
    print("largura depois: ",largura)
    label1 = Label(master, width = largura, height = altura, borderwidth = 1, relief = 'solid', bg = '#ffffff')
    label1.grid(row=0, column=0, rowspan = 2)
    label1.update()
    

    mainloop()

main()
"""
def Adicionar():
    telaAdicionar = Tk()
    telaAdicionar.grid()

    tk.Label(telaAdicionar, text='').grid()

    #ramal = int(input("Digite o ramal: "))
    tk.Label(telaAdicionar, text="EmployeeID:").grid(row=0)
    e = tk.Entry(telaAdicionar)
    #nome = input("Digite o nome: ")
    print("Adicionando")

    adicionarRamalDireta = "INSERT INTO agendaDireta (nome, ramal) VALUES ('%s',%s)" %(nome,ramal)
    conexao = sqlite3.connect('agendaTeste.db')
    cursor = conexao.cursor()

    cursor.execute(adicionarRamalDireta)
    conexao.commit()
    print("Ramal adicionado!\n\n")
    mainloop()
Adicionar()
"""
import sqlite3

listaRamalDireta = []
listaNomeDireta = []
listaRamalInterna = []
listaNomeInterna = []
i = 0
menu = 0
ramal = 0
nome = ""
while True:
    print("Menu\n 1 - Adicionar Ramal Interno \n 2 - Adicionar Ramal Direto \n 3 - Excluir Ramal Interno \n 4 - Excluir Ramal Direto \n 5 - Exibir agenda \n 9 - Finalizar")
    menu = int(input("Digite a opção que deseja: "))
    if menu==1:
        print("\n\n\n\nAdicionar Ramal Interno")
        ramal = int(input("Digite o ramal: "))
        nome = input("Digite o nome: ")
        print("Adicionando")

        adicionarRamalInterna = "INSERT INTO agendaInterna (nome, ramal) VALUES ('%s',%s)" %(nome,ramal)
        conexao = sqlite3.connect('agenda.db')
        cursor = conexao.cursor()

        cursor.execute(adicionarRamalInterna)
        conexao.commit()

        print("Ramal adicionado!\n\n")

    if menu==2:
        print("\n\n\n\nAdicionar Ramal Direto")
        ramal = int(input("Digite o ramal: "))
        nome = input("Digite o nome: ")
        print("Adicionando")

        adicionarRamalDireta = "INSERT INTO agendaDireta (nome, ramal) VALUES ('%s',%s)" %(nome,ramal)
        conexao = sqlite3.connect('agenda.db')
        cursor = conexao.cursor()

        cursor.execute(adicionarRamalDireta)
        conexao.commit()
        print("Ramal adicionado!\n\n")
    if menu==3:
        print("\n\n\nExcluir Ramal Interno")
        info = input("Digite o nome ou ramal a ser excluido: ")
        excluirRamalInterno ="DELETE FROM agendaInterna WHERE ramal = "+str(info)
        conexao = sqlite3.connect('agenda.db')
        cursor = conexao.cursor()

        cursor.execute(excluirRamalInterno)
        conexao.commit()
        print("Ramal "+info+" excluido!\n\n")
    if menu==4:
        print("\n\n\nExcluir Ramal Direto")
        info = int(input("Digite o ramal a ser excluido: "))
        excluirRamalInterno = "DELETE FROM agendaDireta WHERE ramal = "+str(info)
        conexao = sqlite3.connect('agenda.db')
        cursor = conexao.cursor()

        cursor.execute(excluirRamalInterno)
        conexao.commit()
        print("Ramal "+str(info)+" excluido!\n\n")
    if menu==5:
        printar = "SELECT * FROM agendaInterna ORDER BY nome"

        conexao = sqlite3.connect('agenda.db')
        cursor = conexao.cursor()

        cursor.execute(printar)
        agendaInterna = cursor.fetchall()
        print("Agenda Interna")
        for i in agendaInterna:
            print("id: ", i[0],"Nome: ", i[1], "Ramal:", i[2])

        printarDireta = "SELECT * FROM agendaDireta ORDER BY nome"

        conexao = sqlite3.connect('agenda.db')
        cursor = conexao.cursor()

        cursor.execute(printarDireta)
        agendaDireta = cursor.fetchall()
        print("Agenda Direta")
        for i in agendaDireta:
            print("id: ", i[0],"Nome: ", i[1], "Ramal:", i[2])
    if menu==9:
        break
"""