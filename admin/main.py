from typing import Container
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class Root(BoxLayout):
    container = ObjectProperty(None)

class adminWindow(App):
    def build(self):
        self.root = Builder.load_file('kv/root.kv')
    
    def nextScreen(self, screen):
        filename = screen + '.kv'
        Builder.unload_file('kv/'+ filename)
        self.root.container.clear_widgets()
        screen = Builder.load_file('kv/'+ filename)
        self.root.container.add_widget(screen)

if __name__ == '__main__':
    adminWindow().run()