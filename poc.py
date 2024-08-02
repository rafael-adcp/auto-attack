import keyboard as kdebug
import pyautogui
from pynput import keyboard



while True:
    kdebug.wait('h')    
    #print(pyautogui.displayMousePosition())
    #pyautogui.moveTo(constants.REGION_BATTLE)
    
    position = (1745, 280, 130, 20)
    image = pyautogui.screenshot("sample.png", region=position)
    #print(pyautogui.locateOnScreen('imgs/battle_region_empty.png', confidence=0.8))