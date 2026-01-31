import raylibpy as rl

font = None

def load_font():
    global font
    font = rl.load_font("assets/fonts/ZalandoSans.ttf")

def text(string, x, y, size, color):
    global font
    if rl.is_font_valid(font):
        rl.draw_text_ex(font, string, rl.Vector2(x, y), size, 1, color)