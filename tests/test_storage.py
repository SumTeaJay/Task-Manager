
###Старые тесты

import pytest

from app.storage import read_file, write_new_task

@pytest.mark.parametrize(
        "file_name",
        [
            "new.db",
            "database.db"
        ]
)

def test_read_file(tmp_path, file_name):
    file_path = tmp_path / file_name
    assert type(read_file(file_path)) is list

@pytest.mark.parametrize(
        "task",
        [
            ({"user": "1", "name": "name", "status": "выполнено", "deadline": "12.09.2007"}),
            ({"user": "2", "name": "test", "status": "не выполнено", "deadline": "12.12.2007"}),
            ({"user": "1", "name": "test1", "status": "выполнено", "deadline": "12.09.2029"}),
        ]
)

def test_write_new_task(task, tmp_path):
    file_path = tmp_path / "database.db"
    read_file(file_path)
    assert write_new_task(task, file_path) is None
