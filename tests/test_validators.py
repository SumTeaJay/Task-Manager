import pytest

from app.validators import validate_name, validate_task

###Валидация имени задачи###
@pytest.mark.parametrize(
    "name",
    [
        "n",
        "h" * 150,
    ]
)
def test_validate_name_valid(name):
    result = validate_name(name)

    assert result is None

@pytest.mark.parametrize(
    "name, message",
    [
        ("", "Отсутствует имя"),
        ("h" * 151, "Название задачи слишком длинное: 151 > 150"),
    ]
)
def test_validate_name_invalid(name, message):
    with pytest.raises(ValueError, match=message):
        validate_name(name)

###Валидация целой задачи###
@pytest.mark.parametrize(
        "task",
        [
            ({"user": "sum_tea_jay", "status": "выполнено", "deadline": "12.09.2007"}),
            ({"user": "sum_tea_jay", "name": "name", "deadline": "12.09.2007"}),
            ({"status": "не выполнено", "name": "name", "deadline": "12.09.2007"}),
            ({"user": "user", "status": "не выполнено", "name": "name"})
        ]
)
def test_validate_task_headers(task):
    with pytest.raises(KeyError):
        validate_task(task)