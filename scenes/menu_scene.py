import raylibpy as rl
import scenes as s
import engine as e

menu_loop_song = None

class MenuScene(s.Scene):
    def __init__(self, manager):
        self.manager = manager
        self.settings = e.load_settings()

        global menu_loop_song
        if not menu_loop_song:
            menu_loop_song = rl.load_sound(e.asset_path("assets/audio/music/menu_loop.mp3"))

    def on_enter(self):
        rl.set_target_fps(self.settings.get("max_fps", 60))
        self.btn_play = e.button("PLAY", 20, 260, 140, 60, on_click=self.on_play_clicked)
        self.btn_settings = e.button("SETTINGS", 20, 330, 140, 45, on_click=self.on_settings_clicked)
        self.btn_help = e.button("HELP", 20, 370, 140, 30, on_click=self.on_help_clicked)

        self.btn_quit = e.button("QUIT TO DESKTOP", 20, 370, 140, 30, on_click=self.on_quit_clicked)
        return super().on_enter()
    
    def on_exit(self):
        return super().on_exit()

    def on_play_clicked(self):
        self.manager.change(s.SaveManager(self.manager))

    def on_settings_clicked(self):
        self.manager.change(s.SettingsScene(self.manager))

    def on_help_clicked(self):
        pass

    def on_quit_clicked(self):
        rl.close_window()
        rl.rlgl_close()

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

        if rl.is_audio_device_ready() and rl.is_sound_valid(menu_loop_song):
            if not rl.is_sound_playing(menu_loop_song):
                menu_loop_song.play()

    def draw(self):
        rl.draw_rectangle_lines(10, 10, rl.get_screen_width() - 20, rl.get_screen_height() - 20, e.get_primary())
        rl.draw_rectangle(rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 15, 30, rl.measure_text("UNSPACE", 80) + 30, 60, e.get_primary())
        e.text("UNSPACE", rl.get_screen_width() / 2 - (rl.measure_text("UNSPACE", 80) / 2) - 13, 20, 80, rl.BLACK)
        self.btn_play.draw()
        self.btn_settings.draw()
        self.btn_help.draw()
        self.btn_quit.draw()