import pyautogui
import constants
import time

def manager_cacarecos(event):
    while not event.is_set():
        if event.is_set():
            return        
        if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
            # se o quiver estiver vazio, refila ele
            if pyautogui.locateOnScreen('imgs/quiver_vazio.png', confidence=0.98, region=constants.REGION_QUIVER):
                # equipa mais felcha no quiver
                # idealmente #TODO: checar se tem flechas pra equipar, se nao qndo tiver no final da hunt vai ficar spamando atoa
                pyautogui.press('num7')
                pyautogui.press('num7')
                pyautogui.press('num7')

        #mover esses cacarecos pra uma outra thread, isso aqui n deveria atrapalhar a rotacao de skill
        #apenas come qndo o icone de fome aparecer, evitar ficar spamando
        if pyautogui.locateOnScreen('imgs/starving.png', confidence=0.8):
            pyautogui.press('0') # mushroom

        # apenas usa utura gran, caso o icone nao esteja na barrinha de status
        if not pyautogui.locateOnScreen('imgs/utura_gran.png', confidence=0.98) and not constants.VOCACAO_EM_USO == constants.Vocation.MS:
            pyautogui.press('9') # utura gran

        
        
        # only casts haste when battle region is empty, this avoids hunts where mobs casts paralyze on you and you keep spamming utani hur
        # nor to mention for MS scenario haste is the same spell group as exori moe so this prevents race condition there
        if pyautogui.locateOnScreen('imgs/battle_region_empty.png', confidence=0.8, region=constants.REGION_BATTLE) and not pyautogui.locateOnScreen('imgs/haste.png', confidence=0.95):
            print("vai dar haste")
            pyautogui.press('f10') # utani hur

        time.sleep(20) # there is no need to hammer this ad eternum