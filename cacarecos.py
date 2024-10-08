import pyautogui
import constants
import time

from log import get_logger

from locate_things_on_screen import PositionsCacheTable, PossibleRegions
from config.general_config import get_general_config
from config.character_hotkey import get_current_vocation_in_use_hotkey

positions_cache_table = PositionsCacheTable()
general_config = get_general_config()
logger = get_logger(__name__)

current_vocation_hotkeys = get_current_vocation_in_use_hotkey()

EQUIPS_REGION = positions_cache_table.data[PossibleRegions.REGION_EQUIPS.name]

def manager_cacarecos(event):
    while not event.is_set():
        if event.is_set():
            return
        did_something = False
        if general_config.vocation_been_used == constants.Vocation.PALADIN.value:
            # se o quiver estiver vazio, refila ele
            if pyautogui.locateOnScreen('imgs/quiver_vazio.png', confidence=0.98, region=EQUIPS_REGION):
                # equipa mais flecha no quiver
                # idealmente #TODO: checar se tem flechas pra equipar se nao qndo tiver no final da hunt vai ficar spamando a toa
                # TODO: aqui baseado em uma config saber qual quiver q ta usando tb seria interessante pra n ter q checar pro todos os quivers
                pyautogui.press(current_vocation_hotkeys.equip_more_arrows)
                pyautogui.press(current_vocation_hotkeys.equip_more_arrows)
                pyautogui.press(current_vocation_hotkeys.equip_more_arrows)
                did_something = True

        #mover esses cacarecos pra uma outra thread, isso aqui n deveria atrapalhar a rotacao de skill
        #apenas come qndo o icone de fome aparecer, evitar ficar spamando
        if pyautogui.locateOnScreen('imgs/starving.png', confidence=0.8, region=EQUIPS_REGION):
            pyautogui.press(general_config.food_to_eat)
            did_something = True

        # apenas usa utura gran, caso o icone nao esteja na barrinha de status
        if not general_config.vocation_been_used == constants.Vocation.MS.value and not pyautogui.locateOnScreen('imgs/utura_gran.png', confidence=0.98, region=EQUIPS_REGION):
            pyautogui.press(general_config.utura_gran)
            did_something = True

        
        
        # only casts haste when battle region is empty, this avoids hunts where mobs casts paralyze on you and you keep spamming utani hur
        # nor to mention for MS scenario haste is the same spell group as exori moe so this prevents race condition there
        if not pyautogui.locateOnScreen('imgs/haste.png', confidence=0.95, region=EQUIPS_REGION):
            # pyautogui.locateOnScreen('imgs/battle_region_empty.png', confidence=0.8, region=positions_cache_table.data[PossibleRegions.BATTLE_REGION.name]) and
            pyautogui.press(general_config.haste)
            did_something = True
        
        if did_something: # if an action was taken we safe to sleep for a bit, no need to keep runing it so often
            time.sleep(10)

        