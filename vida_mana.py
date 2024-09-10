import pyautogui
import constants

from locate_things_on_screen import PositionsCacheTable, PossibleRegions
from log import get_logger

logger = get_logger(__name__)
positions_cache_table = PositionsCacheTable()

from config.character_hotkey import get_current_vocation_in_use_hotkey
from config.general_config import get_general_config
from vida_mana_utils import pixel_match_color

current_vocation_in_use_hotkey = get_current_vocation_in_use_hotkey()
general_config = get_general_config()

LIFE_REGION = positions_cache_table.data[PossibleRegions.REGION_LIFE.name]
MANA_REGION = positions_cache_table.data[PossibleRegions.REGION_MANA.name]
EQUIPS_REGION = positions_cache_table.data[PossibleRegions.REGION_EQUIPS.name]


LIFE_COLOR = positions_cache_table.data[PossibleRegions.LIFE_COLOR.name]
MANA_COLOR = positions_cache_table.data[PossibleRegions.MANA_COLOR.name]


def manager_supplies_rp(event):
    while not event.is_set():
        if event.is_set():
            return
        
        #qndo da caca ele sobe o energy, entao dps q tiver safe volta o prisma e tb pode swapar ssa / might ring
        if pixel_match_color(LIFE_REGION, 80, LIFE_COLOR):
            if pyautogui.locateOnScreen('imgs/energy_ring.png', confidence=0.99, region=EQUIPS_REGION) != None:
                logger.info("tinha dado bosta ne amiguinho, agora q ta tudo bem vou tirar o energy ring e voltar pro prismatic")
                pyautogui.press(current_vocation_in_use_hotkey.ring_default)

            if general_config.vocation_been_used == constants.Vocation.PALADIN.value:
                is_missing_necklace = pyautogui.locateOnScreen('imgs/no_necklace_equipped.png', confidence=0.99, region=EQUIPS_REGION)

                if is_missing_necklace != None:
                    logger.info("tava sem neck, vai colocar o default")
                    pyautogui.press(current_vocation_in_use_hotkey.necklace_default)

                is_missing_ring = pyautogui.locateOnScreen('imgs/no_ring_equipped.png', confidence=0.99, region=EQUIPS_REGION)
                
                if is_missing_ring != None:
                    logger.info("tava sem ring, vai colocar o default")
                    pyautogui.press(current_vocation_in_use_hotkey.ring_default)

            
            if general_config.vocation_been_used == constants.Vocation.MS.value and pyautogui.locateOnScreen('imgs/utamo_vita.png', confidence=0.98, region=EQUIPS_REGION):
                logger.info("vai tirar o utamo") #REVISIT:: i died bkz o this......
                pyautogui.press(current_vocation_in_use_hotkey.remove_utamo_vita)

        
        if not pixel_match_color(LIFE_REGION, general_config.hp_pct_to_use_big_heal, LIFE_COLOR): # BIG HEAL
            pyautogui.press(current_vocation_in_use_hotkey.big_heal) 
        
        elif not pixel_match_color(LIFE_REGION, general_config.hp_pct_to_use_light_heal, LIFE_COLOR): # LIGHT HEAL
            pyautogui.press(current_vocation_in_use_hotkey.light_heal) # ligh heal

        # paladin using energy ring
        if general_config.vocation_been_used == constants.Vocation.PALADIN.value:
                # life is <= X%
                # have at least X% mana
                # is not wearing energy ring
                if (
                    not pixel_match_color(LIFE_REGION, current_vocation_in_use_hotkey.hp_pct_for_energy_ring, LIFE_COLOR) 
                    and pixel_match_color(MANA_REGION, current_vocation_in_use_hotkey.mana_pct_for_energy_ring, MANA_COLOR) 
                    and not pyautogui.locateOnScreen('imgs/energy_ring.png', confidence=0.9, region=EQUIPS_REGION)
                ):
                    # apenas swapa pro energy ring se tiver mana, pq se a mana tiver baixa vai da bosta
                    logger.info("deu caca, vou subir o energy ring")
                    pyautogui.press(current_vocation_in_use_hotkey.energy_ring)

        # SSA general
        if not pixel_match_color(LIFE_REGION, general_config.hp_pct_to_use_ssa, LIFE_COLOR):
            ssa()

        # migh ring general
        if not pixel_match_color(LIFE_REGION, general_config.hp_pct_to_use_might_ring, LIFE_COLOR):
            might_ring()
            


        if not pixel_match_color(LIFE_REGION, general_config.hp_pct_to_pot_life, LIFE_COLOR):
            if general_config.vocation_been_used == constants.Vocation.PALADIN.value:
                pyautogui.press(current_vocation_in_use_hotkey.ultimate_spirit_potion) # hp potion ultimate spirit potion
            elif general_config.vocation_been_used in [constants.Vocation.EK_SOLO.value, constants.Vocation.EK_DUO.value]:
                pyautogui.press(current_vocation_in_use_hotkey.supreme_potion) # supreme
            elif general_config.vocation_been_used == constants.Vocation.MS.value:
                pyautogui.press(current_vocation_in_use_hotkey.exura_vita)

        # botao do panico
        if not pixel_match_color(LIFE_REGION, general_config.hp_pct_to_enter_survival_mode, LIFE_COLOR):
            if general_config.vocation_been_used == constants.Vocation.PALADIN.value:
                ssa_and_might_ring()
            elif general_config.vocation_been_used in [constants.Vocation.EK_SOLO.value, constants.Vocation.EK_DUO.value]:
                logger.info("hmm se assou ne amiguinho... ACORDA O DRUID Q ELE TA DORMINDO!! Enquanto isso vou dar utamo tempo pra vc respirar um pouco......")
                pyautogui.press(current_vocation_in_use_hotkey.utamo_tempo)
                ssa_and_might_ring()

            elif general_config.vocation_been_used == constants.Vocation.MS.value:
                logger.info("santa pedrada batman, vou dar utamo vita")
                pyautogui.press(current_vocation_in_use_hotkey.utamo_vita)
                ssa_and_might_ring()
        else:
            if general_config.vocation_been_used == constants.Vocation.PALADIN.value and not pixel_match_color(MANA_REGION, current_vocation_in_use_hotkey.mana_pct_for_energy_ring, MANA_COLOR):
                pyautogui.press(current_vocation_in_use_hotkey.ultimate_spirit_potion)
                logger.info("[batendo ultimate spirit] ta negativando")
                # se a mana ta abaixo de 50 ele ja ta na merda com enery ring ou swapando ssa e subindo might, fora q ta batendo gran san
                # entao pra nao negativar a mana bate o ultimate spirit
            elif not pixel_match_color(MANA_REGION, general_config.mana_pct_to_use_pot, MANA_COLOR) and general_config.vocation_been_used not in [constants.Vocation.MS.value]:
                # everyone else (rp / ek) needs to keep mana high
                pyautogui.press(current_vocation_in_use_hotkey.mana_potion)
            
            elif not pixel_match_color(MANA_REGION, general_config.mana_pct_to_use_pot, MANA_COLOR) and general_config.vocation_been_used == constants.Vocation.MS.value:
                # for mages (druid / sorcerer) they will probably level up before the need to use a potion, nor to mention they have tons of mana leech
                pyautogui.press(current_vocation_in_use_hotkey.mana_potion)

def ssa():
    if not pyautogui.locateOnScreen('imgs/ssa_equipped.png', confidence=0.9, region=EQUIPS_REGION):
        pyautogui.press(current_vocation_in_use_hotkey.ssa)
        logger.info("olha o amuleto")

def might_ring():
    if not pyautogui.locateOnScreen('imgs/might_ring_equipped.png', confidence=0.9, region=EQUIPS_REGION):
        pyautogui.press(current_vocation_in_use_hotkey.might_ring)
        logger.info("olha o anel")

def ssa_and_might_ring():
    logger.info("meu deus do ceu maggy onde foi que voce meteu a gente")
    ssa()
    might_ring()
    
