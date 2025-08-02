# bank_account.py

class BankAccount:
    """
    A simple BankAccount class to demonstrate Object-Oriented Programming (OOP)
    concepts like encapsulation.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance with an optional initial balance.

        Args:
            initial_balance (float): The starting balance for the account.
                                     Defaults to 0 if not provided.
        """
        # Encapsulation: The account_balance is an internal state
        # that is accessed and modified only through methods.
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount must be a positive number.")
            return False
        self._account_balance += amount
        return True

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds or invalid amount).
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number.")
            return False
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")

