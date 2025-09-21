import datetime as dt
from src.exceptions import InsufficientFundsError, WithdrawlTimeRestrictionError, WithdrawDateRestrictionError


class BankAccount:
    def __init__(self, balance, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.__log_transaction("Cuenta creada.")

    def __log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Error no puedes depositar montos negativos.")
        self.balance += amount
        self.__log_transaction(f"Deposit: {amount}, new balance {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = dt.datetime.now()
        if now.weekday() >= 5:  # no permitir retiros los sabados y domingos
            raise WithdrawDateRestrictionError("Error no puedes hacer retiros los sabados y domingos.")

        if now.hour < 8 or now.hour > 17:  # solo se permiten retiros en horario comercial
            raise WithdrawlTimeRestrictionError("Los retiros son permitidos entre las 8 y las 17")

        if amount < 0:
            raise ValueError("Error no puedes retirar montos negativos.")
        if amount > self.balance:
            self.__log_transaction(f"Saldo insuficiente, no puedes retirar {amount}, tu balance disponble es {self.balance}")
            raise InsufficientFundsError("Error saldo insuficiente")
        self.balance -= amount
        self.__log_transaction(f"Withdraw: {amount}, new balance {self.balance}")
        return self.balance

    def get_balance(self):
        return self.balance

    def get_log(self):
        if self.log_file:
            with open(self.log_file, 'r') as f:
                return f.readlines()
        return None

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)
        self.__log_transaction(f"Transfer: {amount}, new balance {self.balance}")
        return True
