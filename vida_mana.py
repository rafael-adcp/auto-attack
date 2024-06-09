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
LIFE_REGION = (1766, 304, 92, 5)
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
        
        # TODO: mover esse bloco todo pra elif, pra sempre um ter prioridade
        # pq n da pra potar mana e vida no mesmo cd
        
        
        #qndo da caca ele sobe o energy, entao dps q tiver safe volta o prisma
        # se a vida for >= 90 e tiver com energy ring, remove ele
        
        if pixel_match_color(LIFE_REGION, 90, COR_VIDA) and pyautogui.locateOnScreen("energy_ring.png", confidence=0.99) != None:
            print("tinha dado bosta ne amiguinho, agora q ta tudo bem vou tirar o energy ring e voltar pro prismatic")
            pyautogui.press('4') # prismatic ring

        # TODO: criar uma mapping pras hoteksys do ek, e do rp
        
        if not pixel_match_color(LIFE_REGION, 80, COR_VIDA):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                pyautogui.press('F2') # gran san
            else:
                pyautogui.press('F1') # med ico
        
        elif not pixel_match_color(LIFE_REGION, 95, COR_VIDA):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                pyautogui.press('F1') # ligh heal
            else:
                pyautogui.press('F1') # med ico
            
        
            

        if not pixel_match_color(LIFE_REGION, 50, COR_VIDA):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                pyautogui.press('F5') # hp potion f12 pro pot do ek
            else:
                pyautogui.press('F12') # supreme
        
        # botao do panico, sobe o energy ring se ja nao tiver com ele
        if not pixel_match_color(LIFE_REGION, 40, COR_VIDA) and not pyautogui.locateOnScreen("energy_ring.png", confidence=0.9):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                print("deu caca, vou subir o energy ring")
                pyautogui.press('3') # energy ring
            
            else: # se n for paladino da utamo tempo
                print("vai utamar")
                pyautogui.press('p') # utamo tempo

        else:

            if not pixel_match_color(MANA_REGION, 80, COR_MANA):
                pyautogui.press('F4') # pot de mana