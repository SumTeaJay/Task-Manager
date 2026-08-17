import csv

def get_values():
    name = input("Введите название задачи: ")
    status = input("Введите статус задачи: выполнено/не выполнено ")
    deadline = input("Введите дедлайн в формате ДД.ММ.ГГГГ:")

    return {"name": name, "status": status, "deadline": deadline}

def write_values(custom_task: list[dict[str, str]], file_name: str):
    with open(file_name, "a", encoding="utf-8", newline="") as tasks_csv:
        writer = csv.DictWriter(tasks_csv, fieldnames=["name", "status", "deadline"])
        writer.writerow(custom_task)

def change_values(tasks: list[dict[str, str]], file_name: str):
    with open(file_name, "w", encoding="utf-8", newline="") as tasks_csv:
        writer = csv.DictWriter(tasks_csv, fieldnames=["user_name", "name", "status", "deadline"])
        writer.writeheader()
        writer.writerows(tasks)