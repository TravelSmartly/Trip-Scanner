# Test for https://github.com/kivymd/KivyMD/issues/1435:
#
# Test task:
#
# - check the size of the custom font that was installed in the Python code;

from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class TestFontSizeInPythonCode(MDApp):
    def check_font_size(self, *args):
        assert self.root.ids.label.font_size == 24.0
        self.stop()

    def build(self):
        return MDBoxLayout(
            MDLabel(
                id="label",
                text="MDLabel",
                font_style="H5",
            ),
        )

    def on_start(self):
        Clock.schedule_once(self.check_font_size, 1.2)


TestFontSizeInPythonCode().run()
