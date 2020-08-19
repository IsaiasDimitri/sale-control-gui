# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1126, 757)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(180, 0))
        self.frame_menu.setMaximumSize(QSize(180, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_items = QFrame(self.frame_menu)
        self.frame_menu_items.setObjectName(u"frame_menu_items")
        self.frame_menu_items.setFrameShape(QFrame.NoFrame)
        self.frame_menu_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu_items)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.frame_menu_items)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(170, 50))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.frame_16 = QFrame(self.frame_menu_items)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.HLine)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_16)

        self.pushButton_nova_venda = QPushButton(self.frame_menu_items)
        self.pushButton_nova_venda.setObjectName(u"pushButton_nova_venda")
        self.pushButton_nova_venda.setMinimumSize(QSize(0, 50))
        self.pushButton_nova_venda.setMaximumSize(QSize(170, 50))
        self.pushButton_nova_venda.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        self.pushButton_nova_venda.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushButton_nova_venda)

        self.pushButton_cadastrar_cliente = QPushButton(self.frame_menu_items)
        self.pushButton_cadastrar_cliente.setObjectName(u"pushButton_cadastrar_cliente")
        self.pushButton_cadastrar_cliente.setMinimumSize(QSize(0, 50))
        self.pushButton_cadastrar_cliente.setMaximumSize(QSize(170, 50))

        self.verticalLayout_3.addWidget(self.pushButton_cadastrar_cliente)

        self.pushButton_cadastrar_produtos = QPushButton(self.frame_menu_items)
        self.pushButton_cadastrar_produtos.setObjectName(u"pushButton_cadastrar_produtos")
        self.pushButton_cadastrar_produtos.setMinimumSize(QSize(0, 50))
        self.pushButton_cadastrar_produtos.setMaximumSize(QSize(170, 50))

        self.verticalLayout_3.addWidget(self.pushButton_cadastrar_produtos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_menu_items)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: rgb(186, 189, 182);")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFocusPolicy(Qt.WheelFocus)
        self.stackedWidget.setInputMethodHints(Qt.ImhNone)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Alpha Representa\u00e7\u00f5es", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.pushButton_nova_venda.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Venda", None))
        self.pushButton_cadastrar_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.pushButton_cadastrar_produtos.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produtos", None))
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

