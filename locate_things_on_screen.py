import pyautogui
from enum import Enum, auto
import json

from log import get_logger

logger = get_logger(__name__)

pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

class PossibleRegions(Enum):
    BATTLE_REGION = auto()
    REGION_QUIVER = auto()
    REGION_EQUIPS = auto()
    REGION_LIFE = auto()
    REGION_MANA = auto()


class PositionsCacheTable():
    data = {}

    def __init__(self):
        try:
            with open('positions_cache.json', 'r') as fp:
                self.data = json.load(fp)

            # for every key in data cast it from str to tuple
            for key in self.data:
                # value is stored as string, by using eval we convert it to tuple
                self.data[key] = eval(self.data[key])
        except Exception as e:
            logger.error("failed to load positions_cache.json")
            logger.error(e)
            raise e



class LocateOnScreen():

    positions_cache = {}

    def __init__(self):
        self.load_positions_cache()
        self.save_file_to_json()

    def load_positions_cache(self):
        logger.info("Will fetch positions dynamically")
        self.load_battle_region()
        self.load_quiver_region()
        self.load_equips_region()
        self.load_life_and_mana_region()
        logger.info("positions loaded into cache successfully")

    def check_pvp_symbol(self, error_msg):
        pvp_symbol_pos = pyautogui.locateOnScreen("imgs/pvp_symbol.png")
        if not pvp_symbol_pos:
            raise Exception(error_msg)
        
        return pvp_symbol_pos



    def load_battle_region(self):
        battle_dialog_pos = pyautogui.locateOnScreen("imgs/battle_dialog.png")
        
        if battle_dialog_pos:
            self.positions_cache[PossibleRegions.BATTLE_REGION.name] = str((battle_dialog_pos[0], battle_dialog_pos[1], 157, 100))
        else:
            raise Exception("could not find battle region position, make you the battle window is opened and using the proper appearance")

    
    def load_quiver_region(self):
        # given there can be multiple types of quiver, we infer the region using the pvp symbol as an anchor
        pvp_symbol_pos = self.check_pvp_symbol("could not find quiver region position, make you character items are visible")
        
        quiver_pos = (pvp_symbol_pos[0] - 44, pvp_symbol_pos[1] - 22, pvp_symbol_pos[2] - 7, pvp_symbol_pos[3] + 14)

        self.positions_cache[PossibleRegions.REGION_QUIVER.name] = str(quiver_pos)



    def load_equips_region(self):
        # we infer the region using the pvp symbol as an anchor
        pvp_symbol_pos = self.check_pvp_symbol("could not find equips position, make you character items are visible")
        
        equips_pos = (int(pvp_symbol_pos[0] - 123), int(pvp_symbol_pos[1] - 76), 115, 162)

        self.positions_cache[PossibleRegions.REGION_EQUIPS.name] = str(equips_pos)


    def load_life_and_mana_region(self):
        life_icon_pos = pyautogui.locateOnScreen("imgs/life_icon.png", confidence=0.9)
        
        if not life_icon_pos:
            raise Exception("could not find life and mana region position, make you character life and mana are visible")
        
        # from the heart icon we move it to be in the middle of the life bar
        mid_life_bar_pos = (life_icon_pos[0] + 13, life_icon_pos[1] + 0, life_icon_pos[2] + 81,life_icon_pos[3] - 4)

        # mana and life are the exact thing, the only different is the "y" axis, so we just move it
        mid_mana_bar_pos = (mid_life_bar_pos[0], mid_life_bar_pos[1] + 12, mid_life_bar_pos[2], mid_life_bar_pos[3])

        self.positions_cache[PossibleRegions.REGION_LIFE.name] = str(mid_life_bar_pos)
        self.positions_cache[PossibleRegions.REGION_MANA.name] = str(mid_mana_bar_pos)
        


    def save_file_to_json(self):
        with open('positions_cache.json', 'w') as fp:
            json.dump(self.positions_cache, fp, indent=4)