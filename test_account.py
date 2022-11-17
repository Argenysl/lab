from pytest import *
from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Test')

        self.p2 = Account('Jorge')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        """
        This function tests the __init__ functions within the class Account
        """
        assert self.p1.get_name() == 'Test'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'Jorge'
        assert self.p2.get_balance() == 0

    def test_deposit(self):
        """
        This function tests the deposit functon within the class Account
        A positive integer should return True
        A negative integer and a zero value are should return False
        """
        self.p1.deposit(500)
        self.p2.deposit(250)
        assert self.p1.deposit(4.5) is True
        assert self.p1.get_balance() == approx(504.5, abs=.0001)
        assert self.p1.deposit(100) is True
        assert self.p1.deposit(0) is False
        assert self.p1.deposit(-50) is False
        assert self.p1.get_balance() == approx(604.5, abs=.0001)

        assert self.p2.deposit(70.5) is True
        assert self.p2.get_balance() == approx(320.5, abs=.0001)
        assert self.p2.deposit(300) is True
        assert self.p2.deposit(0) is False
        assert self.p2.deposit(-130) is False
        assert self.p2.get_balance() == approx(620.5, abs=.0001)

    def test_withdraw(self):
        """
        This function tests the withdraw functions within the class Account
        p1 has 604.5 in its account
        p2 has 620.5 in its account
        A positive integer should return True
        A negative integer and a zero value are should return False
        A value > amount should return False
        """
        self.p1.deposit(604.5)
        self.p2.deposit(620.5)

        assert self.p1.withdraw(100) is True
        assert self.p1.withdraw(30.25) is True
        assert self.p1.get_balance() == approx(474.25, abs=.0001)
        assert self.p1.withdraw(0) is False
        assert self.p1.withdraw(-200) is False
        assert self.p1.withdraw(800) is False

        assert self.p2.withdraw(200) is True
        assert self.p2.withdraw(40.75) is True
        assert self.p2.get_balance() == approx(379.75, abs=.0001)
        assert self.p2.withdraw(0) is False
        assert self.p2.withdraw(-200) is False
        assert self.p2.withdraw(1000) is False
