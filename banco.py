#!/bin/python3
import mysql.connector

class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
        	host="localhost", 
        	user="sysadmin", 
        	password="bhartolomeu1", 
        	database="RH"
        	)
        self.cursor = self.conexao.cursor()

    def mostrar(self,colunas,tabela, condicao):
    	print("SELECT "+colunas+" FROM "+tabela+" WHERE "+condicao+";")
    	cursor.execute("SELECT "+colunas+" FROM "+tabela+" WHERE "+condicao+";")
    	return cursor.fetchall()

    def inserir(self,comando,dados):
    	#comando="INSERT INTO "+tabela+" VALUES("+valores+")"
    	self.cursor.execute(comando,dados)
    	self.conexao.commit()

    def alterar(self,coluna,tabela):
    	self.cursor.execute("UPDATE "+tabela+" SET "+coluna+" = "+valores+";")

    def desconectar(self):
    	self.cursor.close()
    	self.conexao.close()


