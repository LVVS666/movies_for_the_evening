import sqlite3
import string
import random


def create_db():
    conn = sqlite3.connect('date_user_movies.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS sessions
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_name TEXT
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_name_id TEXT,
        FOREIGN KEY (session_id) REFERENCES sessions(id)
        '''
    )
    conn.commit()
    conn.close()

def users_add_to_session(user):
    global session_id
    conn = sqlite3.connect('date_user_movies.db')
    cursor = conn.cursor()
    session_name = ''
    for i in range(10):
        i = random.choice(string.ascii_letters)
        session_name += i

    cursor.execute('INSERT INTO sessions (session_name) VALUES (?)', (session_name,))
    session_id = cursor.lastrowid
    user_id = user.from_user.id
    cursor.execute('INSERT INTO users (user_id, session_id) VALUES (?, ?)', (user_id, session_id))
    conn.commit()
    conn.close()


def add_second_user_in_session(second_user):
    conn = sqlite3.connect('date_user_movies.db')
    cursor = conn.cursor()
    user_id = second_user.from_user.id
    cursor.execute('INSERT INTO users (user_id, session_id) VALUES (?, ?)', (user_id, session_id))
    conn.commit()
    conn.close()


def add_movie_in_db(user, name, year):
    conn = sqlite3.connect('date_user_movies.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS movies
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
        )
        '''
    )
    user_id_to_find = user.from_user.id
    cursor.execute('SELECT id FROM users WHERE user_id = ?', (user_id_to_find,))
    user_id = cursor.fetchone()[0]
    movie_data = {
        'name': name,
        'year': year,
    }
    cursor.execute(
        '''INSERT INTO movies (name, year, user_id)
         VALUES (?, ?, ?, ?, ?)''',
        (
         movie_data['name'],
         movie_data['year'],
         user_id
         )
    )
    conn.commit()
    conn.close()


def search_movies_in_db(user, movie):
    conn = sqlite3.connect('date_user_movies.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM movies'
                   WHERE user_id = (SELECT id FROM users WHERE user_name_id = ?)
                   AND name = ? ''', (user, movie))
    found_movies = cursor.fetchall()
    conn.close()
    if found_movies:
        return True
    else:
        return False

def search_user_in_db(user):
    conn = sqlite3.connect('date_user_movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user,))
    found_user = cursor.fetchall()
    conn.close()
    if found_user:
        return True
    else:
        return False







