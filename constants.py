from enum import Enum

from config.character_hotkey import get_current_vocation_in_use_hotkey
from config.general_config import get_general_config

general_config = get_general_config()
current_vocation_hotkey = get_current_vocation_in_use_hotkey()

class Vocation(Enum): # this should always be up to date with general_config.py
    PALADIN = 'paladin'
    EK_SOLO = 'ek_solo'
    EK_DUO = 'ek_duo'
    MS = 'ms'


def get_hotkey_rotation_to_use():
    list_hotkeys_para_usar = None
    if general_config.vocation_been_used == Vocation.PALADIN.value:
        list_hotkeys_para_usar = get_rp_hotkeys()
    elif general_config.vocation_been_used == Vocation.EK_DUO.value:
        list_hotkeys_para_usar = get_ek_hotkeys()
    elif general_config.vocation_been_used == Vocation.EK_SOLO.value:
        list_hotkeys_para_usar = get_ek_hotkeys(False)
    # elif general_config.vocation_been_used == constants.Vocation.MS.value:
    #     list_hotkeys_para_usar = get_ms_hotkeys()
    return list_hotkeys_para_usar

def get_rp_hotkeys():
    return [
        {"hotkey": current_vocation_hotkey.amp_res, "delay": 0.2, "descricao": "amp res"} , 
        #{"hotkey": 'o', "delay": 0.2, "descricao": "tapete"} , 
        #{"hotkey": 'p', "delay": 1, "descricao": "granada"} , 
        # as habilidades da roda nao impactam as de ataque

        {"hotkey": current_vocation_hotkey.mas_san, "delay": 2, "descricao": "mas san"} ,
        {"hotkey": current_vocation_hotkey.rune_to_use, "delay": 0.8, "descricao": "avalanche"}, 
            # 0.8 eh so qndo tem o amp res
            # 2 eh qndo n usa ampres
        #dps da ultima spell n precisa de delay
    ]

def get_ek_hotkeys(exeta = True):
    # Para duo:
    #     exori + exeta
    #     utito + exori mas
    #     Exori 
    #     Exori gran + exeta
    #     Exori
    LIST_HOTKEYS = [
            {"hotkey": current_vocation_hotkey.amp_res, "delay": 0.2, "descricao": "amp res"} , 
            {"hotkey": current_vocation_hotkey.exori, "delay": 0.5, "descricao": "exori"} , 
            {"hotkey": current_vocation_hotkey.exeta, "delay": 2, "descricao": "exeta"} , 
            {"hotkey": current_vocation_hotkey.utito_tempo, "delay": 0.3, "descricao": "UTITO"} , 
            {"hotkey": current_vocation_hotkey.exori_mas, "delay": 2, "descricao": "exori mas"} , 
            {"hotkey": current_vocation_hotkey.exori, "delay": 2, "descricao": "exori"} , 
            {"hotkey": current_vocation_hotkey.exori_gran, "delay": 0.3, "descricao": "Exori gran"} , 
            {"hotkey": current_vocation_hotkey.exeta, "delay": 0.3, "descricao": "exeta"} , 
            {"hotkey": current_vocation_hotkey.exori, "delay": 0.1, "descricao": "exori"} , 
            
            #dps da ultima spell n precisa de delay    
        ]
    
    if not exeta:
        LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA = []
        for item in LIST_HOTKEYS:
            if item['descricao'] != "exeta":
                LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA.append(item)
        LIST_HOTKEYS = LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA

    return LIST_HOTKEYS

def get_ms_hotkeys():
    return [
        {"hotkey": current_vocation_hotkey.rune_to_use, "delay": 1.8, "descricao": "avalanche"}, 
        {"hotkey": current_vocation_hotkey.rune_to_use, "delay": 1.8, "descricao": "avalanche"}, 
        {"hotkey": current_vocation_hotkey.rune_to_use, "delay": 1.8, "descricao": "avalanche"}, 
        {"hotkey": current_vocation_hotkey.rune_to_use, "delay": 1.8, "descricao": "avalanche"}, 
    ]