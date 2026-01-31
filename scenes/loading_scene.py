import raylibpy as rl
from scenes.scene import Scene
from scenes.menu_scene import MenuScene
from engine.text import text

class LoadingScene(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.raylib_logo = rl.load_texture("assets/icons/raylib_logo.png")

    def on_exit(self):
        rl.unload_texture(self.raylib_logo)
        return super().on_exit()

    def update(self, dt):
        if rl.get_time() > 1:
            self.manager.change(MenuScene(self.manager))

    def draw(self):
        text("UNSPACE", rl.get_screen_width()/2 - (rl.measure_text("UNSPACE", 70) / 2), rl.get_screen_height()/2 - (70/2), 70, rl.RED)
        text("LOADING...", rl.get_screen_width()/2 - (rl.measure_text("LOADING...", 20) / 2), rl.get_screen_height() - 45, 20, rl.RED)

        rl.draw_texture_ex(self.raylib_logo, rl.Vector2(5, rl.get_screen_height() - (self.raylib_logo.height + 30)), 0, 1, rl.WHITE)
        rl.draw_rectangle(5, rl.get_screen_height() - 25, rl.get_screen_width() - 10, 20, rl.RED)