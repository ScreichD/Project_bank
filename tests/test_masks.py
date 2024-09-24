import pytest
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "number_card, mask",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210123456", "9876 54** **** 3456"),
    ],
)
def test_get_mask_card_number(number_card, mask):
    assert get_mask_card_number(number_card) == mask


@pytest.mark.parametrize(
    "number_account, mask", [("12345678901234567890", "** 7890"), ("98765432109876543210", "** 3210")]
)
def test_get_mask_account(number_account, mask):
    assert get_mask_account(number_account) == mask


@pytest.mark.parametrize(
    "inf_the_card, masks",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Maestro 9876543210123456", "Maestro 9876 54** **** 3456"),
        ("Счет 12345678901234567890", "Счет ** 7890"),
    ],
)
def test_mask_account_card(inf_the_card, masks):
    assert mask_account_card(inf_the_card) == masks
