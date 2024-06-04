import pyautogui
import keyboard as kdebug

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
        
        # TODO: evitar o tira e poe da thread
        # fazer o esquema de localizar pra ver e o ring ja nao esta equipado
        #qndo da caca ele sobe o energy, entao dps q tiver safe volta o prisma
        # if not pixel_match_color(LIFE_REGION, 100, COR_VIDA):
        #     pyautogui.press('4') # prismatic ring

        # TODO: criar uma mapping pras hoteksys do ek, e do rp
        
        if not pixel_match_color(LIFE_REGION, 95, COR_VIDA):
            pyautogui.press('F1') # ligh heal
            
        elif not pixel_match_color(LIFE_REGION, 90, COR_VIDA):
            pyautogui.press('F2') # gran san
            

        if not pixel_match_color(LIFE_REGION, 50, COR_VIDA):
            pyautogui.press('F12') # hp potion
        
        # botao do panico, sobe o energy ring
        # TODO: aqui tambem garantir que ja nao ta o ring la
        # pra evitar o tira e poe da thread
        if not pixel_match_color(LIFE_REGION, 40, COR_VIDA):
            pyautogui.press('3') # energy ring
            # aqui geralmente n da  caca pq ele sobe o energt e a vida ja comeca a subir
            # eh mais por precaução
        
        else:
            if not pixel_match_color(LIFE_REGION, 80, COR_VIDA):
                pyautogui.press('F1') # light healing

            if not pixel_match_color(MANA_REGION, 80, COR_MANA):
                pyautogui.press('F4') # pot de mana