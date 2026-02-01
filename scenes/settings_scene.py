import raylibpy as rl
from scenes.scene import Scene
from engine.text import text
from engine.button import button, buttons
from engine.color import get_primary, set_primary
import scenes as sc

class SettingsScene(Scene):
    def __init__(self, manager):
        self.manager = manager

    def on_enter(self):
        self.btn_back = button("BACK TO MENU", 20, 370, 240, 30, on_click=self.on_back_clicked)
        self.btn_fullscreen = button("FULLSCREEN", 20, 200, 300, 60, on_click=rl.toggle_borderless_windowed, text_size=20)
        return super().on_enter()
    
    def on_back_clicked(self):
        self.manager.change(sc.MenuScene(self.manager))
    
    def on_exit(self):
        return super().on_exit()

    def update(self, dt):
        self.btn_back.y = rl.get_screen_height() - (self.btn_back.height + 20)
        self.btn_back.y = max(self.btn_back.y, 300)

        for btn in buttons:
            if not btn == self.btn_back:
                btn.width = rl.get_screen_width() - (btn.x * 2)

    def draw(self):
        rl.draw_rectangle_lines(10, 10, rl.get_screen_width() - 20, rl.get_screen_height() - 20, get_primary())
        rl.draw_rectangle(rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 15, 30, rl.measure_text("UNSPACE", 80) + 30, 60, get_primary())
        rl.draw_rectangle(rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 15, 100, rl.measure_text("UNSPACE", 80) + 30, 30, get_primary())
        text("UNSPACE", rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 13, 20, 80, rl.BLACK)
        text("SETTINGS", rl.get_screen_width() / 2 - (rl.measure_text("SETTINGS", 30) / 2) - 13, 100, 30, rl.BLACK)
        self.btn_back.draw()
        self.btn_fullscreen.draw()