import logging

from app import read_file, validate_task, type_text, show_tasks_by_filter, write_new_task, change_task, delete_task, check_user
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

TASKS_FILE = DATA_DIR / "tasks.csv"
USERS_FILE = DATA_DIR / "users.csv"
LOG_FILE = PROJECT_DIR / "app.log"

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    encoding="utf-8"
)

def main() -> None:
    users = read_file(USERS_FILE)
    user = check_user(users)
    try:
        tasks = read_file(TASKS_FILE)
        for task in tasks:
            validate_task(task)
    except Exception:
        logging.exception("Непредвиденная ошибка")
    else:
        logging.info("Программа запущена, данные считаны.")
        type_text(f"Привет, {user}! Что именно тебя интересует сегодня?")
        while True:
            try:
                tasks = read_file(TASKS_FILE)
                for task in tasks:
                    validate_task(task)
            except (OSError, ValueError, KeyError) as error:
                logging.critical(error)
            type_text("Выбери одно из пяти действий:\n1 - Вывести задачи по статусу\n2 - Записать задачу\n3 - Изменить данные задачи\n4 - Удалить задачу по имени\n5 - Выйти из программы")
            action = input()
            if action == "1":
                try:
                    show_tasks_by_filter(user, tasks)
                except Exception as error:
                    logging.critical(f"Непредвиденная ошибка: {error}")
                    type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                    break

            elif action == "2":
                try:
                    write_new_task(user)
                except Exception as error:
                    logging.critical(f"Непредвиденная ошибка: {error}")
                    type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                    break

            elif action == "3":
                try:
                    change_task(user, tasks)
                except Exception as error:
                    logging.critical(f"Непредвиденная ошибка: {error}")
                    type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                    break

            elif action == "4":
                try:
                    delete_task(user, tasks)
                except Exception as error:
                    logging.critical(f"Непредвиденная ошибка: {error}")
                    type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                    break

            elif action == "5":
                type_text("Покеда! ;)")
                logging.info("Пользователь вышел из программы.")
                break
                    
            else:
                type_text("Что?\nТебе нужно ввести число от одного до пяти, чтобы выполнить действие")
                logging.warning("Пользователь ввел неверную команду в меню.")

if __name__ == "__main__":
    main()