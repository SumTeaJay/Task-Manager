from .show_info import type_text
import logging
import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

USERS_FILE = DATA_DIR / "users.csv"

def check_login(users: list[dict[str, str]], login: str) -> bool:
    for user in users:
        if login == user["login"]:
            return True
    return False

def check_password(users: dict[str, str], password: str, login = None) -> bool:
    if login is None:
        for user in users:
            if password == user["password"]:
                return True
    else:
        for user in users:
            if user["login"] == login and password == user["password"]:
                return True
    return False        

def write_new_user(login: str, password: str) -> None:
    with open(USERS_FILE, "a", encoding="utf-8", newline="\n") as users_csv:
        writer = csv.DictWriter(users_csv, fieldnames=["login", "password"])
        writer.writerow({"login": login, "password": password})

def create_user(users: list[dict[str, str]]) -> dict[str, str]:
    while True:
        type_text("Введите новый логин")
        login = input()
        if not check_login(users, login):
            break
        else:
            type_text("Такой логин уже существует! Придумайте новый!")
    while True:
        type_text("Введите новый пароль")
        password = input()
        if check_password(users, password):
            type_text("Такой пароль уже существует! Придумайте новый")
        else:
            write_new_user(login, password)
            type_text("Пользователь создан!")
            logging.info(f"Создан новый пользователь - {login}.")
            return {"login": login, "password": password}

def check_user(users: list[dict[str, str]]) -> str:
    while True:
        type_text("Введите логин")
        login = input()
        if check_login(users, login):
            while True:
                type_text("Введите пароль")
                password = input()
                if check_password(users, password, login):
                    return login
                else:
                    type_text("Неверный пароль!")
        else:
            type_text("Такого логина не существует. Напишите 1, если хотите создать нового пользователя, иначе вам снова придется ввести новый логин")
            action = input()
            if action == "1":
                users.append(create_user(users))
                type_text("Введите данные пользователя снова, чтобы войти.")