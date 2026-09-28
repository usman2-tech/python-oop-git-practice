from bank_account import BankAccount


account = BankAccount("Hamza", 1000)

account.display_balance()

account.deposit(500)

account.withdraw(200)

account.display_balance()

print(account.get_account_info())