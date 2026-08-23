def get_parameters_of_task(user):
    name = input("Введите название задачи: ")
    status = input("Введите статус задачи: выполнено/не выполнено ")
    deadline = input("Введите дедлайн в формате ДД.ММ.ГГГГ:")

    return {"user": user, "name": name, "status": status, "deadline": deadline}

def get_task(id: int, user: str, tasks: list[dict[str, str]]) -> dict[str, str] | None:
    for task in tasks:
        if task["id"] == id and task["user"] == user:
            return task
    return None

def filter_user_task(user: str, tasks: list[dict[str, str]]) -> None:
    tasks = list(filter(lambda task: task["user"] == user, tasks))
    if not tasks:
        return None
    return tasks