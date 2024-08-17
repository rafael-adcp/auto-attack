from pydantic import BaseModel
from typing import Literal, Union

from fill_class_from_json import fill_class_from_json
from config.general_config import get_general_config

class DefaultHotkey(BaseModel):
    ring_default: Union[str, int]
    necklace_default: Union[str, int]
    

    mana_potion: Union[str, int]

    ssa: Union[str, int]
    might_ring: Union[str, int]

    big_heal: Union[str, int]
    light_heal: Union[str, int]

class Paladin(DefaultHotkey):
    amp_res: Union[str, int]
    mas_san: Union[str, int]
    rune_to_use: Union[str, int]

    mana_pct_for_energy_ring: int
    energy_ring: Union[str, int]

    # so it knows which quiver to look after to check if it should equip more arrows or not
    quiver_been_used: Literal["brown","blue", "red", "jungle", "naga", "alicorn"]
    equip_more_arrows: Union[str, int]

    ultimate_spirit_potion: Union[str, int]

    # TODO: tapete and granada are not yet been used
    # tapete: Union[str, int]
    # granada: Union[str, int]

class Knight(DefaultHotkey):
    exeta: Union[str, int]
    exori: Union[str, int]
    exori_gran: Union[str, int]
    utito_tempo: Union[str, int]
    exori_mas: Union[str, int]
    utamo_tempo: Union[str, int]

    should_use_exeta: bool # when hunting solo and a monster that doesnt run
    supreme_potion: Union[str, int]

class MasterSorcerer(DefaultHotkey):
    rune_to_use: Union[str, int]
    utamo_vita: Union[str, int]
    remove_utamo_vita: Union[str, int]
    exura_vita: Union[str, int]


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
