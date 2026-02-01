import raylibpy as rl
from engine.text import text
from engine.color import get_primary

buttons = []

def button_update():
    global buttons
    if not rl.get_mouse_delta() == rl.Vector2(0, 0):
        mouse_pos = rl.get_mouse_position()
        for btn in buttons:
            if mouse_pos.x > btn.x and mouse_pos.y > btn.y and mouse_pos.x < btn.x + btn.width and mouse_pos.y < btn.y + btn.height:
                btn.selected = True
            else:
                btn.selected = False

class button:
    def __init__(self, text, x, y, width, height, on_click=None, text_size=0, color=get_primary()):
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
        global buttons
        buttons.append(self)

    def draw(self):
        if self.color:
            color = self.color
            bg_color = self.color
        else:
            color = get_primary()
            bg_color = get_primary()
        if self.text_size:
            text_size = self.text_size
        else:
            text_size = self.height - 10
        offset = 0
        if self.selected:
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
        rl.draw_rectangle_lines_ex(rl.Rectangle(self.x - offset, self.y - offset, self.width + (offset * 2), self.height + (offset * 2)), 2, color)
        text(self.text, self.x + (self.width / 2) - (rl.measure_text(self.text, text_size) / 2), (self.y + (self.height / 2) - (text_size / 2)) - offset, text_size, color)

def del_buttons():
    buttons.clear()