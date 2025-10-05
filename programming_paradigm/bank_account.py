# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Deduct the amount from the balance if sufficient funds exist."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        # ✅ Fixed formatting: show two decimal places as required
        print(f"Current Balance: ${self.__account_balance:.2f}")
