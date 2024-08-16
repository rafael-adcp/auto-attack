import pyautogui
from pynput import keyboard
import keyboard as kdebug
import logging
logging.basicConfig(format='[%(asctime)s] - (%(levelname)s):: %(message)s', level=logging.INFO)
pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception





while True:
    kdebug.wait('h')
    
    # given there can be multiple types of quiver, we infer the region using the pvp symbol as an anchor
    print(pyautogui.locateOnScreen("imgs/life_icon.png"))
    print(pyautogui.locateOnScreen("imgs/mana_icon.png"))
    pos = None
    print(pos)
            
    pyautogui.moveTo((1766, 304, 92, 5), duration=0.5)
    photo = pyautogui.screenshot(region=(1766 - 15, 316 - 2, 14, 14))
    photo.save('poc.png')
    #box parameters left=1416, top=562, width=50, height=41)
    #pos = (1766, 304, 92, 5)
    print(pos)
    if pos:
        print(type(pos[0]))
        print(type(pos[1]))
        print(isinstance(pos[0], int))
        print(isinstance(pos[1], int))
        print(isinstance(pos[2], int))
        print(isinstance(pos[3], int))
        pyautogui.moveTo(pos, duration=0.5)
        pyautogui.screenshot('poc.png', region = (pos))

