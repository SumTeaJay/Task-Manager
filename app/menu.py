from .validators import *
from .storage import *
from .show_info import *
import logging
import questionary
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data"
TASKS_FILE = DATA_DIR / "database.db"

def show_tasks_by_filter(user: str, tasks: list[dict[str, str]]) -> None:
    if get_user_tasks(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачу, выбрав опцию 'Создать задачу'.")
        return None  
    user_status = questionary.select(
        "Выберите фильтр:",
        choices=[
            "Выполнено",
            "Не выполнено",
            "Вывести все"
        ],
        instruction="Чтобы выбрать действие, используйте стрелки на клавиатуре. Нажмите Enter, чтобы подтвердить выбор.",
        use_indicator=True,
        show_selected=True,
        style=questionary.Style([
            ("qmark", "fg:#62a874"),       
            ("question", "bold"),             
            ("answer", "fg:#62a874 bold"), 
            ("pointer", "fg:#62a874 bold"),     
            ("highlighted", "fg:#000000 bg:#62a874"),
            ("selected", "fg:#62a874"),
            ("instruction", ""),
            ("text", ""),
        ])).ask()

    logging.info("Вывод файлов")
    print_tasks(user, tasks, user_status.lower()) 
    logging.info("Данные считаны.")   

def add_new_task(user: str) -> None:
    while True:
        custom_task = get_values(user)
        try:
            validate_task(custom_task)
        except ValueError as error:
            type_text(f"У вас ошибка: {error}. Попробуйте еще раз! ")
            logging.warning(f"Пользователь ввел неправильные данные: {error}")
        else:
            write_new_task(custom_task, TASKS_FILE)
            type_text("Задача успешно записана!")
            logging.info("Пользователь записал новую задачу.")

        action = questionary.select(
                "Продолжить записывать задачи?",
                choices=[
                    "Продолжить",
                    "Выйти в меню"
                ],
                instruction="Чтобы выбрать действие, используйте стрелки на клавиатуре. Нажмите Enter, чтобы подтвердить выбор.",
                use_indicator=True,
                show_selected=True,
                style=questionary.Style([
                    ("qmark", "fg:#62a874"),       
                    ("question", "bold"),             
                    ("answer", "fg:#62a874 bold"), 
                    ("pointer", "fg:#62a874 bold"),     
                    ("highlighted", "fg:#000000 bg:#62a874"),
                    ("selected", "fg:#62a874"),
                    ("instruction", ""),
                    ("text", ""),
                ])).ask()
        if action == "Выйти в меню":
            logging.info("Пользователь вышел в меню.")
            break

def check_deadline(new_deadline:str, task:dict[str, str]) -> dict[str, str] | None:
    try:
        validate_deadline(new_deadline)
    except ValueError as error:
        type_text("Неправильный дедлайн!")
        logging.warning(f"Пользователь ввел неправильную дату: {error}")
        return None
    else:
        logging.info(f"Пользователь поменял параметр deadline в {task["name"]} с {task["deadline"]} на {new_deadline}")
        task["deadline"] = new_deadline
        return new_deadline

def check_status(new_status: str, task:dict[list, list]) -> dict[str, str] | None:
    try:
        validate_status(new_status)
    except ValueError as error:
        type_text("Неправильный статус!")
        logging.warning(f"Пользователь ввел несуществующий статус: {error}")
        return None
    else: 
        logging.info(f"Пользователь поменял параметр статус в {task["name"]} с {task["status"]} на {new_status}")
        task["status"] = new_status
        return new_status

def get_task(id: int, user: str, tasks: list[dict[str, str]]) -> dict[str, str] | None:
    for task in tasks:
        if task["id"] == id and task["user"] == user:
            return task
    else:
        return None

def change_task(user, tasks: list[dict[str, str]]) -> None:
    if get_user_tasks(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачу, выбрав опцию 'Создать задачу'.")
        return None
    type_text("Введите идентификатор задачи, данные которой вы хотите изменить.")
    id = int(input())
    task_to_change = get_task(id, user, tasks)
    if task_to_change is not None:
        while True:
            action = questionary.select(
                "Вы хотите изменить дедлайн или статус задачи?",
                choices=[
                    "Дедлайн",
                    "Статус"
                ],
                instruction="Чтобы выбрать действие, используйте стрелки на клавиатуре. Нажмите Enter, чтобы подтвердить выбор.",
                use_indicator=True,
                show_selected=True,
                style=questionary.Style([
                    ("qmark", "fg:#62a874"),       
                    ("question", "bold"),             
                    ("answer", "fg:#62a874 bold"), 
                    ("pointer", "fg:#62a874 bold"),     
                    ("highlighted", "fg:#000000 bg:#62a874"),
                    ("selected", "fg:#62a874"),
                    ("instruction", ""),
                    ("text", ""),
                ])).ask()
            if action == "Дедлайн":
                type_text("Введите новый дедлайн")
                new_deadline = input()
                try:
                    validate_deadline(new_deadline)
                except ValueError as error:
                    type_text("Неправильный дедлайн!")
                    logging.warning(f"Пользователь ввел неправильную дату: {error}")
                else:
                    logging.info(f"Пользователь поменял данные параметр deadline в {task_to_change["id"]} с {task_to_change["deadline"]} на {new_deadline}")                    
                    write_new_deadline(task_to_change["id"], new_deadline, TASKS_FILE)
                    type_text(f"Дедлайн в задаче с идентификатором №{task_to_change["id"]} успешно изменен!")
                    break
            elif action == "Статус":
                type_text("Введите новый статус задачи")
                new_status = input()
                try:
                    validate_status(new_status)
                except ValueError as error:
                    type_text("Неправильный дедлайн!")
                    logging.warning(f"Пользователь ввел неправильную дату: {error}")
                else:
                    logging.info(f"Пользователь поменял данные параметр status в {task_to_change["id"]} с {task_to_change["status"]} на {new_status}")                    
                    write_new_status(task_to_change["id"], new_status, TASKS_FILE)
                    type_text(f"Статус в задаче с идентификатором №{task_to_change["id"]} успешно изменен!")
                    break
    else:
        type_text("Такой задачи не существует!")

def delete_task(user: str, tasks: list[dict[str, str]]) -> None:
    if get_user_tasks(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачу, выбрав опцию 'Создать задачу'.")
        return None
    type_text("Введите идентификатор задачи, которую хотите удалить.")
    id = int(input())
    task_to_be_deleted = get_task(id, user, tasks)
    if task_to_be_deleted is not None:
        del tasks[tasks.index(task_to_be_deleted)]
        remove_task(task_to_be_deleted["id"], TASKS_FILE)
        type_text("Задача успешно удалена!")
        logging.info(f"Задача '{task_to_be_deleted}' была удалена")
    else:
        type_text("Такой задачи не существует!")
        logging.warning(f"Пользователь попытался удалить несуществующую задачу: {task_to_be_deleted}")
        


    