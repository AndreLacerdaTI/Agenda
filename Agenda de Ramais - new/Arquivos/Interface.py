import tkinter
from tkinter import *
from tkinter import ttk

janela = Tk()

janela.title('Administrador Agenda')

texto = Label(janela, text='Bem vindo!',padx=100, pady=100)

texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Visualizar', command="")

botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text='')

texto_resposta.grid(column=0, row=2, padx=10, pady=10)
janela = Label(width = 60, height = 12, borderwidth = 1, relief = 'solid', bg = '#58FAF4')

janela.mainloop()
