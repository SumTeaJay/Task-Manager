from .ui import type_text

def print_tasks(user: str, tasks: list[dict[str, str]], status=None) -> None:      
    tasks = list(filter(lambda task: task["user"] == user, tasks))
    if status != "вывести все":
        tasks = list(filter(lambda task: task["status"] == status, tasks))
    if tasks:
        for index, task in enumerate(tasks, 1):
            type_text(f"{index}) {task["name"]};\nИдентификатор: {task["id"]};\nСтатус: {task["status"]};\nДедлайн: {task["deadline"]}.")
    else:
        type_text("У вас нет задач по заданному фильтру.")

