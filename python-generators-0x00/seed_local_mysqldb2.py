#!/usr/bin/env python3
"""
This module provides functions to interact with a MySQL database.
"""

import csv
import uuid
import mysql.connector
from mysql.connector import Error


def connect_db():
    """
    Connect to a MySQL database server.

    Returns:
        connection, cursor: MySQLConnection object and cursor if successful, None otherwise
    """
    try:
        connection = mysql.connector.connect()
        return connection
    except Error as e:
        print(f"Error connecting to server: {e}")
        return None


def create_database(connection):
    """
    Create a MySQL database if it does not exist.

    Args:
        connection: MySQLConnection object

    Returns:
        None
    """
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """
    Connect to the ALX_prodev database.

    Returns:
        connection: MySQLConnection object if successful, None otherwise
    """
    try:
        connection = mysql.connector.connect()
        cursor = connection.cursor()
        cursor.execute("USE ALX_prodev")
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

    return connection


def create_table(connection):
    """
    Creates a table, user_table, in the ALX_prodev if it does not exist.

    Args:
        connection: MySQLConnection object

    Returns:
        None
    """
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,   -- UUID stored as CHAR(36)
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10, 2) NOT NULL,    -- Specify precision for DECIMAL
                INDEX (user_id),                -- Index the user_id column
                UNIQUE INDEX (name, email, age) -- Index the combination of name, email, and age to ensure they are unique
            )
        """
        )
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, data):
    """
    Insert data into the user_table from a CSV file.

    Args:
        connection: MySQLConnection object
        data: path to the CSV file containing the user data

    Returns:
        None
    """
    try:
        cursor = connection.cursor()

        # Open the CSV file and read its contents
        with open(data, newline="", encoding="utf-8") as file:
            csvfile = csv.reader(file)
            next(csvfile, None)  # Skip the header row

            for row in csvfile:
                if len(row) != 3:  # Validate row structure
                    print(f"Skipping invalid row: {row}")
                    continue

                user_id = str(uuid.uuid4())
                name, email, age = row

                cursor.execute(
                    """
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE     -- Relies on the UNIQUE INDEX in crete_table() to determine if a row already exists
                    name = VALUES(name), email = VALUES(email), age = VALUES(age)
                    """,
                    (user_id, name, email, age),
                )
        connection.commit()

    except Error as e:
        print(f"Error inserting data: {e}")
