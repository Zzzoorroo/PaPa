from PyQt5 import QtWidgets
from views.main_view import MainView
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainView()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
