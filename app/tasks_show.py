import time

def type_text(text, delay=0.03):
    for symbol in text:
        print(symbol, end="", flush=True)
        time.sleep(delay)
    print()

def show_tasks(tasks: list[dict[str, str]], status=None) -> None:
    if status is not None:
        tasks = filter(lambda task: task["status"]==status, tasks)
    for index, task in enumerate(tasks, 1):
        type_text(f"{index}) {task["name"]}\nСтатус: {task["status"]}\nДедлайн: {task["deadline"]}")

