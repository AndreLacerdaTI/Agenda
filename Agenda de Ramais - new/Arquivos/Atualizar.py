# to open/create a new html file in the write mode
f = open('C:\Agenda de Ramais - new\index.html', 'w', encoding="utf-8")
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
    TabelaInterna = TabelaInterna + "<tr>\n    <td>"+str(i[2])+"</td>\n    <td>"+str(i[1])+"</td>\n</tr>"

print(TabelaInterna)

# ADICIONANDO AGENDA DIRETA A VARIAVEL "TabelaDireta"

AgendaDireta = "SELECT * FROM agendaDireta ORDER BY nome"

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute(AgendaDireta)
AgendaDireta = cursor.fetchall()

for i in AgendaDireta:
    TabelaDireta = TabelaDireta + "<tr>\n    <td>"+str(i[2])+"</td>\n    <td>"+str(i[1])+"</td>\n</tr>"

print(AgendaDireta)



# CRIANDO O HTML ATUALIZADO INSERINDO AS DUAS VARIAVEIS (TabelaInterna e TabelaDireta) CONTENDO A TABELA

html_template = """<html>
    <style>
        @media print { 
        #noprint { display:none; } 
        body { background: #fff; }
        }
        @page {
            size:"A4";
            width: 21cm;
            height: 29.7cm;
        }
        ul{
            display: flex;
            list-style-type: none;
        }
        ul li a{
            display: flex;
            position: relative;
            width: 250px;
            height: 80px;
            border-radius: 23px;
            border: 2px solid #FED100;
            margin-right: 50px;
            font-size: 50px;
            text-decoration: none;
            justify-content: center;
            align-items: center;
            color: rgba(255,255,255,0.7);
            z-index: 5;
            transition: 0.3s;
        }
        /*
        ul li a::after{
            content: " ";
            position: absolute;
            left: 0;
            top: 0;
            width: 150px;
            height: 80px;
            border-radius: 23px;
            border: 2px solid #FED100;
            background: rgba(255, 255, 255, 0.325);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            z-index: -1;
            transition: 0.3s;
        }
        */
        ul li a:hover {
        /*transform: rotate(-5deg);*/
        transform: scale(1.15);
        }
        ul li a:hover::before {
            transform: rotate(-8deg);
        }
        /*
        ul li a::before {
            content: " ";
            position: absolute;
            width: 150px;
            height: 80px;
            background: #FED100;
            right: 0px;
            bottom: 0;
            border-radius: 23px;
            z-index: -1;
            transform-origin: 100% 100%;
            transform: rotate(-2deg);
            transition: 0.3s;
        }

        */
        body {
            background-color: #ffffff;
            height: 29.7cm;
            padding: 10;
        }

        div {
            margin: 10;
            float: left;
            width: 40%;
            padding: 1%;
            
            border-radius: 40px;
            border: 2px solid #FED100;
        }
        h1 {
            text-align: center;
            padding: 10px;
            color: #363636;
            font-size: 20;
            font-family: 'Arial';
            font-weight: 600;
            border-radius: 23px;
            border: 2px solid #FED100;
            width: 40%;
            float: left;
            margin: 12;

        }
        h2 {
            color: #363636;
            text-align: center;
            font-size: 8;
            font-family: 'Arial';
            font-weight: 600;
            padding: 10;
        }
        table {
            width: 100%;
            font-family: 'Arial';
            padding: 1;
        }
        .titulo-ramal  {
            width:30%;
            background:#262424;
            border-radius: 50px 0px 0px 0px;
        }
        .titulo-nome  {
            text-align: center;
            width:70%;
            background:#262424;
            border-radius: 0px 50px 0px 0px;

        }
        .rodape-ramal  {
            width:30%;
            background:#ffffff;
            border-radius: 0px 0px 0px 50px;
        }
        .rodape-nome  {
            text-align: center;
            width:70%;
            background:#ffffff;
            border-radius: 0px 0px 50px 0px;

        }
        th, td {
            color:#262424;
            text-align: center;
            font-weight: bold;
            border-bottom: 1px solid #aaaaaa;
            padding: 8px;
            }

        tr:hover {
            background-color: #FED100;
            transition: 0.3s;
        }
    </style>
<head>
    <title>Ramais Copobras MG</title>
    <meta http-equiv=”Content-Type” content=”text/html; charset=utf-8″>
    <link rel="stylesheet" type="text/css" href="Style/style.css" media="screen"/>
    <center>
      <img width= 30%; src="Imagens/ai.png">
    </center>
    <!-target="_blank" rel="noopener noreferrer"->
    <ul id="noprint">
        <li>
            <a href="imprimir.html">
                <h2>GERAR IMPRESSÃO</h2>
                <p><img src="Imagens/icone-impressora.png" width="35px" height="35px"></i></p>
            </a>
        </li>
    </ul>
</head>
<body class="A4">
    <h1>RAMAL INTERNO</h1>
    <h1>RAMAL DIRETO</h1>
    <div>
        <table>
        <tr>
            <th class="titulo-ramal"><img width= 10%; src="Imagens/Telef_icone.png" align="middle"></th>
            <th class="titulo-nome"><img width= 5%; src="Imagens/Pessoa_icone.png" align="middle"></th>
        </tr>
        """+TabelaInterna+"""
        </table> 
    </div>
    <div>
        <table>
            <tr>
                <th class="titulo-ramal"><img width= 10%; src="Imagens/Telef_icone.png" align="middle"></th>
                <td class="titulo-nome"><img width= 5%; src="Imagens/Pessoa_icone.png" align="middle"></td>
            </tr>
            """+TabelaDireta+"""
        </table>
    </div>
</body>
</html>"""
# writing the code into the file
f.write(html_template)
# close the file
f.close()




