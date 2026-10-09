import os
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle

GOLD = (1, 0.84, 0, 1)
WHITE = (1, 1, 1, 1)
BLACK = (0.035, 0.035, 0.035, 1)
PURPLE = (0.25, 0.12, 0.38, 1)

class EDHTltyApp(App):
    def build(self):
        Window.clearcolor = BLACK
        Window.fullscreen = 'auto'
        root = BoxLayout(orientation='vertical', padding=8, spacing=8)
        with root.canvas.before:
            Color(*BLACK)
            self.bg = Rectangle(pos=root.pos, size=root.size)
        root.bind(pos=self.update_bg, size=self.update_bg)
        header = Label(text='[b]EDH Tlty♪♪♪[/b]', markup=True, color=GOLD, font_size='26sp', size_hint_y=None, height=52)
        root.add_widget(header)
        self.status = Label(text='Bienvenue ! Prépare-toi à regarder des vidéos.', color=WHITE, font_size='15sp', size_hint_y=None, height=44)
        root.add_widget(self.status)
        self.player = None
        self.files = []
        self.index = 0
        folder = os.path.join(os.path.dirname(__file__), 'videos')
        if os.path.isdir(folder):
            self.files = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.lower().endswith(('.mp4', '.m4v', '.3gp'))]
        self.area = BoxLayout()
        root.add_widget(self.area)
        controls = BoxLayout(size_hint_y=None, height=58, spacing=8)
        self.play_button = Button(text='▶ LIRE', background_normal='', background_color=PURPLE, color=WHITE)
        self.play_button.bind(on_release=self.toggle_play)
        next_button = Button(text='VIDÉO SUIVANTE', background_normal='', background_color=(0.55, 0.40, 0.02, 1), color=WHITE)
        next_button.bind(on_release=self.next_video)
        controls.add_widget(self.play_button)
        controls.add_widget(next_button)
        root.add_widget(controls)
        if self.files:
            self.load_video()
        else:
            self.show_message('Aucune vidéo pour le moment.\nAjoute un fichier MP4 dans le dossier videos.')
        return root

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def show_message(self, message):
        self.area.clear_widgets()
        self.status.text = message
        self.player = None
        self.play_button.text = '▶ LIRE'

    def load_video(self):
        if not self.files:
            return
        self.area.clear_widgets()
        path = self.files[self.index]
        try:
            self.player = Video(source=path, state='play', options={'eos': 'loop'}, allow_stretch=True, keep_ratio=False)
            self.area.add_widget(self.player)
            self.status.text = 'Vidéo ' + str(self.index + 1) + ' / ' + str(len(self.files))
            self.play_button.text = '❚❚ PAUSE'
        except Exception:
            self.show_message('Impossible de charger cette vidéo.')

    def toggle_play(self, instance):
        if not self.player:
            self.status.text = 'Ajoute une vidéo MP4 dans le dossier videos.'
            return
        if self.player.state == 'play':
            self.player.state = 'pause'
            self.play_button.text = '▶ LIRE'
        else:
            self.player.state = 'play'
            self.play_button.text = '❚❚ PAUSE'

    def next_video(self, instance):
        if not self.files:
            self.status.text = 'Aucune vidéo disponible pour le moment.'
            return
        self.index = (self.index + 1) % len(self.files)
        self.load_video()

if __name__ == '__main__':
    EDHTltyApp().run()
