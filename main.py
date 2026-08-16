import logging

from app import read_file, validate_task, validate_status, show_tasks, get_values, write_values, type_text

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
        validate_task(tasks)
    except (OSError, ValueError, KeyError) as error:
        type_text("Работа невозможна - ошибка в файле.")
        logging.critical(error)

    logging.info("Программа запущена, данные считаны.")
    type_text("Привет, пользователь! Что именно тебя интересует сегодня?")
    while True:
        type_text("Выбери одно из трех действий:\n1 - Вывести задачи по статусу\n2 - Записать задачу\n3 - Выйти из программы")
        action = input()
        if action == "1":
            tasks = read_file(r"data\tasks.csv")
            validate_task(tasks)

            logging.info("Данные считаны.")
            type_text("Выберите фильтр: выполнено/не выполнено/вывести все")

            filter = input()
            if filter == "вывести все": filter = None
            try:
                validate_status(filter)
            except ValueError as error:
                type_text("Неправильный фильтр!")
                logging.warning(f"Пользователь ввел неправильный статус: {error}")
            logging.info("Вывод файлов")
            show_tasks(tasks, filter)

        elif action == "2":
            while True:
                custom_task = get_values()
                try:
                    validate_task(custom_task)
                except ValueError as error:
                    type_text(f"У вас ошибка: {error}. Попробуйте еще раз! ")
                    logging.warning(f"Пользователь ввел неправильный статус: {error}")
                else:
                    write_values(custom_task, r"data\tasks.csv")
                    type_text("Задача успешно записана!")
                    logging.info("Пользователь записал новую задачу.")
                action = input("Введите 1, если хотите продолжить записывать задачи. Любые другие символы перейдут к выходу в меню.\n")
                if action != "1":
                    logging.info("Пользователь вышел в меню.")
                    break
        elif action == "3":
            type_text("Покеда! ;)")
            logging.info("Пользователь вышел из программы.")
            break
                
        else:
            type_text("Что?\nТебе нужно ввести число от одного до трех, чтобы выполнить действие")
            logging.warning("Пользователь ввел неверную команду в меню.")

if __name__ == "__main__":
    main()