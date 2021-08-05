from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="192.168.0.11",
    user="root",
    passwd="",
    database="marias_comodato"
)
cursor = banco.cursor()




"""pesquisa cliente ok """
def Button_Pc():
    linha_pes = alug.edtPesquisa_cliente.text()
    tipo_pes = alug.cbPesquisa_cliente.currentText()
    alug.edtPesquisa_cliente.setText("")
    while (alug.gridCliente.rowCount() > 0):
        alug.gridCliente.removeRow(0)
    
    comando_SQL = "SELECT * FROM cliente WHERE "+str(tipo_pes)+" LIKE '"+str(linha_pes)+"%'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    alug.gridCliente.setRowCount(len(dados_lidos))
    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            alug.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

"""pesquisa maquina ok """
def Button_Pm():
    linha_pes = alug.edtPesquisa_maquina.text()
    tipo_pes = alug.cbPesquisa_maquina.currentText()
    alug.edtPesquisa_maquina.setText("")
    while (alug.gridMaquina.rowCount() > 0):
        alug.gridMaquina.removeRow(0)

    comando_SQL = "SELECT * FROM maquina WHERE "+str(tipo_pes)+" LIKE '"+str(linha_pes)+"%' AND situacao = 'DISPONIVEL'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    alug.gridMaquina.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 7):
            alug.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


"""comodata"""
def Button_al():
    linha_cl = alug.gridCliente.currentItem()
    linha_maq = alug.gridMaquina.currentItem()
    if linha_cl and linha_maq:
        data = alug.lineEdit.text()
        linha_cl = alug.gridCliente.currentItem().row()
        codi = alug.gridCliente.item(linha_cl, 0).text()
        comando_SQL = "SELECT * FROM cliente WHERE cod = '" + str(codi) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        comodatos = str(dados_lidos[0][9])

        linha_maq = alug.gridMaquina.currentItem().row()
        patri = alug.gridMaquina.item(linha_maq, 0).text()

        comando_SQL = "SELECT * FROM maquina WHERE patrimonio =  '" + str(patri) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        situacao = str(dados_lidos[0][2])
        historico = str(dados_lidos[0][7])
        if data:
            comando_SQL = "INSERT INTO alugados (cod_cli, patrimonio) VALUES (%s,%s)"
            dados = (str(codi), str(patri))
            cursor.execute(comando_SQL,dados)
            banco.commit()
            situacao = "ALUGADO"
            historico = historico +"\nAlugado por "+str(codi)+" na data "+str(data)
            comando_SQL = "UPDATE maquina SET historico = '"+str(historico)+"', situacao = '"+str(situacao)+"'WHERE patrimonio = '" + str(patri) + "'"
            cursor.execute(comando_SQL)
            banco.commit()
            comodatos = comodatos + "\nComodatou o patrimonio " +str(patri)+ " na data " +str(data)
            comando_SQL = "UPDATE cliente SET historico = '" +str(comodatos)+ "' WHERE cod = '" + str(codi)+"'"
            cursor.execute(comando_SQL)
            banco.commit()


            NOT.label.setText("ITEM COMODATADO")
            NOT.show()
        
        else:
            NOT.label.setText("ERRO:DIGITE UMA DATA")
            NOT.show()










        comando_SQL = "SELECT * FROM maquina WHERE situacao = 'DISPONIVEL'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        alug.gridMaquina.setRowCount(len(dados_lidos))
        for i in range(0, len(dados_lidos)):
            for j in range(0, 7):
                alug.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
    elif linha_cl:
        NOT.label.setText("SELECIONE MAQUINA")
        NOT.show()
    elif linha_maq:
        NOT.label.setText("SELECIONE CLIENTE")
        NOT.show()
    else:
        NOT.label.setText("SELECIONE CLIENTE E MAQUINA")
        NOT.show()


NOT=uic.loadUi("interface/NOTIF.ui")
app=QtWidgets.QApplication([])
alug=uic.loadUi("interface/alugar.ui")

alug.btnPesquisar_cliente.clicked.connect(Button_Pc)
alug.btnPesquisar_maquina.clicked.connect(Button_Pm)
alug.pushButton.clicked.connect(Button_al)





#CHAMA TELA COMODATAR
#****************************************************************************************************#
def Button_alu():
    #listando dados da tabela cliente
    comando_SQL = "SELECT * FROM cliente"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    alug.gridCliente.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            alug.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    #listando dados da tabela cliente
    comando_SQL = "SELECT * FROM maquina WHERE situacao = 'DISPONIVEL'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    alug.gridMaquina.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 7):
            alug.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    alug.show()