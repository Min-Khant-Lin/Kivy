from typing import Text
from kivy.app import App
from kivy.uix.label import Label

class firstKivy(App):
    def build(self):
        return Label(text='Hello Kivy.')

firstKivy().run()