# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_inicio.ui'
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


class Ui_page_inicio(object):
    def setupUi(self, page_inicio):
        if not page_inicio.objectName():
            page_inicio.setObjectName(u"page_inicio")
        page_inicio.resize(929, 729)
        page_inicio.setStyleSheet(u"background-color: rgb(186, 189, 182);")
        self.gridLayout = QGridLayout(page_inicio)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(page_inicio)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame = QFrame(page_inicio)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_titulo_pagina_2 = QLabel(self.frame)
        self.label_titulo_pagina_2.setObjectName(u"label_titulo_pagina_2")

        self.gridLayout_2.addWidget(self.label_titulo_pagina_2, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QFrame.Panel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.listWidget_lancamentos_agendados = QListWidget(self.frame_9)
        QListWidgetItem(self.listWidget_lancamentos_agendados)
        QListWidgetItem(self.listWidget_lancamentos_agendados)
        QListWidgetItem(self.listWidget_lancamentos_agendados)
        QListWidgetItem(self.listWidget_lancamentos_agendados)
        self.listWidget_lancamentos_agendados.setObjectName(u"listWidget_lancamentos_agendados")
        self.listWidget_lancamentos_agendados.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.listWidget_lancamentos_agendados, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_9, 1, 0, 1, 1)

        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.Panel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.listWidget_3 = QListWidget(self.frame_17)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_8.addWidget(self.listWidget_3)


        self.gridLayout_2.addWidget(self.frame_17, 2, 0, 1, 1)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_5 = QPushButton(self.frame_10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(150, 50))
        self.pushButton_5.setMaximumSize(QSize(170, 50))

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 50))
        self.pushButton_2.setMaximumSize(QSize(170, 50))

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.gridLayout_2.addWidget(self.frame_10, 0, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setFrameShape(QFrame.Panel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.listWidget_2 = QListWidget(self.frame_14)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_7.addWidget(self.listWidget_2)


        self.gridLayout_2.addWidget(self.frame_14, 1, 1, 2, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignTop)


        self.retranslateUi(page_inicio)

        QMetaObject.connectSlotsByName(page_inicio)
    # setupUi

    def retranslateUi(self, page_inicio):
        page_inicio.setWindowTitle(QCoreApplication.translate("page_inicio", u"Form", None))
        self.label_titulo_pagina_2.setText(QCoreApplication.translate("page_inicio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">In\u00edcio</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("page_inicio", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Entregas Agendadas</span></p></body></html>", None))

        __sortingEnabled = self.listWidget_lancamentos_agendados.isSortingEnabled()
        self.listWidget_lancamentos_agendados.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_lancamentos_agendados.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("page_inicio", u"Carlos - 8305,48 - 27/02/2021", None));
        ___qlistwidgetitem1 = self.listWidget_lancamentos_agendados.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("page_inicio", u"Carlos - 8305,48 - 27/02/2021", None));
        ___qlistwidgetitem2 = self.listWidget_lancamentos_agendados.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("page_inicio", u"Carlos - 8305,48 - 27/02/2021", None));
        ___qlistwidgetitem3 = self.listWidget_lancamentos_agendados.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("page_inicio", u"Carlos - 8305,48 - 27/02/2021", None));
        self.listWidget_lancamentos_agendados.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate("page_inicio", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Or\u00e7amentos Gerados</span></p></body></html>", None))

        __sortingEnabled1 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.listWidget_3.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("page_inicio", u"Luiz Renner - 19/08/2020", None));
        ___qlistwidgetitem5 = self.listWidget_3.item(1)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("page_inicio", u"Jaca\u00fana LTDA - 19/08/2020", None));
        ___qlistwidgetitem6 = self.listWidget_3.item(2)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("page_inicio", u"Paulo Almeida - 19/08/2020", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled1)

        self.pushButton_5.setText(QCoreApplication.translate("page_inicio", u"Estoque", None))
        self.pushButton_2.setText(QCoreApplication.translate("page_inicio", u"Atualizar", None))
        self.label_5.setText(QCoreApplication.translate("page_inicio", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Hist\u00f3rico de Vendas</span></p></body></html>", None))

        __sortingEnabled2 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.listWidget_2.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("page_inicio", u"Vendedor: #001 - Cliente: Paulo Almeida - Data: 19/02/2020 - CONFIRMADO", None));
        ___qlistwidgetitem8 = self.listWidget_2.item(1)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("page_inicio", u"Vendedor: #003 - Cliente: Jaca\u00fana LTD - Data: 19/02/2020 - CANCELADO", None));
        ___qlistwidgetitem9 = self.listWidget_2.item(2)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("page_inicio", u"Vendedor: #002 - Cliente: Paulo Ara\u00fajo - Data: 19/02/2020 - CONFIRMADO", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled2)

    # retranslateUi

