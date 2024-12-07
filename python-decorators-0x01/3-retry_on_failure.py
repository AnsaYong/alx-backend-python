import time
import sqlite3
import functools


# 1. with_db_connection Decorator (from previous task)
def with_db_connection(func):
    """
    This decorator opens a connection to the SQLite database,
    passes it to the decorated function, and then closes the connection.
    """

    @functools.wraps(func)
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


# 2. retry_on_failure Decorator
def retry_on_failure(retries=3, delay=2):
    """
    Decorator that retries the function in case of a failure,
    retrying a specified number of times with a delay between each retry.

    Args:
        retries: The number of times to retry the function in case of failure.
        delay: The number of seconds to wait between retries.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    # Try to execute the function
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"Failed after {retries} attempts.")
                        raise  # Re-raise the exception if retries are exhausted

        return wrapper

    return decorator


# 3. Example function that uses both decorators


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetch all users from the database, with retries in case of failure.

    Args:
        conn: Database connection object.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# 4. Attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
