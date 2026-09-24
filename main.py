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

        root = BoxLayout(orientation="vertical", padding=18, spacing=12)

        with root.canvas.before:
            Color(*BLACK)
            self.bg = RoundedRectangle(
                pos=root.pos,
                size=root.size,
                radius=[0]
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
        root.add_widget(logo)

        welcome = Label(
            text="Musique • Vidéos • Talents africains",
            font_size="18sp",
            color=WHITE,
            halign="center"
        )
        root.add_widget(welcome)

        video = BoxLayout(orientation="vertical", spacing=10)

        title = Label(
            text="[b]Bienvenue sur EDH Tlty♪♪♪[/b]",
            markup=True,
            font_size="24sp",
            color=WHITE
        )
        video.add_widget(title)

        message = Label(
            text="Découvre des vidéos, de la musique\n"
                 "et de nouveaux talents.",
            font_size="17sp",
            color=WHITE,
            halign="center"
        )
        video.add_widget(message)

        start = Button(
            text="COMMENCER",
            font_size="18sp",
            size_hint_y=None,
            height=55,
            background_normal="",
            background_color=PURPLE,
            color=WHITE
        )
        start.bind(on_press=self.open_discover)
        video.add_widget(start)

        root.add_widget(video)

        nav = BoxLayout(
            size_hint_y=None,
            height=65,
            spacing=6
        )

        buttons = [
            ("⌂\nAccueil", "home"),
            ("⌕\nDécouvrir", "discover"),
            ("+\nPublier", "publish"),
            ("♧\nInbox", "inbox"),
            ("●\nProfil", "profile"),
        ]

        for text, screen_name in buttons:
            button = Button(
                text=text,
                font_size="13sp",
                background_normal="",
                background_color=(0.08, 0.08, 0.08, 1),
                color=GOLD
            )
            button.bind(
                on_press=lambda instance, name=screen_name:
                self.change_screen(name)
            )
            nav.add_widget(button)

        root.add_widget(nav)

        self.add_widget(root)

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def change_screen(self, name):
        self.manager.current = name

    def open_discover(self, instance):
        self.manager.current = "discover"


class SimpleScreen(Screen):
    def __init__(self, title, text, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        with layout.canvas.before:
            Color(*BLACK)
            self.bg = RoundedRectangle(
                pos=layout.pos,
                size=layout.size
            )

        layout.bind(
            pos=lambda obj, value: setattr(self.bg, "pos", value),
            size=lambda obj, value: setattr(self.bg, "size", value)
        )

        layout.add_widget(
            Label(
                text=title,
                font_size="30sp",
                color=GOLD
            )
        )

        layout.add_widget(
            Label(
                text=text,
                font_size="18sp",
                color=WHITE,
                halign="center"
            )
        )

        back = Button(
            text="Retour à l'accueil",
            size_hint_y=None,
            height=55,
            background_normal="",
            background_color=PURPLE,
            color=WHITE
        )
        back.bind(
            on_press=lambda instance:
            setattr(self.manager, "current", "home")
        )

        layout.add_widget(back)
        self.add_widget(layout)


class EDHTltyApp(App):
    def build(self):
        manager = ScreenManager()

        manager.add_widget(
            MainScreen(name="home")
        )

        manager.add_widget(
            SimpleScreen(
                name="discover",
                title="Découvrir",
                text="Trouve des artistes,\n"
                     "des musiques et des vidéos populaires."
            )
        )

        manager.add_widget(
            SimpleScreen(
                name="publish",
                title="Publier",
                text="Ici, tu pourras publier\n"
                     "tes vidéos et tes créations."
            )
        )

        manager.add_widget(
            SimpleScreen(
                name="inbox",
                title="Inbox",
                text="Tes notifications,\n"
                     "messages et interactions."
            )
        )

        manager.add_widget(
            SimpleScreen(
                name="profile",
                title="Profil",
                text="Ton profil EDH Tlty♪♪♪\n"
                     "et tes publications."
            )
        )

        return manager


if __name__ == "__main__":
    EDHTltyApp().run()
