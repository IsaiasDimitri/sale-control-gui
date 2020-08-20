from PySide2.QtWidgets import QDialog, QTableWidgetItem
from .estoque import Ui_Dialog
from models.produto import Produto
from database.db_mongo import DBMongo as DB

class Estoque(QDialog):
    def __init__(self):
        super(Estoque, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        ui = self.ui

        # Set initial state
        produtos = DB().select_all(Produto._TABLE)
        print(produtos)
        ui.tableWidget.setColumnCount(len(Produto._COLUMNS_OF_TABLE))
        ui.tableWidget.setRowCount(len(produtos))
        ui.tableWidget.setHorizontalHeaderLabels(Produto._COLUMNS_OF_TABLE)
        self.populate_table(ui, produtos)

        # Combobox Itens
        for i in range(ui.comboBox.count()):
            ui.comboBox.removeItem(i)
        ui.comboBox.addItems(["kadeshe", "makita", "Bosch"])

        # Buttons
        ui.pushButton.clicked.connect(lambda: self.search())
        ui.pushButton_2.clicked.connect(lambda: self.export_pdf())

    def populate_table(self, ui, produtos):
        ui.tableWidget.clear()
        for n, key in enumerate(Produto._COLUMNS_OF_TABLE):
            for m, item in enumerate(produtos):
                value = str(item.get(key, '--'))
                newitem = QTableWidgetItem(value)
                ui.tableWidget.setItem(m, n, newitem)

    def search(self):
        search_text = self.ui.textEdit.toPlainText()
        if len(search_text):
            query = {
                'empresa': self.ui.comboBox.currentText(),
                'nome': { "$regex": f'{search_text}*', "$options" :'i' }
                }
            result = DB().select(Produto._TABLE, query)
            self.populate_table(self.ui, result)

    def export_pdf(self):
        print("Olha aeeee")