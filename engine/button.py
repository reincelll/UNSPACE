import raylibpy as rl
from engine.text import text
from engine.color import get_primary
from engine.assets import asset_path

buttons = []

def button_update():
    mouse_pos = rl.get_mouse_position()
    global buttons
    global click_sfx
    for btn in buttons:
        btn.selected =  mouse_pos.x > btn.x and mouse_pos.y > btn.y and mouse_pos.x < btn.x + btn.width and mouse_pos.y < btn.y + btn.height

click_sfx = None

def load_btn_assets():
    global click_sfx
    if not click_sfx:
        click_sfx = rl.load_sound(asset_path("assets/audio/sound effects/click.mp3"))
        rl.set_sound_volume(click_sfx, 0.1)

class button:
    def __init__(self, text, x, y, width, height, on_click=None, text_size=0, color=get_primary(), text_offset=rl.Vector2(0, 0)):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        self.on_click = on_click
        self.clicked = False
        self.text_size = text_size
        self.color = color
        self.text_offset = text_offset
        self.disabled = False

        global buttons
        buttons.append(self)

    def draw(self):
        global click_sfx
        if not self.disabled:
            color = self.color
            bg_color = self.color
        else:
            color = rl.Color(self.color.r / 2, self.color.g / 2, self.color.b / 2, 255)
            bg_color = rl.Color(self.color.r / 2, self.color.g / 2, self.color.b / 2, 255)
        if self.text_size:
            text_size = self.text_size
        else:
            text_size = self.height - 10
        offset = 0
        if self.selected and not self.disabled:
            color = rl.BLACK
            if rl.is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
                offset = 2
            else:
                offset = 5
            rl.draw_rectangle(self.x, self.y, self.width, self.height, bg_color)
            if rl.is_mouse_button_released(rl.MOUSE_BUTTON_LEFT):
                if not self.clicked:
                    self.clicked = True
                    if self.on_click:
                        self.on_click()
            else:
                self.clicked = False
        else:
            self.clicked = False
        if rl.is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT) and self.selected and not self.disabled:
            rl.play_sound(click_sfx)
        rl.draw_rectangle_lines_ex(rl.Rectangle(self.x - offset, self.y - offset, self.width + (offset * 2), self.height + (offset * 2)), 2, color)
        text(self.text, (self.x + (self.width / 2) - (rl.measure_text(self.text, text_size) / 2)) + self.text_offset.x, ((self.y + (self.height / 2) - (text_size / 2)) - offset) + self.text_offset.y, text_size, color)

class slider:
    def __init__(self, x, y, width, height, min_value=0, max_value=100, initial_value=50, on_change=None, color=get_primary()):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.on_change = on_change
        self.color = color
        self.handle_width = 10
        self.dragging = False
        self.disabled = False

    def draw(self):
        rl.draw_rectangle(self.x, self.y + self.height // 2 - 2, self.width, 4, self.color)
        handle_x = self.x + int((self.value - self.min_value) / (self.max_value - self.min_value) * (self.width - self.handle_width))
        handle_y = self.y
        rl.draw_rectangle(handle_x, handle_y, self.handle_width, self.height, self.color)

        mouse_x, mouse_y = rl.get_mouse_x(), rl.get_mouse_y()
        if rl.is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
            if (self.x <= mouse_x <= self.x + self.width and
                self.y <= mouse_y <= self.y + self.height) or self.dragging:
                self.dragging = True
                relative_x = max(self.x, min(mouse_x - self.handle_width // 2, self.x + self.width - self.handle_width))
                self.value = self.min_value + (relative_x - self.x) / (self.width - self.handle_width) * (self.max_value - self.min_value)
                if self.on_change:
                    self.on_change(self.value)
        else:
            self.dragging = False

def del_buttons():
    buttons.clear()