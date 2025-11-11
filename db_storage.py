import sqlite3

class DBStorage:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price TEXT,
            title TEXT,
            description TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save(self, data):
        for entry in data:
            self.conn.execute(
                "INSERT INTO data (name, price, title, description) VALUES (?, ?, ?, ?)",
                (
                    entry.get("name"),
                    entry.get("price"),
                    entry.get("title"),
                    entry.get("description")
                )
            )
        self.conn.commit()
