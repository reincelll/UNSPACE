import raylibpy as rl
import scenes as s
import engine as e

class SettingsScene(s.Scene):
    def __init__(self, manager):
        self.manager = manager
        self.settings = e.load_settings()

    def on_enter(self):
        self.bl_fullscreen = self.settings["fullscreen"]
        self.btn_back = e.button("BACK", 20, 370, 280, 30, on_click=self.on_back_clicked)
        self.btn_apply = e.button("APPLY", 20, 370, 280, 30, on_click=self.on_apply_clicked)
        self.btn_fullscreen = e.button("FULLSCREEN", 20, 190, 300, 300, on_click=self.toggle_fullscreen, text_size=20, text_offset=rl.Vector2(0, 133))
        if rl.get_screen_width() == rl.get_monitor_width(rl.get_current_monitor()) and rl.get_screen_height() == rl.get_monitor_height(rl.get_current_monitor()):
            self.bl_fullscreen = True
        if not self.bl_fullscreen:
            self.btn_fullscreen.text = "WINDOWED"
        self.sldr_fps = e.slider(122, 525, 130, 30, 0, 360, self.settings.get("max_fps", 60))

        self.img_fullscreenhint = rl.load_texture(e.asset_path("assets/images/settingsfullscreenhint.png"))
        self.img_windowedhint = rl.load_texture(e.asset_path("assets/images/settingswindowedhint.png"))

        return super().on_enter()
    
    def toggle_fullscreen(self):
        if not self.bl_fullscreen:
            self.bl_fullscreen = True
            self.btn_fullscreen.text = "FULLSCREEN"
        else:
            self.bl_fullscreen = False
            self.btn_fullscreen.text = "WINDOWED"
        self.settings["fullscreen"] = self.bl_fullscreen
    
    def on_back_clicked(self):
        self.manager.change(s.MenuScene(self.manager))

    def on_apply_clicked(self):
        e.save_settings(self.settings)
        rl.set_target_fps(self.settings["max_fps"])
        if rl.get_screen_width() == rl.get_monitor_width(rl.get_current_monitor()) and rl.get_screen_height() == rl.get_monitor_height(rl.get_current_monitor()):
            if self.btn_fullscreen.text == "WINDOWED":
                rl.toggle_borderless_windowed()
        else:
            if self.btn_fullscreen.text == "FULLSCREEN":
                rl.toggle_borderless_windowed()
    
    def on_exit(self):
        rl.unload_texture(self.img_fullscreenhint)
        rl.unload_texture(self.img_windowedhint)
        return super().on_exit()

    def update(self, dt):
        self.btn_back.y = rl.get_screen_height() - (self.btn_back.height + 20)
        self.btn_back.y = max(self.btn_back.y, 300)
        self.btn_apply.y = self.btn_back.y
        self.btn_apply.x = self.btn_back.x + self.btn_back.width + 10
        self.btn_apply.width = rl.get_screen_width() - (self.btn_back.x + self.btn_back.width) - 30
        self.sldr_fps.width = rl.get_screen_width() - (self.sldr_fps.x + 20)

        self.btn_fullscreen.width = 486
        self.btn_fullscreen.x = (rl.get_screen_width() / 2) - (self.btn_fullscreen.width / 2)

        if rl.is_key_pressed(rl.KEY_ESCAPE):
            self.btn_back.on_click()
        if rl.is_key_pressed(rl.KEY_ENTER) and not self.btn_apply.disabled:
            self.btn_apply.on_click()
        if rl.is_key_pressed(rl.KEY_F11):
            self.toggle_fullscreen()

    def draw(self):
        rl.draw_rectangle_lines(10, 10, rl.get_screen_width() - 20, rl.get_screen_height() - 20, e.get_primary())
        rl.draw_rectangle(rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 15, 30, rl.measure_text("UNSPACE", 80) + 30, 60, e.get_primary())
        rl.draw_rectangle(rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 15, 100, rl.measure_text("UNSPACE", 80) + 30, 30, e.get_primary())
        e.text("UNSPACE", rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 13, 20, 80, rl.BLACK)
        e.text("SETTINGS", rl.get_screen_width() / 2 - (rl.measure_text("SETTINGS", 30) / 2) - 13, 100, 30, rl.BLACK)
        self.btn_back.draw()
        self.btn_apply.draw()
        self.btn_fullscreen.draw()
        self.sldr_fps.draw()
        if self.btn_fullscreen.text == "FULLSCREEN":
            rl.draw_texture_ex(self.img_fullscreenhint, rl.Vector2((rl.get_screen_width() / 2) - (self.img_fullscreenhint.width / 2), 200), 0, 1, rl.WHITE)
        else:
            rl.draw_texture_ex(self.img_windowedhint, rl.Vector2((rl.get_screen_width() / 2) - (self.img_windowedhint.width / 2), 200), 0, 1, rl.WHITE)
        e.text(f"FPS: {round(self.sldr_fps.value / 10) * 10}", 20, 530, 20, e.get_primary())

        if not self.sldr_fps.dragging and not self.settings["max_fps"] == round(self.sldr_fps.value / 10) * 10:
            self.sldr_fps.value = round(self.sldr_fps.value / 10) * 10
            self.update_fps()

    def update_fps(self):
        self.settings["max_fps"] = round(self.sldr_fps.value / 10) * 10