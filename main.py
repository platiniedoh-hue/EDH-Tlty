from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, RoundedRectangle


GOLD = (1, 0.84, 0, 1)
WHITE = (1, 1, 1, 1)
BLACK = (0.04, 0.04, 0.04, 1)
PURPLE = (0.35, 0.12, 0.55, 1)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=18,
            spacing=12
        )

        with root.canvas.before:
            Color(*BLACK)
            self.bg = RoundedRectangle(
                pos=root.pos,
                size=root.size,
                radius=[20]
            )

        root.bind(pos=self.update_bg, size=self.update_bg)

        logo = Label(
            text="[b]EDH Tlty♪♪♪[/b]",
            markup=True,
            font_size="30sp",
            color=GOLD,
            size_hint_y=None,
            height=70
        )

        welcome = Label(
            text="EDH Tlty♪♪♪ — VERSION TEST 2026",
            font_size="20sp",
            color=WHITE
        )

        button = Button(
            text="COMMENCER",
            font_size="18sp",
            background_normal="",
            background_color=PURPLE,
            color=WHITE,
            size_hint_y=None,
            height=60
        )

        root.add_widget(logo)
        root.add_widget(welcome)
        root.add_widget(button)

        self.add_widget(root)

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size


class EDHTltyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        return sm


if __name__ == "__main__":
    EDHTltyApp().run()
