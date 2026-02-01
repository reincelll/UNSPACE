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
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        global buttons
        buttons.append(self)

    def draw(self):
        color = rl.RED
        offset = 0
        if self.selected:
            color = rl.WHITE
            rl.draw_rectangle_gradient_h(self.x - offset, self.y - offset, self.width + (offset * 2), self.height + (offset * 2), rl.Color(240, 41, 55, 172), rl.Color(240, 41, 55, 0))
            if rl.is_mouse_button_down(rl.MOUSE_BUTTON_LEFT):
                offset = 2
            else:
                offset = 5
        else:
            rl.draw_rectangle_gradient_h(self.x - offset, self.y - offset, self.width / 4 + (offset * 2), self.height + (offset * 2), rl.Color(240, 41, 55, 60), rl.Color(240, 41, 55, 0))
        rl.draw_rectangle_lines_ex(rl.Rectangle(self.x - offset, self.y - offset, self.width + (offset * 2), self.height + (offset * 2)), 2, color)
        text(self.text, self.x + 10 + offset, self.y + 5, (self.height - 10), color)