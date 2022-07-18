from model import TransactionState

class Viewer:
    def __init__(self, bank) -> None:
        self.account = None
        self.bank = bank

        self.message = {}
        self.message[TransactionState.IDLE] = "取引可能"
        self.message[TransactionState.OK] = "取引成立"
        self.message[TransactionState.PIN_INCORRECT] = "暗証番号が合致しない"
        self.message[TransactionState.NAME_INCORRECT] = "存在しない口座"
    
    def setAccount(self, account):
        self.account = account

    def show(self):
        print("Respoce:")
        if self.account is None:
            print("No account is selected.")

        print("name {}, balance {}".format(self.account.name, self.account.balance))
        print("state:" + self.message[self.bank.state])