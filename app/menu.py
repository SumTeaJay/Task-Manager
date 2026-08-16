from .validators import *
from .tasks_write import *
from .print_tasks import *
import logging


def show_tasks_by_filter(tasks: list[dict[str, str]]) -> None:
    type_text("Выберите фильтр: выполнено/не выполнено/вывести все")
    user_status = input()

    try:
        validate_status(user_status)
    except ValueError as error:
        type_text("Неправильный фильтр!")
        logging.warning(f"Пользователь ввел неправильный статус: {error}")
    else:
        logging.info("Вывод файлов")
        print_task(tasks, user_status) 
        logging.info("Данные считаны.")   

def write_new_task() -> None:
    while True:
        custom_task = get_values()
        try:
            validate_task(custom_task)
        except ValueError as error:
            type_text(f"У вас ошибка: {error}. Попробуйте еще раз! ")
            logging.warning(f"Пользователь ввел неправильные данные: {error}")
        else:
            write_values(custom_task, r"data\tasks.csv")
            type_text("Задача успешно записана!")
            logging.info("Пользователь записал новую задачу.")

        action = input("Введите 1, если хотите продолжить записывать задачи. Любые другие символы перейдут к выходу в меню.\n")
        if action != "1":
            logging.info("Пользователь вышел в меню.")
            break

def change_task(tasks: list[dict[str, str]]) -> None:
    type_text("Введите название задачи, данные которой вы хотите изменить.")
    old_task = {}
    name = input()
    for task in tasks:
        if task["name"] == name:
            old_task = task     #я сделал это специально, чтобы мне не приходилось снова переназначать данные
            break
    else:
        type_text("Такой задачи нет! Вы можете создать ее в меню.")
        return None

    type_text("Введите 1, если хотите изменить дедлайн задачи; введите 2, если хотите изменить статус задачи")
    while True:
        action = input()
        if action == "1":
            type_text("Введите новый дедлайн")
            new_deadline = input()
            try:
                validate_deadline(new_deadline)
            except ValueError as error:
                type_text("Неправильный дедлайн!")
                logging.warning(f"Пользователь ввел неправильную дату: {error}")
            else:
                logging.info(f"Пользователь поменял данные параметр deadline в {name} с {old_task["deadline"]} на {new_deadline}")
                old_task["deadline"] = new_deadline
                change_values(tasks, r"data\tasks.csv")
                break
        elif action == "2":
            type_text("Введите новый статус задачи")
            new_status = input()
            try:
                validate_status(new_status)
            except ValueError as error:
                type_text("Неправильный статус!")
                logging.warning(f"Пользователь ввел несуществующий статус: {error}")
            else: 
                logging.info(f"Пользователь поменял данные параметр статус в {name} с {old_task["staths"]} на {new_status}")
                old_task["status"] = new_status      
                change_values(tasks, r"data\tasks.csv")
                break
        else:
            type_text("Что? Попробуйте еще раз.")
        


    