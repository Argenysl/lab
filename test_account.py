import pytest
from account import *

account = Account('Test_Account')


def test_main():
    assert account.account_name == 'Test_Account'
    assert account.account_balance == 0

    account_diff_name = Account('Different_Name')
    assert account_diff_name.account_name == 'Different_Name'


def test_deposit():
    assert account.deposit(100) is True
    assert account.deposit(0) is False
    assert account.deposit(-50) is False


def test_withdraw():
    account.deposit(500)
    assert account.withdraw(100) is True
    assert account.withdraw(0) is False
    assert account.withdraw(-200) is False
    assert account.withdraw(550) is False
