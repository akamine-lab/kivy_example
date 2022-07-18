from model import Bank
from text_viewer import Viewer

class Controller:
    def __init__(self, view : Viewer, bank : Bank) -> None:
        self.view = view
        self.bank = bank 

    def test(self):
        account = self.bank.makeAccount("taro", 100, "0123")
        self.view.setAccount(account)
        self.view.show()

if __name__ == "__main__":
    bank = Bank()
    Controller(Viewer(bank), bank).test()