from PyQt5 import QtWidgets

class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fitness Tracker')
        self.setGeometry(300, 300, 800, 600)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        
        self.label = QtWidgets.QLabel('Welcome to Fitness Tracker')
        self.layout.addWidget(self.label)

        # Adding a button for demonstration
        self.button = QtWidgets.QPushButton('Click Me')
        self.layout.addWidget(self.button)

        self.show()
