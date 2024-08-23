from pydantic import BaseModel
from typing import Literal

from fill_class_from_json import fill_class_from_json
from config.general_config import get_general_config

# PS hotkeys CANNOT BE INT, THEY NEED TO BE STR OTHERWISE PYGUI WILL ERROR

class DefaultHotkey(BaseModel):
    ring_default: str
    necklace_default: str
    

    mana_potion: str

    ssa: str
    might_ring: str

    big_heal: str
    light_heal: str

class Paladin(DefaultHotkey):
    amp_res: str
    mas_san: str
    rune_to_use: str

    mana_pct_for_energy_ring: int
    hp_pct_for_energy_ring: int
    energy_ring: str

    # so it knows which quiver to look after to check if it should equip more arrows or not
    quiver_been_used: Literal["brown","blue", "red", "jungle", "naga", "alicorn"]
    equip_more_arrows: str

    ultimate_spirit_potion: str

    # TODO: tapete and granada are not yet been used
    # tapete: str
    # granada: str

class Knight(DefaultHotkey):
    exeta: str
    exori: str
    exori_gran: str
    utito_tempo: str
    exori_mas: str
    utamo_tempo: str

    should_use_exeta: bool # when hunting solo and a monster that doesnt run
    supreme_potion: str
    amp_res: str

class MasterSorcerer(DefaultHotkey):
    rune_to_use: str
    utamo_vita: str
    remove_utamo_vita: str
    exura_vita: str


def get_paladin_hotkey_config():
    
    return fill_class_from_json(Paladin, 'rp_hotkey.json')

def get_ek_hotkey_config():
    return fill_class_from_json(Paladin, 'ek_hotkey.json')

def get_ms_hotkey_config():
    return fill_class_from_json(Paladin, 'ms_hotkey.json')


def get_current_vocation_in_use_hotkey():
    general_config = get_general_config()
    hotkeys = None

    if general_config.vocation_been_used == "paladin":
        hotkeys = get_paladin_hotkey_config()
    elif general_config.vocation_been_used in ["ek_solo", "ek_duo"]:
        hotkeys = get_ms_hotkey_config()
    elif general_config.vocation_been_used == "ms":
        hotkeys = get_ek_hotkey_config    

    if hotkeys is None:
        raise Exception("Somethiong went wrong while reading the hotkeys for {}".format(general_config.vocation_been_used))

    return hotkeys
