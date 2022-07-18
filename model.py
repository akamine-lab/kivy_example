from enum import Enum

class Account:
    def __init__(self, name, deposite, pin):
        self.name = name
        self.balance = deposite
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount):
        self.balance -= amount

class TransactionState(Enum):
    IDLE = 0
    OK = 1
    PIN_INCORRECT = 2
    NAME_INCORRECT = 3

class Bank:
    def __init__(self):
        self.accounts = {}
        self.state = TransactionState.IDLE

    def makeAccount(self,name, deposite, pin):
        new_account = Account(name, deposite, pin)
        self.accounts[name] = new_account
        return new_account

    def getAccount(self, name, pin):
        if name in self.accounts:
            account = self.accounts[name]

            if account.pin == pin:
                self.state = TransactionState.OK
                return account
            else:
                self.state = TransactionState.PIN_INCORRECT
                return None
        else:
            self.state = TransactionState.NAME_INCORRECT
            return None

class Teller:
    def __init__(self) -> None:
        self.handlingAccount = None
    
    def deposite(self, amount):
        pass

    def withdraw(self, amount):
        pass