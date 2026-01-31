import raylibpy as rl
from engine.scene_manager import SceneManager
from scenes import *
from engine.text import load_font
from engine.button import button_update, buttons
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

def main():
    rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
    rl.init_window(1080, 740, "UNSPACE")
    rl.set_target_fps(30)
    rl.set_exit_key(rl.KEY_NULL)
    rl.hide_cursor()

    load_font()

    debug = True

    cursor_image = rl.load_texture("assets/cursor.png")
    cursor_color = rl.RED

    scene_manager = SceneManager()
    scene_manager.change(LoadingScene(scene_manager))

    while not rl.window_should_close():
        dt = rl.get_frame_time()
        dpi = 1.0 / min(rl.get_screen_width() / 1080, rl.get_screen_height() / 720)
        dpi = rl.clamp(dpi, 0.75, 1.5)

        button_update()

        scene_manager.update(dt)

        if rl.is_key_pressed(rl.KEY_F11):
            rl.toggle_borderless_windowed()

        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        scene_manager.draw()
        if debug:
            rl.draw_rectangle(3, 3, rl.measure_text(str(round(rl.get_fps())), 12) + 3, 15, rl.Color(0, 0, 0, 172))
            rl.draw_text(str(round(rl.get_fps())), 5, 5, 12, rl.WHITE)

        cursor_color = rl.RED
        for btn in buttons:
            if btn.selected:
                cursor_color = rl.WHITE

        rl.draw_texture_ex(cursor_image, rl.Vector2(rl.get_mouse_x() - 2, rl.get_mouse_y() - 2), 0, dpi * 2, cursor_color)

        rl.end_drawing()

    rl.close_window()
    rl.rlgl_close()

try:
    main()
    rl.close_window()
except Exception as e:
    messagebox.showerror(
        "Error",
        f"{type(e).__name__}\n{e}"
    )
    rl.close_window()
    rl.rlgl_close()

root.mainloop()