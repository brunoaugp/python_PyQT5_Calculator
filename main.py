import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora PyQT5')  # altera nome do titulo da janela
        self.setFixedSize(400, 400)  # deixa o tamanho da janela fixo
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()  # cria o display da calculadora
        self.grid.addWidget(self.display, 0, 0, 1, 5)  # coloca o display na grid(lin inic,col inic, lin ocup,col ocup)
        self.display.setDisabled(True)  # nao deixa escrever no display
        self.display.setStyleSheet(
            '*{background: white; color: #000; font-size: 30px;}'  # configura cores e tamanho da fonte DO DISPLAY
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # autoajuste do display na tela

        ### ADICIONANDO BOTÕES ###

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)  # add botao na linha 1, col 0, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)  # add botao na linha 1, col 1, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)  # add botao na linha 1, col 2, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)  # add botao na linha 1, col 3, ocupando 1 linha e 1 coluna
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),  # apaga tudo que tiver no display
            'background: #d5580d;color: #fff;font-size: 20px;font-weight:300'
        )  # add botao na linha 1, col 4, ocupando 1 linha e 1 coluna

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)  # add botao na linha 2, col 0, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)  # add botao na linha 2, col 1, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)  # add botao na linha 2, col 2, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)  # add botao na linha 2, col 3, ocupando 1 linha e 1 coluna
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]  # apaga apenas o ultimo caractere do display
            ),
            'background: #13890a;color: #fff;font-size: 20px;font-weight:300'
        )  # add botao na linha 2, col 4, ocupando 1 linha e 1 coluna

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)  # add botao na linha 3, col 0, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)  # add botao na linha 3, col 1, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)  # add botao na linha 3, col 2, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)  # add botao na linha 3, col 3, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton(''), 3, 4, 1, 1)  # add botao na linha 3, col 4, ocupando 1 linha e 1 coluna

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)  # add botao na linha 4, col 0, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)  # add botao na linha 4, col 1, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton(''), 4, 2, 1, 1)  # add botao na linha 4, col 2, ocupando 1 linha e 1 coluna
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)  # add botao na linha 4, col 3, ocupando 1 linha e 1 coluna
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #095177;color: #fff;font-size: 20px;font-weight:300'
        )  # add botao na linha 4, col 4, ocupando 1 linha e 1 coluna

        self.setCentralWidget(self.cw)  # seta o widget central como o self.cw

    ### DEFININDO FUNCAO DE ADICIONAR BOTOES ###

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None,style=None):  # funcao para adicionar botoes
        self.grid.addWidget(btn, row, col, rowspan, colspan)  # para adicionar o botao

        if not funcao:  # verifica se o botao tem funcao (delete,clear,igual,etc)
            btn.clicked.connect(  # adiciona o texto do botao no display ao clicar para botoes sem funcao (1,2,3,4...)
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:  #se tiver style diferenciado, executa o style mencionada
            btn.setStyleSheet(style)
        else:
            btn.setStyleSheet(
                    '*{font-size: 20px;}'  # se nao, seta o tamanho da fonte DOS BOTOES
                )

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # autoajuste do botão na tela

    ### DEFININDO FUNCAO DE VERIFICAR A CONTA VÁLIDA ###
    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))  # executa a conta e passa o resultado para str
            )
        except Exception as e:
            self.display.setText('Conta Inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()  # instanciando calculadora
    calc.show()
    qt.exec_()
