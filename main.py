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

        button.bind(on_release=self.start_app)

        root.add_widget(logo)
        root.add_widget(welcome)
        root.add_widget(button)
        self.add_widget(root)

    def start_app(self, instance):
        self.manager.current = "home"

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        with root.canvas.before:
            Color(*BLACK)
            self.bg = RoundedRectangle(
                pos=root.pos,
                size=root.size,
                radius=[20]
            )

        root.bind(pos=self.update_bg, size=self.update_bg)

        title = Label(
            text="[b]BIENVENUE SUR EDH Tlty♪♪♪[/b]",
            markup=True,
            font_size="24sp",
            color=GOLD
        )

        message = Label(
            text="Ton espace commence ici !",
            font_size="18sp",
            color=WHITE
        )

        back_button = Button(
            text="RETOUR",
            font_size="18sp",
            background_normal="",
            background_color=PURPLE,
            color=WHITE,
            size_hint_y=None,
            height=60
        )

        back_button.bind(
            on_release=lambda instance: setattr(
                self.manager, "current", "main"
            )
        )

        root.add_widget(title)
        root.add_widget(message)
        root.add_widget(back_button)
        self.add_widget(root)

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size


class EDHTltyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    EDHTltyApp().run()
