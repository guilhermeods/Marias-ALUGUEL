from PyQt5 import uic,QtWidgets
import mysql.connector



banco = mysql.connector.connect(
    host="192.168.0.11",
    user="root",
    passwd="",
    database="marias_comodato"
)
cursor= banco.cursor()


"""PESQUISAR CLIENTE ok"""
def Button_Pc():
    linha_pes = PES.edtPesquisa_cliente.text()
    tipo_pes = PES.cbPesquisa_cliente.currentText()
    PES.edtPesquisa_cliente.setText("")
    while (PES.gridCliente.rowCount() > 0):
        PES.gridCliente.removeRow(0)
    
    comando_SQL = "SELECT * FROM cliente WHERE "+str(tipo_pes)+" LIKE '"+str(linha_pes)+"%'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    PES.gridCliente.setRowCount(len(dados_lidos))
    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            PES.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


"""PESQUISAR MAQUINA ok"""
def Button_Pm():
    linha_pes = PES.edtPesquisa_maquina.text()
    tipo_pes = PES.cbPesquisa_maquina.currentText()
    PES.edtPesquisa_maquina.setText("")
    while (PES.gridMaquina.rowCount() > 0):
        PES.gridMaquina.removeRow(0)

    comando_SQL = "SELECT * FROM maquina WHERE "+str(tipo_pes)+" LIKE '"+str(linha_pes)+"%'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    PES.gridMaquina.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 7):
            PES.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


"""VISUALIZAR CLIENTE ok"""
def Button_vcli():

    linha = PES.gridCliente.currentItem()
    if linha:
        linha = PES.gridCliente.currentItem().row()
        codi = PES.gridCliente.item(linha, 0).text()

        comando_SQL = "SELECT * FROM cliente WHERE cod = '" + str(codi) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        nome = str(dados_lidos[0][1])
        cnpj = str(dados_lidos[0][2])
        endereco = str(dados_lidos[0][3])
        email = str(dados_lidos[0][4])
        telefone = str(dados_lidos[0][5])
        bairro = str(dados_lidos[0][6])
        cep = str(dados_lidos[0][7])
        cidade = str(dados_lidos[0][8])
        comodatos = str(dados_lidos[0][9])
        
        VISU_CLI.label_10.setText(nome)
        VISU_CLI.label_11.setText(cnpj)
        VISU_CLI.label_12.setText(telefone)
        VISU_CLI.label_13.setText(email)
        VISU_CLI.label_14.setText(endereco)
        VISU_CLI.label_15.setText(bairro)
        VISU_CLI.label_16.setText(cep)
        VISU_CLI.label_17.setText(cidade)
        VISU_CLI.label_18.setText(codi)
        if comodatos:
            VISU_CLI.textBrowser.setText(comodatos)


            
        VISU_CLI.show()
    else:
        NOT.label.setText("NADA FOI SELECIONADO")
        NOT.show()


"""VISUALIZAR MAQUINA ok"""
def Button_vmaq():
    linha = PES.gridMaquina.currentItem()
    if linha:
        linha = PES.gridMaquina.currentItem().row()
        patri = PES.gridMaquina.item(linha, 0).text()

        comando_SQL = "SELECT * FROM maquina WHERE patrimonio =  '" + str(patri) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        descricao = str(dados_lidos[0][1])
        situacao = str(dados_lidos[0][2])
        marca = str(dados_lidos[0][3])
        numero_de_serie = str(dados_lidos[0][4])
        voltagem = str(dados_lidos[0][5])
        tipo = str(dados_lidos[0][6])
        historico = str(dados_lidos[0][7])



        VISU_COMO.label_9.setText(descricao)
        VISU_COMO.label_14.setText(situacao)
        VISU_COMO.label_11.setText(marca)
        VISU_COMO.label_12.setText(numero_de_serie)
        VISU_COMO.label_10.setText(voltagem)
        VISU_COMO.label_13.setText(tipo)
        VISU_COMO.label_15.setText(patri)
        if historico:
            VISU_COMO.textBrowser.setText(historico)

        VISU_COMO.show()
    else :
        NOT.label.setText("NADA FOI SELECIONADO")
        NOT.show()


