from pathlib import Path
import json

def get_settings_path():
    save_dir = Path.home() / ".unspace"
    save_dir.mkdir(exist_ok=True)
    return save_dir / "settings.json"

def load_settings():
    path = get_settings_path()
    if not path.exists():
        settings = {"max_fps": 60, "fullscreen": False}
        save_settings(settings)
    else:
        with open(path, "r") as f:
            settings = json.load(f)
    return settings

def save_settings(settings):
    path = get_settings_path()
    with open(path, "w") as f:
        json.dump(settings, f, indent=4)