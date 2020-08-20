from PySide2.QtWidgets import QWidget
from .cadastro import Ui_page_cadastro_cliente_1 
from functools import partial
from models.cliente import Cliente
import random, datetime

class PageCadastroCliente(QWidget):
    def __init__(self):
        super(PageCadastroCliente, self).__init__()
        self.ui = Ui_page_cadastro_cliente_1()
        self.ui.setupUi(self)
        self.setup_func()
    
    def setup_func(self):
        # Radio Buttons
        self.ui.radioButton_pf_3.toggled.connect(lambda: self.radio_button('pf'))
        self.ui.radioButton_pj_3.toggled.connect(lambda: self.radio_button('pj'))
        self.ui.radioButton_outro_3.toggled.connect(lambda: self.radio_button('other'))

        # Record Button
        self.ui.pushButton_cadastrar.clicked.connect(lambda: self.record_client())

    def radio_button(self, person_type):
        def pf(ui):
            ui.label_cliente_3.setText("Nome: ")
            ui.label_cpf_cnpj_3.setText("CPF: ")
            ui.label_selecionar_data.show()
            ui.pushButton_selecionar_data.show()
        def pj(ui):
            ui.label_cpf_cnpj_3.setText("CNPJ: ")
            ui.label_selecionar_data.hide()
            ui.pushButton_selecionar_data.hide()
        def other(ui):
            ui.label_cpf_cnpj_3.setText("Identificação: ")
            ui.label_selecionar_data.hide()
            ui.pushButton_selecionar_data.hide()
        options = {
            'pf': pf,
            'pj': pj,
            'other': other
        }
        choice = options.get(person_type, lambda: None)
        return choice(self.ui)

    def record_client(self):
        #'codigo': str(random.choice(range(1000))).zfill(5),
        print('Cadastrando..')
        ui = self.ui
        insert_query = {
            'nome': ui.textEdit_cliente.toPlainText() or None,
            'cpf/cnpj': ui.textEdit_cpf_cnpj.toPlainText() or None,
            'email': ui.textEdit_email.toPlainText() or None,
            'telefone': ui.textEdit_telefone.toPlainText() or None,
            'telefone_alt': ui.textEdit_telefone_alt.toPlainText() or None,
            'data_criacao': datetime.datetime.today().strftime("%d/%m/%Y") or None,
            'endereco': {
                'cep': ui.textEdit_cep.toPlainText() or None,
                'rua': ui.textEdit_rua.toPlainText() or None,
                'bairro': ui.textEdit_bairro.toPlainText() or None,
                'cidade': ui.textEdit_cidade.toPlainText() or None,
                'complemento': ui.textEdit_complemento.toPlainText() or None
            }
        }
        cliente = Cliente(**insert_query)
        cliente.save()
        print(cliente._id)