# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance (default to 0)."""
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw amount if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount > self.__account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
