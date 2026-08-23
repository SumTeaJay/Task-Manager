# Task-Manager
Консольный проект, позволяющий выводить, изменять и удалять задачи для определенных пользователей.

## Возможности проекта
- Создавать нового пользователя
- Входить в аккаунт
- Выводить список задач для пользователя по трем фильтрам: выполнено/не выполнено/вывести все
- Записывать новые задачи
- Изменять параметры задачи: статус и дедлайн
- Удалять задачи
- Выходить из программы

## Требования
Python 3.14+

## Установка

Перейдите в папку, куда хотите установить проект, указав полный путь:
```bash
cd C:\Users\example
```

Клонируйте репозиторий:

```bash
git clone https://github.com/SumTeaJay/Task-Manager.git
```

Создайте виртуальное окружение:

```bash
python -m venv .venv
```

Активируйте его в PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Установите зависимости для разработки:

```bash
pip install -r requirements.txt
```


## Запуск

Введите следующую команду:

```bash
python main.py
```

## Структура проекта

```text
Task-Manager/
├── app/
│   ├── authorization.py
│   ├── check_the_parameters.py
│   ├── get_the_parameters.py
│   ├── interaction_with_database.py
│   ├── launch_of_program.py
│   ├── menu.py
│   ├── show_info.py
│   ├── ui.py
│   └── validators.py
├── tests/
├── data/
│   └── database.db
├── main.py
├── pyproject.toml
├── config.toml
├── app.log
├── requirements.txt
└── README.md
```

- `app/authorization.py` — авторизация пользователя.
- `app/check_the_parameters.py` — обработка неправильных данных и поиск данных
- `app/get_the_parameters.py` — получение данных
- `app/interaction_with_database.py` — работа с базой данных.
- `app/launch_of_program.py` — подготовка программы к работе.
- `app/menu.py` — работа меню.
- `app/show_info.py` — вывод данных.
- `app/ui.py` — эффект печатания на клавиатуре.
- `app/validators.py` — проверка данных.
- `tests/` — автоматические тесты.
- `main.py` — точка входа.