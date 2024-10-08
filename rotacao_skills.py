import pyautogui
import json

from locate_things_on_screen import PositionsCacheTable, PossibleRegions
from log import get_logger
from config.general_config import get_general_config
from constants import get_hotkey_rotation_to_use

logger = get_logger(__name__)
general_config = get_general_config()

positions_cache_table = PositionsCacheTable()
def execute_hotkey(hotkey, delay = None):
    pyautogui.press(hotkey)
    if delay:
        pyautogui.sleep(delay)

  
def rotate_skills_attack(event_rotate_skills):
    list_hotkeys_para_usar = get_hotkey_rotation_to_use()
    
    logger.info("Skill rotation to be used:")
    logger.info(json.dumps(list_hotkeys_para_usar, indent = 2))
    while not event_rotate_skills.is_set() and list_hotkeys_para_usar != None:
        # bellow actions should happen regardless if there are monsters or not

        for attack in list_hotkeys_para_usar:
            if event_rotate_skills.is_set():
                return # upon asking the thread to die we abort he skill rotation imediately

            if pyautogui.locateOnScreen('imgs/battle_region_empty.png', confidence=0.5, region=positions_cache_table.data[PossibleRegions.BATTLE_REGION.name]):
                # avoids castin runes / spells if there is no monster available on the battle list
                # cant "return" otherwise would leave the thread and stop the skill rotation
                continue

            if general_config.auto_attack:
                # ensure we only hit space whenever we are not targetting something, this prevents wasting an attack turn
                if pyautogui.locateOnScreen("imgs/something_targeted.png",  confidence=0.99, region=positions_cache_table.data[PossibleRegions.BATTLE_REGION.name]) is None:
                    # ensures we are always targeting the closest mob to us
                    pyautogui.press('esc')
                    pyautogui.press('space')
            
                logger.debug(f"will use hotkey: {attack['hotkey']}")
                execute_hotkey(attack['hotkey'], attack['delay'])
 