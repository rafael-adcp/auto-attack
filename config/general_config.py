from typing import Literal
from pydantic import BaseModel

from fill_class_from_json import fill_class_from_json

class GeneralConfig(BaseModel):
    vocation_been_used : Literal["paladin", "ek_solo", "ek_duo", "ms"] # any additions here need to also be reflected on constants.py
    
    hp_pct_to_use_big_heal: int
    hp_pct_to_use_light_heal: int
    hp_pct_to_enter_survival_mode: int


def get_general_config():
    return fill_class_from_json(GeneralConfig, "general_config.json")