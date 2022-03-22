#banco_dados_sqlite.py

import sqlite3

#cria conexão
conexao = sqlite3.connect('escola.db')

#cria um cursor
cursor = conexao.cursor()

def criarTabela():
    sql = 'CREATE TABLE if not exists aluno ('\
            'id integer primary key, '\
            'nome varchar (100), '\
            'email varchar (100), '\
            'telefone varchar (14))'

    #cria tabela
    cursor.execute(sql)

def inserirDados():
    sql = 'INSERT INTO aluno VALUES (?, ?, ?, ?)'

    #dados
    recset = [
            (1, 'João da Silva', 'joao@gmail.com', '(42)98412-1234'),
            (2, 'Maria Padilha', 'maria@hotmail.com', '(42)991154567'),
            (3, 'Valdirene Conceição', 'valdicao@bol.com.br', '(42)991342387')
            ]

#insere dados na tabela
    for rec in recset:
        cursor.execute(sql, rec)

#confirma a transação
    conexao.commit()

def listarDados():
    #seleciona todos os registros da tabela aluno
    cursor.execute('select*from aluno')

    #recupera os resultados
    recset = cursor.fetchall()

    #mostra na tela
    for rec in recset:
        print ('ID: %d \t nome: %-18s \t E-mail: %-20s \t Telefone: %-20s' %rec)

    #fecha a conexão com o banco
        conexao.close()
    
#programa principal
if (__name__=='__main__'):
    #criarTabela()
    #inserirDados()
    listarDados()
