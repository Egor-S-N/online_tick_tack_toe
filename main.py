from PyQt5.QtWidgets import QApplication
import sys
from app import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
