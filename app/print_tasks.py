import time

def type_text(text, delay=0.03):
    for symbol in text:
        print(symbol, end="", flush=True)
        time.sleep(delay)
    time.sleep(delay * 10)
    print()

def print_task(user: str, tasks: list[dict[str, str]], status=None) -> None:
    tasks = filter(lambda task: task["user_name"] == user, tasks)
    if status != "вывести все":
        tasks = filter(lambda task: task["status"] == status, tasks)
    for index, task in enumerate(tasks, 1):
        type_text(f"{index}) {task["name"]}\nСтатус: {task["status"]}\nДедлайн: {task["deadline"]}")

