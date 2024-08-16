import pyautogui
import constants
import json

from locate_things_on_screen import PositionsCacheTable, PossibleRegions
from log import get_logger

logger = get_logger(__name__)

positions_cache_table = PositionsCacheTable()
def execute_hotkey(hotkey, delay = None):
    pyautogui.press(hotkey)
    if delay:
        pyautogui.sleep(delay)

# TODO: move this to its own file for redability + reusa within cave hunt
def rotate_skills_attack(event_rotate_skills):
    list_hotkeys_para_usar = None
    if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
        list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_PALADIN
    elif constants.VOCACAO_EM_USO == constants.Vocation.EK_DUO:
        list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_KNIGH_DUO
    elif constants.VOCACAO_EM_USO == constants.Vocation.EK_SOLO:
        list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA  
    # elif constants.VOCACAO_EM_USO == constants.Vocation.MS:
    #     list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_MS


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

            if constants.AUTO_ATACK:
                # ensure we only hit space whenever we are not targetting something, this prevents wasting an attack turn
                if pyautogui.locateOnScreen("imgs/something_targeted.png",  confidence=0.99, region=positions_cache_table.data[PossibleRegions.BATTLE_REGION.name]) is None:
                    # ensures we are always targeting the closest mob to us
                    pyautogui.press('esc')
                    pyautogui.press('space')
            
                logger.debug(f"will use hotkey: {attack['hotkey']}")
                execute_hotkey(attack['hotkey'], attack['delay'])
 