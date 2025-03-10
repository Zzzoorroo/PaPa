#Imports
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBOXLayout,QMessageBox, QTableWidget,QTableWidgetItem, QhederView, QCheckBox, QDateEdit , QLineEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from sys import exit


#Main class
class PAPA(QWidget):
    def _init_(self):
        super()._init_()
            
    #init Ui
    def initUI(self):
        self.date_box = QDateEdit()
        self.date_box.setDAte(QDate.currentDate())
        self.kal_box = QLineEdit()
        self.kal_box.setPlaceholderText("Number of Burned Calories")
        self.distance_box = QLineEdit()
        self.distance_box.setPlaceholderText("Enter distance ran")
        self.description = QLineEdit()
        self.description.setPlacehlderText("Enter a description")
        
        self.submit_btn = QPushButton("Submit")
        self.add_btn = QPushButton("Add")
        self.delete_btn = QPushButton("Delete")
        self.clear_btn = QPushButton("Clear")
        self.dark_mode =  QPushButton("Dark mode")
        
        
        self.table -  QTableWidget()

        
        self.figure = plt.figure()
        self.canvas =  FigureCanvas(self.figure)
        
        #Desing Out Layout
        self.master_layout = QHBOXLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
        
        self.sub_row1 = QHBOXLayout()
        self.sub_row2 = QHBOXLayout()
        self.sub_row3 = QHBOXLayout()
        self.sub_row4 = QHBOXLayout()

        self.sub_row1.addWidget(QLabel("Date:"))
        self.sub_row1.addWidget(self.date_box)
        self.sub_row2.addWidget(QLabel("Calories:"))
        self.sub_row2.addWidget(self.kal_box)
        self.sub_row3.addWidget(QLabel("KM:"))
        self.sub_row3.addWidget(self.distance_box)
        self.sub_row4.addWidget(QLabel("Description"))
        self.sub_row4.addWIdget(self.description)    
        
        self.col1.addLayout(self.sub_row1)
        self.col1.addLayout(self.sub_row2)
        self.col1.addLayout(self.sub_row3)
        self.col1.addLayout(self.sub_row4)
        self.col1.addWidget(self.dark_mode)
        
        
        btn_row1 = QHBOXLayout()
        btn_row2 = QHBOXLayout()
        
       
        
    #Load Tables
    
    
    #Add Tables
    
    
    #Delete Tables
    
    
    #Calculate Table
    
    
    #CLick
    
    #Dark Mode
    #Reset
    
#Initialize my DB