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


# Decorator to manage transactions: commits or rolls back based on success or failure
def transactional(func):
    """
    This decorator ensures that a function running a database operation
    is wrapped inside a transaction. If the function raises an error,
    it will perform a rollback, otherwise, it will commit the transaction.
    """

    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Start a transaction by disabling autocommit
            conn.isolation_level = None  # This disables autocommit
            cursor = conn.cursor()

            # Begin a transaction
            cursor.execute("BEGIN TRANSACTION")

            # Call the original function, passing the connection and other arguments
            result = func(conn, *args, **kwargs)

            # Commit the transaction if no errors
            conn.commit()
            return result
        except Exception as e:
            # If an error occurs, roll back the transaction
            conn.rollback()
            print(f"Error during transaction: {e}")
        finally:
            # Reset isolation level to default (autocommit mode)
            conn.isolation_level = None  # Back to autocommit mode

    return wrapper


# Example function using both decorators to manage database connection and transaction
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Update the email of a user by their ID.

    Args:
        conn: Database connection object.
        user_id: ID of the user to update.
        new_email: New email address for the user.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
