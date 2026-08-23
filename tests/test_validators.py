import pytest

from app.validators import validate_name, validate_task, validate_status, validate_deadline

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

###Валидация статуса задачи###
@pytest.mark.parametrize(
    "status",
    [
        "ВЫПОЛНЕНО",
        "выполнено",
        "Не ВыПоЛнЕнО",
        "ВЫПОЛНено",
        "не ВЫПОЛНЕНО",
        "не " + "выполнено"
    ]
)

def test_validate_status(status):
    result = validate_status(status)

    assert result is None

###Валидация дедлайна###
@pytest.mark.parametrize(
    "deadline",
    [
        "31.02.2026"
        "01-02-2027",
        "2027.08.01",
        "31 декабря 2008 года",
        "12.27.2042",
        "19.04,21",
        "27.09.26",
        "27-09-26",
        "01.03 2015"
    ]
)
def test_validate_deadline(deadline):
    with pytest.raises(ValueError):
        validate_deadline(deadline)

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