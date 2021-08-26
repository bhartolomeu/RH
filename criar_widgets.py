#!/usr/bin/python3
#!/bin/python3
from tkinter import *
from tkinter import ttk

class Criar_Label:
    def __init__(self,root,texto,abcissa,ordenada,fonte,fundo):
         self.label=Label(root)
         self.label["text"]=texto
         self.label["font"]=fonte
         self.label["bg"]=fundo
         self.label.place(x=abcissa,y=ordenada)

#Será que deveríamos fazer polimorfismo aqui e fazer da classe Criar_Label a classe mãe?
class Criar_Label_Titulo:
    def __init__(self,root,texto,fonte,fundo):
         self.titulo=Label(root)
         self.titulo["text"]=texto
         self.titulo["font"]=fonte
         self.titulo["bg"]=fundo
         self.titulo.pack()

class Criar_Entry:
    def __init__(self,root,abcissa,ordenada,fonte,segredo):
         self.entry=Entry(root,font=fonte)
         self.entry.place(x=abcissa,y=ordenada)
         if segredo:
             self.entry["show"]="*"

class Criar_Button:
    def __init__(self,root,texto,fonte,fundo,comando,abcissa,ordenada):
         self.button=Button(root)
         self.button["text"]=texto
         self.button["font"]=fonte
         self.button["bg"]=fundo
         self.button["command"]=comando     
         self.button.place(x=abcissa,y=ordenada)
        
class Criar_RadioButton:
    def __init__(self,root,fonte,fundo,texto,abcissa,ordenada,var,identificador):
        
        self.radiobutton=Radiobutton(root)
        self.radiobutton["font"]=fonte
        self.radiobutton["bg"]=fundo
        self.radiobutton["text"]=texto
        self.radiobutton["value"]=identificador
        self.radiobutton["variable"]=var

        self.radiobutton.place(x=abcissa,y=ordenada)

class Criar_Spinbox:
    def __init__(self,root,origem,fim,abcissa,ordenada,largura):
         self.spinbox=Spinbox(root,from_=origem,to=fim,width=largura)
         self.spinbox.place(x=abcissa,y=ordenada)

class Criar_Listbox:
    def __init__(root,fonte,abcissa,ordenada,lista):
        self.listbox=Listbox(root,fonte,abcissa,ordenada)
        for i in lista:
            self.listbox.insert(lista[i])
        self.listbox.yview()
        self.place(x=abcissa,y=ordenada)

class Criar_Tabela():
    def __init__(self,root,conteudo,n_colunas,colunas):
        self.tabela=ttk.Treeview(root,columns=n_colunas,show="headings",height="60")
        for i in n_colunas:
            self.tabela.heading(i, colunas[i-1])
