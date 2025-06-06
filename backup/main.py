from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QCheckBox, QDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from sys import exit
import sqlite3

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)

        self.user_id = None  # Store logged-in user ID
        
        # Create widgets
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter Email")
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login", self)
        self.cancel_btn = QPushButton("Cancel", self)

        # Layout for login window
        layout = QVBoxLayout(self)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.cancel_btn)

        # Connect buttons
        self.login_btn.clicked.connect(self.handle_login)
        self.cancel_btn.clicked.connect(self.reject)

    def handle_login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        user_data = self.get_user(email)

        if user_data:
            user_id, stored_password = user_data
            if password == stored_password:
                self.user_id = user_id  # Save user ID for later use
                QMessageBox.information(self, "Login Success", "You are now logged in!")
                self.accept()
            else:
                QMessageBox.warning(self, "Login Failed", "Incorrect password.")
        else:
            # Create a new account
            new_user_id = self.create_account(email, password)
            if new_user_id:
                self.user_id = new_user_id  # Save new user ID
                QMessageBox.information(self, "Account Created", "Your account has been created. You are now logged in!")
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Failed to create account.")

    def get_user(self, email):
        """Retrieve user ID and password from database if email exists."""
        conn = sqlite3.connect("users.db")  # Replace with your database file
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, password FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        
        conn.close()
        return user  # Returns (id, password) if user exists, otherwise None

    def create_account(self, email, password):
        """Create a new user account and return the new user ID."""
        conn = sqlite3.connect("users.db")  # Replace with your database file
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            user_id = cursor.lastrowid  # Get the newly created user ID
        except sqlite3.Error:
            user_id = None  # If an error occurs, return None
        
        conn.close()
        return user_id  # Return new user ID if successful, None otherwise

