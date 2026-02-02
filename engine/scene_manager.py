from engine.button import del_buttons

loaded_scenes = []

class SceneManager:
    def __init__(self):
        self.current = None

    def change(self, scene):
        scene_to_unload = None
        if self.current:
            scene_to_unload = self.current
            print(f"unloading {self.current}...")
        del_buttons()
        self.current = scene
        self.current.on_enter()
        self.current.draw()
        print(f"loading {self.current}...")
        loaded_scenes.append(self.current)
        if scene_to_unload:
            scene_to_unload.on_exit()
            loaded_scenes.remove(scene_to_unload)

    def update(self, dt):
        if self.current:
            self.current.update(dt)

    def draw(self):
        if self.current:
            self.current.draw()
        
    def get_scenes(self):
        print(loaded_scenes)