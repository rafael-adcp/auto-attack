import pyautogui
from log import get_logger

from locate_things_on_screen import PositionsCacheTable, PossibleRegions

logger = get_logger(__name__)
pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

positions_cache_table = PositionsCacheTable()
EQUIPS_REGION = positions_cache_table.data[PossibleRegions.REGION_EQUIPS.name]

def sell_loot():
    missing_backpack = pyautogui.locateOnScreen("imgs/no_bp_equipped.png", region=EQUIPS_REGION)
    
    if missing_backpack:
        logger.error("You are missing a bp equipped, without one you can't sell loot, otherwise all money would go on the floor")
    else:
        pyautogui.press(";")
        pyautogui.sleep(1)
        pyautogui.press(".")
        
        pyautogui.sleep(2)
        sell_loot_panel = pyautogui.locateOnScreen("imgs/npc_sell_loot_panel.png")
        if not sell_loot_panel:
            logger.info("could not find sell loot dialog")
        else:
            sell_loot_panel_box = (
                int(sell_loot_panel[0]), 
                int(sell_loot_panel[1]), 
                int(sell_loot_panel[2]), 
                int(sell_loot_panel[3] + 500 ) 
            )

            logger.info("will start selling loot")
            sell_button = pyautogui.locateOnScreen("imgs/sell_button.png")
            pyautogui.click(sell_button)
            pyautogui.sleep(1)
            should_stop = False

            ok_button = pyautogui.locateOnScreen("imgs/ok_button.png")

            while not should_stop:
                something_to_sell = pyautogui.locateOnScreen("imgs/item_to_sell.png", region=sell_loot_panel_box, confidence=0.99)
                # TODO:: replace this with locate all on screen, then iterate over a list and implement an ignore list to avoid selic gems
                if not something_to_sell:
                    should_stop = True
                else:
                    pyautogui.click(something_to_sell)
                    pyautogui.sleep(0.5)
                    pyautogui.click(ok_button)
                    pyautogui.sleep(0.5)