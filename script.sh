#!/bin/bash
 
echo "Criando arquivos.py..."
pyside2-uic ui/base.ui > ui/base_ui/base.py
pyside2-uic ui/page_vendas.ui > ui/page_venda/page_venda.py
pyside2-uic ui/page_inicio.ui > ui/page_inicio/page_inicio.py
pyside2-uic ui/product_dialog.ui > ui/product_dialog/product_dialog.py
pyside2-uic ui/estoque.ui > ui/estoque/estoque.py
echo "Interfaces criadas."