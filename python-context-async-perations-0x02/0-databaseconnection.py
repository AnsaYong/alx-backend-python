#!/usr/env/bin python3
"This module provides a custom class based context manager for Database connection"

import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        """Initialize the class with the database name"""
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Called when entering the context with 'with' statement.
        This method establishes the database connection and returns the cursor.
        """
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, traceback):
        """
        Called when exiting the context.
        This method closess the cursor and connection,
        and ensures the connection is properly handled even in case of an error.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        # If an exception occured, let it propagate by returning False
        return exc_type is None


# Usage example
if __name__ == "__main__":
    db_name = "mydatabase.db"

    # Create a sample database and table for demonstration
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"
        )
        cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        cursor.execute("INSERT INTO users (name) VALUES ('Bob')")

    # Use the custom context manager to query the database
    with DatabaseConnection("mydatabase.db") as cursor:
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
