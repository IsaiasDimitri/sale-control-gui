# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_dialog.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Estoque")
        Dialog.resize(977, 603)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 15, 15, 0)
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.frame_5, 2, 1, 1, 1, Qt.AlignRight)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 2, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 40))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setInputMethodHints(Qt.ImhNone)
        self.textEdit_2.setFrameShape(QFrame.StyledPanel)
        self.textEdit_2.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.textEdit_2, 4, 1, 1, 2)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.spinBox = QSpinBox(self.frame_6)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 40))
        self.spinBox.setMaximumSize(QSize(60, 40))
        self.spinBox.setFont(font)

        self.horizontalLayout_3.addWidget(self.spinBox)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5, 0, Qt.AlignLeft)


        self.gridLayout_2.addWidget(self.frame_6, 5, 1, 2, 1)

        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 40))
        self.textEdit.setMaximumSize(QSize(16777215, 40))
        self.textEdit.setFont(font)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout_2.addWidget(self.textEdit, 2, 1, 1, 2)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 40))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setAcceptDrops(False)
        self.textEdit_3.setInputMethodHints(Qt.ImhNone)
        self.textEdit_3.setFrameShape(QFrame.StyledPanel)
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_3.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.textEdit_3, 8, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.HLine)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_7, 7, 0, 1, 3)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.comboBox.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox, 3, 1, 1, 2)


        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_2, 1, 2, 5, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7, 0, Qt.AlignLeft)

        self.treeWidget = QTreeWidget(self.frame_4)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_3.addWidget(self.treeWidget)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 6, 1)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Limpar Campos", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Confirmar", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Desconto: ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Quantidade: ", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Total: ", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Quantidade de Items", None))
        self.spinBox.setSuffix("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nome ou Codigo do Produto", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Empresa: ", None))
        self.textEdit_3.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Buscar: ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Kadeshe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Bosch", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Makita", None))

        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Informa\u00e7\u00f5es de Estoque</span></p></body></html>", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Dialog", u"Estoque", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Dialog", u"Preco", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"Nome", None));
    # retranslateUi

