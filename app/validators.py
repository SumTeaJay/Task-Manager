import re
from datetime import date
from .launch_of_program import load_config
config = load_config()
max_length_of_task = config["limitations"]["max_length_of_task"]
required_fields = ["user", "name", "status", "deadline"]
task_status = ["выполнено", "не выполнено"]

def validate_name(name: str) -> None:
    if len(name) > max_length_of_task:
        raise ValueError(f"Название задачи слишком длинное: {len(name)} > {max_length_of_task}")
    if not name.strip():
        raise ValueError("Отсутствует имя")
    
def validate_status(status: str) -> None:
    if status not in task_status:
        raise ValueError("Ошибка в значении статуса задачи")

def validate_deadline(deadline: str) -> None:
    if not re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", deadline):
        raise ValueError("Неверный формат даты")
    
    try:
        deadline = date.strptime(deadline, "%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Даты {deadline} не существует")

def validate_task(raw_task: dict[str, str]) -> None:
    for required_field in required_fields:
        if required_field not in raw_task:
            raise KeyError(f"Отсутствует необходимое поле {required_field}")

    validate_name(raw_task["name"])
    validate_status(raw_task["status"])
    validate_deadline(raw_task["deadline"])

    