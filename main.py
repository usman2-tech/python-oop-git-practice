import bank_account


account = bank_account.BankAccount("Hamza", 1000)

account.display_balance()

account.deposit(500)

account.withdraw(200)

account.display_balance()