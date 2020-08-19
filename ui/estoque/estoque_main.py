from PySide2.QtWidgets import QDialog
from .estoque import Ui_Dialog
#from functools import partial

class Estoque(QDialog):
    def __init__(self):
        super(Estoque, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        # Navigation Buttons
        pass