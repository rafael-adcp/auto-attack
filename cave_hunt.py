from pynput.keyboard import Listener
from pynput import keyboard
import pyautogui
pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

import threading

from vida_mana import manager_hp_and_mp
from rotacao_skills import rotate_skills_attack
from cacarecos import manager_cacarecos

import json

REGION_MAP = (1748, 24,116,114) # TODO: fazer isso aqui ler dinamico

# hotekeys in game
RING_BOX = '1'
RING_LURANDO = '2'
COMER_FOOD = '3'



REGION_BATTLE = (1572,24,157,37) # TODO: utilizar o valor via a classe nova, pra ficar 100% dinamico

global event_th
event_th = threading.Event()

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
            global th_start_rotate_skills_attack, event_rotate_skills, th_supplies, event_supplies, th_cacarecos, event_cacarecos
            
            event_rotate_skills = threading.Event()
            th_start_rotate_skills_attack = threading.Thread(target=rotate_skills_attack, args=(event_rotate_skills,)) # pq ta em outro arquivo tem q usar o args
            th_start_rotate_skills_attack.start()

            event_supplies = threading.Event()
            th_supplies = threading.Thread(target=manager_hp_and_mp, args=(event_supplies,)) # pq ta em outro arquivo tem q usar o args
            th_supplies.start()

            event_cacarecos =  threading.Event()
            th_cacarecos = threading.Thread(target=manager_cacarecos, args=(event_cacarecos,)) # pq ta em outro arquivo tem q usar o args
            th_cacarecos.start()

            th_run = threading.Thread(target=run)
            th_run.start()
            

            
            
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
    return pyautogui.locateOnScreen('char_map_position.png', confidence=0.8, region=REGION_MAP)

def go_to_flag(instructions):
    try:
        # reduzindo o escopo da busca pra ficar mais rapido
        print('vai tentar localizar')
        pyautogui.press('7') # equipa mais felcha no quiver

        print(instructions)
        print(instructions['path'])
        flag = pyautogui.locateOnScreen(instructions['path'], 
                                    confidence=0.8,
                                    region=REGION_MAP)
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
    
    while not pyautogui.locateOnScreen('imgs/battle_region_empty.png', confidence=0.8, region=constants.REGION_BATTLE):
        # sleeping so it can kill monsters
        pyautogui.sleep(0.5)
    
    go_to_flag(instruction)
    # se conseguir ver o crosshair branquinho tenta ir novamente
    while check_player_position():
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



        
