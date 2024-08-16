from enum import Enum
REGION_BATTLE = (1572,24,157,37) # TODO:: remove this once migrated to locate on screen.py (cacarecos still using it)

HOTKEY_RING_DEFAULT = '4'
HOTKEY_NECKLACE_DEFAULT = '7'

# RP CONFIGS
REGION_QUIVER = (1825, 188, 40, 42) # TODO:: remove this once migrated to locate on screen.py
MANA_PCT_FOR_ENERGY_RING = 40

# when false, it will only utani hur ; eat food / utura gran
AUTO_ATACK = True

class Vocation(Enum):
    PALADIN = 1
    EK_SOLO = 2
    EK_DUO = 3
    MS = 4

VOCACAO_EM_USO = Vocation.PALADIN


LIST_HOTKEYS_ATTACK_PALADIN = [
    
    {"hotkey": 'g', "delay": 0.2, "descricao": "amp res"} , 
    #{"hotkey": 'o', "delay": 0.2, "descricao": "tapete"} , 
    #{"hotkey": 'p', "delay": 1, "descricao": "granada"} , 
    # as habilidades da roda nao impactam as de ataque

    {"hotkey": 'F3', "delay": 2, "descricao": "mas san"} ,
    {"hotkey": 'F6', "delay": 0.8, "descricao": "avalanche"}, 
        # 0.8 eh so qndo tem o amp res
        # 2 eh qndo n usa ampres
    #dps da ultima spell n precisa de delay
]


# exori + exeta
# utito + exori mas
# Exori 
# Exori gran + exeta
# Exori
exori_hotkey = 'F6'
exeta_hotkey = 'F3'
LIST_HOTKEYS_ATTACK_KNIGH_DUO = [
    {"hotkey": 'j', "delay": 0.2, "descricao": "amp res"} , 
    {"hotkey": exori_hotkey, "delay": 0.5, "descricao": "exori"} , 
    {"hotkey": exeta_hotkey, "delay": 2, "descricao": "exeta"} , 
    {"hotkey": 'F8', "delay": 0.3, "descricao": "UTITO"} , 
    {"hotkey": 'F7', "delay": 2, "descricao": "exori mas"} , 
    {"hotkey": exori_hotkey, "delay": 2, "descricao": "exori"} , 
    {"hotkey": 'F5', "delay": 0.3, "descricao": "Exori gran"} , 
    {"hotkey": exeta_hotkey, "delay": 0.3, "descricao": "exeta"} , 
    {"hotkey": exori_hotkey, "delay": 0.1, "descricao": "exori"} , 
    
    #dps da ultima spell n precisa de delay    
]

LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA = []
for item in LIST_HOTKEYS_ATTACK_KNIGH_DUO:
    if item['descricao'] != "exeta":
        LIST_HOTKEYS_ATTACK_KNIGH_SEM_EXETA.append(item)


LIST_HOTKEYS_ATTACK_MS = [
    {"hotkey": 'F6', "delay": 1.8, "descricao": "avalanche"}, 
    {"hotkey": 'F6', "delay": 1.8, "descricao": "avalanche"}, 
    {"hotkey": 'F6', "delay": 1.8, "descricao": "avalanche"}, 
    {"hotkey": 'F6', "delay": 1.8, "descricao": "avalanche"}, 
]