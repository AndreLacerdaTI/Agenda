#!/usr/bin/python
# -*- coding: utf-8 -*-
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
teste = 1
input("Não se esqueça de atualizar o site!\nTecle qualquer tecla para fechar\n")
'''
#listaRamalDireta = [733,721,728,722,781,732,726,716,720,711,714,770,738,712,744,761,750,718,724,760,729,743,742,735,717,730,751,768,734,755,766,719,764,762,713,723,725,737,739,773,778,759,740,767,710,779,748,752,753,754,741,745]
#listaNomeDireta = ['ALAN','ALISSON – GERENTE','ANA FLÁVIA  (GIN)','ANDERSON (ELÉTRICA)','ANDRÉ (TI)','ARNALDO MORAIS','BRUNA BEATRIZ (GIN)','BRUNO (ELÉTR.BANDEJA)','CAMILA DINIZ (VENDAS)','CARLOS DINIZ (TEC. SEGURANÇA)','CARLOS FAGNER (ELETR.BANDEJA)','CORPO DE BOMBEIRO DE OLIVEIRA','COSME MORAIS (EXTRUSÃO)','DANIELA SILVA  (PCP)','DR.NINA','ELIAS','ÉLISSON (ELÉTRICA)','FÁBIO JÚNIOR (EXTRUSÃO)','FABIANA (TEC.SEGURANÇA)','FERNANDO GELAPE (ELÉTRICA)','GILBERTO ','GILBERTO (CASA)','GISELITUR (FIXO)','GISLENE (ALMOXARIFADO)','GRAZIELE BRAGA(LOGÍSTICA)','GRAZIELE PAZ(ALMOXARIFADO)','GUILHERME','JOAO PAULO(ELÉTRICA)','LUCIANO (MOTORISTA)','LUCIANO (MECÂNICO)','MAGNO (EXTRUSÃO)','MARCELINA (TEC.SEGURANÇA)','MARCIO BAGGIO','MARLON  ','NILTON (ELETR.BANDEJA)','OSTEC CENTRAL','POLÍCIA MILITAR','PRISCILA (ENFERMEIRA)','PRISCILA (ENFERMEIRA)','PRONTOMED','PRONTOMED','REST.CASARÃO','RICARDO RH','RONALDO (ELÉTRICA)','SAMU','SESMT','SODEXO (VANESSA)','TAXI – ARNALDO','TAXI – HUMBERTO','TAXI-TONINHO','VICENTE (GISELITUR CEL.)','VICENTE (GISELITUR CEL)']
#listaRamalInterna = [246,262,257,206,210,216,200,219,240,202,211,217,252,205,207,243,251,225,222,202,260,238,229,255,254,204,218,233,203,245,249,236,208,220,239,247,227,253,250,259,230,235,209,223,256,244,248,241,228,234,214,242,263,226,224,231,221,215,232,237,212,258]
#listaNomeInterna = ['ALAN','ALAN - ESTAGIO MANUTENÇÃO','ALEXSANDRO','ALISSON- GERENTE','ALLINY – LOGISTICA','ALMOXARIFADO','ANA ELISA-RECEPÇÃO','ANA FLAVIA – GIN','ANDRÉ – TI','ARNALDO MORAIS','AUDITÓRIO','BRUNA – GIN','BIANCA ANDRADE  - ESTAGIO BANDEJA','CAMILA- AUDIOMETRIA','CAMILA – VENDAS','CÉLIA','DANIELA DA SILVA – PCP','ESTAGIO TERMOFORMAGEM COPO','EDUARDO – LOGISTICA','ELÉTRICA - COPO','ELÉTRICA - BANDEJA','ELIAS','EXPEDIÇÃO – BANDEJA','EXPEDIÇÃO – COPO','EXTRUSÃO – BANDEJA','EXTRUSÃO - BANDEJA - SALA','EXTRUSÃO – COPO','FATURAMENTO ','FABIANA/CARLOS','ESTAGIO COPO','GABRIEL FALEIRO - MANUTENÇÃO','GILBERTO -CONTABILIDADE','GISLENE','GRAZIELE BRAGA','GUARITA','GUILHERME','JAQUELINE BORGES - VENDAS','LUANA ASSIS – CONTABILIDADE','LUANA - RH/DESENVOLVIMENTO','LYANDRA - VENDAS','MARCIA- RH','MÁRCIO BAGGIO','MIRIAM – RH/DESENVOLVIMENTO','MARIANA – VENDAS','MARLON – PCM','MATEUS – MANUTENÇÃO','MARCELINA','PRISCILA – ENFERMEIRA','REJANE – LOGISTICA','RENATA – LOGISTICA','RESTAURANTE','SALA DA EXTRUSÃO COPO','SALA VIDEO CONFERÊNCIA','TERMOFORMAGEM BANDEJA','TERMOFORMAGEM COPO','THAIS - RH ','VALERIA','VITOR  (ELÉTRICA)','GERALDO LIMA','WESLEY  - PCP','WICTOR - PCM','WITANY']
while i < len(listaRamalDireta):
    adicionarRamalDireta = "INSERT INTO agendaDireta (nome, ramal) VALUES ('%s',%s)" %(listaNomeDireta[i],listaRamalDireta[i])
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute(adicionarRamalDireta)
    conexao.commit()
    i = i+1
    print(i)
i = 0
while i < len(listaRamalInterna):
    adicionarRamalInterna = "INSERT INTO agendaInterna (nome, ramal) VALUES ('%s',%s)" %(listaNomeInterna[i],listaRamalInterna[i])
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute(adicionarRamalInterna)
    conexao.commit()
    i = i+1
    print(i)
'''
# adicionarRamal = "INSERT INTO agenda (nome, ramal) VALUES ('andre',240)"