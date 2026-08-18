import csv

def get_values(user):
    name = input("Введите название задачи: ")
    status = input("Введите статус задачи: выполнено/не выполнено ")
    deadline = input("Введите дедлайн в формате ДД.ММ.ГГГГ:")

    return {"user_name": user, "name": name, "status": status, "deadline": deadline}

def write_values(custom_task: dict[str, str], file_name: str):
    with open(file_name, "a", encoding="utf-8", newline="\n") as tasks_csv:
        writer = csv.DictWriter(tasks_csv, fieldnames=["user_name", "name", "status", "deadline"])
        writer.writerow(custom_task)

def change_values(tasks: list[dict[str, str]], file_name: str):
    with open(file_name, "w", encoding="utf-8", newline="") as tasks_csv:
        writer = csv.DictWriter(tasks_csv, fieldnames=["user_name", "name", "status", "deadline"])
        writer.writeheader()
        writer.writerows(tasks)

def read_file(file_name: str) -> list[dict[str, str]]:
    with open(file_name, encoding="utf-8", newline="") as tasks_csv:
        return list(csv.DictReader(tasks_csv))