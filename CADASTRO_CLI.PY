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
    nome = CAD_CLI.lineEdit_name.text()
    cnpj = CAD_CLI.lineEdit_cnpj.text()
    tel = CAD_CLI.lineEdit_end_2.text()
    email  = CAD_CLI.lineEdit_end_3.text()
    end  = CAD_CLI.lineEdit_end.text()
    bairro = CAD_CLI.lineEdit_bairro.text()
    cep = CAD_CLI.lineEdit_cep.text()
    cidade = CAD_CLI.lineEdit_cid.text()
    cod = CAD_CLI.lineEdit_cod.text()

    #limpa os campos
    CAD_CLI.lineEdit_name.setText("")
    CAD_CLI.lineEdit_cnpj.setText("")
    CAD_CLI.lineEdit_end_2.setText("")
    CAD_CLI.lineEdit_end_3.setText("")
    CAD_CLI.lineEdit_end.setText("")
    CAD_CLI.lineEdit_bairro.setText("")
    CAD_CLI.lineEdit_cep.setText("")
    CAD_CLI.lineEdit_cid.setText("")
    CAD_CLI.lineEdit_cod.setText("")

    comando_SQL = "SELECT cod FROM cliente WHERE cod = '"+str(cod)+"'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    if dados_lidos:
        NOT.show()
        NOT.label.setText("ERRO: Codigo Existente")
        
    else:
        #insere na tabela os dados
        comando_SQL = "INSERT INTO cliente (nome, cnpj, tel, email, end, bairro, cep, cidade, cod) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(nome),str(cnpj),str(tel),str(email),str(end),str(bairro),str(cep),str(cidade), str(cod))
        cursor.execute(comando_SQL,dados)
        banco.commit()
        NOT.show()
        NOT.label.setText("Cliente Cadastrado Com Sucesso")



app=QtWidgets.QApplication([])
CAD_CLI=uic.loadUi("interface/CADASTRO_CLIENTE.ui")
NOT = uic.loadUi("interface/NOTIF.ui")
CAD_CLI.pushButton_salvar.clicked.connect(Button_salvar)




#CHAMA TELA CADASTRO
#****************************************************************************************************#
def Button_CP():
    CAD_CLI.show()