from pynput.keyboard import Listener
from pynput import keyboard
import keyboard as kdebug
import pyautogui
import constants

pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

import threading

from vida_mana import manager_supplies_rp



# while True:
#     kdebug.wait('h')
#     print(pyautogui.locateOnScreen('battle_region.png', confidence=0.8))

def execute_hotkey(hotkey, delay = None):
    pyautogui.press(hotkey)
    if delay:
        pyautogui.sleep(delay)


def rotate_skills_attack():
    list_hotkeys_para_usar = None
    if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
        list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_PALADIN
    elif constants.VOCACAO_EM_USO == constants.Vocation.EK_DUO:
        list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_KNIGH_DUO
    elif constants.VOCACAO_EM_USO == constants.Vocation.EK_SOLO:
        list_hotkeys_para_usar = constants.LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA        

    print("vai usar")
    print(list_hotkeys_para_usar)
    while not event_rotate_skills.is_set() and list_hotkeys_para_usar != None:
        for attack in list_hotkeys_para_usar:
            if event_rotate_skills.is_set():
                return # caso acabe a box no meio n precisa terminar a rotacao
            
            if pyautogui.locateOnScreen('battle_region.png', confidence=0.8, region=constants.REGION_BATTLE):
                # evita ficar castando magias se nao tiver mob na tela
                # se der return ele sai da thread e para de rotacionar
                continue

            if constants.VOCACAO_EM_USO == constants.Vocation.PALADIN:
                # se o quiver estiver vazio, refila ele
                if pyautogui.locateOnScreen('quiver_vazio.png', confidence=0.98, region=constants.REGION_QUIVER):
                    # equipa mais felcha no quiver
                    # idealmente #TODO: checar se tem flechas pra equipar, se nao qndo tiver no final da hunt vai ficar spamando atoa
                    pyautogui.press('7')
                    pyautogui.press('7')
                    pyautogui.press('7')

            #apenas come qndo o icone de fome aparecer, evitar ficar spamando
            if pyautogui.locateOnScreen('starving.png', confidence=0.8):
                pyautogui.press('0') # mushroom

            # apenas usa utura gran, caso o icone nao esteja na barrinha de status
            if not pyautogui.locateOnScreen('utura_gran.png', confidence=0.98):
                pyautogui.press('9') # utura gran

            if constants.VOCACAO_EM_USO != constants.Vocation.SOMENTE_HEAL:
                pyautogui.press('esc') #tira o target pra sempre garantir bater no q ta mais perto
                pyautogui.press('space') # pra entre a rotação ele sempre ter um target
                #print(f"vai usar: ", attack['descricao'])
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
            
        else:
            running = False
            print("parando rotacao de skills")
            
            event_rotate_skills.set() #desabilita a rotacao de skills
            event_supplies.set() # desabilitia o monitoring de vida e mana

            th_start_rotate_skills_attack.join()
            th_supplies.join()

with Listener(on_press=key_code) as listener:
    listener.join()