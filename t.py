import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import sqlite3

class CalorieTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie & Weight Tracker")
        
        self.weight = tk.DoubleVar()
        self.goal_weight = tk.DoubleVar()
        self.daily_calories = tk.IntVar()
        self.meals = []
        
        self.setup_database()
        
        tk.Label(root, text="Current Weight (kg):").pack()
        tk.Entry(root, textvariable=self.weight).pack()
        
        tk.Label(root, text="Goal Weight (kg):").pack()
        tk.Entry(root, textvariable=self.goal_weight).pack()
        
        tk.Label(root, text="Daily Calorie Intake:").pack()
        tk.Entry(root, textvariable=self.daily_calories).pack()
        
        tk.Button(root, text="Create Meal", command=self.create_meal).pack()
        tk.Button(root, text="Calculate Goal Date", command=self.calculate_goal_date).pack()
        
        self.meal_listbox = tk.Listbox(root)
        self.meal_listbox.pack()
    
    def setup_database(self):
        self.conn = sqlite3.connect("food_database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS foods (
                                id INTEGER PRIMARY KEY, 
                                name TEXT, 
                                calories INTEGER)''')
        self.conn.commit()
    
    def create_meal(self):
        meal_name = simpledialog.askstring("Create Meal", "Enter meal name:")
        if meal_name:
            ingredients = []
            total_calories = 0
            while True:
                ingredient = simpledialog.askstring("Add Ingredient", "Enter ingredient name (or 'done' to finish):")
                if ingredient == "done":
                    break
                self.cursor.execute("SELECT calories FROM foods WHERE name = ?", (ingredient,))
                result = self.cursor.fetchone()
                if result:
                    calories = result[0]
                    ingredients.append((ingredient, calories))
                    total_calories += calories
                else:
                    messagebox.showerror("Error", f"Ingredient '{ingredient}' not found in database!")
                    continue
            
            meal_entry = f"{meal_name} - {total_calories} kcal ({', '.join(i[0] for i in ingredients)})"
            self.meals.append(meal_entry)
            self.meal_listbox.insert(tk.END, meal_entry)
    
    def calculate_goal_date(self):
        try:
            current_weight = self.weight.get()
            goal_weight = self.goal_weight.get()
            daily_calories = self.daily_calories.get()
            deficit_per_day = 500  # Approximation (adjustable based on activity)
            weight_loss_needed = current_weight - goal_weight
            
            if weight_loss_needed <= 0:
                messagebox.showinfo("Result", "You've already reached your goal!")
                return
            
            days_needed = (weight_loss_needed * 7700) / deficit_per_day  # 7700 kcal = 1 kg of fat
            goal_date = datetime.date.today() + datetime.timedelta(days=int(days_needed))
            
            messagebox.showinfo("Estimated Goal Date", f"You will reach your goal by: {goal_date}")
        except Exception as e:
            messagebox.showerror("Error", "Please enter valid inputs!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieTrackerApp(root)
    root.mainloop()
