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
        
    #Load Tables
    
    
    #Add Tables
    
    
    #Delete Tables
    
    
    #Calculate Table
    
    
    #CLick
    
    #Dark Mode
    #Reset
    
#Initialize my DB