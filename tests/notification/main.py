from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import os
from plyer import notification

kv_path = os.path.join(os.path.dirname(__file__), 'main.kv')
# print(kv_path)
# exit()
kv = Builder.load_file(kv_path)

class MyLayout(Widget):
    def press(self):
        notification.notify(
            title="Hello",
            message="100m od Ciebie jest Piękny Domek"
        )

class myApp(App):
    def build(self):
        return MyLayout()

myApp().run()
