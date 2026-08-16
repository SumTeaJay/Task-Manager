import logging

from app import read_file, validate_task, type_text, show_tasks_by_filter, write_new_task, change_task

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    encoding="utf-8"
)

def main() -> None:
    tasks = read_file(r"data\tasks.csv")
    try:
        for task in tasks:
            validate_task(task)
    except (OSError, ValueError, KeyError) as error:
        print("Работа невозможна - ошибка в файле.")
        print(f"Ошибка: {error}")
        logging.critical(error)
    else:
        logging.info("Программа запущена, данные считаны.")
        type_text("Привет, пользователь! Что именно тебя интересует сегодня?")
        while True:
            type_text("Выбери одно из четырех действий:\n1 - Вывести задачи по статусу\n2 - Записать задачу\n3 - Изменить данные задачи\n4 - Выйти из программы")
            action = input()
            if action == "1":
                tasks = read_file(r"data\tasks.csv")
                for task in tasks:
                    validate_task(task)

                show_tasks_by_filter(tasks)

            elif action == "2":
                write_new_task()

            elif action == "3":
                change_task(tasks)

            elif action == "4":
                type_text("Покеда! ;)")
                logging.info("Пользователь вышел из программы.")
                break
                    
            else:
                type_text("Что?\nТебе нужно ввести число от одного до трех, чтобы выполнить действие")
                logging.warning("Пользователь ввел неверную команду в меню.")

if __name__ == "__main__":
    main()