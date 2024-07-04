from pynput.keyboard import Listener
from pynput import keyboard
import keyboard as kdebug
import pyautogui
pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

import threading

from vida_mana import manager_supplies_rp
import json

# hotekeys in game
RING_BOX = '1'
RING_LURANDO = '2'
COMER_FOOD = '3'



REGION_BATTLE = (1572,24,157,37)

global event_th
event_th = threading.Event()

# while True:
#     kdebug.wait('h')
#     print(pyautogui.locateOnScreen('battle_region.png', confidence=0.8))

def execute_hotkey(hotkey, delay = None):
    pyautogui.press(hotkey)
    if delay:
        pyautogui.sleep(delay)

LIST_HOTKEYS_ATTACK = [
    {"hotkey": 'f3', "delay": 1, "descricao": "amp res"} , 
    #{"hotkey": 'F3', "delay": 2, "descricao": "mas san"} ,
    #{"hotkey": 'F6', "delay": 2, "descricao": "avalanche"},
]

def rotate_skills_attack():
    while not event_rotate_skills.is_set():
        for attack in LIST_HOTKEYS_ATTACK:
            if event_rotate_skills.is_set():
                return # caso acabe a box no meio n precisa terminar a rotacao
            
            if pyautogui.locateOnScreen('battle_region.png', confidence=0.8, region=REGION_BATTLE):
                # evita ficar castando magias se nao tiver mob na tela
                # se der return ele sai da thread e para de rotacionar
                continue
            #pyautogui.press('esc') #tira o target pra sempre garantir bater no q ta mais perto
            pyautogui.press('space') # pra entre a rotação ele sempre ter um target
            execute_hotkey(attack['hotkey'], attack['delay'])
            

running = False
def key_code(key):
    global running
    if key == keyboard.Key.delete:
        print("Bot encerrado")
        return False # para o bot
    elif hasattr(key, 'char') and key.char == 'f': #rotacao skills
        if running == False:
            print("iniciando rotação de skills")
            running = True
            global th_start_rotate_skills_attack, event_rotate_skills, th_supplies, event_supplies
            
            event_rotate_skills = threading.Event()
            th_start_rotate_skills_attack = threading.Thread(target=rotate_skills_attack)
            th_start_rotate_skills_attack.start()

            event_supplies = threading.Event()
            th_supplies = threading.Thread(target=manager_supplies_rp, args=(event_supplies,)) # pq ta em outro arquivo tem q usar o args
            th_supplies.start()

            th_run = threading.Thread(target=run)
            th_run.start()
            
            execute_hotkey(RING_BOX)
            

            
            
        else:
            running = False
            print("parando rotacao de skills")
            
            event_rotate_skills.set() #desabilita a rotacao de skills
            event_supplies.set() # desabilitia o monitoring de vida e mana
            event_th.set()


            th_start_rotate_skills_attack.join()
            th_supplies.join()
            th_run.join()

import constants
def check_player_position():
    return pyautogui.locateOnScreen('imgs/char_map_position.png', confidence=0.8, region=constants.REGION_MAP)

def go_to_flag(instructions):
    try:
        # reduzindo o escopo da busca pra ficar mais rapido
        print('vai tentar localizar')
        pyautogui.press('7') # equipa mais felcha no quiver

        print(instructions)
        print(instructions['path'])
        flag = pyautogui.locateOnScreen(instructions['path'], 
                                    confidence=0.8,
                                    region=constants.REGION_MAP)
        print(flag)
        if not flag:
            print("problema ao encontrar a flag")
        else:
            print('encontrou vai buscar o centro')
            x,y = pyautogui.center(flag)
            print('vai mover o mouse para')
            print(x,y)
            pyautogui.moveTo(x,y)
            
            print('vai clicar')
            pyautogui.click()

            if flag: # apenas dorme se achar pra evitar delay ao começar no meio da cave
                print('vai dormir')
                pyautogui.sleep(instructions['wait'])
    except Exception as e:
        print('============')
        print("erro no go_to_flag")
        print(instructions)
        print(e)
        print('============')
        #raise e


def core(instruction):
    print("\n\n\n\n\n============")
    print(instruction)
    
    go_to_flag(instruction)
    # se conseguir ver o crosshair branquinho tenta ir novamente
    if check_player_position():
        print("aparentemente ta preso, vai chamar dnv")
        go_to_flag(instruction)
    

def run():
    with open('infos.json', 'r') as file:
        data = json.loads(file.read())

    while not event_th.is_set():
        for item in data:
            core(item)

with Listener(on_press=key_code) as listener:
    listener.join()



        
