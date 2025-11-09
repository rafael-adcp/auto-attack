from pynput.keyboard import Listener
from pynput import keyboard


from log import get_logger

logger = get_logger(__name__)

key_to_trigger_eye = 'y'

logger.info("Bot is ready, press {key_to_trigger_eye} to start or 'delete' to exit")

def key_code(key):
    logger.info(key)
    if hasattr(key, 'char') and key.char == key_to_trigger_eye:
        logger.info("Bot encerrado")
        return False # para o bot


with Listener(on_press=key_code) as listener:
    listener.join()