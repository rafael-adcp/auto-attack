import pyautogui
import constants

from locate_things_on_screen import PositionsCacheTable, PossibleRegions
positions_cache_table = PositionsCacheTable()

from log import get_logger

logger = get_logger(__name__)


WIDTH = 92 # size of the full bar

LIFE_REGION = positions_cache_table.data[PossibleRegions.REGION_LIFE.name]
MANA_REGION = positions_cache_table.data[PossibleRegions.REGION_MANA.name]
EQUIPS_REGION = positions_cache_table.data[PossibleRegions.REGION_EQUIPS.name]


LIFE_COLOR = (240,97,97)
MANA_COLOR = (83,80,217)

def calcula_width(percent):
    return int ((WIDTH * percent) / 100)


# logger.info(pixel_match_color(MANA_REGION, 50, MANA_COLOR))
def pixel_match_color(region, percent, color):
    result_percent = calcula_width(percent)
    x = region[0] + result_percent
    y = region[1] + region[3]
    return pyautogui.pixelMatchesColor(int(x), int(y), color, 10)



def manager_supplies_rp(event):
    while not event.is_set():
        if event.is_set():
            return
        
        #qndo da caca ele sobe o energy, entao dps q tiver safe volta o prisma e tb pode swapar ssa / might ring
        if pixel_match_color(LIFE_REGION, 90, LIFE_COLOR):
            
            if pyautogui.locateOnScreen('imgs/energy_ring.png', confidence=0.99, region=EQUIPS_REGION) != None:
                logger.info("tinha dado bosta ne amiguinho, agora q ta tudo bem vou tirar o energy ring e voltar pro prismatic")
                pyautogui.press(constants.HOTKEY_RING_DEFAULT)
            
            # THINK: should this be moved to "cacarecos?"
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                #spare unecessary usage of ssa
                is_missing_necklace = pyautogui.locateOnScreen('imgs/no_necklace_equipped.png', confidence=0.99, region=EQUIPS_REGION)
                is_ussing_ssa = pyautogui.locateOnScreen('imgs/ssa_equipped.png', confidence=0.9, region=EQUIPS_REGION)
                
                if is_missing_necklace != None or is_ussing_ssa != None:
                    logger.info("tava sem neck (ou tava de ssa), vai colocar o default")
                    pyautogui.press(constants.HOTKEY_NECKLACE_DEFAULT)

                #spare unecessary usage of might ring
                is_missing_ring = pyautogui.locateOnScreen('imgs/no_ring_equipped.png', confidence=0.99, region=EQUIPS_REGION)
                is_using_might_ring = pyautogui.locateOnScreen('imgs/might_ring_equipped.png', confidence=0.9, region=EQUIPS_REGION)
                
                if is_missing_ring != None or is_using_might_ring != None:
                    logger.info("tava sem ring (ou de might), vai colocar o default")
                    pyautogui.press(constants.HOTKEY_RING_DEFAULT)

            
            if constants.VOCACAO_EM_USO == constants.Vocation.MS and pyautogui.locateOnScreen('imgs/utamo_vita.png', confidence=0.98, region=EQUIPS_REGION):
                logger.info("vai tirar o utamo") #REVISIT:: i died bkz o this......
                pyautogui.press("r")

        if not pixel_match_color(LIFE_REGION, 80, LIFE_COLOR):
            pyautogui.press('F2') # BIG HEAL
        
        elif not pixel_match_color(LIFE_REGION, 90, LIFE_COLOR):
            pyautogui.press('F1') # ligh heal
            

        if not pixel_match_color(LIFE_REGION, 50, LIFE_COLOR):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                pyautogui.press('F5') # hp potion ultimate spirit potion
            elif constants.VOCACAO_EM_USO in [constants.Vocation.EK_SOLO, constants.Vocation.EK_DUO]:
                pyautogui.press('F12') # supreme
            elif constants.VOCACAO_EM_USO == constants.Vocation.MS:
                pyautogui.press('F2')

        # botao do panico
        if not pixel_match_color(LIFE_REGION, 45, LIFE_COLOR):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                # apenas swapa pro energy ring se tiver mana, pq se a mana tiver baixa vai da bosta
                if  pixel_match_color(MANA_REGION, constants.MANA_PCT_FOR_ENERGY_RING, MANA_COLOR) and not pyautogui.locateOnScreen('imgs/energy_ring.png', confidence=0.9, region=EQUIPS_REGION):
                    logger.info("deu caca, vou subir o energy ring")
                    pyautogui.press('3') # energy ring
                else:
                    # TODO move this to its own method given ssa and might ring are common to all vocations
                    #swap ssa / might ring
                    logger.info("meu deus do ceu maggy onde foi que voce meteu a gente")
                    if not pyautogui.locateOnScreen('imgs/might_ring_equipped.png', confidence=0.9, region=EQUIPS_REGION):
                        pyautogui.press('5') # might ring
                        logger.info("olha o anel")
                    if not pyautogui.locateOnScreen('imgs/ssa_equipped.png', confidence=0.9, region=EQUIPS_REGION):
                        pyautogui.press('6') # SSA 
                        logger.info("olha o amuleto")
            
            elif constants.VOCACAO_EM_USO in [constants.Vocation.EK_SOLO, constants.Vocation.EK_DUO]:
                logger.info("hmm se assou ne amiguinho... ACORDA ODRUID Q ELE TA DORMINDO.. enquanto isso vou dar utamo tempo pra vc respirar um pouco......")
                pyautogui.press('p') # utamo tempo

            elif constants.VOCACAO_EM_USO == constants.Vocation.MS:
                logger.info("santa pedrada batman, vou dar utamo vita")
                pyautogui.press('f4') # utamo vita

        else:
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN and not pixel_match_color(MANA_REGION, constants.MANA_PCT_FOR_ENERGY_RING, MANA_COLOR):
                pyautogui.press('F5')
                logger.info("[batendo ultimate spirit] ta negativando")
                # se a mana ta abaixo de 50 ele ja ta na merda com enery ring ou swapando ssa e subindo might, fora q ta batendo gran san
                # entao pra nao negativar a mana bate o ultimate spirit
            elif not pixel_match_color(MANA_REGION, 80, MANA_COLOR) and constants.VOCACAO_EM_USO not in [constants.Vocation.MS]:
                # everyone else (rp / ek) needs to keep mana high
                pyautogui.press('F4') # pot de mana
            
            elif not pixel_match_color(MANA_REGION, 50, MANA_COLOR) and constants.VOCACAO_EM_USO == constants.Vocation.MS:
                # for mages (druid / sorcerer) they will probably level up before the need to use a potion, nor to mention they have tons of mana leech
                pyautogui.press('F5') # pot de mana                