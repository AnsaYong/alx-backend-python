#!/usr/bin/env python3
"This module provides a custom class based context manager for executing queries"

import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        """
        Initialize the class with the database name, query, and optional parameters.
        """
        self.db_name = db_name
        self.query = query
        self.params = params or []
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Set up the database connection and cursor.
        Execute the query and fetch the results.
        """
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        # Fetch the results immediately so they are available to the caller
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the cursor and the connection, ensuring cleanup.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        # Allow exceptions to propagate
        return exc_type is None


# Example usage
if __name__ == "__main__":
    db_name = "example.db"

    # Create a sample database and table for demonstration
    with sqlite3.connect(db_name) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        )
        conn.executemany(
            "INSERT OR IGNORE INTO users (name, age) VALUES (?, ?)",
            [("Alice", 30), ("Bob", 20), ("Charlie", 35)],
        )

    # Use the ExecuteQuery context manager
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery(db_name, query, params) as results:
        for row in results:
            print(row)
