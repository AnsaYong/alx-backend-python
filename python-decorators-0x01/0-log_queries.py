#!/usr/bin/env python3
"""
Decorators to log SQL queries before executing them.
"""
import sqlite3
import functools


# Decorator to log SQL queries
def log_queries(func):
    """
    Decorator to log SQL queries before executing them.

    Args:
        func: The function to be decorated.

    Returns:
        wrapper function that logs the query and then calls the original function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query parameter from the function's arguments
        query = (
            kwargs.get("query") or args[0]
        )  # Get query from kwargs or positional args

        # Log the query before executing
        print(f"Executing SQL query: {query}")

        # Call the original function and return its result
        return func(*args, **kwargs)

    return wrapper


# Function to fetch all users, decorated with log_queries
@log_queries
def fetch_all_users(query):
    """
    Fetch all users from the database using the provided query.

    Args:
        query: The SQL query to execute.

    Returns:
        results: A list of all rows fetched by the query.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
