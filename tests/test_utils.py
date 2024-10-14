import os

import pytest

from src.utils import file_opening


@pytest.fixture
def path_to_file():
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"
    )


@pytest.fixture
def path_to_file_empty():
    return os.path.join(os.path.dirname(__file__), "data", "operations_empty.json")


def test_file_opening_empty(path_to_file_empty):
    assert file_opening(path_to_file_empty) == []


def test_file_opening(path_to_file):
    assert file_opening(path_to_file)[0] == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
