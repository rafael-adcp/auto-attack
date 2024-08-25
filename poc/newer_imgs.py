import pyautogui
import keyboard

battle = ["imgs/battle_dialog.png",
          "imgs/battle_dialog_2.png",
            "imgs/battle_dialog_3.png", ]


empty_battle = ["imgs/battle_region_empty.png", "imgs/battle_region_empty_1.png"]

pvp = ["imgs/pvp_symbol.png", "imgs/pvp_symbol_1.png", "imgs/pvp_symbol_2.png", "imgs/pvp_symbol_3.png", "imgs/pvp_symbol_4.png"]




def fetch_img_pos(img):
    try:
        keyboard.wait("h")
        print("will atempt to find", img)
        pos = pyautogui.locateOnScreen(img)
        print(pos)
        pyautogui.moveTo(pos.left, pos.top, duration=0.5)
    except:
        print("failed to find", img)
    finally:
        print("\n\n\n")

for img in battle:
    fetch_img_pos(img)

for img in empty_battle:
    fetch_img_pos(img)

for img in pvp:
    fetch_img_pos(img)