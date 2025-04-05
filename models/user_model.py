import sqlite3

class UserModel:
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.connection.commit()

    def fetch_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
