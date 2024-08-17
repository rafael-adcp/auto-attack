from log import get_logger
from config.character_hotkey import get_current_vocation_in_use_hotkey

logger = get_logger(__name__)
# this needs to happen before everything so we have the data saved
# allowing the threads to read them safely without running into a race condition
from locate_things_on_screen import LocateOnScreen
LocateOnScreen()
get_current_vocation_in_use_hotkey()