import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import json

class Rec:
    def __init__(self):
        self.count = 0
        self.coordinates = []

    def photo(self):
        x, y = pg.position()
        photo = pg.screenshot(region=(x - 6, y - 6, 12, 12))
        path = f'foto_new_{self.count}.png'
        photo.save(path)
        self.count = self.count + 1
        infos = {
            "path": path,
            "down": 0,
            "up": 0,
            "wait": 2
        }
        self.coordinates.append(infos)
        print("took a photo")
    
    def down_stair(self):
        last_coordinates = self.coordinates[-1]
        last_coordinates["down"] = 1

    def up_stair(self):
        last_coordinates = self.coordinates[-1]
        last_coordinates["up"] = 1

    def key_code(self, key):
        if key == keyboard.Key.esc:
            # antes de fechar, salvar as instruções
            with open('infos.json', 'w') as file:
                file.write(json.dumps(self.coordinates, indent=2))
            return False
        if key == keyboard.Key.insert:
            self.photo()
        if key == keyboard.Key.page_down:
            self.down_stair()
        if key == keyboard.Key.page_up:
            self.up_stair()
        

    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()




record = Rec()
record.start()