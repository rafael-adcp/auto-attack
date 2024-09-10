import time

from log import get_logger

from config.general_config import get_general_config
from constants import get_hotkey_rotation_to_use

general_config = get_general_config()
list_hotkeys_para_usar = get_hotkey_rotation_to_use()
logger = get_logger(__name__)


def as_is_today(time_to_run_in_minutes = 0):
    start = time.time()
    atks = {}

    while time.time() - start < time_to_run_in_minutes * 60:
        for attack in list_hotkeys_para_usar:    
            #logger.info(f"will use hotkey: {attack['hotkey']}")
            
            # check if attack[descricao] exists on atks
            
            
            if attack["descricao"] not in atks:
                atks[attack["descricao"]] = 0

            atks[attack["descricao"]] = atks[attack["descricao"]] + 1
            if attack['delay']:
                time.sleep(attack['delay'])
    logger.info(atks)
    logger.info(time.time() - start)
########################################
def new_one(time_to_run_in_minutes = 0):
    spells = [
        {"hotkey": None, "spell_cooldown": 1, "name": "default atk",  "group_name": "attack", "group_cd": 1, "last_cast_time": 0} , 
        {"name": "exevo mas san", "spell_cooldown": 4, "group_cd": 2, "group_name": "attack", "last_cast_time": 0},
        {"name": "avalanche", "spell_cooldown": 2, "group_cd": 2, "group_name": "attack", "last_cast_time": 0}
    ]

    groups = {"attack": {"last_cast_time": 0}}
    atks = {}

    def cast_spell(spell):
        print(f"Casting {spell['name']}!")
        spell["last_cast_time"] = time.time()
        groups[spell["group_name"]]["last_cast_time"] = time.time()

    def check_cooldowns(spell):
        current_time = time.time()
        if current_time - groups[spell["group_name"]]["last_cast_time"] >= spell["group_cd"]:
            if current_time - spell["last_cast_time"] >= spell["spell_cooldown"]:
                return True
        return False
    # run a loop for 15 minutes

    start = time.time()
    # Add a variable to keep track of the last executed attack
    last_executed_attack = None

    while time.time() - start < time_to_run_in_minutes * 60:
        for spell in spells:
            if spell["name"] not in atks:
                atks[spell["name"]] = 0
            if check_cooldowns(spell):
                cast_spell(spell)
                atks[spell["name"]] = atks[spell["name"]] + 1
        time.sleep(1)
    print(atks)


print("as_is_today")
#as_is_today(15)
print("--------------")
print("new_one")
new_one(15)