import pyautogui

class LocateOnScreen:
    

    def __init__(self): 
        self.hungry_position = None
        self.hungry_path = "imgs/starving.png"

    def getStatusBarPosition(self):
        self.hungry_position = pyautogui.locateOnScreen('imgs/starving.png', confidence=0.8)