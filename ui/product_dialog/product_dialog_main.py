from PySide2.QtWidgets import QDialog
from .product_dialog import Ui_Dialog
from functools import partial

class Podutos(QDialog):
    def __init__(self):
        super(Podutos, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        # Popup Buttons
        pass