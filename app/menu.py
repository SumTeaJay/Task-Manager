from .validators import *
from .tasks_write import *
from .print_tasks import *
import logging

def show_tasks_by_filter(user: str, tasks: list[dict[str, str]]) -> None:
    if check_if_there_tasks(user, tasks) is None:
        type_text("У вас пока нет задач. Вы можете добавить их, написав в меню '2'")
        return None  
    type_text("Выберите фильтр: выполнено/не выполнено/вывести все")
    user_status = input()

    try:
        validate_status(user_status)
    except ValueError as error:
        type_text("Неправильный фильтр!")
        logging.warning(f"Пользователь ввел неправильный статус: {error}")
    else:
        logging.info("Вывод файлов")
        print_task(user, tasks, user_status) 
        logging.info("Данные считаны.")   

def write_new_task(user: str) -> None:
    while True:
        custom_task = get_values(user)
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

def change_deadline(task):
    new_deadline = input()
    try:
        validate_deadline(new_deadline)
    except ValueError as error:
        type_text("Неправильный дедлайн!")
        logging.warning(f"Пользователь ввел неправильную дату: {error}")
        return None
    else:
        logging.info(f"Пользователь поменял данные параметр deadline в {task["name"]} с {task["deadline"]} на {new_deadline}")
        return new_deadline

def change_status(task):
    new_status = input()
    try:
        validate_status(new_status)
    except ValueError as error:
        type_text("Неправильный статус!")
        logging.warning(f"Пользователь ввел несуществующий статус: {error}")
        return None
    else: 
        logging.info(f"Пользователь поменял данные параметр статус в {task["name"]} с {task["status"]} на {new_status}")
        return new_status  

def get_task(user: str, tasks: list[dict[str, str]]):
    name = input()
    for task in tasks:
        if task["name"] == name and task["user_name"] == user:
            return task
    else:
        return None

def change_task(user, tasks: list[dict[str, str]]) -> None:
    if check_if_there_tasks(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачи, написав в меню '2'.")
        return None
    type_text("Введите название задачи, данные которой вы хотите изменить.")
    old_task = get_task(user, tasks)
    if old_task is not None:
        type_text("Введите 1, если хотите изменить дедлайн задачи; введите 2, если хотите изменить статус задачи")
        while True:
            action = input()
            if action == "1":
                type_text("Введите новый дедлайн")
                new_deadline = change_deadline(old_task)
                if new_deadline is not None:
                    old_task["deadline"] = new_deadline
                    change_values(tasks, r"data\tasks.csv")
                    type_text(f"Параметр 'deadline' в задаче '{old_task["name"]}' успешно изменен!")
                    break
            elif action == "2":
                type_text("Введите новый статус задачи")
                new_status = change_status(old_task)
                if new_status is not None:
                    old_task["status"] = new_status
                    type_text(f"Параметр 'status' в задаче '{old_task["name"]}' успешно изменен!")
                    change_values(tasks, r"data\tasks.csv")
                    break
            else:
                type_text("Что? Попробуйте еще раз.")
    else:
        type_text("Такой задачи не существует!")

def delete_task(user: str, tasks: list[dict[str, str]]) -> None:
    if check_if_there_tasks(user, tasks) is None:
        type_text("Список задач пуст! Создайте задачи, написав в меню '2'.")
        return None
    type_text("Введите имя задачи, которую хотите удалить.")
    task_to_be_deleted = get_task(user, tasks)
    if task_to_be_deleted is not None:
        del tasks[tasks.index(task_to_be_deleted)]
        change_values(tasks, r"data\tasks.csv")
        type_text("Задача успешно удалена!")
        logging.info(f"Задача '{task_to_be_deleted}' была удалена")
    else:
        type_text("Такой задачи не существует!")
        logging.warning(f"Пользователь попытался удалить несуществующую задачу: {task_to_be_deleted}")
        


    