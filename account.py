class Account:
    def __init__(self, name: str) -> None:
        """
        This is the main function, it contains the account name and balance.

        :param name: Name given to the account
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: int) -> bool:
        """
        This function takes the account balance and increases it by the amount given.

        :param amount: This is the amount added to the account.
        :return: False if amount is negative or zero. True otherwise.
        """
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount: int) -> bool:
        """
        This function takes a given amount out of the account balance.

        :param amount: This is the amount taken from the account balance.
        :return: False if amount is negative, zero, or more than the account balance. True otherwise.
        """
        if amount <= 0:
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self) -> str:
        """
        This function shows the balance of the account.

        :return: The account balance
        """
        return f'Account Balance: {self.account_balance}'

    def get_name(self) -> str:
        """
        This function shows the name of the account.

        :return: The account name
        """
        return f'Account Name: {self.account_name}'
