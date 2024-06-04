from enum import Enum
REGION_BATTLE = (1572,24,157,37)




# encontrar_posicao_mini_mapa retornar a posicao
REGION_MAP = (1748, 24,116,114)

REGION_QUIVER = (1825, 188, 40, 42)


class Vocation(Enum):
    PALADIN = 1
    EK_SOLO = 2
    EK_DUO = 3
    SOMENTE_HEAL = 4

VOCACAO_EM_USO = Vocation.EK_SOLO