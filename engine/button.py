import raylibpy as rl
from engine.text import text

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
    def __init__(self, text, x, y, width, height, on_click=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        self.on_click = on_click
        self.clicked = False
        global buttons
        buttons.append(self)

    def draw(self):
        color = rl.RED
        bg_color = rl.RED
        offset = 0
        if self.selected:
            color = rl.BLACK
            if rl.is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
                offset = 2
                bg_color = rl.Color(255, 71, 85, 255)
            else:
                offset = 5
                bg_color = rl.RED
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
        text(self.text, self.x + (self.width / 2) - (rl.measure_text(self.text, self.height - 10) / 2), self.y + 5, self.height - 10, color)