from .print_tasks import type_text
import logging
import csv
import re


def check_login(users: dict[str, str], login):
    for user in users:
        if login == user["login"]:
            raise KeyError("Такой логин уже существует! Придумайте новый!")

def check_password(users: dict[str, str], password):
    for user in users:
        if password == user["password"]:
            raise KeyError()

def write_new_user(login: str, password: str) -> None:
    with open(r"..\data\users", "a", encoding="utf-8", newline="") as users_csv:
        writer = csv.DictWriter(users_csv, fieldnames=["login", "password"])
        writer.writerow({"login": login, "password": password})

def create_user(users: dict[str, str]) -> None:
    while True:
        type_text("Введите новый логин")
        login = input()
        try:
            check_login(users, login)
        except KeyError:
            type_text("Такой логин уже существует! Придумайте новый!")
        else:
            break
    while True:
        type_text("Введите новый пароль")
        password = input()
        try:
            check_password(users, password)
        except KeyError:
            type_text("Такой пароль уже существует! Придумайте новый!")
        else:
            write_new_user(login, password)
            type_text("Пользователь создан!")
            logging.info(f"Создан новый пользователь - {login}.")
            break

def check_user(users: list[dict[str, str]]) -> None:
    type_text("Введите логин")
    login = input()
    type_text("Введите пароль")
    while True:
        password = input()
        for user in users:
            if user["login"] == login:
                if user["password"] != password:
                    type_text("Неверный пароль!")
                    break
            


