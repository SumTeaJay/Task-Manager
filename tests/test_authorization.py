import pytest

from app.authorization import enter_program, create_user

@pytest.mark.parametrize(
    "answers",
    [
        [
            "sum_tea_jay",
            "1234",
            "12",
            "123",            
        ]
    ]
)

def test_enter_program(monkeypatch, answers):
    users = [
        {"login": "sum_tea_jay", "password": "123"}
    ]

    answers = iter(answers)

    monkeypatch.setattr(
        "builtins.input",
        lambda: next(answers)
    )

    monkeypatch.setattr(
        "app.interaction_with_database.write_new_user",
        lambda user, file: None
    )

    result = enter_program(users)

    assert result == "sum_tea_jay"

def test_create_user(monkeypatch):
    users = [
        {"login": "sum_tea_jay", "password": "123"}
    ]

    answers = iter([
        "sum_tea_jay",
        "danya",
        "123",
        "qwerty",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda: next(answers)
    )

    monkeypatch.setattr(
        "app.interaction_with_database.write_new_user",
        lambda user, file: None
    )

    result = create_user(users)

    assert result == {
        "login": "danya",
        "password": "qwerty"
    }