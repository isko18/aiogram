import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS  sql(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    username VARCAR(100)
                )                                                  
            """)
            
    def add_user(self, user_id, username):
        with self.connection:
            self.cursor.execute("INSERT INTO sql (user_id, username) VALUES(?, ?)", (user_id, username))
    
    def get_user(self, user_id):
            with self.connection:
                return self.cursor.execute("SELECT * FROM sql WHERE user_id = ?", (user_id,)).fetchone()