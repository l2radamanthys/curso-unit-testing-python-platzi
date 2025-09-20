class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Error no puedes depositar montos negativos.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Error no puedes retirar montos negativos.")
        if amount > self.balance:
            raise Exception("Error saldo insuficiente")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)
        return True
