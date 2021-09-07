from kivy.uix.button import Button
from kivy.app import App
from functools import partial

class KivyButton(App):
    def disable(self, instance, *args):
        instance.disabled = True

    def update(self, instance, *args):
        instance.text = 'I am Disabled!'
    
    def build(self):
        myBtn = Button(text='Click me to disable')
        myBtn.bind(on_press= partial(self.disable, myBtn))
        myBtn.bind(on_press= partial(self.update, myBtn))

        return myBtn

KivyButton().run()