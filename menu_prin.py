from PyQt5 import uic,QtWidgets
import CADASTRO_CLI
import CADASTRO_COMD
import PESQ
import ALUG
import DEV

#MAIN CODE
#****************************************************************************************************#
app=QtWidgets.QApplication([])
MENU_PRIN=uic.loadUi("interface/MENU_PRIN.ui")


#COMANDO DOS BOTOES
#****************************************************************************************************#
MENU_PRIN.pushButton_AL.clicked.connect(ALUG.Button_alu)
MENU_PRIN.pushButton_CP.clicked.connect(CADASTRO_CLI.Button_CP)
MENU_PRIN.pushButton_CC.clicked.connect(CADASTRO_COMD.Button_CC)
MENU_PRIN.pushButton_PC.clicked.connect(PESQ.Button_PC)
MENU_PRIN.pushButton_D.clicked.connect(DEV.Button_D)






 





MENU_PRIN.show()
app.exec() 