# Task-Manager
Консольный проект, позволяющий выводить, изменять и удалять задачи для определенных пользователей.

# Возможности проекта
- Создавать нового пользователя
- Входить в аккаунт
- Выводить список задач для пользователя по трем фильтрам: выполнено/не выполнено/вывести все
- Записывать новые задачи
- Изменять параметры задачи: статус и дедлайн
- Удалять задачи
- Выходить из программы

# Требования
Python 3.14+

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/SumTeaJay/Task-Manager.git
cd movie-library
```

Создайте виртуальное окружение:

```bash
python -m venv venv
```

Активируйте его в PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Установите проект и зависимости для разработки:

```bash
pip install pytest
```

P.S Полный список зависимостей находится в requirements.txt

## Запуск

Запускайте приложение из папки app:

```bash
python main.py
```

## Структура проекта

```text
movie-library/
├── app/
│   ├── authorization.py
│   ├── menu.py
│   ├── show_info.py
│   ├── storage.py
│   ├── ui.py
│   └── validators.py
├── tests/
├── data/
│   └── movies.db
├── main.py
├── pyproject.toml
└── README.md
```

- `app/authorization.py` — авторизация пользователя.
- `app/menu.py` — работа меню.
- `app/show_info.py` — вывод данных.
- `app/storage.py` — работа с файлами.
- `app/ui.py` — эффект печатания на клавиатуре.
- `app/validators.py` — проверка данных.
- `tests/` — автоматические тесты.
- `main.py` — точка входа.