# to open/create a new html file in the write mode
f = open('C:\Agenda de Ramais\index.html', 'w')
#i = 0
TabelaInterna = ""
TabelaDireta = ""
# Importar banco

import sqlite3

# ADICIONANDO AGENDA INTERNA A VARIAVEL "TabelaInterna"

AgendaInterna = "SELECT * FROM agendaInterna ORDER BY nome"

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute(AgendaInterna)
AgendaInterna = cursor.fetchall()

for i in AgendaInterna:
    TabelaInterna = TabelaInterna + "<tr>\n    <th>"+str(i[2])+"</th>\n    <td>"+str(i[1])+"</td>\n</tr>"

print(TabelaInterna)

# ADICIONANDO AGENDA DIRETA A VARIAVEL "TabelaDireta"

AgendaDireta = "SELECT * FROM agendaDireta ORDER BY nome"

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute(AgendaDireta)
AgendaDireta = cursor.fetchall()

for i in AgendaDireta:
    TabelaDireta = TabelaDireta + "<tr>\n    <th>"+str(i[2])+"</th>\n    <td>"+str(i[1])+"</td>\n</tr>"

print(AgendaDireta)



# CRIANDO O HTML ATUALIZADO INSERINDO AS DUAS VARIAVEIS (TabelaInterna e TabelaDireta) CONTENDO A TABELA

# the html code which will go in the file GFG.html
html_template = """<html>
<style>
    @page {
        size:"A4";
        width: 21cm;
        height: 29.7cm;
    }
    body {
        background-color: #ffffff;
        height: 29.7cm;
    }
    th {
        background-color: #ffffff;
        width: 30%;
        border: 2px solid rgb(0, 0, 0);
    }
    td {
        background-color: #ffffff;
        width: 70%;
        border: 2px solid rgb(0, 0, 0);
    }

    div {
        float: left;
        width: 45%;
        padding-left: 4%;
    }
    h1 {
        text-align: center;
        background-color: #FED100;
        color: #242021;
        font-size: 20;
        font-family: 'Heavitas';
        border-radius: 50px;
    }
    table {
        background-color: #ffffff;
        width: 100%;
        font-family: 'Arial';
    }
    img {
        padding-bottom: 10;
        width: 30%;
    }
</style>
<head>
    <title>Ramais Copobras MG</title>
    <center>
      <img src="Imagens/ai.png" align="middle">
    </center>
</head>
<body class="A4">
    <div>
        <h1>RAMAL INTERNO</h1>
        <table>
"""+TabelaInterna+"""
        </table> 
    </div>
    <div>
        <h1 id="titulo-dir">RAMAL DIRETO</h1>
        <table>
"""+TabelaDireta+"""
        </table>
    </div>
</body>
</html>
"""
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()