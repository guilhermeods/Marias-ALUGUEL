from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="192.168.0.11",
    user="root",
    passwd="",
    database="marias_comodato"
)
cursor = banco.cursor()

#cadastro do cliente
def Button_salvar():
    
    #recebe valor
    descricao = CAD_COMAND.textEdit_descri.toPlainText()
    voltagem = CAD_COMAND.lineEdit_volt.text()
    marca = CAD_COMAND.lineEdit_marca.text()
    num_de_serie  = CAD_COMAND.lineEdit_num.text()
    tipo  = CAD_COMAND.lineEdit_tipo.text()
    historico = CAD_COMAND.textEdit.toPlainText()
    patrimonio = CAD_COMAND.lineEdit_patri.text()

    #limpa os campos
    CAD_COMAND.textEdit_descri.setText("")
    CAD_COMAND.lineEdit_volt.setText("")
    CAD_COMAND.lineEdit_marca.setText("")
    CAD_COMAND.lineEdit_num.setText("")
    CAD_COMAND.lineEdit_tipo.setText("")
    CAD_COMAND.textEdit.setText("")
    CAD_COMAND.lineEdit_patri.setText("")

    comando_SQL = "SELECT patrimonio FROM maquina WHERE patrimonio = '"+str(patrimonio)+"'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    if dados_lidos:
        NOT.show()
        NOT.label.setText("ERRO: Patrimonio Existente")
        
    else:
        #insere na tabela os dados
        comando_SQL = "INSERT INTO maquina (descricao, voltagem, marca, numero_de_serie, tipo, historico, patrimonio, situacao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(descricao),str(voltagem),str(marca),str(num_de_serie),str(tipo),str(historico),str(patrimonio), "DISPONIVEL")
        cursor.execute(comando_SQL,dados)
        banco.commit()
        NOT.show()
        NOT.label.setText("Comodato Cadastrado Com Sucesso")


app=QtWidgets.QApplication([])
CAD_COMAND=uic.loadUi("interface/CADASTRO_COMANDADO.ui")
NOT = uic.loadUi("interface/NOTIF.ui")
CAD_COMAND.pushButton_salvar.clicked.connect(Button_salvar)




#CHAMA TELA CADASTRO
#****************************************************************************************************#
def Button_CC():
    CAD_COMAND.show()
    