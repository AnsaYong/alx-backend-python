#!/usr/bin/env python3
"""
This module provides functions to interact with a MySQL database.
"""
import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator to fetch rows in batches from the user_data table.

    Args:
        batch_size: The number of rows to fetch per batch.

    Yields:
        list: A list of rows, where each row is a dictionary with column names as keys and values as row data.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, name, email, age FROM user_data")

        # Fetch the column names from the cursor's description attribute
        column_names = [column[0] for column in cursor.description]

        while True:
            # Fetch a batch of rows
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break  # No more rows, stop the loop

            # Yield a batch of rows as dictionaries
            batch = [dict(zip(column_names, row)) for row in rows]
            yield batch

    except Error as e:
        print(f"Database error: {e}")


def batch_processing(batch_size):
    """
    Process each batch fetched by the stream_users_in_batches function to filter users over the age of 25.

    Args:
        batch_size: The number of rows to process per batch.

    Yields:
        list: A filtered list of dictionaries with users older than 25.
    """
    for batch in stream_users_in_batches(batch_size):
        # Filter users older than 25
        filtered_batch = [user for user in batch if user["age"] > 25]

        for user in filtered_batch:
            print(user)
