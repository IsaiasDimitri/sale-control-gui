from PySide2.QtWidgets import QWidget
from .page_venda import Ui_page_venda
from ..product_dialog.product_dialog_main import Podutos
#from functools import partial

class PageVenda(QWidget):
    def __init__(self):
        super(PageVenda, self).__init__()
        self.ui = Ui_page_venda()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        # Popup Buttons
        self.ui.pushButton_add_produto_table_3.clicked.connect(self.selec_produtos)

    def selec_produtos(self):
        self.produtos = Podutos()
        self.produtos.show()