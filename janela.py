#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from criar_widgets import *
from banco import *

class Janelas:
    def __init__(self,fonte,fundo,titulo,tela):
        #Esta é a variável da janela mãe
        self.root = Tk()

        #Esta é a cor de fundo da janela
        self.root["bg"]=fundo

        #Este é o título
        self.root.title(titulo)
        #self.root.wm_title(titulo)
        #self.titulo=Criar_Label_Titulo(self.root,titulo,fonte,fundo)

        #Este é o tamanho da janela
        self.root.geometry(tela)

class Menu(Janelas):
    def __init__(self,fonte,fundo,xy,tela,titulo):
        super().__init__(fonte,fundo,titulo,tela)

        abaixar,alinhar=30,70

        #logo=Image.open("logotipo.png")
        #logotipo = ImageTk.PhotoImage(logo)


        self.bt_login=Criar_Button(self.root,"AUTENTICAR",fonte,fundo,lambda:Autenticar(self.root, fonte, fundo, xy,"260x190","AUTENTICAR"),xy[0]+alinhar-5,xy[1]-10)

        self.bt_cadastrar=Criar_Button(self.root,"CADASTRO",fonte,fundo,lambda:Cadastrar(self.root,fonte, fundo,xy,"510x410","CADASTRO"),xy[0]+alinhar,xy[1]+abaixar+5)

class Autenticar(Janelas):
    def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo):

        janela_antiga.destroy()

        super().__init__(fonte,fundo,titulo,tela)

        abaixar,alinhar=30,70

        #self.title("Autenticar")
        self.var=StringVar()
        
        self.rg=Criar_RadioButton(self.root,fonte,fundo,"RG",xy[0]+alinhar,5,self.var,"rg")
        self.cpf=Criar_RadioButton(self.root,fonte,fundo,"CPF",xy[0],5,self.var,"cpf")
        self.escolha=Criar_Button(
            self.root,
            "Escolher",
            fonte,
            fundo,
            lambda:self.escolher_id(
                xy,
                abaixar,
                alinhar,
                fonte,
                fundo
                ),
            xy[0]+alinhar*2,
            5
            )

        self.orientar=Criar_Label(self.root,"ESCOLHA CPF OU RG",xy[0],xy[1]+abaixar,['Roboto',15],fundo)

        #Este é o tamanho da janela
        self.root.mainloop()

    def escolher_id(self,xy,abaixar,alinhar,fonte,fundo):        
        self.orientar.label.destroy()

        self.usuario=Criar_Label(self.root,self.var.get().upper(),xy[0],xy[1]+abaixar,fonte,fundo)
        self.entrar_usuario=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,False)

        #Label e entrada da senha respectivamente
        self.senha=Criar_Label(self.root,"SENHA",xy[0],xy[1]+abaixar*2,fonte,fundo)
        self.entrar_senha=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar*2,fonte,True)
        
        #Botão que fará a mudança para uma nova tela
        self.botao=Criar_Button(
            self.root,
            "AUTENTICAR",
            fonte,
            fundo,
            lambda:self.autenticar(fonte,fundo,xy),
            xy[0],
            xy[1]+abaixar*3)
        
    def autenticar(self,fonte,fundo,xy):
        banco=Banco()
        if self.var.get()=="cpf" or self.var.get()=="rg":
            print("cpf = '"+self.entrar_usuario.entry.get()+"'")
            banco.resultado = banco.mostrar(self.var.get()+",senha","Funcionario",self.var.get()+" = '"+self.entrar_usuario.entry.get()+"'")
            if (self.entrar_usuario.entry.get() == str(banco.resultado[0][0]) and self.entrar_senha.entry.get() == banco.resultado[0][1]):
                print("Você logou")
                menu_logado=Menu2(self.root,fonte,fundo,xy,"260x190","MENU")
            else:
                print("Usuário ou senha inválidos\nUsuario inserido:"+self.entrar_usuario.entry.get()+" Senha inserida:"+self.entrar_senha.entry.get()+"\nUsuario do banco:"+banco.resultado[0][0]+" Senha do banco:"+banco.resultado[0][1])  
        
