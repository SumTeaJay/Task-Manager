import re
from datetime import date
required_fields = ["name", "status", "deadline"]

def validate_name(name: str) -> None:
    if len(name) > 150:
        raise ValueError(f"Название задачи слишком длинное: {len(name)} > 150")
    if not name:
        raise ValueError("Отсутствует имя")

def validate_status(status: str) -> None:
    if status is not None and status.lower() != "выполнено" and status.lower() != "не выполнено":
        raise ValueError("Ошибка в значении статуса задачи")

def validate_deadline(deadline: str) -> None:
    if not re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", deadline):
        raise ValueError("Неверный формат даты")
    
    try:
        deadline = date.strptime(deadline, "%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Даты {deadline} не существует")

def validate_task(raw_data: list[dict[str, str]]) -> None:
    for task in raw_data:
        for required_field in required_fields:
            if required_field not in task:
                raise KeyError(f"Отсутствует необходимое поле {required_field}")
        
    for row in raw_data:
        validate_name(row["name"])
        validate_status(row["status"])
        validate_deadline(row["deadline"])

    