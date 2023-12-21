import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="admin",
    password="root"
)

def register_user(username, password):
    hashed_password = generate_password_hash(password, method='pbkdf2')
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO user_auth (username, password) VALUES (%s, %s);", (username, hashed_password))
    conn.commit()

def login_user(username, password):
    with conn.cursor() as cursor:
        cursor.execute("SELECT password FROM user_auth WHERE username = %s;", (username,))
        result = cursor.fetchone()
        if result and check_password_hash(result[0], password):
            return True
        else:
            return False