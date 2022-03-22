#tela1.py
#pip install pyqt5
#https://github.com/pyqt/examples

from PyQt5.QtWidgets import*

#cria evento
def botao_clicado():
    alert=QMessageBox()
    alert.setText('Você clicou!')
    alert.exec_()

#cria aplicação
app=QApplication([])

#  cria botões
botaoAcima=QPushButton('Acima')
botaoAbaixo= QPushButton('Abaixo')

#define eventos dos botões
botaoAcima.clicked.connect(botao_clicado)
botaoAbaixo.clicked.connect(botao_clicado)

#cria layout vertical
layout= QVBoxLayout()


#adiciona botôes no layout
layout.addWidget(botaoAcima)
layout.addWidget (botaoAbaixo)

#cria  uma janela
window = QWidget()

#define o layout da janela
window.setLayout(layout)

#mostra a janela com o layout vertical e os botões
window.show()
app.exec_()
