from PySide2.QtWidgets import QWidget
from .cadastro import Ui_page_cadastro_cliente_1 
#from functools import partial

class PageCadastroCliente(QWidget):
    def __init__(self):
        super(PageCadastroCliente, self).__init__()
        self.ui = Ui_page_cadastro_cliente_1()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        # Navigation Buttons
        pass