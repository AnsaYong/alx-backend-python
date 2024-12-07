#!/usr/bin/env python3
"""
This module contains a generator to stream user ages from the user_data table
and one to calculate the average age of users.
"""
import mysql.connector
from mysql.connector import Error


def stream_user_ages():
    """
    Generator to fetch user ages one by one from the user_data table.

    Yields:
        float: The age of each user.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect()  # Provide your MySQL connection details
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")  # Assuming the 'age' column exists

        while True:
            # Fetch one row at a time
            row = cursor.fetchone()
            if row is None:
                break  # No more rows, stop the loop
            # Yield the age of the current user
            yield row[0]

    except Error as e:
        print(f"Database error: {e}")
    finally:
        # Ensure the connection and cursor are closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def calculate_average_age():
    """
    Calculate the average age of users by consuming the ages generated by stream_user_ages.

    Returns:
        float: The average age of users.
    """
    total_age = 0
    user_count = 0

    for age in stream_user_ages():
        total_age += age
        user_count += 1

    if user_count == 0:
        return 0  # Avoid division by zero if there are no users

    return total_age / user_count


# Call the function and print the result
average_age = calculate_average_age()
print(f"Average age of users: {average_age}")