
from model import Account, Bank, TransactionState

class Controller:
    def __init__(self, bank : Bank, view) -> None:
        self.bank = bank
        self.view = view
        self.account = None
        

    def selectAccount(self, name, pin):
        account = self.bank.getAccount(name, pin)
        self.account = account
        self.view.setAccount(account)
        self.view.show()

    def withdraw(self, amount):
        if self.account:
            self.account.withdraw(amount)
        self.view.show()

    def deposit(self, amount):
        if self.account:
            self.account.deposit(amount)
        self.view.show()

class View:
    def __init__(self, bank : Bank, widget) -> None:
        self.bank = bank
        self.account : Account = None
        self.widget = widget

    def setAccount(self, account):
        self.account = account

    def show(self):
        self.widget.show(self.account.name, self.account.balance, self.bank.state)

