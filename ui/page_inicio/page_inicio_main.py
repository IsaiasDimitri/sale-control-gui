from PySide2.QtWidgets import QWidget
from .page_inicio import Ui_page_inicio 
from ..estoque.estoque_main import Estoque
from functools import partial

class PageInicio(QWidget):
    def __init__(self):
        super(PageInicio, self).__init__()
        self.ui = Ui_page_inicio()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        # Popup Buttons
        self.ui.pushButton_5.clicked.connect(self.show_estoque)
        
    def show_estoque(self):
        self.estoque = Estoque()
        self.estoque.show()