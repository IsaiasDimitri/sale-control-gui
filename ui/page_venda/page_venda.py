# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_vendas.ui'
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


class Ui_page_venda(object):
    def setupUi(self, page_venda):
        if not page_venda.objectName():
            page_venda.setObjectName(u"page_venda")
        page_venda.resize(761, 609)
        page_venda.setFocusPolicy(Qt.StrongFocus)
        page_venda.setStyleSheet(u"background-color: rgb(186, 189, 182);")
        self.gridLayout_11 = QGridLayout(page_venda)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_titulo_pagina_4 = QLabel(page_venda)
        self.label_titulo_pagina_4.setObjectName(u"label_titulo_pagina_4")
        self.label_titulo_pagina_4.setMaximumSize(QSize(500, 50))
        self.label_titulo_pagina_4.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_11.addWidget(self.label_titulo_pagina_4, 0, 0, 1, 1, Qt.AlignLeft)

        self.frame_cliente_dados_2 = QFrame(page_venda)
        self.frame_cliente_dados_2.setObjectName(u"frame_cliente_dados_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_cliente_dados_2.sizePolicy().hasHeightForWidth())
        self.frame_cliente_dados_2.setSizePolicy(sizePolicy)
        self.frame_cliente_dados_2.setFrameShape(QFrame.NoFrame)
        self.frame_cliente_dados_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_cliente_dados_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_selecionar_data_entrega_3 = QLabel(self.frame_cliente_dados_2)
        self.label_selecionar_data_entrega_3.setObjectName(u"label_selecionar_data_entrega_3")
        font = QFont()
        font.setPointSize(12)
        self.label_selecionar_data_entrega_3.setFont(font)

        self.gridLayout_9.addWidget(self.label_selecionar_data_entrega_3, 1, 0, 1, 1)

        self.pushButton_selecionar_data_entrega_3 = QPushButton(self.frame_cliente_dados_2)
        self.pushButton_selecionar_data_entrega_3.setObjectName(u"pushButton_selecionar_data_entrega_3")
        self.pushButton_selecionar_data_entrega_3.setMinimumSize(QSize(0, 30))

        self.gridLayout_9.addWidget(self.pushButton_selecionar_data_entrega_3, 1, 1, 1, 1)

        self.pushButton_buscar_cliente_2 = QPushButton(self.frame_cliente_dados_2)
        self.pushButton_buscar_cliente_2.setObjectName(u"pushButton_buscar_cliente_2")
        self.pushButton_buscar_cliente_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_9.addWidget(self.pushButton_buscar_cliente_2, 0, 1, 1, 1)

        self.label_cliente_3 = QLabel(self.frame_cliente_dados_2)
        self.label_cliente_3.setObjectName(u"label_cliente_3")
        self.label_cliente_3.setMaximumSize(QSize(200, 16777215))
        self.label_cliente_3.setFont(font)

        self.gridLayout_9.addWidget(self.label_cliente_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_cliente_dados_2, 1, 0, 1, 1)

        self.frame_6 = QFrame(page_venda)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_tabela_produtos_2 = QTreeWidget(self.frame_6)
        QTreeWidgetItem(self.treeWidget_tabela_produtos_2)
        QTreeWidgetItem(self.treeWidget_tabela_produtos_2)
        self.treeWidget_tabela_produtos_2.setObjectName(u"treeWidget_tabela_produtos_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeWidget_tabela_produtos_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_tabela_produtos_2.setSizePolicy(sizePolicy2)
        self.treeWidget_tabela_produtos_2.setMaximumSize(QSize(16777214, 16777215))
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        self.treeWidget_tabela_produtos_2.setFont(font1)
        self.treeWidget_tabela_produtos_2.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.treeWidget_tabela_produtos_2.setMouseTracking(False)
        self.treeWidget_tabela_produtos_2.setFocusPolicy(Qt.ClickFocus)
        self.treeWidget_tabela_produtos_2.setStyleSheet(u"font: 11pt \"DejaVu Sans\";")
        self.treeWidget_tabela_produtos_2.setFrameShape(QFrame.Box)
        self.treeWidget_tabela_produtos_2.setFrameShadow(QFrame.Plain)
        self.treeWidget_tabela_produtos_2.setLineWidth(0)
        self.treeWidget_tabela_produtos_2.setAutoScrollMargin(16)
        self.treeWidget_tabela_produtos_2.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.treeWidget_tabela_produtos_2.setProperty("showDropIndicator", False)
        self.treeWidget_tabela_produtos_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget_tabela_produtos_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeWidget_tabela_produtos_2.setTextElideMode(Qt.ElideMiddle)
        self.treeWidget_tabela_produtos_2.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeWidget_tabela_produtos_2.setIndentation(1)
        self.treeWidget_tabela_produtos_2.setRootIsDecorated(False)
        self.treeWidget_tabela_produtos_2.setUniformRowHeights(False)
        self.treeWidget_tabela_produtos_2.setSortingEnabled(True)
        self.treeWidget_tabela_produtos_2.setAnimated(True)
        self.treeWidget_tabela_produtos_2.setWordWrap(False)
        self.treeWidget_tabela_produtos_2.setHeaderHidden(False)
        self.treeWidget_tabela_produtos_2.setExpandsOnDoubleClick(True)
        self.treeWidget_tabela_produtos_2.setColumnCount(4)
        self.treeWidget_tabela_produtos_2.header().setCascadingSectionResizes(True)
        self.treeWidget_tabela_produtos_2.header().setDefaultSectionSize(100)
        self.treeWidget_tabela_produtos_2.header().setHighlightSections(True)
        self.treeWidget_tabela_produtos_2.header().setProperty("showSortIndicator", True)
        self.treeWidget_tabela_produtos_2.header().setStretchLastSection(True)

        self.gridLayout_10.addWidget(self.treeWidget_tabela_produtos_2, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_6, 2, 0, 2, 1)

        self.frame_4 = QFrame(page_venda)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_add_produto_table_3 = QPushButton(self.frame_4)
        self.pushButton_add_produto_table_3.setObjectName(u"pushButton_add_produto_table_3")
        self.pushButton_add_produto_table_3.setMinimumSize(QSize(150, 30))
        self.pushButton_add_produto_table_3.setMaximumSize(QSize(150, 30))

        self.verticalLayout_9.addWidget(self.pushButton_add_produto_table_3)

        self.pushButton_limpar_tabela_2 = QPushButton(self.frame_4)
        self.pushButton_limpar_tabela_2.setObjectName(u"pushButton_limpar_tabela_2")
        self.pushButton_limpar_tabela_2.setMinimumSize(QSize(150, 30))
        self.pushButton_limpar_tabela_2.setMaximumSize(QSize(150, 30))

        self.verticalLayout_9.addWidget(self.pushButton_limpar_tabela_2)

        self.pushButton_add_produto_table_4 = QPushButton(self.frame_4)
        self.pushButton_add_produto_table_4.setObjectName(u"pushButton_add_produto_table_4")
        self.pushButton_add_produto_table_4.setMinimumSize(QSize(150, 30))
        self.pushButton_add_produto_table_4.setMaximumSize(QSize(150, 30))

        self.verticalLayout_9.addWidget(self.pushButton_add_produto_table_4)


        self.gridLayout_11.addWidget(self.frame_4, 2, 1, 1, 1)

        self.frame_button_actions_2 = QFrame(page_venda)
        self.frame_button_actions_2.setObjectName(u"frame_button_actions_2")
        self.frame_button_actions_2.setFrameShape(QFrame.NoFrame)
        self.frame_button_actions_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_button_actions_2)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_cancelar_venda_2 = QPushButton(self.frame_button_actions_2)
        self.pushButton_cancelar_venda_2.setObjectName(u"pushButton_cancelar_venda_2")
        self.pushButton_cancelar_venda_2.setMinimumSize(QSize(0, 30))
        self.pushButton_cancelar_venda_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_cancelar_venda_2)

        self.pushButton_gerar_proposta_2 = QPushButton(self.frame_button_actions_2)
        self.pushButton_gerar_proposta_2.setObjectName(u"pushButton_gerar_proposta_2")
        self.pushButton_gerar_proposta_2.setMinimumSize(QSize(0, 30))
        self.pushButton_gerar_proposta_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_gerar_proposta_2)


        self.gridLayout_11.addWidget(self.frame_button_actions_2, 3, 1, 1, 1)


        self.retranslateUi(page_venda)

        QMetaObject.connectSlotsByName(page_venda)
    # setupUi

    def retranslateUi(self, page_venda):
        page_venda.setWindowTitle("")
        self.label_titulo_pagina_4.setText(QCoreApplication.translate("page_venda", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Formul\u00e1rio de Venda</span></p></body></html>", None))
        self.label_selecionar_data_entrega_3.setText(QCoreApplication.translate("page_venda", u"Data Entrega", None))
        self.pushButton_selecionar_data_entrega_3.setText(QCoreApplication.translate("page_venda", u"Escolher Data", None))
        self.pushButton_buscar_cliente_2.setText(QCoreApplication.translate("page_venda", u"Buscar", None))
        self.label_cliente_3.setText(QCoreApplication.translate("page_venda", u"Cliente", None))
        ___qtreewidgetitem = self.treeWidget_tabela_produtos_2.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("page_venda", u"Preco Total", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("page_venda", u"Desconto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("page_venda", u"Quantidade", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("page_venda", u"Produto", None));

        __sortingEnabled = self.treeWidget_tabela_produtos_2.isSortingEnabled()
        self.treeWidget_tabela_produtos_2.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_tabela_produtos_2.topLevelItem(0)
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("page_venda", u"3089,33", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("page_venda", u"8%", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("page_venda", u"33", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("page_venda", u"Capacete", None));
        ___qtreewidgetitem2 = self.treeWidget_tabela_produtos_2.topLevelItem(1)
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("page_venda", u"5034,49", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("page_venda", u"5%", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("page_venda", u"23", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("page_venda", u"Bota", None));
        self.treeWidget_tabela_produtos_2.setSortingEnabled(__sortingEnabled)

        self.pushButton_add_produto_table_3.setText(QCoreApplication.translate("page_venda", u"Adicionar Produto", None))
        self.pushButton_limpar_tabela_2.setText(QCoreApplication.translate("page_venda", u"Limpar Tabela", None))
        self.pushButton_add_produto_table_4.setText(QCoreApplication.translate("page_venda", u"Editar Selecionado", None))
        self.pushButton_cancelar_venda_2.setText(QCoreApplication.translate("page_venda", u"Cancelar", None))
        self.pushButton_gerar_proposta_2.setText(QCoreApplication.translate("page_venda", u"Gerar Proposta", None))
    # retranslateUi

