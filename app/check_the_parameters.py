import logging

from .validators import validate_deadline
from .ui import type_text

def check_deadline(new_deadline:str, task:dict[str, str]) -> str | None:
    try:
        validate_deadline(new_deadline)
    except ValueError as error:
        type_text("Неправильный дедлайн!")
        logging.warning(f"Пользователь ввел неправильную дату: {error}")
        return None
    else:
        task["deadline"] = new_deadline
        return new_deadline

def check_login(users: list[dict[str, str]], login: str) -> bool:
    for user in users:
        if login == user["login"]:
            return True
    return False

def check_password(users: dict[str, str], password: str, login = None) -> bool:
    for user in users:
        if password == user["password"] and login is None:
            return True    
        elif password == user["password"] and login == user["login"]:
            return True
    return False