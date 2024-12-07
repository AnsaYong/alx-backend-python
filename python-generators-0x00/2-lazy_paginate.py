#!/usr/bin/env python3
"""
This module contains a generator to lazily paginate users from the user_data table.
"""
seed = __import__("seed")


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator to lazily paginate users from the user_data table.
    Fetch the next page of users only when needed.

    Args:
        page_size: The number of users to fetch per page.

    Yields:
        list: A batch of users for the current page.
    """
    offset = 0

    while True:
        # Get the current page of users
        batch = paginate_users(page_size, offset)

        # If no more users, break the loop
        if not batch:
            break

        # Yield the current batch of users
        yield batch

        # Update the offset for the next page
        offset += page_size
