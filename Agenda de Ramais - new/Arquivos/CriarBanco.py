import sqlite3

CriarAgendaInterna = """ CREATE TABLE IF NOT EXISTS agendaInterna (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        nome text NOT NULL,
                        ramal integer NOT NULL
                      ); """
CriarAgendaDireta = """ CREATE TABLE IF NOT EXISTS agendaDireta (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        nome text NOT NULL,
                        ramal integer NOT NULL
                      ); """                      

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute(CriarAgendaInterna)
cursor.execute(CriarAgendaDireta)