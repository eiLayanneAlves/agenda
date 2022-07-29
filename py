# Autor: Layanne Silva Alves
# Data: 19/08/2021
# Linguagem: Python
 

 
import time
import os
import sys
import string
import MySQLdb
 
if __name__=='__main__':
    opcaoUsuario()
def opcaoUsuario():
 
    os.system("clear");
    print "==================================="
    print "======= Agenda de Contatos ========"
    print "==================================="
    opcao = raw_input("Escolha a opcao desejada \n\n[1] - Cadastrar\n[2] - Consultar\n[3] - Alterar\n[4] - Excluir\n[5] - Mostrar Todos\n[6] - Sair")
 
    try:
        opcao = int(opcao)
        if opcao<1 or opção>6:
            os.system("clear");
            print "OPCAO INVALIDA: Verifique o valor digitado."
            time.sleep(2)
            opcaoUsuario()
    except:
        os.system("clear");
        print "OPÇÃOO INVÁLIDA: Verifique o valor digitado."
        time.sleep(2)
        opcaoUsuario()
 
    if opcao == 1:
        conecta = conectaBanco()
        funcCadastrar(conecta)
 
    elif opcao == 2:
        conecta = conectaBanco()
        funcConsultar(conecta)
 
    elif opcao == 3:
        conecta = conectaBanco()
        funcAlterar(conecta)
 
    elif opcao == 4:
        conecta = conectaBanco()
        funcExcluir(conecta)
 
    elif opcao == 5:
        conecta = conectaBanco()
        funcMostrarTodos(conecta)
 
    elif opcao == 6:
        sys.exit()
		
	def conectaBanco():
 
    HOST = "localhost"
    USER = "root"
    PASSWD = "SenhaDoseuBancodeDados"
    BANCO = "Agenda"
 
    try:
        conecta = MySQLdb.connect(HOST, USER, PASSWD)
        conecta.select_db(BANCO)
 
        except MySQLdb.Error, e:
            print "Erro: O banco especificado não foi encontrado.",e
        menu = raw_input()
        os.system("clear")
        opcaoUsuario()
 
    return conecta
	def funcCadastrar(conecta):
 
    print "\n\n Digite os dados: \n"
    name = str(raw_input("Nome: "))
    name = (name.upper())
    address = str(raw_input("Endereço: "))
    address = (address.upper())
    mail = str(raw_input("E-mail: "))
    mail = (mail.upper())
    fone = str(raw_input("Telefone: "))
    fone = (fone.upper())
    cursor = conecta.cursor()
 
    sql="INSERT INTO pessoas (nome,endereçoo,email,telefone) VALUES ('"+name+"','"+address+"','"+mail+"','"+fone+"')"
 
    try:
            cursor.execute(sql)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "Dados gravados com sucesso."
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()
	def funcConsultar(conecta):
 
    name = str(raw_input("\nDigite o Nome a Pesquisar: "))
    name = (name.upper())
    cursor = conecta.cursor()
    sql="SELECT * FROM pessoas WHERE nome='"+name+"'"
    resultados = 0
 
    try:
            cursor.execute(sql)
        resultado = cursor.fetchall()
        for dados in resultado:
            ide = dados[0]
                    nome = dados[1]
            endereco = dados[2]
            email = dados[3]
            telefone = dados[4]
            resultados= int(resultados)
            resultados = resultados + 1
            print"\n----------------------------\n"
            print " ID: %s\n Nome: %s\n Endereço: %s\n Email: %s\n Telefone: %s"%(ide, nome, endereco, email, telefone)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "\n\n Foram encontrados %d resultados"%resultados
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()
	def funcAlterar(conecta):
 
    print "\n\n Digite os dados:\n"
    ide = raw_input("ID do contato a alterar: ")
    novo_nome = raw_input("Novo Nome: ")
    novo_nome = (novo_nome.upper())
    cursor = conecta.cursor()
 
    sql = "UPDATE pessoas SET nome='"+novo_nome+"' WHERE id='"+ide+"'"
    try:
            cursor.execute(sql)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "Alteracao feita com sucesso."
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()
	def funcExcluir(conecta):
 
    print "\n\nDigite os dados:\n"
    ide_exclusao = raw_input("ID a Excluir: ")
    cursor = conecta.cursor()
 
    sql = "DELETE FROM pessoas WHERE id='"+ide_exclusao+"'"
    try:
            cursor.execute(sql)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "Exclusao feita com Sucesso."
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()
	def funcMostrarTodos(conecta):
 
    resultados = 0
    cursor = conecta.cursor()
    sql="SELECT * FROM pessoas;"
 
    try:
            cursor.execute(sql)
        resultado = cursor.fetchall()
 
        for dados in resultado:
            ide = dados[0]
                    nome = dados[1]
            endereço = dados[2]
            e-mail = dados[3]
            telefone = dados[4]
            resultados= int(resultados)
            resultados = resultados + 1
            print"----------------------------------"
            print " ID: %s\n Nome: %s\n Endereco: %s\n Email: %s\n Telefone: %s"%(ide, nome, endereco, email, telefone)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "\n\n Foram encontrados %d resultados"%resultados
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()
