from PyQt5.QtCore import  QDate
from PyQt5.QtWidgets import   QLabel, QDateEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QHeaderView, QCheckBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.button_click()
        self.show()
            
    #Settings 
    def settings(self):
        self.setWindowTitle("Fitness Tracker")
        self.resize(800, 600)
    # Initialize UI
    def initUI(self):
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.kal_box = QLineEdit()
        self.kal_box.setPlaceholderText("Number of Burned Calories")
        self.distance_box = QLineEdit()
        self.distance_box.setPlaceholderText("Enter distance ran")
        self.description = QLineEdit()
        self.description.setPlaceholderText("Enter a description")
        
        self.submit_btn = QPushButton("Submit")
        self.add_btn = QPushButton("Add")
        self.delete_btn = QPushButton("Delete")
        self.clear_btn = QPushButton("Clear")
        self.dark_mode = QCheckBox("Dark mode")
        self.login_btn = QPushButton("Login")  # Defined here before usage

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Date", "Calories", "Distance", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # Layout
        self.master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
        
        self.sub_row1 = QHBoxLayout()
        self.sub_row2 = QHBoxLayout()
        self.sub_row3 = QHBoxLayout()
        self.sub_row4 = QHBoxLayout()

        self.sub_row1.addWidget(QLabel("Date:"))
        self.sub_row1.addWidget(self.date_box)
        self.sub_row2.addWidget(QLabel("Calories:"))
        self.sub_row2.addWidget(self.kal_box)
        self.sub_row3.addWidget(QLabel("KM:"))
        self.sub_row3.addWidget(self.distance_box)
        self.sub_row4.addWidget(QLabel("Description"))
        self.sub_row4.addWidget(self.description)    

        self.col1.addLayout(self.sub_row1)
        self.col1.addLayout(self.sub_row2)
        self.col1.addLayout(self.sub_row3)
        self.col1.addLayout(self.sub_row4)
        self.col1.addWidget(self.dark_mode)
        
        btn_row1 = QHBoxLayout()
        btn_row2 = QHBoxLayout()
        btn_row3 = QHBoxLayout()
        
        btn_row1.addWidget(self.add_btn)
        btn_row1.addWidget(self.delete_btn)
        btn_row2.addWidget(self.submit_btn)
        btn_row2.addWidget(self.clear_btn)
        btn_row3.addWidget(self.login_btn)
       
        self.col1.addLayout(btn_row1)
        self.col1.addLayout(btn_row2)
        self.col1.addLayout(btn_row3)

        self.col2.addWidget(self.canvas)
        self.col2.addWidget(self.table)



        self.master_layout.addLayout(self.col1, 30)
        self.master_layout.addLayout(self.col2, 70)
        self.setLayout(self.master_layout)  

        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
