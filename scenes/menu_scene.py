import raylibpy as rl
from scenes.scene import Scene
from engine.text import text
from engine.button import button, buttons

class MenuScene(Scene):
    def __init__(self, manager):
        self.manager = manager

    def on_enter(self):
        rl.set_target_fps(rl.get_monitor_refresh_rate(rl.get_current_monitor()))
        self.btn_play = button("PLAY", 20, 260,140, 60)
        self.btn_settings = button("SETTINGS", 20, 330, 140, 45)
        self.btn_help = button("HELP", 20, 370, 140, 30)
        self.btn_quit = button("QUIT", 20, 370, 140, 30)
        return super().on_enter()
    
    def on_exit(self):
        for btn in buttons:
            del btn
        return super().on_exit()

    def update(self, dt):
        self.btn_play.width = rl.get_screen_width() - (self.btn_play.x * 2)
        self.btn_settings.width = rl.get_screen_width() - (self.btn_settings.x * 2)
        self.btn_help.width = (rl.get_screen_width() / 2) - 25
        self.btn_quit.x = (rl.get_screen_width() / 2) + 5
        self.btn_quit.width = (rl.get_screen_width() / 2) - 25

        self.btn_quit.y = rl.get_screen_height() - (self.btn_quit.height + 20)
        self.btn_quit.y = max(self.btn_quit.y, 300)
        self.btn_help.y = self.btn_quit.y
        self.btn_settings.y = self.btn_help.y - (self.btn_settings.height + 10)
        self.btn_play.y = self.btn_settings.y - (self.btn_play.height + 10)

    def draw(self):
        rl.draw_rectangle_lines(10, 10, rl.get_screen_width() - 20, rl.get_screen_height() - 20, rl.RED)
        text("UNSPACE", rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2), 20, 80, rl.RED)
        self.btn_play.draw()
        self.btn_settings.draw()
        self.btn_help.draw()
        self.btn_quit.draw()