from engine.button import del_buttons

loaded_scenes = []

class SceneManager:
    def __init__(self):
        self.current = None

    def change(self, scene):
        if self.current:
            self.current.on_exit()
            print(f"unloading {self.current}...")
            loaded_scenes.remove(self.current)
            del self.current
        del_buttons()
        self.current = scene
        self.current.on_enter()
        print(f"loading {self.current}...")
        loaded_scenes.append(self.current)

    def update(self, dt):
        if self.current:
            self.current.update(dt)

    def draw(self):
        if self.current:
            self.current.draw()
        
    def get_scenes(self):
        print(loaded_scenes)