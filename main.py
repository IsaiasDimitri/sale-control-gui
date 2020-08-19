import sys
from PySide2.QtWidgets import QApplication
from ui.base_ui.base_main import MainWindow 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())