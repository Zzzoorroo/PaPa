# Imports
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QTableWidget, QDateEdit, QLineEdit
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sys

print("Script started...")

try:
    from PyQt5.QtWidgets import QApplication, QWidget
    print("PyQt5 imported successfully")
except Exception as e:
    print("Error importing PyQt5:", e)
    sys.exit(1)

app = QApplication([])
print("QApplication initialized")
main = QWidget()
main.show()
print("Main window displayed")
app.exec_()
print("App execution ended")

print("Script started...")

# Main class
class PAPA(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
            
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
        self.dark_mode = QPushButton("Dark mode")

        self.table = QTableWidget()
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
        
        btn_row1.addWidget(self.add_btn)
        btn_row1.addWidget(self.delete_btn)
        btn_row2.addWidget(self.submit_btn)
        btn_row2.addWidget(self.clear_btn)
       
        self.col1.addLayout(btn_row1)
        self.col1.addLayout(btn_row2)

        self.master_layout.addLayout(self.col1)
        self.setLayout(self.master_layout)  

    
# Run the application
if __name__ == "__main__":
    app = QApplication([])
    main = PAPA()  
    main.show()
    print("App is running...")
    app.exec_()

