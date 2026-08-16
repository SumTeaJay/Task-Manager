import csv

def read_file(file_name: str) -> dict[str: str]:
    with open(file_name, encoding="utf-8", newline="") as tasks_csv:
        return list(csv.DictReader(tasks_csv))