# Main class
class PAPA(QWidget):
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

        # Add Login Button to layout
       

        self.apply_styles()
        self.load_table()

    #Events
    def button_click(self):
        self.add_btn.clicked.connect(self.add_workout)
        self.delete_btn.clicked.connect(self.delete_workout)
        self.submit_btn.clicked.connect(self.calculate_calories)
        self.dark_mode.stateChanged.connect(self.toggle_dark_mode)
        self.clear_btn.clicked.connect(self.reset)
        self.login_btn.clicked.connect(self.show_login_dialog)

    #Show Login Dialog

    def show_login_dialog(self):
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QDialog.Accepted:
            print("Login Successful!")  # You can handle login success logic here
        else:
            print("Login Cancelled!")

    #Load Tables
    def load_table(self):
        self.table.setRowCount(0)
        query = QSqlQuery("SELECT * FROM fitness ORDER BY date DESC")
        row = 0
        while query.next():
            fit_id = query.value(0)
            date = query.value(1)
            calories = query.value(2)
            distance = query.value(3)
            description =   query.value(4)

            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(fit_id)))
            self.table.setItem(row, 1, QTableWidgetItem(date))
            self.table.setItem(row, 2, QTableWidgetItem(str(calories)))
            self.table.setItem(row, 3, QTableWidgetItem(str(distance)))
            self.table.setItem(row, 4, QTableWidgetItem(description))
            row += 1

    #Add Tables
    def add_workout(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        calories = self.kal_box.text()
        distance = self.distance_box.text()
        description = self.description.text()

        query =QSqlQuery("""
                INSERT INTO fitness (date, calories, distance, description )
                         VALUES (?,?,?,?)
                        """)
        query.addBindValue(date)
        query.addBindValue(calories)
        query.addBindValue(distance)
        query.addBindValue(description)
        query.exec_()

        self.date_box.setDate(QDate.currentDate())
        self.kal_box.clear()
        self.distance_box.clear()
        self.description.clear()

        self.load_table()

    #Delete Tables
    def delete_workout(self):
        selected_row =  self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "ERROR","Please choose a row to delete")

        fit_id = int(self.table.item(selected_row,0).text())
        confirm = QMessageBox.question(self, "Are you sure?", "Doelete this workout", QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.No:
            return
        
        query = QSqlQuery()
        query.prepare("DELETE FROM fitness WHERE id = ?")
        query.addBindValue(fit_id)
        query.exec_()

        self.load_table()

    #Calculate Calories
    def calculate_calories(self):
        distances = []
        calories = []

        query = QSqlQuery("SELECT distance, calories FROM fitness ORDER BY calories ASC")
        while query.next():
            distance = query.value(0)
            calorie = query.value(1)
            distances.append(distance)
            calories.append(calorie)

        try:
            if not calories:  # Check if there's no data
                raise ValueError("No data available")

            min_calorie = min(calories)
            max_calories = max(calories)
            normalized_calories = [(calorie - min_calorie) / (max_calories - min_calorie) for calorie in calories]

            # **Clear the figure before drawing a new one**
            self.figure.clear()  
            ax = self.figure.subplots()

            # Sorting data to maintain line order
            sorted_indices = np.argsort(distances)
            sorted_distances = np.array(distances)[sorted_indices]
            sorted_calories = np.array(calories)[sorted_indices]

            # Scatter plot
            scatter = ax.scatter(sorted_distances, sorted_calories, c=normalized_calories, cmap="viridis", label="Data Points")

            # Line plot
            ax.plot(sorted_distances, sorted_calories, linestyle='-', color='blue', alpha=0.7, label="Trend Line")

            ax.set_title("Distance vs Calories")
            ax.set_xlabel("Distance")
            ax.set_ylabel("Calories")

            # **Create new colorbar for each update**
            cbar = self.figure.colorbar(scatter, ax=ax, label="Normalized Calories")

            ax.legend()

            # **Reanvas**
            self.canvas.draw()

        except Exception as e:
            print(f"ERROR: {e}")
            QMessageBox.warning(self, "ERROR", "Please input some data")



    #Set background colors
    def apply_styles(self):
        # Set background colors
        self.setStyleSheet("""
            QWidget {
                background-color: #b8c9e1;
            }
            
            QLabel {
                color: #333;
                font-size: 14px;
            }
            
            QLineEdit, QComboBox, QDateEdit, QPushButton {
                background-color: #b8c9e1;
                color: #333;
                border: 1px solid #444;
                padding: 5px;
            }
            
            QTableWidget {
                background-color: #b8c9e1;
                color: #333;
                border: 1px solid #444;
                selection-background-color: #ddd;
            }
            
            QPushButton {
                background-color: #4caf50;
                color: #fff;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
            }
            
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        figure_color = "#b8c9e1"
        self.figure.patch.set_facecolor(figure_color)
        self.canvas.setStyleSheet(f"background-color: {figure_color};")

        if self.dark_mode.isChecked():
            self.setStyleSheet(
                """
                FitnessApp {
                    background-color: #222222;
                }

                QLineEdit, QPushButton, QDateEdit {
                    background-color:#222222;
                    color: #eeeeee;
                    border: 1px solid #444;
                    padding: 5px;
                }
                QLabel{
                     background-color:#222222;
                    color: #eeeeee;
                    padding: 5px;
                }

                QTableWidget {
                    background-color: #444444;
                    color: #eeeeee;
                }
                
                QCheckBox{
                    color: #eeeeee;
                }
                QPushButton {
                background-color: #40484c;
                color: #fff;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
            }
            
                QPushButton:hover {
                    background-color: #444d4f;
                }
                """
            )
            figure_color = "#40484c"
            self.figure.patch.set_facecolor(figure_color)
            self.canvas.setStyleSheet(f"background-color: {figure_color};")

    #Dark mode        
    def toggle_dark_mode(self):
        self.apply_styles()

    #Reset
    def reset(self):
        self.date_box.setDate(QDate.currentDate())
        self.kal_box.clear()
        self.distance_box.clear()
        self.description.clear()
        self.figure.clear()
        self.canvas.draw()

        self.load_table()
   # def delete_workouts(
#Initialize my DB
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("fitness.db")

if not db.open():
    QMessageBox.critical(None, "ERROR", "Can not open database")
    exit(2)

query = QSqlQuery()
query.exec_("""
        CREATE TABLE IF NOT EXISTS fitness(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           date TEXT,
           calories REAL,
           distance REAL,
           descriptio TEXT,
           FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT)
""")


# Run the application
if __name__ == "__main__":
    app = QApplication([])
    main = PAPA()  
    main.show()
    print("App is running...")
    app.exec_()