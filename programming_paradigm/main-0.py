import sys
import os
from bank_account import BankAccount

BALANCE_FILE = "balance.txt"

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as file:
            return float(file.read())
    return 100.0  # Default starting balance

def save_balance(balance):
    with open(BALANCE_FILE, 'w') as file:
        file.write(str(balance))

def main():
    balance = load_balance()
    account = BankAccount(balance)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        save_balance(account._BankAccount__account_balance)  # Access private var
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            save_balance(account._BankAccount__account_balance)
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
