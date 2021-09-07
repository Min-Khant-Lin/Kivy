from kivy.app import App

from kivy.uix.button import Label

class KivyButton(App):

    def build(self):

        return Label(text="Hello Label", font_size='30')

KivyButton().run()