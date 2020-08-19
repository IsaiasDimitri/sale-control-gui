import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui.base_ui.base import Ui_MainWindow 
from ui.page_cadastro_cliente.cadastro_main import PageCadastroCliente
from ui.page_inicio.page_inicio_main import PageInicio
from ui.page_venda.page_venda_main import PageVenda
from functools import partial
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_func()
        self.go_to_page(self.ui.page_inicio)
    
    def setup_func(self):
        # Setting Pages
        self.ui.page_cadastro = PageCadastroCliente()
        self.ui.stackedWidget.addWidget(self.ui.page_cadastro)
        self.ui.page_inicio = PageInicio()
        self.ui.stackedWidget.addWidget(self.ui.page_inicio)
        self.ui.page_venda = PageVenda()
        self.ui.stackedWidget.addWidget(self.ui.page_venda)
        
        # Navigation Buttons
        self.ui.pushButton.clicked.connect(partial(self.go_to_page, self.ui.page_inicio))
        self.ui.pushButton_nova_venda.clicked.connect(partial(self.go_to_page, self.ui.page_venda))
        self.ui.pushButton_cadastrar_cliente.clicked.connect(partial(self.go_to_page, self.ui.page_cadastro))

    def go_to_page(self, page_widget):
        print(repr(page_widget))
        self.ui.stackedWidget.setCurrentWidget(page_widget)