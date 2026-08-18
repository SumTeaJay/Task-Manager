import pytest
from pathlib import Path

from app.menu import show_tasks_by_filter
from app.storage import read_file


###У меня функция 'show_tasks_by_filter' - говно, ее сложно тестировать и ее нужно декомпозировать
# PROJECT_DIR = Path(__file__).resolve().parent
# DATA_DIR = PROJECT_DIR / "data"

# TASKS_FILE = DATA_DIR / "tasks.csv"
# tasks = read_file(TASKS_FILE)

# @pytest.mark.parametrize(
#     "user, tasks",
#     [
#         ("sum_tea_jay")
#     ]
# )

# def test_show_tasks_by_filter(user, tasks):
#     result = show_tasks_by_filter(user, tasks)
#     assert result is None