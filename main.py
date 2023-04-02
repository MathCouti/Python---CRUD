from PyQt6 import uic, QtWidgets

def ChamarJanela():
    print("teste1")
    cadastro.show()


app = QtWidgets.QApplication([])
menu = uic.loadUi('telalogin.ui')
cadastro = uic.loadUi('cadastro.ui')
menu.Bt_cad.clicked.connect(ChamarJanela)

menu.show()
app.exec()