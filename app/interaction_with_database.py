import sqlite3

def write_new_task(new_task: dict[str, str], file_name: str):
    with sqlite3.connect(file_name) as connection:
        cur = connection.cursor()
        cur.execute("""
            INSERT INTO tasks (user, name, status, deadline)
            VALUES(?, ?, ?, ?)
        """, (new_task["user"], new_task["name"], new_task["status"], new_task["deadline"]))
    connection.close()

def write_new_user(new_user: dict[str, str], file_name: str):
    with sqlite3.connect(file_name) as connection:
        cur = connection.cursor()
        cur.execute("""
            INSERT INTO users (login, password)
            VALUES(?, ?)
        """, (new_user["login"], new_user["password"]))
    connection.close()

def remove_task(id: int, file_name: str):
    with sqlite3.connect(file_name) as connection:
        cur = connection.cursor()
        cur.execute("""
            DELETE FROM tasks WHERE id = ?
        """, (id, ))
    connection.close()

def write_new_deadline(task_id: int, deadline: str, file_name: str):
    with sqlite3.connect(file_name) as connection:
        cur = connection.cursor()
        cur.execute("""
            UPDATE tasks
            SET deadline = ?
            WHERE id = ?
        """, (deadline, task_id))
    connection.close()

def write_new_status(task_id: int, status: str, file_name: str):
    with sqlite3.connect(file_name) as connection:
        cur = connection.cursor()
        cur = connection.cursor()
        cur.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
        """, (status, task_id))
    connection.close()

def read_tasks(file_name: str) -> list[dict[str, str]]:
    with sqlite3.connect(file_name) as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                user TEXT,
                name VARCHAR(150),
                status TEXT,
                deadline TEXT,
                PRAGMA foreign_keys = ON;
                FOREIGN KEY (user) REFERENCES users (login)
            );
        """)
        cur.execute("""
            SELECT * FROM tasks;
        """)

        tasks = []
        rows = cur.fetchall()

        for row in rows:
            tasks.append(dict(row))
    connection.close()
    return tasks


def read_users(file_name: str) -> list[dict[str, str]]:
    with sqlite3.connect(file_name) as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                login TEXT PRIMARY KEY,
                password TEXT
            );
        """) 
        cur.execute("""
            SELECT * FROM users;
        """)

        users = []
        rows = cur.fetchall()

        for row in rows:
            users.append(dict(row))
    connection.close()

    return users