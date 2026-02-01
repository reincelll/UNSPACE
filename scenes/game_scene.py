import raylibpy as rl
from scenes.scene import Scene
from engine.text import text

class GameScene(Scene):
    def __init__(self, manager):
        self.manager = manager

    def on_exit(self):
        return super().on_exit()

    def update(self, dt):
        return super().update(dt)

    def draw(self):
        text("UNSPACE", rl.get_screen_width()/2 - (rl.measure_text("UNSPACE", 70) / 2), rl.get_screen_height()/2 - (70/2), 70, rl.RED)