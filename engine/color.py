import raylibpy as rl
import json

with open("data/settings.json") as f:
    settings = json.load(f)

color_map = {
    "RED": rl.RED,
    "GREEN": rl.GREEN,
    "BLUE": rl.BLUE,
    "WHITE": rl.WHITE,
    "YELLOW": rl.YELLOW,
}

color_name = settings.get("primary_color", "WHITE")
primary_color = color_map.get(color_name.upper(), rl.WHITE)

def get_primary():
    return primary_color

def set_primary(color_name):
    global primary_color
    color_name = color_name.upper()
    
    if color_name in color_map:
        primary_color = color_map[color_name]
        settings["primary_color"] = color_name
        with open("data/settings.json", "w") as f:
            json.dump(settings, f, indent=4)
    else:
        raise ValueError(f"Color '{color_name}' is not in color_map")