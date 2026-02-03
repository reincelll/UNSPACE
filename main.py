import raylibpy as rl

import scenes as s
import engine as e

import tkinter as tk
from tkinter import messagebox
import sys
import ctypes
import traceback

root = tk.Tk()
root.withdraw()

if "--console" in sys.argv:
    ctypes.windll.kernel32.AllocConsole()
    sys.stdout = open("CONOUT$", "w")
    sys.stderr = open("CONOUT$", "w")
    sys.stdin  = open("CONIN$", "r")

info = {
    "version": "0.1.2",
    "build_notes": "2/2/26; 9:53PM"
}

click_sfx = None

def draw_debug(text, x, y):
    rl.draw_rectangle(x, y, rl.measure_text(text, 12) + 6, 15, rl.Color(255, 255, 255, 172))
    rl.draw_text(text, x + 2, y + 2, 12, rl.BLACK)

def main():
    rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
    rl.init_window(1080, 740, "UNSPACE")
    rl.set_target_fps(30)
    rl.set_exit_key(rl.KEY_NULL)
    rl.hide_cursor()
    rl.init_audio_device()
    rl.set_window_min_size(640, 480)

    e.load_btn_assets()

    settings = e.load_settings()
    
    if settings["fullscreen"]:
        rl.toggle_borderless_windowed()

    e.load_font()

    debug = False

    cursor_image = rl.load_texture(e.asset_path("assets/cursor.png"))
    cursor_color = e.get_primary()

    scene_manager = e.SceneManager()
    scene_manager.change(s.LoadingScene(scene_manager))

    while not rl.window_should_close():
        settings = e.load_settings()
        dt = rl.get_frame_time()

        e.button_update()

        scene_manager.update(dt)

        if rl.is_key_pressed(rl.KEY_F11):
            rl.toggle_borderless_windowed()
            if rl.get_screen_width() == rl.get_monitor_width(rl.get_current_monitor()) and rl.get_screen_height() == rl.get_monitor_height(rl.get_current_monitor()):
                bl_fullscreen = True
            else:
                bl_fullscreen = False
            settings["fullscreen"] = bl_fullscreen
            s.save_settings(settings)
        if rl.is_key_pressed(rl.KEY_F10):
            debug = not debug

        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        scene_manager.draw()
        if debug:
            draw_debug(f"Frames Per Second: {str(round(rl.get_fps()))}", 3, 3)
            draw_debug(f"Delta Time: {str(round(rl.get_frame_time(), 8))}", 3, 18)
            draw_debug(str(e.loaded_scenes), 3, 33)
            draw_debug(info["version"], 3, 48)
            if getattr(sys, 'frozen', False):
                draw_debug("Compiled/Build", 3, 63)
            else:
                draw_debug("Python/File", 3, 63)
            draw_debug(str(e.buttons), 3, 78)
            draw_debug(info["build_notes"], 3, 93)

        cursor_color = rl.WHITE
        for btn in e.buttons:
            if btn.selected and not btn.disabled:
                cursor_color = e.get_primary()
        if rl.is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            cursor_color = e.get_primary()

        rl.draw_texture_ex(cursor_image, rl.Vector2(rl.get_mouse_x() - 2, rl.get_mouse_y() - 2), 0, 0.5, cursor_color)

        rl.end_drawing()

    rl.rlgl_close()
    rl.close_audio_device()
    rl.close_window()

try:
    main()
    rl.close_audio_device()
    rl.close_window()
except Exception as e:
    exc_type, exc_value, exc_tb = sys.exc_info()

    tb = traceback.extract_tb(exc_tb)
    last = tb[-1] if tb else None

    error_details = f"""
    UNSPACE Engine crashed 💥

    Exception Type:
    {exc_type.__name__}

    Message:
    {e}

    File:
    {last.filename if last else 'Unknown'}

    Line:
    {last.lineno if last else 'Unknown'}

    Function:
    {last.name if last else 'Unknown'}

    ------------------------------
    Full Traceback:
    {''.join(traceback.format_exception(exc_type, exc_value, exc_tb))}
    """

    if not last.name == "close_window":
        messagebox.showerror("UNSPACE Engine Error!", error_details)
    rl.rlgl_close()
    rl.close_audio_device()
    rl.close_window()

root.mainloop()