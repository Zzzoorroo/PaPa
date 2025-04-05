# Fitness Tracker

## Overview
The **Fitness Tracker** is a PyQt5-based desktop application designed to help users track their workouts, burned calories, and distances covered. It also provides graphical analysis of calorie expenditure over distances.

## Features
- **User Interface**: Built with PyQt5, featuring a structured layout for input fields, buttons, and tables.
- **Data Storage**: Uses SQLite for storing workout details.
- **Workout Management**:
  - Add new workout records.
  - Delete existing workout records.
  - View stored data in a table format.
- **Graphical Analysis**:
  - Displays a scatter plot of distance vs. calories burned.
  - Normalizes calorie values for better visualization.
- **Dark Mode**: Toggle between light and dark themes for better user experience.

## Dependencies
Ensure you have the following Python libraries installed before running the application:
```
pip install PyQt5 matplotlib numpy
```

## How to Run
1. Install the required dependencies.
2. Run the script using:
   ```
   python fitness_tracker.py
   ```
3. Use the UI to input workout details and analyze your progress.

## Usage
1. **Input Workout Data**:
   - Select a date.
   - Enter burned calories, distance covered, and a description.
   - Click "Add" to save the entry.
2. **View and Manage Workouts**:
   - Stored data appears in the table.
   - Select a row and click "Delete" to remove an entry.
3. **Analyze Data**:
   - Click "Submit" to generate a scatter plot of distance vs. calories burned.
4. **Toggle Dark Mode**:
   - Use the "Dark mode" checkbox to switch themes.

## Database Structure
The application uses an SQLite database with the following structure:
```
CREATE TABLE fitness (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    calories INTEGER,
    distance REAL,
    description TEXT
);
```

## Troubleshooting
- If the graph does not display, ensure you have entered at least one valid workout entry.
- If buttons do not respond, restart the application.

## Author
Developed by Ilyass Bel-Mehdi.

## License
This project is open-source and licensed under the MIT License.

