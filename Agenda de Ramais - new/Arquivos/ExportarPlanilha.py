from openpyxl import Workbook
# Conexão com banco
import sqlite3

printar = "SELECT * FROM agendaInterna"
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute(printar)
agendaInterna = cursor.fetchall()

Direta = "SELECT * FROM agendaDireta"
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute(Direta)
agendaDireta = cursor.fetchall()

# Criando planilha
book = Workbook()
sheet = book.active
nome_xlsx = 'Ramais Atualizados.xlsx'

sheet['A1'] = 'Ramais Internos'
sheet['C1'] = 'Ramais Diretos'
sheet['A2'] = 'Ramal'
sheet['B2'] = 'Nome'
sheet['C2'] = 'Ramal'
sheet['D2'] = 'Nome'

cont = 3
for i in agendaInterna:
  print("Nome: ", i[1], "Ramal", i[2])
  sheet['A'+str(cont)] = int(i[2])
  sheet['B'+str(cont)] = str(i[1])
  cont = cont + 1
cont = 3
for i in agendaDireta:
  print("Nome: ", i[1], "Ramal", i[2])
  sheet['C'+str(cont)] = int(i[2])
  sheet['D'+str(cont)] = str(i[1])
  cont = cont + 1

book.save(nome_xlsx)