from .validators import validate_task
from .interaction_with_database import *
from .show_info import *
from .launch_of_program import load_config, determine_directory_of_database
from .check_the_parameters import check_deadline
from .get_the_parameters import get_parametres_of_task, get_task, filter_user_task
import logging
import questionary

config = load_config()
DATABASE_FILE = determine_directory_of_database()

def show_tasks_by_filter(user: str, tasks: list[dict[str, str]]) -> None:
    if filter_user_task(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачу, выбрав опцию 'Создать задачу'.")
        return None  
    user_status = questionary.select(
        "Выберите фильтр:",
        choices=[
            "Выполнено",
            "Не выполнено",
            "Вывести все"
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

    logging.info("Вывод файлов")
    print_tasks(user, tasks, user_status.lower()) 
    logging.info("Данные считаны.")   

def add_new_task(user: str) -> None:
    while True:
        custom_task = get_parametres_of_task(user)
        try:
            validate_task(custom_task)
        except ValueError as error:
            type_text(f"У вас ошибка: {error}. Попробуйте еще раз! ")
            logging.warning(f"Пользователь ввел неправильные данные: {error}")
        else:
            write_new_task(custom_task, DATABASE_FILE)
            type_text("Задача успешно записана!")
            logging.info("Пользователь записал новую задачу.")

        action = questionary.select(
                "Продолжить записывать задачи?",
                choices=[
                    "Продолжить",
                    "Выйти в меню"
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
        if action == "Выйти в меню":
            logging.info("Пользователь вышел в меню.")
            break

def change_task(user, tasks: list[dict[str, str]]) -> None:
    if filter_user_task(user, tasks) is None:
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
            if action == "Дедлайн":
                type_text("Введите новый дедлайн")
                new_deadline = input()
                if check_deadline(new_deadline, task_to_change) is not None:
                    write_new_deadline(task_to_change["id"], new_deadline, DATABASE_FILE)
                    logging.info(f"Пользователь поменял данные параметр deadline в {task_to_change["id"]} с {task_to_change["deadline"]} на {new_deadline}")   
                    type_text(f"Дедлайн в задаче с идентификатором №{task_to_change["id"]} успешно изменен!")
                    break
            elif action == "Статус":
                if task_to_change["status"] == "выполнено":
                    logging.info(f"Пользователь поменял данные параметр status в {task_to_change["id"]} с 'выполнено' на 'не выполнено'")   
                    task_to_change["status"] = "не выполнено"                 
                    write_new_status(task_to_change["id"], "не выполнено", DATABASE_FILE)
                else:
                    logging.info(f"Пользователь поменял данные параметр status в {task_to_change["id"]} с 'не выполнено' на 'выполнено'")   
                    task_to_change["status"] = "выполнено"                    
                    write_new_status(task_to_change["id"], "выполнено", DATABASE_FILE)
                type_text(f"Статус в задаче с идентификатором №{task_to_change["id"]} успешно изменен!")
                break                                        
    else:
        type_text("Такой задачи не существует!")

def delete_task(user: str, tasks: list[dict[str, str]]) -> None:
    if filter_user_task(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачу, выбрав опцию 'Создать задачу'.")
        return None
    type_text("Введите идентификатор задачи, которую хотите удалить.")
    id = int(input())
    task_to_be_deleted = get_task(id, user, tasks)
    if task_to_be_deleted is not None:
        del tasks[tasks.index(task_to_be_deleted)]
        remove_task(task_to_be_deleted["id"], DATABASE_FILE)
        type_text("Задача успешно удалена!")
        logging.info(f"Задача '{task_to_be_deleted}' была удалена")
    else:
        type_text("Такой задачи не существует!")
        logging.warning(f"Пользователь попытался удалить несуществующую задачу: {task_to_be_deleted}")
        


    