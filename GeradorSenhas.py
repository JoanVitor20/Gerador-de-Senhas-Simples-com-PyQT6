from random import *
import string
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
import pyperclip


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Gerador_de_Senhas/ui_GeradorSenha.ui', self) #Load the .ui file
        ######## Ações dos Botões ########
        self.BtnGerarSenha.clicked.connect(lambda: generateNewPass(self))
        self.BtnCopiarSenha.clicked.connect(lambda: copyPassToClipboard  (self))

        self.senha = ''
        def generateNewPass(self):
            self.senha = ''
            qtdCaracteres = self.quantidadeCaracteres.value() # Reference: https://doc.qt.io/qt-6/qspinbox.html

            if self.checkBox.isChecked(): #Reference: https://doc.qt.io/qt-6/qcheckbox.html
                # print('True')
                lista_caracteres = string.ascii_letters + string.digits + string.punctuation
            else:
                # print('False')
                lista_caracteres = string.ascii_letters + string.digits


            for x in range(qtdCaracteres):
                self.senha += (''.join(choice(lista_caracteres)))
            self.LblSenhaGerada.setText(self.senha)

            # print(qtdCaracteres)
            # print(self.senha)

        def copyPassToClipboard(self):
            if self.senha != '':
                pyperclip.copy(self.senha)
                self.LblAlertCopy.setText(f'A senha {self.senha}\nfoi copiada para o seu clipboard (CTRL + C).')
            else:
                print(self.senha)
                self.LblAlertCopy.setText('Gere uma senha antes de tentar copiar.')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')