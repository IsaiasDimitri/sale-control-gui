#!/bin/bash
cd /home/dimitri/Work/Alpha_Gui/ui
echo -e "Criando arquivos.py..."

pyside2-uic base.ui > base_ui/base.py
pyside2-uic page_vendas.ui > page_venda/page_venda.py
pyside2-uic page_inicio.ui > page_inicio/page_inicio.py
pyside2-uic product_dialog.ui > product_dialog/product_dialog.py
pyside2-uic estoque.ui > estoque/estoque.py

echo -e "Interfaces criadas."