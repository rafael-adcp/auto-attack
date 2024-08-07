import pyautogui
import keyboard as kdebug
import constants

# # # obtendo posicoes pixels e suas cores pras threads
# kdebug.wait('h')
# while True:
#     pyautogui.displayMousePosition() # PRA PEGAR A POSICAO DAS BARRINHAS DE VIDA / MANA FULL
#     print(pyautogui.displayMousePosition())
#     pyautogui.sleep(20)


#pyautogui.moveTo(1766,304, 2) # 0% vida
#pyautogui.moveTo(1766+46,304+5, 2) # 50% vida
#pyautogui.moveTo(1766+92,304, 2) # 100% vida

WIDTH = 92 # tamanho barrinha cheia
# posicao no meio da barrinha de vida
LIFE_REGION = (1766, 304, 92, 5)
# posicao no meio da barrinha de mana
MANA_REGION = (1766, 316, 92, 5)

COR_VIDA = (240,97,97)
COR_MANA = (83,80,217)

def calcula_width(percent):
    return int ((WIDTH * percent) / 100)


# print(check_color(LIFE_REGION, 50))
# print(check_color(MANA_REGION, 50))
def check_color(region, percent):
    result_percent = calcula_width(percent)
    x = region[0] + result_percent
    y = region[1] + region[3]
    print(
        pyautogui.pixel(x,y)
    )

# print(pixel_match_color(MANA_REGION, 50, COR_MANA))
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
        # se a vida for >= 90 e tiver com energy ring, remove ele
        
        if pixel_match_color(LIFE_REGION, 90, COR_VIDA):
            if pyautogui.locateOnScreen('imgs/energy_ring.png', confidence=0.99) != None:
                print("tinha dado bosta ne amiguinho, agora q ta tudo bem vou tirar o energy ring e voltar pro prismatic")
                pyautogui.press(constants.HOTKEY_RING_DEFAULT)
            
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                if pyautogui.locateOnScreen('imgs/no_necklace_equipped.png', confidence=0.99) != None:
                    print("tava sem neck, vai colcoar")
                    pyautogui.press(constants.HOTKEY_NECKLACE_DEFAULT)

                if pyautogui.locateOnScreen('imgs/no_ring_equipped.png', confidence=0.99) != None:
                    print("tava sem ring, vai colcoar")
                    pyautogui.press(constants.HOTKEY_RING_DEFAULT)

            
            if constants.VOCACAO_EM_USO == constants.Vocation.MS and pyautogui.locateOnScreen('imgs/utamo_vita.png', confidence=0.98):
                print("vai tirar o utamo")
                pyautogui.press("r")

        if not pixel_match_color(LIFE_REGION, 80, COR_VIDA):
            pyautogui.press('F2') # BIG HEAL
        
        elif not pixel_match_color(LIFE_REGION, 90, COR_VIDA):
            pyautogui.press('F1') # ligh heal
            
        
            

        if not pixel_match_color(LIFE_REGION, 50, COR_VIDA):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                pyautogui.press('F5') # hp potion ultimate spirit potion
            elif constants.VOCACAO_EM_USO == constants.Vocation.EK_SOLO or constants.VOCACAO_EM_USO == constants.Vocation.EK_DUO:
                pyautogui.press('F12') # supreme
            elif constants.VOCACAO_EM_USO == constants.Vocation.MS:
                pyautogui.press('F2')

        # botao do panico
        if not pixel_match_color(LIFE_REGION, 45, COR_VIDA):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:

                # apenas swapa pro energy ring se tiver mana, pq se a mana tiver baixa vai da bosta
                if  pixel_match_color(MANA_REGION, constants.MANA_PCT_FOR_ENERYING, COR_MANA) and not pyautogui.locateOnScreen('imgs/energy_ring.png', confidence=0.9):
                    print("deu caca, vou subir o energy ring")
                    pyautogui.press('3') # energy ring
                else:
                    # TODO move this to its own method given ssa and might ring are common to all vocations
                    #swap ssa / might ring
                    print("meu deus do ceu maggy onde foi que voce meteu a gente")
                    if not pyautogui.locateOnScreen('imgs/might_ring_equipped.png', confidence=0.9):
                        pyautogui.press('5') # might ring
                        print("olha o anel")
                    if not pyautogui.locateOnScreen('imgs/ssa_equipped.png', confidence=0.9):
                        pyautogui.press('6') # SSA
                        print("olha o amuleto")
            # if vocacao_em_use is either EK_SOLO or EK_DUO print hellow world
            
            elif constants.VOCACAO_EM_USO == constants.Vocation.EK_SOLO or constants.VOCACAO_EM_USO == constants.Vocation.EK_DUO: # se n for paladino da utamo tempo
                print("vai utamar")
                pyautogui.press('p') # utamo tempo

            elif constants.VOCACAO_EM_USO == constants.Vocation.MS:
                print("vai dar utamo vita")
                pyautogui.press('f4') # utamo vita

        else:
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN and not pixel_match_color(MANA_REGION, constants.MANA_PCT_FOR_ENERYING, COR_MANA):
                pyautogui.press('F5')
                print("ta negativando")
                # se a mana ta abaixo de 50 ele ja ta na merda com enery ring ou swapando ssa e subindo might, fora q ta batendo gran san
                # entao pra nao negativar a mana bate o ultimate spirit
            elif not pixel_match_color(MANA_REGION, 80, COR_MANA) and not constants.VOCACAO_EM_USO == constants.Vocation.MS:
                pyautogui.press('F4') # pot de mana
            
            elif not pixel_match_color(MANA_REGION, 50, COR_MANA) and constants.VOCACAO_EM_USO == constants.Vocation.MS:
                pyautogui.press('F5') # pot de mana                