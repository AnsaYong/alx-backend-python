#!/usr/bin/env python3
"""
This module provides functions to interact with a MySQL database.
"""
import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator to fetch rows from the user_data table one by one.

    Yields:
        row: A single row of data from the user_data table.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, name, email, age FROM user_data")

        # Fetch the column names from the cursor's description attribute
        column_names = [column[0] for column in cursor.description]

        # Use fetchone to retrieve rows one by one
        while True:
            row = cursor.fetchone()  # Fetch the next row
            if row is None:
                break  # No more rows, break the loop

            # Create a dictionary by zipping column names with the row values
            row_dict = dict(zip(column_names, row))
            yield row_dict

    except Error as e:
        print(f"Database error: {e}")
