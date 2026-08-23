import re
from datetime import date
required_fields = ["user", "name", "status", "deadline"]
task_status = ["выполнено", "не выполнено"]

def validate_name(name: str) -> None:
    if len(name) > 150:
        raise ValueError(f"Название задачи слишком длинное: {len(name)} > 150")
    if not name.strip():
        raise ValueError("Отсутствует имя")
    
def validate_status(status: str) -> None:
    if status.lower() not in task_status:
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

    