"""EXCLUIR CLIENTE ok"""
def Button_excli():
    linha = PES.gridCliente.currentItem()
    if linha:
        linha = PES.gridCliente.currentItem().row()
        codi = PES.gridCliente.item(linha, 0).text()
        comando_SQL = "SELECT * FROM cliente WHERE cod = '" + str(codi) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        nome = str(dados_lidos[0][1])
        cnpj = str(dados_lidos[0][2])
        endereco = str(dados_lidos[0][3])
        email = str(dados_lidos[0][4])
        telefone = str(dados_lidos[0][5])
        bairro = str(dados_lidos[0][6])
        cep = str(dados_lidos[0][7])
        cidade = str(dados_lidos[0][8])
        comodatos = str(dados_lidos[0][9])
        EXCLUI_CLI.label_10.setText(nome)
        EXCLUI_CLI.label_11.setText(cnpj)
        EXCLUI_CLI.label_12.setText(telefone)
        EXCLUI_CLI.label_13.setText(email)
        EXCLUI_CLI.label_14.setText(endereco)
        EXCLUI_CLI.label_15.setText(bairro)
        EXCLUI_CLI.label_16.setText(cep)
        EXCLUI_CLI.label_17.setText(cidade)
        EXCLUI_CLI.label_18.setText(codi)

        def excluir():
            comando_SQL = "DELETE FROM cliente WHERE cod = '" + str(codi) + "'"
            cursor.execute(comando_SQL)
            banco.commit()

            while (PES.gridCliente.rowCount() > 0):
                PES.gridCliente.removeRow(0)
            comando_SQL = "SELECT * FROM cliente"
            cursor.execute(comando_SQL)
            dados_lidos = cursor.fetchall()
            PES.gridCliente.setRowCount(len(dados_lidos))

            for i in range(0, len(dados_lidos)):
                for j in range(0, 6):
                    PES.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            EXCLUI_CLI.hide()
            NOT.label.setText("ITEM EXCLUIDO")
            NOT.show()



        EXCLUI_CLI.pushButton_salvar.clicked.connect(excluir)
        EXCLUI_CLI.show()    
    else:
        NOT.label.setText("NADA FOI SELECIONADO")
        NOT.show()
    

"""EXCLUIR MAQUINA ok"""
def Button_exmaq():
    linha = PES.gridMaquina.currentItem()
    if linha:
        linha = PES.gridMaquina.currentItem().row()
        patri = PES.gridMaquina.item(linha, 0).text()

        comando_SQL = "SELECT * FROM maquina WHERE patrimonio =  '" + str(patri) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        descricao = str(dados_lidos[0][1])
        situacao = str(dados_lidos[0][2])
        marca = str(dados_lidos[0][3])
        numero_de_serie = str(dados_lidos[0][4])
        voltagem = str(dados_lidos[0][5])
        tipo = str(dados_lidos[0][6])
        historico = str(dados_lidos[0][7])
        EXCLUI_MAQ.textBrowser.setText(descricao)
        EXCLUI_MAQ.label_11.setText(marca)
        EXCLUI_MAQ.label_12.setText(numero_de_serie)
        EXCLUI_MAQ.label_10.setText(voltagem)
        EXCLUI_MAQ.label_3.setText(tipo)
        EXCLUI_MAQ.label_13.setText(patri)

        def excluir():
            comando_SQL = "DELETE FROM maquina WHERE patrimonio =  '" + str(patri) + "'"
            cursor.execute(comando_SQL)
            banco.commit()
            while (PES.gridMaquina.rowCount() > 0):
                PES.gridMaquina.removeRow(0)

            comando_SQL = "SELECT * FROM maquina"
            cursor.execute(comando_SQL)
            dados_lidos = cursor.fetchall()
            PES.gridMaquina.setRowCount(len(dados_lidos))
            for i in range(0, len(dados_lidos)):
                for j in range(0, 7):
                    PES.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            EXCLUI_MAQ.hide()
            NOT.label.setText("ITEM EXCLUIDO")
            NOT.show()
        
        
        EXCLUI_MAQ.pushButton_salvar.clicked.connect(excluir)
        EXCLUI_MAQ.show()
        if str(situacao) == "ALUGADO":
            EXCLUI_MAQ.hide()
            NOT.label.setText("ESSE ITEM ESTA COMODATADO")
            NOT.show()

    else :
        NOT.label.setText("NADA FOI SELECIONADO")
        NOT.show()


