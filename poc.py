import pyautogui
from pynput import keyboard


import keyboard as kdebug
kdebug.wait('h')
# while True:
#     print(pyautogui.displayMousePosition())

#pyautogui.screenshot('screenshot.png', region=(1592, 52, 135, 8))
#pyautogui.screenshot('screenshot.png', region=(1592, 74, 135, 8))
battle_content_region = (1592,40,3,350)
pyautogui.screenshot('somente_beradinha.png', region=battle_content_region)    

possible = pyautogui.locateAllOnScreen('monster_life_bar.png', region=battle_content_region)
#print(list(possible))

for pos in possible:
    print(pos)
    kdebug.wait('h')    
    pyautogui.moveTo(
        pos,
        duration=0.5
    )
#print(pyautogui.displayMousePosition())
#pyautogui.moveTo(constants.REGION_BATTLE)

# possible = pyautogui.locateAllOnScreen(
#     "monster_life_bar.png",
#     region=constants.REGION_BATTLE,
#     confidence=0.5,
#       #grayscale=True
#     )






#print(pyautogui.locateOnScreen('imgs/battle_region_empty.png', confidence=0.8))