import raylibpy as rl
from scenes.scene import Scene
from engine.text import text
from engine.button import button, slider, buttons
from engine.assets import asset_path
from engine.color import get_primary
import scenes as sc
import engine.settings as s

class SettingsScene(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.settings = s.load_settings()

    def on_enter(self):
        self.btn_back = button("BACK TO MENU", 20, 370, 240, 30, on_click=self.on_back_clicked)
        self.btn_fullscreen = button("FULLSCREEN", 20, 200, 300, 60, on_click=self.toggle_fullscreen, text_size=20)
        self.sldr_fps = slider(20, 300, 130, 30, 30, 360, self.settings.get("max_fps", 60))
        return super().on_enter()
    
    def toggle_fullscreen(self):
        rl.toggle_borderless_windowed()
        self.settings["fullscreen"] = rl.is_window_fullscreen()
        s.save_settings(self.settings)
    
    def on_back_clicked(self):
        s.save_settings(self.settings)
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
        text(f"FPS: {round(self.sldr_fps.value / 10) * 10}", 20, 280, 20, get_primary())
        self.sldr_fps.draw()

        if not self.sldr_fps.dragging and not self.settings["max_fps"] == round(self.sldr_fps.value / 10) * 10:
            self.sldr_fps.value = round(self.sldr_fps.value / 10) * 10
            self.update_fps()

    def update_fps(self):
        rl.set_target_fps(round(self.sldr_fps.value / 10) * 10)
        self.settings["max_fps"] = round(self.sldr_fps.value / 10) * 10
        s.save_settings(self.settings)