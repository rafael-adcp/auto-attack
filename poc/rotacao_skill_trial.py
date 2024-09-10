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

MODO = "old_one"
logger.info(">>>>>>>>>>>>>>>> VAI USAR: " + MODO)
from config.character_hotkey import get_current_vocation_in_use_hotkey        
current_vocation_hotkey = get_current_vocation_in_use_hotkey()

RP_SKILLS = [
        {"hotkey": current_vocation_hotkey.amp_res, "spell_cooldown": 16, "descricao": "amp res",  "group_name": "suporte", "group_cd": 2, "last_cast_time": 0} , 
        #{"hotkey": 'o', "spell_cooldown": 0.2, "descricao": "tapete"} , 
        #{"hotkey": 'p', "spell_cooldown": 1, "descricao": "granada"} , 
        # as habilidades da roda nao impactam as de ataque

        {"hotkey": current_vocation_hotkey.mas_san, "spell_cooldown": 4, "descricao": "mas san",  "group_cd": 2, "group_name": "attack", "last_cast_time": 0} ,
        {"hotkey": current_vocation_hotkey.rune_to_use, "spell_cooldown": 2, "descricao": "avalanche",  "group_cd": 2, "group_name": "attack", "last_cast_time": 0}, 
    ]

groups = {
    "attack":  {"last_cast_time": 0},
    "suporte": {"last_cast_time": 0}
}

import time
def check_cooldowns(spell):
    current_time = time.time()
    if current_time - groups[spell["group_name"]]["last_cast_time"] >= spell["group_cd"]:
        if current_time - spell["last_cast_time"] >= spell["spell_cooldown"]:
            return True
    return False

def cast_spell(spell):
    #logger.info(f"Casting {spell['descricao']}!")
    pyautogui.press(spell["hotkey"])
    #updating spell last time casted and group last time casted
    # also make sure we update the last_Cast_time inside of RP_SKills

    spell["last_cast_time"] = time.time()

    groups[spell["group_name"]]["last_cast_time"] = time.time()

def rotate_skills_attack(event_rotate_skills):
    list_hotkeys_para_usar = None
    if MODO == "old_one":
        list_hotkeys_para_usar = get_hotkey_rotation_to_use()
    else:
        list_hotkeys_para_usar = RP_SKILLS
    
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
                
                if MODO == "old_one":
                    execute_hotkey(attack['hotkey'], attack['delay'])
                else: 
                    if check_cooldowns(attack):
                        cast_spell(attack)
 