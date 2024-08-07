from pynput.keyboard import Listener
from pynput import keyboard
import pyautogui

pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

import threading

from vida_mana import manager_supplies_rp
from rotacao_skills import rotate_skills_attack
from cacarecos import manager_cacarecos

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
            # se estivesse no msm arquivo seria somente th_start_rotate_skills_attack = threading.Thread(target=rotate_skills_attack)
            th_start_rotate_skills_attack.start()

            event_supplies = threading.Event()
            th_supplies = threading.Thread(target=manager_supplies_rp, args=(event_supplies,)) # pq ta em outro arquivo tem q usar o args
            th_supplies.start()


            event_cacarecos =  threading.Event()
            th_cacarecos = threading.Thread(target=manager_cacarecos, args=(event_cacarecos,)) # pq ta em outro arquivo tem q usar o args
            th_cacarecos.start()
        else:
            running = False
            print("parando rotacao de skills")
            
            event_rotate_skills.set() #desabilita a rotacao de skills
            # life / mana should always be monitored
            #event_supplies.set() # desabilitia o monitoring de vida e mana

            th_start_rotate_skills_attack.join()
            #th_supplies.join()


            #th_cacarecos.join() # desabilita os cacarecos
            event_cacarecos.set()

with Listener(on_press=key_code) as listener:
    listener.join()