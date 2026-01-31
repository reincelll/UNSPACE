class SceneManager:
    def __init__(self):
        self.current = None

    def change(self, scene):
        if self.current:
            self.current.on_exit()
        self.current = scene
        self.current.on_enter()

    def update(self, dt):
        if self.current:
            self.current.update(dt)

    def draw(self):
        if self.current:
            self.current.draw()
