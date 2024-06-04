from pynput.keyboard import Listener
from pynput import keyboard
import keyboard as kdebug
import pyautogui
import constants

pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

import threading

from vida_mana import manager_supplies_rp

# hotekeys in game
RING_BOX = '1'
RING_LURANDO = '2'
COMER_FOOD = '3'



# while True:
#     kdebug.wait('h')
#     print(pyautogui.locateOnScreen('battle_region.png', confidence=0.8))

def execute_hotkey(hotkey, delay = None):
    pyautogui.press(hotkey)
    if delay:
        pyautogui.sleep(delay)

LIST_HOTKEYS_ATTACK = [
    
    {"hotkey": 'g', "delay": 0.8, "descricao": "amp res"} , 
    {"hotkey": 'o', "delay": 0.8, "descricao": "tapete"} , 
    {"hotkey": 'p', "delay": 1, "descricao": "granada"} , 
    # as habilidades da roda nao impactam as de ataque

    {"hotkey": 'F3', "delay": 2, "descricao": "mas san"} ,
    {"hotkey": 'F6', "delay": 0.8, "descricao": "avalanche"},
    #dps da ultima spell n precisa de delay
]

def rotate_skills_attack():
    while not event_rotate_skills.is_set():
        for attack in LIST_HOTKEYS_ATTACK:
            if event_rotate_skills.is_set():
                return # caso acabe a box no meio n precisa terminar a rotacao
            
            if pyautogui.locateOnScreen('battle_region.png', confidence=0.8, region=constants.REGION_BATTLE):
                # evita ficar castando magias se nao tiver mob na tela
                # se der return ele sai da thread e para de rotacionar
                continue

            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                # se o quiver estiver vazio, refila ele
                if pyautogui.locateOnScreen('quiver_vazio.png', confidence=0.8, region=constants.REGION_QUIVER):
                    # equipa mais felcha no quiver
                    # idealmente #TODO: checar se tem flechas pra equipar, se nao qndo tiver no final da hunt vai ficar spamando atoa
                    pyautogui.press('7')
                    pyautogui.press('7')
                    pyautogui.press('7')

            #apenas come e bate utura gran qndo o icone de fome aparecer, evitar ficar spamando
            if pyautogui.locateOnScreen('starving.png', confidence=0.8):
                print("deveria bater as coisas")
                pyautogui.press('9') # utura gran
                pyautogui.press('0') # mushroom

            if constants.VOCACAO_EM_USO != constants.Vocation.SOMENTE_HEAL:
                pyautogui.press('esc') #tira o target pra sempre garantir bater no q ta mais perto
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
            #th_start_rotate_skills_attack.start()

            event_supplies = threading.Event()
            th_supplies = threading.Thread(target=manager_supplies_rp, args=(event_supplies,)) # pq ta em outro arquivo tem q usar o args
            th_supplies.start()
            
            execute_hotkey(RING_BOX)
            

            
            
        else:
            running = False
            print("parando rotacao de skills")
            execute_hotkey(RING_LURANDO)
            execute_hotkey(COMER_FOOD)
            
            event_rotate_skills.set() #desabilita a rotacao de skills
            event_supplies.set() # desabilitia o monitoring de vida e mana

            th_start_rotate_skills_attack.join()
            th_supplies.join()

with Listener(on_press=key_code) as listener:
    listener.join()