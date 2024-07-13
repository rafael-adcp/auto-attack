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
        
        if not pixel_match_color(LIFE_REGION, 90, COR_VIDA):
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
                pyautogui.press('F5') # hp potion ultimate spirit potion
            else:
                pyautogui.press('F12') # supreme

        # botao do panico
        if not pixel_match_color(LIFE_REGION, 45, COR_VIDA):
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:

                # apenas swapa pro energy ring se tiver mana, pq se a mana tiver baixa vai da bosta
                if  pixel_match_color(MANA_REGION, constants.MANA_PCT_FOR_ENERYING, COR_MANA) and not pyautogui.locateOnScreen("energy_ring.png", confidence=0.9):
                    print("deu caca, vou subir o energy ring")
                    pyautogui.press('3') # energy ring
                else: # TODO: testar isso aqui na posta de haleluja com as true asura, colocar um if FALSE ali em cima ou so omitir o pot de sp
                    #swap ssa / might ring
                    print("meu deus do ceu maggy onde foi que voce meteu a gente")
                    
                    if not pyautogui.locateOnScreen("might_ring_equipped.png", confidence=0.9):
                        pyautogui.press('5') # might ring
                        print("olha o anel")
                    
                    if not pyautogui.locateOnScreen("ssa_equipped.png", confidence=0.9):
                        pyautogui.press('6') # SSA
                        print("olha o amuleto")
                
            else: # se n for paladino da utamo tempo
                print("vai utamar")
                pyautogui.press('p') # utamo tempo

        else:
            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN and not pixel_match_color(MANA_REGION, constants.MANA_PCT_FOR_ENERYING, COR_MANA):
                pyautogui.press('F5')
                print("ta negativando")
                # se a mana ta abaixo de 50 ele ja ta na merda com enery ring ou swapando ssa e subindo might, fora q ta batendo gran san
                # entao pra nao negativar a mana bate o ultimate spirit
            elif not pixel_match_color(MANA_REGION, 80, COR_MANA):
                pyautogui.press('F4') # pot de mana