"""EDITAR CLIENTE ok"""
def Button_edcli():
    linha = PES.gridCliente.currentItem()
    if linha:
        linha = PES.gridCliente.currentItem().row()
        codi = PES.gridCliente.item(linha, 0).text()
        comando_SQL = "SELECT * FROM cliente WHERE cod = '" + str(codi) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        nome = str(dados_lidos[0][1])
        cnpj = str(dados_lidos[0][2])
        endereco = str(dados_lidos[0][3])
        email = str(dados_lidos[0][4])
        telefone = str(dados_lidos[0][5])
        bairro = str(dados_lidos[0][6])
        cep = str(dados_lidos[0][7])
        cidade = str(dados_lidos[0][8])
        comodatos = str(dados_lidos[0][9])
        EDITAR_CLI.lineEdit_name.setText(nome)
        EDITAR_CLI.lineEdit_cnpj.setText(cnpj)
        EDITAR_CLI.lineEdit_end_2.setText(telefone)
        EDITAR_CLI.lineEdit_end_3.setText(email)
        EDITAR_CLI.lineEdit_end.setText(endereco)
        EDITAR_CLI.lineEdit_bairro.setText(bairro)
        EDITAR_CLI.lineEdit_cep.setText(cep)
        EDITAR_CLI.lineEdit_cid.setText(cidade)
        EDITAR_CLI.label_10.setText(codi)
        def editar():
            nome = EDITAR_CLI.lineEdit_name.text()
            cnpj = EDITAR_CLI.lineEdit_cnpj.text()
            endereco = EDITAR_CLI.lineEdit_end.text()
            email = EDITAR_CLI.lineEdit_end_3.text()
            telefone = EDITAR_CLI.lineEdit_end_2.text()
            bairro = EDITAR_CLI.lineEdit_bairro.text()
            cep = EDITAR_CLI.lineEdit_cep.text()
            cidade = EDITAR_CLI.lineEdit_cid.text()
            
            comando_SQL = "UPDATE cliente SET nome = '"+str(nome)+"',cnpj = '"+str(cnpj)+"',end = '"+str(endereco)+"',email = '"+str(email)+"',tel = '"+str(telefone)+"',bairro = '"+str(bairro)+"',cep = '"+str(cep)+"', cidade = '"+str(cidade)+ "' WHERE cod = '" + str(codi)+"'"
            cursor.execute(comando_SQL)
            banco.commit()
            while (PES.gridCliente.rowCount() > 0):
                PES.gridCliente.removeRow(0)
            comando_SQL = "SELECT * FROM cliente"
            cursor.execute(comando_SQL)
            dados_lidos = cursor.fetchall()
            PES.gridCliente.setRowCount(len(dados_lidos))

            for i in range(0, len(dados_lidos)):
                for j in range(0, 6):
                    PES.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            EDITAR_CLI.hide()
            NOT.label.setText("ITEM EDITADO")
            NOT.show()

        EDITAR_CLI.pushButton_salvar.clicked.connect(editar)
        EDITAR_CLI.show()

    else :
        NOT.label.setText("NADA FOI SELECIONADO")
        NOT.show()


