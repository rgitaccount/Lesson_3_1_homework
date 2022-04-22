import sqlite3
from config import bot


def sql_create():
    global connection, cursor
    connection = sqlite3.connect("hw_db.sqlite3")
    cursor = connection.cursor()
    if connection:
        print("Database connected succesfully")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users
        (telegram_account_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT)
        """
    )
    connection.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        try:
            cursor.execute("""
            INSERT INTO users VALUES (?, ?, ?, ?)""", tuple(data.values()))
            connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)


async def sql_select(message):
    for result in cursor.execute("""SELECT * FROM users""").fetchall():
        await bot.send_message(message.chat.id, text=f'UserID: {result[0]}\n'
                                                     f'Username: {result[1]}\n'
                                                     f'Firstname: {result[2]}\n'
                                                     f'Lastname: {result[3]}\n')


async def sql_select_all():
    return cursor.execute("""SELECT * FROM users""").fetchall()


async def sql_delete(data):
    cursor.execute("""
    DELETE FROM users WHERE telegram_account_id == ?
    """, (data,))
    connection.commit()
