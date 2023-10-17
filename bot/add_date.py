import random
import sqlite3
import string


def create_db():
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_name_id INTEGER,
        session_id INTEGER,
        FOREIGN KEY (session_id) REFERENCES sessions(id))
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movies
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        year INTEGER,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movies_date
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        year INTEGER,
        description TEXT,
        poster TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def users_add_to_session(user):
    global session_id
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    session_name = ""
    for i in range(10):
        i = random.choice(string.ascii_letters)
        session_name += i

    cursor.execute("INSERT INTO sessions (session_name) VALUES (?)", (session_name,))
    session_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO users (user_name_id, session_id) VALUES (?, ?)", (user, session_id)
    )
    conn.commit()
    conn.close()


def add_second_user_in_session(user_id):
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_name_id, session_id) VALUES (?, ?)",
        (user_id, session_id),
    )
    conn.commit()
    conn.close()


def add_movie_in_db(user, name, year):
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE user_name_id = ?", (user,))
    user_id = cursor.fetchone()[0]
    cursor.execute(
        "INSERT INTO movies (name, year, user_id) VALUES (?, ?, ?)",
        (name, year, user_id),
    )
    conn.commit()
    conn.close()


def search_movies_in_db(user, movie):
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM movies WHERE user_id = (SELECT id FROM users WHERE user_name_id = ?) AND name = ?",
        (user, movie),
    )
    found_movies = cursor.fetchall()
    conn.close()
    if found_movies:
        return True
    else:
        return False


def search_user_in_db(user):
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_name_id = ?", (user,))
    found_user = cursor.fetchall()
    conn.close()
    if found_user:
        return True
    else:
        return False


def create_movie_date(item):
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO movies_date (name, year, description, poster) VALUES (?, ?, ?, ?)",
        (item["name"], item["year"], item["description"], item["poster"]),
    )
    conn.commit()
    conn.close()


def return_movie(id):
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies_date WHERE id = ?", (id,))
    date = cursor.fetchall()
    date_movie = {
        "name": date[0][1],
        "year": date[0][2],
        "description": date[0][3],
        "poster": date[0][4],
    }
    conn.close()
    return date_movie


def create_list_users():
    conn = sqlite3.connect("date_user_movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    row = cursor.fetchall()
    list_users = []
    for i in row:
        list_users.append(i[1])
    conn.close()
    return list_users
