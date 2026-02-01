import raylibpy as rl
from engine.scene_manager import SceneManager, loaded_scenes
from scenes import *
from engine.text import load_font
from engine.button import button_update, buttons
import tkinter as tk
from tkinter import messagebox
from engine.assets import asset_path
import sys
from engine.color import get_primary

root = tk.Tk()
root.withdraw()

info = {
    "version": "0.0.0"
}

def draw_debug(text, x, y):
    rl.draw_rectangle(x, y, rl.measure_text(text, 12) + 6, 15, rl.Color(255, 255, 255, 172))
    rl.draw_text(text, x + 2, y + 2, 12, rl.BLACK)

def main():
    rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
    rl.init_window(1080, 740, "𝚄𝙽𝚂𝙿𝙰𝙲𝙴")
    rl.set_target_fps(30)
    rl.set_exit_key(rl.KEY_NULL)
    rl.hide_cursor()
    rl.set_window_min_size(640, 480)

    load_font()

    debug = False

    cursor_image = rl.load_texture(asset_path("assets/cursor.png"))
    cursor_color = get_primary()

    scene_manager = SceneManager()
    scene_manager.change(LoadingScene(scene_manager))

    while not rl.window_should_close():
        dt = rl.get_frame_time()

        button_update()

        scene_manager.update(dt)

        if rl.is_key_pressed(rl.KEY_F11):
            rl.toggle_borderless_windowed()
        if rl.is_key_pressed(rl.KEY_F10):
            debug = not debug

        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        scene_manager.draw()
        if debug:
            draw_debug(f"Frames Per Second: {str(round(rl.get_fps()))}", 3, 3)
            draw_debug(f"Delta Time: {str(round(rl.get_frame_time(), 8))}", 3, 18)
            draw_debug(str(loaded_scenes), 3, 33)
            draw_debug(info["version"], 3, 48)
            if getattr(sys, 'frozen', False):
                draw_debug("Compiled/Build", 3, 63)
            else:
                draw_debug("Python/File", 3, 63)
            draw_debug(str(buttons), 3, 78)

        cursor_color = rl.WHITE
        for btn in buttons:
            if btn.selected:
                cursor_color = get_primary()
        if rl.is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            cursor_color = get_primary()

        rl.draw_texture_ex(cursor_image, rl.Vector2(rl.get_mouse_x() - 2, rl.get_mouse_y() - 2), 0, 0.5, cursor_color)

        rl.end_drawing()

    rl.close_window()
    rl.rlgl_close()

try:
    main()
    rl.close_window()
except Exception as e:
    messagebox.showerror(
        "UNSPACE Engine Error!",
        f"{type(e).__name__}\n{e}"
    )
    rl.close_window()
    rl.rlgl_close()

root.mainloop()