imp = open('C:\Agenda de Ramais - new\imprimir.html', 'w', encoding="utf-8")
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
    TabelaInterna = TabelaInterna + "<tr>\n    <td>"+str(i[2])+"</td>\n    <td>"+str(i[1])+"</td>\n</tr>"

print(TabelaInterna)

# ADICIONANDO AGENDA DIRETA A VARIAVEL "TabelaDireta"

AgendaDireta = "SELECT * FROM agendaDireta ORDER BY nome"

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute(AgendaDireta)
AgendaDireta = cursor.fetchall()

for i in AgendaDireta:
    TabelaDireta = TabelaDireta + "<tr>\n    <td>"+str(i[2])+"</td>\n    <td>"+str(i[1])+"</td>\n</tr>"

print(AgendaDireta)

# CRIANDO O HTML ATUALIZADO INSERINDO AS DUAS VARIAVEIS (TabelaInterna e TabelaDireta) CONTENDO A TABELA

html_imprimir = """<html>
    <style>
        body {
            background: rgb(255, 255, 255);
        }
        @page {
            background: white;
            display: block;
            margin: 0 auto;
            margin-bottom: 0.5cm;
            box-shadow: 0 0 0.5cm rgba(0, 0, 0, 0.5);
        }
        page[size="A4"] {
            width: 21cm;
            height: 29.7cm;
        }
        page[size="A4"][layout="portrait"] {
            width: 29.7cm;
            height: 21cm;
        }
        @media print {
            #noprint { display:none; }
            body,
            page {
            margin: 0;
            box-shadow: 0;
            }
        }
        head {
            padding: 10px;
            text-align: center;
            border: 2px solid #000000;
        }
        table {
            border-collapse: collapse;
            width: 50%;
            height: 50px;
            font-size: 80%;
            float: left;
        }
        table th {
            background-color: #ffffff;
            color: rgb(0, 0, 0);
            text-align: center;
        }
        th, td {
            border: 1px solid #000000;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #ffffff
        }

        ul{
            display: flex;
            list-style-type: none;
        }
        ul li a{
            display: flex;
            position: relative;
            width: 150px;
            height: 80px;
            border-radius: 23px;
            border: 2px solid #FED100;
            margin-right: 50px;
            font-size: 60px;
            text-decoration: none;
            justify-content: center;
            align-items: center;
            color: rgba(255,255,255,0.7);
            z-index: 5;
            transition: 0.3s;
            float: left;
        }
        h2 {
            color: #363636;
            text-align: center;
            font-size: 15;
            font-family: 'Arial';
            font-weight: 600;
            padding: 10;
        }
    </style>
    <head>
        <ul id="noprint">
            <li>
                <a href="" onclick="window.print()">
                    <h2>IMPRIMIR</h2>
                    <p><img src="Imagens/icone-impressora.png" width="40px" height=40px"></i></p>
                </a>
                <a href="index.html">
                    <h2>VOLTAR</h2>
                    <p><img src="Imagens/icone-voltar.png" width="35px" height="35px"></i></p>
                </a>
            </li>
        </ul>
        <title>Ramais Copobras MG</title>
        <meta http-equiv=”Content-Type” content=”text/html; charset=utf-8″>        
        <center>
          <img width= 20%; src="Imagens/ai.png">
        </center>
        <!-target="_blank" rel="noopener noreferrer"->
    </head>
    <body>
        
        
        <page size="A4">
            <table class="table">
            <thead>
                <tr>
                <th>Ramal</th>
                <th>Nome</th>
                </tr>
            </thead>
            <tbody>
        """+TabelaInterna+"""
        </tbody>
            </table>
        </page>
        <page size="A4">
            <table class="table">
                <thead>
                    <tr>
                    <th>Ramal</th>
                    <th>Nome</th>
                    </tr>
                </thead>
                <tbody>
            """+TabelaDireta+"""
        </tbody>
                </table>

        </page>
    </body>"""
# writing the code into the file
imp.write(html_imprimir)

# close the file
imp.close()