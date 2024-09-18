from typing import Literal
from pydantic import BaseModel

from fill_class_from_yaml import fill_class_from_yaml

class GeneralConfig(BaseModel):
    vocation_been_used : Literal["paladin", "ek_solo", "ek_duo", "ms"] # any additions here need to also be reflected on constants.py
    
    hp_pct_to_use_big_heal: int
    hp_pct_to_use_light_heal: int

    hp_pct_to_pot_life: int

    mana_pct_to_use_pot: int

    # when false, it will only utani hur / eat food / utura gran
    auto_attack : bool

    food_to_eat: str
    utura_gran: str
    haste: str


    hp_pct_to_use_might_ring: int
    hp_pct_to_use_ssa: int


def get_general_config():
    return fill_class_from_yaml(GeneralConfig, "general_config.yaml")