import pyautogui

WIDTH = 92 # size of the full bar

def calcula_width(percent):
    return int ((WIDTH * percent) / 100)

def get_position(region, percent):
    result_percent = calcula_width(percent)
    x = region[0] + result_percent
    y = region[1] + region[3]
    
    return x, y

# logger.info(pixel_match_color(MANA_REGION, 50, MANA_COLOR))
def pixel_match_color(region, percent, color):
    x,y = get_position(region, percent)
    return pyautogui.pixelMatchesColor(int(x), int(y), color, 10)
