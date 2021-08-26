drop database RH;
create database IF NOT EXISTS RH;
use RH;

create table IF NOT EXISTS Funcionario (
	id_func int not null AUTO_INCREMENT,
	cpf varchar(11) not null unique,
	rg varchar(9) not null unique,
	senha varchar(160) not null,
	email varchar(160) not null,
	cargo varchar(160) not null,
	formacao varchar(160) not null,
    salario_inicial int not null,
	PRIMARY KEY(id_func)
);

create table IF NOT EXISTS Projeto(
    id_proj int not null AUTO_INCREMENT,
    id_func1 int not null,
    id_func2 int not null,
    descricao varchar(160) not null,
    orcamento int,
    prazo date,

    PRIMARY KEY(id_proj),
    FOREIGN KEY (id_func1) REFERENCES Funcionario(id_func),
    FOREIGN KEY (id_func2) REFERENCES Funcionario(id_func)
);

create table IF NOT EXISTS Salario(
    numero_conta_bancaria varchar(16) not null unique,
    conta_bancaria varchar(8) not null unique,
    agencia varchar(4),
    id_func int not null,
    carga_horaria int not null,
    carga_horaria_cumprida int not null,
    carteira_de_trabalho varchar(160) not null,
    salario int not null,

    PRIMARY KEY(numero_conta_bancaria, conta_bancaria),
    FOREIGN KEY (id_func) REFERENCES Funcionario(id_func)
);

create table IF NOT EXISTS Ultima_Alter (
	id_Alt int not null AUTO_INCREMENT unique,
	id_func int not null,
    ultima_modificao date not null,
    autor varchar(160) not null,
    descricao varchar(160) not null,

    cpf_momento varchar(11) not null unique,
    rg_momento varchar(9) not null unique,
	senha_momento varchar(160) not null,
	email_momento varchar(160) not null,
	formacao_momento varchar(160) not null,

    conta_bancaria_momento varchar(16) not null,
    carteira_de_trabalho varchar(160) not null,
    agencia_momento varchar(4) not null,
    carga_horaria_momento int not null,
    carga_horaria_cumprida_momento int not null,
    salario_momento int not null,
    bonus_salarial int,
    aumento int,

    PRIMARY KEY(id_Alt),
    FOREIGN KEY (id_func) REFERENCES Funcionario(id_func)
);