"""EDITAR MAQUINA """
def Button_edmaq():
    linha = PES.gridMaquina.currentItem()
    if linha:
        linha = PES.gridMaquina.currentItem().row()
        patri = PES.gridMaquina.item(linha, 0).text()

        comando_SQL = "SELECT * FROM maquina WHERE patrimonio =  '" + str(patri) + "'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()

        descricao = str(dados_lidos[0][1])
        situacao = str(dados_lidos[0][2])
        marca = str(dados_lidos[0][3])
        numero_de_serie = str(dados_lidos[0][4])
        voltagem = str(dados_lidos[0][5])
        tipo = str(dados_lidos[0][6])
        historico = str(dados_lidos[0][7])



        EDITAR_MAQ.textEdit_descri.setText(descricao)
        EDITAR_MAQ.lineEdit_marca.setText(marca)
        EDITAR_MAQ.lineEdit_num.setText(numero_de_serie)
        EDITAR_MAQ.lineEdit_volt.setText(voltagem)
        EDITAR_MAQ.lineEdit_tipo.setText(tipo)
        EDITAR_MAQ.label_9.setText(patri)
        EDITAR_MAQ.textEdit.setText(historico)

        def editar():
            descricao = EDITAR_MAQ.textEdit_descri.toPlainText() 
            marca = EDITAR_MAQ.lineEdit_marca.text()
            numero_de_serie = EDITAR_MAQ.lineEdit_num.text()
            voltagem = EDITAR_MAQ.lineEdit_volt.text()
            tipo = EDITAR_MAQ.lineEdit_tipo.text()
            historico = EDITAR_MAQ.textEdit.toPlainText()
            if EDITAR_MAQ.radioButton.isChecked() :
                situacao = "DISPONIVEL"
            elif EDITAR_MAQ.radioButton_2.isChecked() :
                situacao = "MANUTENCAO"
            else:
                situacao = "REVISAO"
            comando_SQL = "UPDATE maquina SET descricao = '"+str(descricao)+"', situacao = '"+str(situacao)+"', marca = '"+str(marca)+"', numero_de_serie = '"+str(numero_de_serie)+"', voltagem = '"+str(voltagem)+"', tipo = '"+str(tipo)+"', historico = '"+str(historico)+"' WHERE patrimonio = '" + str(patri) + "'"
            cursor.execute(comando_SQL)
            banco.commit()

            comando_SQL = "SELECT * FROM maquina"
            cursor.execute(comando_SQL)
            dados_lidos = cursor.fetchall()
            PES.gridMaquina.setRowCount(len(dados_lidos))

            for i in range(0, len(dados_lidos)):
                for j in range(0, 7):
                    PES.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            
            EDITAR_MAQ.hide()
            NOT.label.setText("ITEM EDITADO")
            NOT.show()




        EDITAR_MAQ.pushButton_salvar.clicked.connect(editar)
        EDITAR_MAQ.show()
        if str(situacao) == "ALUGADO":
            EDITAR_MAQ.hide()
            NOT.label.setText("ESSE ITEM ESTA COMODATADO")
            NOT.show()

    else :
        NOT.label.setText("NADA FOI SELECIONADO")
        NOT.show()



app=QtWidgets.QApplication([])
PES=uic.loadUi("interface/PESQUISA.ui")
VISU_CLI=uic.loadUi("interface/VISUALIZAR_CLIENTE.ui")
VISU_COMO=uic.loadUi("interface/VISUALIZA_MAQUINA.ui")
EXCLUI_CLI=uic.loadUi("interface/EXCLUIR_CLIENTE.ui")
EXCLUI_MAQ=uic.loadUi("interface/EXCLUIR_MAQUINA.ui")
EDITAR_CLI=uic.loadUi("interface/EDITAR_CLIENTE.ui")
EDITAR_MAQ=uic.loadUi("interface/EDITAR_MAQUINA.ui")
NOT=uic.loadUi("interface/NOTIF.ui")




PES.btnPesquisar_cliente.clicked.connect(Button_Pc)
PES.btnPesquisar_maquina.clicked.connect(Button_Pm)
PES.pushButton_vizualizar_cli.clicked.connect(Button_vcli)
PES.pushButton_vizualizar_maquina.clicked.connect(Button_vmaq)
PES.pushButton_excluir_cliente.clicked.connect(Button_excli)
PES.pushButton_excluir_maquina.clicked.connect(Button_exmaq)
PES.pushButton_editar_cliente.clicked.connect(Button_edcli)
PES.pushButton_editar_cliente_2.clicked.connect(Button_edmaq)












#CHAMA TELA PESQUISA
#****************************************************************************************************#
def Button_PC():
    #listando dados da tabela cliente
    comando_SQL = "SELECT * FROM cliente"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    PES.gridCliente.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            PES.gridCliente.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    #listando dados da tabela cliente
    comando_SQL = "SELECT * FROM maquina"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    PES.gridMaquina.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 7):
            PES.gridMaquina.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



    PES.show()