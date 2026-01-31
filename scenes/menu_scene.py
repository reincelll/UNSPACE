import raylibpy as rl
from scenes.scene import Scene
from engine.text import text
from engine.button import button, buttons

class MenuScene(Scene):
    def __init__(self, manager):
        self.manager = manager

    def on_enter(self):
        rl.set_target_fps(rl.get_monitor_refresh_rate(rl.get_current_monitor()))
        self.btn_play = button("PLAY", 20, 60, 140, 60)
        self.btn_settings = button("SETTINGS", 20, 130, 140, 30)
        return super().on_enter()
    
    def on_exit(self):
        for btn in buttons:
            del btn
        return super().on_exit()

    def update(self, dt):
        self.btn_play.width = rl.get_screen_width() - (self.btn_play.x * 2)
        self.btn_settings.width = rl.get_screen_width() - (self.btn_settings.x * 2)

    def draw(self):
        rl.draw_rectangle_lines(10, 10, rl.get_screen_width() - 20, rl.get_screen_height() - 20, rl.RED)
        text("UNSPACE", 20, 20, 30, rl.RED)
        self.btn_play.draw()
        self.btn_settings.draw()