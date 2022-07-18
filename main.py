from ast import Nonlocal, Str
from os import access
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty

import re

####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで

from widget import BankWidget
from view_controller import View, Controller
from model import Bank, Account


class BankApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Bank'

    def on_start(self):
        bank = self.makeDummyData()
        view = View(bank, self.root)
        controller = Controller(bank, view)
        self.root.controller = controller
        pass

    def makeDummyData(self):
        bank = Bank()

        bank.makeAccount("taro", 100, "0123")
        bank.makeAccount("jiro", 90000, "0000")
        return bank

if __name__ == '__main__':
    BankApp().run()