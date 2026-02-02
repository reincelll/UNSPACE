import raylibpy as rl
from scenes.scene import Scene
import scenes as sc
from engine.text import text
from engine.assets import asset_path
from engine.color import get_primary

class LoadingScene(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.raylib_logo = rl.load_texture(asset_path("assets/icons/raylib_logo.png"))
        self.game_icon = rl.load_image(asset_path("assets/icon.png"))
        rl.image_format(self.game_icon, rl.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8)
        rl.set_window_icon(self.game_icon)

    def on_exit(self):
        rl.unload_texture(self.raylib_logo)
        return super().on_exit()

    def update(self, dt):
        if rl.get_time() > 1:
            self.manager.change(sc.MenuScene(self.manager))

    def draw(self):
        text("UNSPACE", rl.get_screen_width()/2 - (rl.measure_text("UNSPACE", 70) / 2), rl.get_screen_height()/2 - (70/2), 70, get_primary())
        text("LOADING...", rl.get_screen_width()/2 - (rl.measure_text("LOADING...", 20) / 2), rl.get_screen_height() - 45, 20, get_primary())

        rl.draw_texture_ex(self.raylib_logo, rl.Vector2(5, rl.get_screen_height() - (self.raylib_logo.height + 30)), 0, 1, rl.WHITE)
        rl.draw_rectangle(5, rl.get_screen_height() - 25, rl.get_screen_width() - 10, 20, get_primary())