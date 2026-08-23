from .show_info import type_text
from .interaction_with_database import write_new_user
from .check_the_parameters import check_login, check_password
from .launch_of_program import determine_directory_of_database, load_config

import logging
import questionary

config = load_config()
DATABASE_FILE = determine_directory_of_database()

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
        write_new_user({"login": login, "password": password}, DATABASE_FILE)
        type_text("Пользователь создан!")
        logging.info(f"Создан новый пользователь - {login}.")
        return {"login": login, "password": password}

def enter_program(users: list[dict[str, str]]) -> str:
    while True:
        type_text("Введите логин: ")
        login = input()
        if check_login(users, login):
            while True:
                type_text("Введите пароль: ")
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