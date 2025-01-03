import aiosqlite
import asyncio


async def async_fetch_users(db_name):
    """
    Fetch all users from the database.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            print("All Users:")
            for row in results:
                print(row)
            return results


async def async_fetch_older_users(db_name):
    """
    Fetch users older than 40.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            results = await cursor.fetchall()
            print("Users older than 40:")
            for row in results:
                print(row)
            return results


async def fetch_concurrently(db_name):
    """
    Run both queries concurrently using asyncio.gather.
    """
    all_users_task = async_fetch_users(db_name)
    older_users_task = async_fetch_older_users(db_name)

    # Run both tasks concurrently
    results = await asyncio.gather(all_users_task, older_users_task)
    return results


if __name__ == "__main__":
    db_name = "example.db"

    # Create a sample database and table for demonstration
    async def setup_database():
        async with aiosqlite.connect(db_name) as db:
            await db.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
            )
            await db.executemany(
                "INSERT OR IGNORE INTO users (name, age) VALUES (?, ?)",
                [
                    ("Alice", 30),
                    ("Bob", 50),
                    ("Charlie", 45),
                    ("Diana", 25),
                    ("Eve", 42),
                ],
            )
            await db.commit()

    # Setup database and run the concurrent fetch
    asyncio.run(setup_database())
    asyncio.run(fetch_concurrently(db_name))
