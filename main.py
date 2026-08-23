import logging
import questionary

from app import read_users, read_tasks, validate_task, type_text, show_tasks_by_filter, add_new_task, change_task, delete_task, enter_program, load_config, determine_directory_of_database, create_log_file

config = load_config()
DATABASE_FILE = determine_directory_of_database()
create_log_file()

def main() -> None:
    try:
        users = read_users(DATABASE_FILE)
        user = enter_program(users)

        tasks = read_tasks(DATABASE_FILE)

        for task in tasks:
            validate_task(task)

    except Exception:
        logging.exception("Непредвиденная ошибка")
        return

    logging.info("Программа запущена, данные считаны.")
    type_text(f"Здравствуйте, {user}! Что именно интересует вас сегодня?")

    while True:
        try:
            tasks = read_tasks(DATABASE_FILE)
            for task in tasks:
                validate_task(task)
        except (OSError, ValueError, KeyError) as error:
            logging.critical(error)
        action = questionary.select(
            "Выберите одно из пяти действий.\n",
            choices=[
                "Вывести задачи по статусу",
                "Записать задачу",
                "Изменить данные задачи",
                "Удалить задачу по идентификатору",
                "Выйти из программы"
            ],
            instruction=config["ui"]["instruction_text"],
            use_indicator=True,
            show_selected=True,
            style=questionary.Style([
                ("qmark", f"fg:{config["ui"]["default_color"]}"),       
                ("question", "bold"),             
                ("answer", f"fg:{config["ui"]["default_color"]} bold"), 
                ("pointer", f"fg:{config["ui"]["default_color"]} bold"),     
                ("highlighted", f"fg:#000000 bg:{config["ui"]["default_color"]}"),
                ("selected", f"fg:{config["ui"]["default_color"]}"),
                ("instruction", ""),
                ("text", ""),
            ])).ask()
        if action == "Вывести задачи по статусу":
            try:
                show_tasks_by_filter(user, tasks)
            except Exception as error:
                logging.critical(f"Непредвиденная ошибка: {error}")
                type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                break

        elif action == "Записать задачу":
            try:
                add_new_task(user)
            except Exception as error:
                logging.critical(f"Непредвиденная ошибка: {error}")
                type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                break

        elif action == "Изменить данные задачи":
            try:
                change_task(user, tasks)
            except Exception as error:
                logging.critical(f"Непредвиденная ошибка: {error}")
                type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                break

        elif action == "Удалить задачу по идентификатору":
            try:
                delete_task(user, tasks)
            except Exception as error:
                logging.critical(f"Непредвиденная ошибка: {error}")
                type_text("Возникла непредвиденная ошибка, из-за которой дальнейшая работа программы невозможна. Проверьте app.log")
                break

        elif action == "Выйти из программы":
            type_text("До скорой встречи!")
            logging.info("Пользователь вышел из программы.")
            break

if __name__ == "__main__":
    main()