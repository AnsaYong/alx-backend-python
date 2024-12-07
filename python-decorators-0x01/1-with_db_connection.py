import sqlite3
import functools


# Decorator to automatically handle the opening and closing of the database connection
def with_db_connection(func):
    """
    This decorator opens a connection to the SQLite database,
    passes it to the decorated function, and then closes the connection.
    """

    @functools.wraps(func)  # To preserve function metadata
    def wrapper(*args, **kwargs):
        # Open the database connection
        conn = sqlite3.connect("users.db")

        try:
            # Call the original function with the connection as the first argument
            result = func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed after the function execution
            conn.close()

        return result

    return wrapper


# Using the with_db_connection decorator
@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetches a user by their ID from the database.

    Args:
        conn: Database connection object.
        user_id: ID of the user to fetch.

    Returns:
        The user record as a tuple.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


# Fetch a user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
