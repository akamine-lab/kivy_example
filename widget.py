
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty

import re
from view_controller import Controller
from model import TransactionState

class DigitInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        return super().insert_text(s, from_undo=from_undo)

class BankWidget(Widget):
    ac_name = StringProperty("no account is selected")
    ac_balance = NumericProperty(0)
    state = StringProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None

        self.message = {}
        self.message[TransactionState.IDLE] = "取引可能"
        self.message[TransactionState.OK] = "取引成立"
        self.message[TransactionState.PIN_INCORRECT] = "暗証番号が合致しない"
        self.message[TransactionState.NAME_INCORRECT] = "存在しない口座"

    def onStartTransaction(self):
        if self.controller:
            self.controller.selectAccount(
                                        self.ids.owner_name.text, 
                                        self.ids.pin.text)
                        
    def onWithdraw(self):
        amount = int(self.ids.amount.text)
        self.controller.withdraw(amount)

    def onDeposit(self):
        amount = int(self.ids.amount.text)
        self.controller.deposit(amount)
        
    def show(self, name, balance, state):
        self.ac_name = name
        self.ac_balance = balance
        self.state = self.message[state]    
