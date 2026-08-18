from .print_tasks import type_text
import logging
import csv


def check_login(users: dict[str, str], login):
    for user in users:
        if login == user["login"]:
            return True
    return False

def check_password(users: dict[str, str], password: str, login = None) -> True | False:
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
    with open(r"data\users.csv", "a", encoding="utf-8", newline="\n") as users_csv:
        writer = csv.DictWriter(users_csv, fieldnames=["login", "password"])
        writer.writerow({"login": login, "password": password})

def create_user(users: list[dict[str, str]]) -> None:
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

def check_user(users: list[dict[str, str]]) -> None:
    while True:
        type_text("Введите логин")
        login = input()
        if check_login(users, login):
            type_text("Введите пароль")
            while True:
                password = input()
                if check_password(users, password, login):
                    return login
                else:
                    type_text("Неверный пароль!")
                    break
        else:
            type_text("Такого логина не существует. Напишите 1, если хотите создать нового пользователя, иначе вам снова придется ввести новый логин")
            action = input()
            if action == "1":
                users.append(create_user(users))
                type_text("Введите данные пользователя снова, чтобы войти.")