class Cadastrar(Janelas):
    def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo):
        #Adeus janela  antiga
        janela_antiga.destroy()

        #olá janela nova
        super().__init__(fonte,fundo,titulo,tela)

        #As variáveis a seguir serão usadas para alinhar e abaixar cada widget
        abaixar,alinhar=30,150

        #Label e entrada do nome
        self.nome=Criar_Label(self.root,"NOME",xy[0],xy[1],fonte,fundo)
        self.entrar_nome=Criar_Entry(self.root,xy[0]+alinhar,xy[1],fonte,False)

        #Label e entrada do CPF
        self.cpf=Criar_Label(self.root,"CPF",xy[0],xy[1]+abaixar,fonte,fundo)
        self.entrar_cpf=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+abaixar,fonte,False)

        #Label e entrada do RG
        self.rg=Criar_Label(self.root,"RG",xy[0],xy[1]+2*abaixar,fonte,fundo)
        self.entrar_rg=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+2*abaixar,fonte,False)

        #Label e entrada do senha
        self.senha=Criar_Label(self.root,"SENHA",xy[0],xy[1]+3*abaixar,fonte,fundo)
        self.entrar_senha=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+3*abaixar,fonte,True)

        #Label e entrada do E-mail
        self.email=Criar_Label(self.root,"E-mail",xy[0],xy[1]+4*abaixar,fonte,fundo)
        self.entrar_email=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+4*abaixar,fonte,False)

        #Label e entrada do cargo
        self.cargo=Criar_Label(self.root,"CARGO",xy[0],xy[1]+5*abaixar,fonte,fundo)
        self.entrar_cargo=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+5*abaixar,fonte,False)

        #Label e entrada da formação
        self.formacao=Criar_Label(self.root,"FORMAÇÃO",xy[0],xy[1]+6*abaixar,fonte,fundo)
        self.entrar_formacao=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+6*abaixar,fonte,False)

        #Label e entrada do salário inicial
        self.sal_in=Criar_Label(self.root,"SALÁRIO INICIAL",xy[0],xy[1]+7*abaixar,fonte,fundo)
        self.entrar_sal_in=Criar_Entry(self.root,xy[0]+alinhar,xy[1]+7*abaixar,fonte,False)

        #Botão para cadastrar
        self.botao_cadastrar=Criar_Button(
            self.root,
            "CADASTRAR",
            fonte,
            fundo,
            lambda:self.salvar(
                (
                self.entrar_cpf.entry.get(),
                self.entrar_rg.entry.get(),
                self.entrar_senha.entry.get(),
                self.entrar_email.entry.get(),
                self.entrar_cargo.entry.get(),
                self.entrar_formacao.entry.get(),
                self.entrar_nome.entry.get(),
                self.entrar_sal_in.entry.get()
                ),
                fonte,
                fundo,
                xy
            ),
            xy[0]+alinhar,
            xy[1]+8*abaixar
            )

        self.root.mainloop()

    def salvar(self,dados,fonte,fundo,xy):
        #Conexão com o banco
        banco=Banco()
        #Inserir dados no banco
        banco.inserir("INSERT INTO Funcionario(cpf,rg,senha,email,cargo,formacao,nome,salario_inicial) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",dados)
        #Desconectando
        banco.desconectar()

        logar = Autenticar(self.root,fonte,fundo,xy,"260x190","AUTENTICAR")
    

class Menu2(Janelas):
    def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo):

        #Adeus janela  antiga
        janela_antiga.destroy()

        super().__init__(fonte,fundo,titulo,tela)

        abaixar,alinhar=30,70

        #logo=Image.open("logotipo.png")
        #logotipo = ImageTk.PhotoImage(logo)

        #Criando o título da Janela
        labelTitulo=Criar_Label_Titulo(self.root,"MENU",fonte,fundo)

        #Aqui está o botão para a janela de Projetos
        self.bt_proj=Criar_Button(
            self.root,
            "PROJETOS",
            fonte,
            fundo,
            lambda:Projetos(
                self.root, 
                fonte, 
                fundo, 
                xy,
                "260x190",
                "PROJETOS"
            ),
            xy[0]+alinhar-5,
            xy[1]-10
        )

        l       

        #self.bt_cadastrar=Criar_Button(self.root,"CADASTRO",fonte,fundo,lambda:Cadastrar(self.root,fonte, fundo,xy,"510x410","CADASTRO"),xy[0]+alinhar,xy[1]+abaixar+5)


class Projetos(Janelas):
    def __init__(self,janela_antiga,fonte,fundo,xy,tela,titulo):
        #Adeus janela  antiga
        janela_antiga.destroy()

        #olá janela nova
        super().__init__(fonte,fundo,titulo,tela)

        #Aqui está sendo colocado o título
        labelTitulo=Criar_Label_Titulo(self.root,"PROJETOS",fonte,fundo)
        
        #Aqui está o spinbox
        lista_campos=Criar_Spinbox(self.root,fonte,xy[0],xy[1],['ID','NOME DO PROJETO','INTEGRANTE','PRAZO','ORÇAMENTO'])

        #Aqui está a entrada para 
        entrar_valor=Criar_Entry(self.root,xy[0]+20,xy[1],fonte,False)

        #Aqui está o botão para submeter
        bt_confirmar=Criar_Button(
            self.root,
            "CONFIRMAR",
            fonte,
            fundo,
            lambda:Projetos.buscar_projeto(),
            xy[0]+40,
            xy[1]
            )
    def buscar_projeto(self):
        banco==Banco()
        __resultado=banco.mostrar()
        #__resultado
        self.mostrar_resultado=Criar_Tabela(root,(1,2,3,4),('ID','NOME DO PROJETO','INTEGRANTE','PRAZO','ORÇAMENTO'))
        self.mostrar_resultado.tabela.insert()
        print(__resultado)
        #self.chat1.insert()
