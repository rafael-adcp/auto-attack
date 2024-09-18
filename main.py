from pynput.keyboard import Listener
from pynput import keyboard
import threading

from log import get_logger

logger = get_logger(__name__)

# anything that depends on screen poisition needs to be here, aka after the data is populated on previous step
from vida_mana import manager_supplies_rp
from rotacao_skills import rotate_skills_attack
from cacarecos import manager_cacarecos

from thread_manager import ThreadManager

global thread_manager
thread_manager = ThreadManager()
running = False

def key_code(key):
    global running
    if key == keyboard.Key.delete:
        logger.info("Bot encerrado")
        return False # para o bot
    elif hasattr(key, 'char') and key.char == 'f': #rotacao skills
        if running == False:
            logger.info("Starting bot")
            running = True
            thread_manager.create_thread('rotate_skills_attack', rotate_skills_attack)
            thread_manager.create_thread('manager_supplies_rp', manager_supplies_rp, should_be_stopped=False)
            thread_manager.create_thread('manager_cacarecos', manager_cacarecos, should_be_stopped=False)
        else:
            running = False
            logger.info("parando o bot (algumas coisas podem continuar rodando, por exemplo healing)")
            thread_manager.stop_all_threads()
            logger.info("Bot parado")

logger.info("Bot is ready, press 'f' to start or 'delete' to exit")

with Listener(on_press=key_code) as listener:
    listener.join()