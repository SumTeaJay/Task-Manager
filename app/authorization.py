from .show_info import type_text
from .storage import write_new_user, load_config
import logging
import questionary
from pathlib import Path

config = load_config()

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data"
TASKS_FILE = DATA_DIR / "database.db"

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
            write_new_user({"login": login, "password": password}, TASKS_FILE)
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
            action = questionary.select(
                "Такого логина не существует. Хотите создать нового пользователя?",
                choices=[
                    "Создать нового пользователя",
                    "Продолжить вводить логин"
                ],
                instruction=config["ui"]["instruction_text"],
                use_indicator=True,
                show_selected=True,
                style=questionary.Style([
                    ("qmark", f"fg:{config["ui"]["default_color"]}"),       
                    ("question", "bold"),             
                    ("answer", f"fg:{config["ui"]["default_color"]} bold"), 
                    ("pointer", f"fg:{config["ui"]["default_color"]} bold"),     
                    ("highlighted", f"fg:#000000 bg:{config["ui"]["default_color"]}"),
                    ("selected", f"fg:{config["ui"]["default_color"]}"),
                    ("instruction", ""),
                    ("text", ""),
                ])).ask()
            if action == "Создать нового пользователя":
                users.append(create_user(users))
                type_text("Введите данные пользователя снова, чтобы войти.")