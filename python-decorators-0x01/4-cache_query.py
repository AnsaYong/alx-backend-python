import time
import sqlite3
import functools

# In-memory cache for storing query results
query_cache = {}


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


# 2. cache_query Decorator
def cache_query(func):
    """
    A decorator that caches query results based on the SQL query string.

    Args:
        func: The decorated function that performs the database query.

    Returns:
        A function that caches the results of the database query.
    """

    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if the query result is already in the cache
        if query in query_cache:
            print("Returning cached result for query:", query)
            return query_cache[query]  # Return cached result

        # If not in cache, execute the query and cache the result
        result = func(conn, query, *args, **kwargs)

        # Cache the result
        query_cache[query] = result
        print("Query executed and cached:", query)
        return result

    return wrapper


# 3. Example function that uses both decorators


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetch all users from the database with query caching.

    Args:
        conn: Database connection object.
        query: SQL query string to fetch users.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# 4. First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# 5. Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
