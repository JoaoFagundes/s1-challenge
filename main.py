import sys
from gui.interface import Interface
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = Interface()
    interface.show()

    sys.exit(app.exec_())
