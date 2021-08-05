from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="192.168.0.11",
    user="root",
    passwd="",
    database="marias_comodato"
)
cursor = banco.cursor()

def pesquisar():
    tipo = dev.cbPesquisa.currentText()
    linha = dev.lineEdit.text()
    while (dev.gridCliente.rowCount() > 0):
        dev.gridCliente.removeRow(0)

    if tipo == "Codigo do cliente":
        comando_SQL = "SELECT patrimonio FROM alugados WHERE cod_cli = '"+str(linha)+"'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        dev.gridCliente.setRowCount(len(dados_lidos))
        comandoc_SQL = "SELECT * FROM cliente WHERE cod = '"+str(linha)+"'"
        cursor.execute(comandoc_SQL)
        dados_lidosc = cursor.fetchall()
        for i in range(0, len(dados_lidos)):
            for j in range(0, 6):
                dev.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidosc[0][j])))
                dev.gridCliente.setItem(i,6,QtWidgets.QTableWidgetItem(str(dados_lidos[i][0])))
    
    elif tipo == "Patrimonio" :
        comando_SQL = "SELECT cod_cli FROM alugados WHERE patrimonio = '"+str(linha)+"'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        if dados_lidos:
            dev.gridCliente.setRowCount(len(dados_lidos))
            codi= dados_lidos[0][0]
            comandoc_SQL = "SELECT * FROM cliente WHERE cod = '"+str(codi)+"'"
            cursor.execute(comandoc_SQL)
            dados_lidosc = cursor.fetchall()
            for i in range(0, len(dados_lidos)):
                for j in range(0, 6):
                    dev.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidosc[0][j])))
                    dev.gridCliente.setItem(i,6,QtWidgets.QTableWidgetItem(str(linha)))


        

def devolver():
    data = dev.lineEdit_2.text()
    linha_cl = dev.gridCliente.currentItem()
    if linha_cl:
        linha_cl = dev.gridCliente.currentItem().row()
        codi = dev.gridCliente.item(linha_cl, 0).text()
        comando_SQL = "SELECT * FROM cliente WHERE cod = '" + str(codi) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        comodatos = str(dados_lidos[0][9])
        patri = dev.gridCliente.item(linha_cl, 6).text()
        comando_SQL = "SELECT * FROM maquina WHERE patrimonio =  '" + str(patri) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        situacao = str(dados_lidos[0][2])
        historico = str(dados_lidos[0][7])
        if data:
            comando_SQL = "DELETE FROM alugados WHERE patrimonio =  '" + str(patri) + "'"
            cursor.execute(comando_SQL)
            banco.commit()
            situacao = "REVISAO"
            historico = historico +"-Devolvido na data "+str(data)
            comando_SQL = "UPDATE maquina SET historico = '"+str(historico)+"', situacao = '"+str(situacao)+"'WHERE patrimonio = '" + str(patri) + "'"
            cursor.execute(comando_SQL)
            banco.commit()
            comodatos = comodatos + "\nDevolveu o patrimonio " +str(patri)+ " na data " +str(data)
            comando_SQL = "UPDATE cliente SET historico = '" +str(comodatos)+ "' WHERE cod = '" + str(codi)+"'"
            cursor.execute(comando_SQL)
            banco.commit()

            NOT.label.setText("ITEM DISTRATADO")
            NOT.show()

        else:
            NOT.label.setText("ERRO:DIGITE UMA DATA")
            NOT.show()
    else:
        NOT.label.setText("ERRO:SELECIONE UM ITEM")
        NOT.show()

    #listando dados da tabela cliente
    comando_SQL = "SELECT * FROM alugados"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    dev.gridCliente.setRowCount(len(dados_lidos))
    for i in range(0, len(dados_lidos)):
        codi= dados_lidos[i][0]
        patri= dados_lidos[i][1]
        comandoc_SQL = "SELECT * FROM cliente WHERE cod = '"+str(codi)+"'"
        cursor.execute(comandoc_SQL)
        dados_lidosc = cursor.fetchall()
        for j in range(0, 6):
            dev.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidosc[0][j])))
            dev.gridCliente.setItem(i,6,QtWidgets.QTableWidgetItem(str(patri)))


NOT=uic.loadUi("interface/NOTIF.ui")
app = QtWidgets.QApplication([])
dev = uic.loadUi("interface/DEVOLVER.ui")




dev.btnPesquisar.clicked.connect(pesquisar)
dev.btnExcluir.clicked.connect(devolver)

#CHAMA TELA DISTRATO
#****************************************************************************************************#
def Button_D():
    #listando dados da tabela cliente
    comando_SQL = "SELECT * FROM alugados"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    dev.gridCliente.setRowCount(len(dados_lidos))
    for i in range(0, len(dados_lidos)):
        codi= dados_lidos[i][0]
        patri= dados_lidos[i][1]
        comandoc_SQL = "SELECT * FROM cliente WHERE cod = '"+str(codi)+"'"
        cursor.execute(comandoc_SQL)
        dados_lidosc = cursor.fetchall()
        for j in range(0, 6):
            dev.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidosc[0][j])))
            dev.gridCliente.setItem(i,6,QtWidgets.QTableWidgetItem(str(patri)))

    dev.show()