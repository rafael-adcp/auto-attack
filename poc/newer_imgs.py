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
        #pyautogui.moveTo(pos.left, pos.top, duration=0.5)
        return pos
    except:
        print("failed to find", img)
    finally:
        print("\n\n\n")

for img in battle:
    pos = fetch_img_pos(img)
    if pos:
        pyautogui.screenshot(
            'imgs/FOUNDED_battle_region_{}.png'.format(
                img.split(".")[0].split("/")[-1]
            ), region=(int(pos.left), int(pos.top), 157, 100)
        )


for img in empty_battle:
    fetch_img_pos(img)

for img in pvp:
    pos = fetch_img_pos(img)
    #equips_pos = (int(pvp_symbol_pos[0] - 123), int(pvp_symbol_pos[1] - 76), 115, 162)
    if pos:
        pyautogui.screenshot(
            'imgs/FOUNDED_pvp_symbol_{}.png'.format(
                img.split(".")[0].split("/")[-1]
            ), region=(int(pos.left - 123), int(pos.top - 76), 115, 162)
        )
