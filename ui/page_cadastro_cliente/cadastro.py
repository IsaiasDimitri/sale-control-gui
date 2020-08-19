# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_cadastro_cliente.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_page_cadastro_cliente_1(object):
    def setupUi(self, page_cadastro_cliente_1):
        if not page_cadastro_cliente_1.objectName():
            page_cadastro_cliente_1.setObjectName(u"page_cadastro_cliente_1")
        page_cadastro_cliente_1.resize(934, 658)
        self.gridLayout = QGridLayout(page_cadastro_cliente_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_cliente_contato_form = QFrame(page_cadastro_cliente_1)
        self.frame_cliente_contato_form.setObjectName(u"frame_cliente_contato_form")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_cliente_contato_form.sizePolicy().hasHeightForWidth())
        self.frame_cliente_contato_form.setSizePolicy(sizePolicy)
        self.frame_cliente_contato_form.setFrameShape(QFrame.NoFrame)
        self.frame_cliente_contato_form.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_cliente_contato_form)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_14 = QLabel(self.frame_cliente_contato_form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)

        self.gridLayout_9.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_15 = QLabel(self.frame_cliente_contato_form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_9.addWidget(self.label_15, 6, 0, 1, 1)

        self.label_16 = QLabel(self.frame_cliente_contato_form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_9.addWidget(self.label_16, 7, 0, 1, 1)

        self.textEdit_bairro_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_bairro_2.setObjectName(u"textEdit_bairro_2")
        self.textEdit_bairro_2.setMaximumSize(QSize(300, 30))
        self.textEdit_bairro_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_bairro_2, 6, 1, 1, 1)

        self.label_17 = QLabel(self.frame_cliente_contato_form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(200, 16777215))
        self.label_17.setFont(font)

        self.gridLayout_9.addWidget(self.label_17, 3, 0, 1, 1)

        self.textEdit_email_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_email_2.setObjectName(u"textEdit_email_2")
        self.textEdit_email_2.setMaximumSize(QSize(300, 30))
        self.textEdit_email_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_email_2, 1, 1, 1, 1)

        self.textEdit_complemento_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_complemento_2.setObjectName(u"textEdit_complemento_2")
        self.textEdit_complemento_2.setMaximumSize(QSize(300, 30))
        self.textEdit_complemento_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_complemento_2, 8, 1, 1, 1)

        self.textEdit_cep_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_cep_2.setObjectName(u"textEdit_cep_2")
        self.textEdit_cep_2.setMaximumSize(QSize(300, 30))
        self.textEdit_cep_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_cep_2, 4, 1, 1, 1)

        self.textEdit_cidade_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_cidade_2.setObjectName(u"textEdit_cidade_2")
        self.textEdit_cidade_2.setMaximumSize(QSize(300, 30))
        self.textEdit_cidade_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_cidade_2, 7, 1, 1, 1)

        self.textEdit_telefone_alt_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_telefone_alt_2.setObjectName(u"textEdit_telefone_alt_2")
        self.textEdit_telefone_alt_2.setMaximumSize(QSize(300, 30))
        self.textEdit_telefone_alt_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_telefone_alt_2, 3, 1, 1, 1)

        self.label_18 = QLabel(self.frame_cliente_contato_form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_9.addWidget(self.label_18, 8, 0, 1, 1)

        self.label_19 = QLabel(self.frame_cliente_contato_form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(200, 16777215))
        self.label_19.setFont(font)

        self.gridLayout_9.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_cliente_contato_form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_9.addWidget(self.label_20, 4, 0, 1, 1)

        self.textEdit_rua_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_rua_2.setObjectName(u"textEdit_rua_2")
        self.textEdit_rua_2.setMaximumSize(QSize(300, 30))
        self.textEdit_rua_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_rua_2, 5, 1, 1, 1)

        self.textEdit_telefone_2 = QTextEdit(self.frame_cliente_contato_form)
        self.textEdit_telefone_2.setObjectName(u"textEdit_telefone_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_telefone_2.sizePolicy().hasHeightForWidth())
        self.textEdit_telefone_2.setSizePolicy(sizePolicy1)
        self.textEdit_telefone_2.setMaximumSize(QSize(300, 30))
        self.textEdit_telefone_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.textEdit_telefone_2, 2, 1, 1, 1)

        self.label_21 = QLabel(self.frame_cliente_contato_form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_9.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_22 = QLabel(self.frame_cliente_contato_form)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_cliente_contato_form, 2, 1, 1, 1, Qt.AlignTop)

        self.frame_cliente_dados_gerais_form = QFrame(page_cadastro_cliente_1)
        self.frame_cliente_dados_gerais_form.setObjectName(u"frame_cliente_dados_gerais_form")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_cliente_dados_gerais_form.sizePolicy().hasHeightForWidth())
        self.frame_cliente_dados_gerais_form.setSizePolicy(sizePolicy2)
        self.frame_cliente_dados_gerais_form.setFrameShape(QFrame.NoFrame)
        self.frame_cliente_dados_gerais_form.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_cliente_dados_gerais_form)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(30)
        self.label_cliente_3 = QLabel(self.frame_cliente_dados_gerais_form)
        self.label_cliente_3.setObjectName(u"label_cliente_3")
        self.label_cliente_3.setMaximumSize(QSize(200, 16777215))
        self.label_cliente_3.setFont(font)

        self.gridLayout_10.addWidget(self.label_cliente_3, 3, 0, 1, 1)

        self.label_23 = QLabel(self.frame_cliente_dados_gerais_form)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_10.addWidget(self.label_23, 0, 0, 1, 1)

        self.textEdit_cpf_3 = QTextEdit(self.frame_cliente_dados_gerais_form)
        self.textEdit_cpf_3.setObjectName(u"textEdit_cpf_3")
        sizePolicy1.setHeightForWidth(self.textEdit_cpf_3.sizePolicy().hasHeightForWidth())
        self.textEdit_cpf_3.setSizePolicy(sizePolicy1)
        self.textEdit_cpf_3.setMaximumSize(QSize(300, 30))
        self.textEdit_cpf_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.textEdit_cpf_3, 6, 1, 1, 1)

        self.label_cpf_cnpj_3 = QLabel(self.frame_cliente_dados_gerais_form)
        self.label_cpf_cnpj_3.setObjectName(u"label_cpf_cnpj_3")
        self.label_cpf_cnpj_3.setMaximumSize(QSize(200, 16777215))
        self.label_cpf_cnpj_3.setFont(font)

        self.gridLayout_10.addWidget(self.label_cpf_cnpj_3, 6, 0, 1, 1)

        self.frame_tipo_pessoa_2 = QFrame(self.frame_cliente_dados_gerais_form)
        self.frame_tipo_pessoa_2.setObjectName(u"frame_tipo_pessoa_2")
        self.frame_tipo_pessoa_2.setFrameShape(QFrame.NoFrame)
        self.frame_tipo_pessoa_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tipo_pessoa_2)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 10)
        self.radioButton_pf_3 = QRadioButton(self.frame_tipo_pessoa_2)
        self.radioButton_pf_3.setObjectName(u"radioButton_pf_3")
        self.radioButton_pf_3.setChecked(True)

        self.horizontalLayout_12.addWidget(self.radioButton_pf_3)

        self.radioButton_pj_3 = QRadioButton(self.frame_tipo_pessoa_2)
        self.radioButton_pj_3.setObjectName(u"radioButton_pj_3")

        self.horizontalLayout_12.addWidget(self.radioButton_pj_3)

        self.radioButton_outro_3 = QRadioButton(self.frame_tipo_pessoa_2)
        self.radioButton_outro_3.setObjectName(u"radioButton_outro_3")

        self.horizontalLayout_12.addWidget(self.radioButton_outro_3)


        self.gridLayout_10.addWidget(self.frame_tipo_pessoa_2, 1, 0, 1, 3, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_selecionar_data_entrega_3 = QPushButton(self.frame_cliente_dados_gerais_form)
        self.pushButton_selecionar_data_entrega_3.setObjectName(u"pushButton_selecionar_data_entrega_3")
        self.pushButton_selecionar_data_entrega_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_10.addWidget(self.pushButton_selecionar_data_entrega_3, 8, 1, 1, 1)

        self.textEdit_cliente_3 = QTextEdit(self.frame_cliente_dados_gerais_form)
        self.textEdit_cliente_3.setObjectName(u"textEdit_cliente_3")
        self.textEdit_cliente_3.setMaximumSize(QSize(300, 30))
        self.textEdit_cliente_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.textEdit_cliente_3, 3, 1, 1, 1)

        self.label_selecionar_data_entrega_3 = QLabel(self.frame_cliente_dados_gerais_form)
        self.label_selecionar_data_entrega_3.setObjectName(u"label_selecionar_data_entrega_3")
        self.label_selecionar_data_entrega_3.setFont(font)

        self.gridLayout_10.addWidget(self.label_selecionar_data_entrega_3, 8, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_cliente_dados_gerais_form, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_13 = QFrame(page_cadastro_cliente_1)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy3)
        self.frame_13.setStyleSheet(u"background-color: rgb(85, 87, 83);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_13, 3, 0, 1, 2)

        self.frame_titulo = QFrame(page_cadastro_cliente_1)
        self.frame_titulo.setObjectName(u"frame_titulo")
        sizePolicy3.setHeightForWidth(self.frame_titulo.sizePolicy().hasHeightForWidth())
        self.frame_titulo.setSizePolicy(sizePolicy3)
        self.frame_titulo.setFrameShape(QFrame.NoFrame)
        self.frame_titulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_titulo)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_titulo_pagina_4 = QLabel(self.frame_titulo)
        self.label_titulo_pagina_4.setObjectName(u"label_titulo_pagina_4")
        self.label_titulo_pagina_4.setMaximumSize(QSize(500, 50))
        self.label_titulo_pagina_4.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_11.addWidget(self.label_titulo_pagina_4)


        self.gridLayout.addWidget(self.frame_titulo, 0, 0, 2, 1, Qt.AlignLeft|Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(638, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.frame_button_actions_cadastro_2 = QFrame(page_cadastro_cliente_1)
        self.frame_button_actions_cadastro_2.setObjectName(u"frame_button_actions_cadastro_2")
        self.frame_button_actions_cadastro_2.setFrameShape(QFrame.NoFrame)
        self.frame_button_actions_cadastro_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_button_actions_cadastro_2)
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_cancelar_2 = QPushButton(self.frame_button_actions_cadastro_2)
        self.pushButton_cancelar_2.setObjectName(u"pushButton_cancelar_2")
        self.pushButton_cancelar_2.setMinimumSize(QSize(0, 30))
        self.pushButton_cancelar_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_13.addWidget(self.pushButton_cancelar_2)

        self.pushButton_cadastrar_2 = QPushButton(self.frame_button_actions_cadastro_2)
        self.pushButton_cadastrar_2.setObjectName(u"pushButton_cadastrar_2")
        self.pushButton_cadastrar_2.setMinimumSize(QSize(0, 30))
        self.pushButton_cadastrar_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_13.addWidget(self.pushButton_cadastrar_2)


        self.gridLayout.addWidget(self.frame_button_actions_cadastro_2, 4, 1, 1, 1, Qt.AlignRight|Qt.AlignBottom)


        self.retranslateUi(page_cadastro_cliente_1)

        QMetaObject.connectSlotsByName(page_cadastro_cliente_1)
    # setupUi

    def retranslateUi(self, page_cadastro_cliente_1):
        page_cadastro_cliente_1.setWindowTitle(QCoreApplication.translate("page_cadastro_cliente_1", u"Form", None))
        self.label_14.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Telefone", None))
        self.label_15.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Bairro", None))
        self.label_16.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Cidade", None))
        self.label_17.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Telefone 2", None))
        self.label_18.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Complemento", None))
        self.label_19.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Email", None))
        self.label_20.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"CEP", None))
        self.label_21.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Rua", None))
        self.label_22.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Dados de Contato</span></p></body></html>", None))
        self.label_cliente_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Nome", None))
        self.label_23.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Dados Gerais</span></p></body></html>", None))
        self.label_cpf_cnpj_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"CPF", None))
        self.radioButton_pf_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Pessoa F\u00edsica", None))
        self.radioButton_pj_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Pessoa Jur\u00eddica", None))
        self.radioButton_outro_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Outro", None))
        self.pushButton_selecionar_data_entrega_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Escolher Data", None))
        self.label_selecionar_data_entrega_3.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Data Nascimento", None))
        self.label_titulo_pagina_4.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro de Cliente</span></p></body></html>", None))
        self.pushButton_cancelar_2.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Cancelar", None))
        self.pushButton_cadastrar_2.setText(QCoreApplication.translate("page_cadastro_cliente_1", u"Cadastrar", None))
    # retranslateUi

