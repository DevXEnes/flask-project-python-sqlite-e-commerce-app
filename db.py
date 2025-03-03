import sqlite3
import re


def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


def check_user_credentials(username, password):
    conn = get_db_connection()
    query = "SELECT username, password FROM users WHERE username = ?"
    user = conn.execute(query, (username,)).fetchone()
    conn.close()

    if user:
        if user["password"] == password:
            return True
        else:
            return False
    else:
        return None


def create_user(username, password, name, email):
    # E-posta doğrulama için basit bir regex
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Girdi kontrolü
    if (
        len(username) > 8
        and len(password) > 8
        and len(name) > 3
        and re.match(email_pattern, email)
    ):
        conn = get_db_connection()
        query = (
            "INSERT INTO users (username, password, name, email) VALUES (?, ?, ?, ?)"
        )
        conn.execute(query, (username, password, name, email))
        conn.commit()
        conn.close()
        return True  # Kullanıcı başarıyla oluşturuldu
    else:
        return False  # Girdi hatalı
