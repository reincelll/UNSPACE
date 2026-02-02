import raylibpy as rl
import scenes as sc
from engine.text import text
from engine.button import button
from engine.color import get_primary

class SaveManager(sc.Scene):
    def __init__(self, manager):
        self.manager = manager

    def on_enter(self):
        self.btn_back = button("BACK", 20, 370, 280, 30, on_click=self.on_back_clicked)
        return super().on_enter()

    def on_exit(self):
        return super().on_exit()
    
    def on_back_clicked(self):
        self.manager.change(sc.MenuScene(self.manager))

    def update(self, dt):
        self.btn_back.y = rl.get_screen_height() - (self.btn_back.height + 20)
        self.btn_back.y = max(self.btn_back.y, 300)
        self.btn_back.width = rl.get_screen_width() - (self.btn_back.x * 2)
        return super().update(dt)

    def draw(self):
        self.btn_back.draw()
        rl.draw_rectangle_lines(10, 10, rl.get_screen_width() - 20, rl.get_screen_height() - 20, get_primary())