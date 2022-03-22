#Banco de dados.py

#python -m pip install --upgrade pip
#pip3 install PyMySQL

#criar banco escola.db usando sqlite studio

import pymysql

def listaDatabases():
    #executa um comando SQL
    cursor.execute('show databases')

    #recupera resultado
    recordset = cursor.fetchall()  #fetch = buscar

    #mostra o resultado
    for registro in recordset:
        print (record)


if (__name__=='__main__'):
    #cria conexão com o banco
    conexao = mysql.conect(db='escola.db')
    #cria um cursor
    cursor = conexao.cursor()
    listaDatabases()
