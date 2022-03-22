#banco_dados_tela.py

from os.path import exists
from PyQt5.QtWidgets import*
from PyQt5.QtSql import*

import sys

if not exists('escola.db'):
    print('escola.db não existe')

app = QApplication([])

#Acessa a base de dados
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('escola.db')
db.open()

#acessa o banco de dados
model = QSqlTableModel(None,db)
model.setTable('aluno')
model.select()

#tela gráfica
view = QTableView()
view.setModel(model)
view.show()

app.exec_()
