import pyautogui
from log import get_logger
import pytesseract
from PIL import Image
import hashlib

from locate_things_on_screen import PositionsCacheTable, PossibleRegions

logger = get_logger(__name__)
pyautogui.useImageNotFoundException(False) # caso pyauto gui n ache n gera exception

positions_cache_table = PositionsCacheTable()
EQUIPS_REGION = positions_cache_table.data[PossibleRegions.REGION_EQUIPS.name]

def sell_loot():
    missing_backpack = pyautogui.locateOnScreen("imgs/no_bp_equipped.png", region=EQUIPS_REGION)
    
    if missing_backpack:
        logger.error("You are missing a bp equipped, without one you can't sell loot, otherwise all money would go on the floor")
    else:
        pyautogui.press(";")
        pyautogui.sleep(1)
        pyautogui.press(".")
        
        pyautogui.sleep(2)
        sell_loot_panel = pyautogui.locateOnScreen("imgs/npc_sell_loot_panel.png")
        if not sell_loot_panel:
            logger.info("could not find sell loot dialog")
        else:
            sell_items(sell_loot_panel)


images_text_hash = {}


def generate_image_hash(image):
    # Open the image
    
    # Convert the image to grayscale
    image = image.convert("L")

    # Flatten the image into a 1D array of pixel values
    pixels = list(image.getdata())

    # Create a hash value from the pixel values
    hash_value = hashlib.md5("".join(str(pixel) for pixel in pixels).encode()).hexdigest()

    return hash_value

def sell_items(sell_loot_panel):
    images_text_hash = {}
    logger.info("will start selling loot")
    sell_button = pyautogui.locateOnScreen("imgs/sell_button.png")
    pyautogui.click(sell_button)
    
    ABORT_SELLING = 10            

    ok_button = pyautogui.locateOnScreen("imgs/ok_button.png")

    should_not_sell = [
        "MIGHT RING",
        "STONE SKIN AMU.",
        "COLLAR OF BLUE P.",
        "RING OF BLUE PLA.",
        "ENERGY RING",
        "DWARVEN RING",
        "SPEAR",
        "GLACIER AMULET"
    ]
    

    hash_passado = None
    screen_height = pyautogui.size()[1]
    sell_loot_panel_box = (
        int(sell_loot_panel[0]), 
        int(sell_loot_panel[1]), 
        int(sell_loot_panel[2]), 
        screen_height 
    )

    pyautogui.screenshot("aaaaa.png", region=sell_loot_panel_box)

    while ABORT_SELLING <= 10:
        pyautogui.sleep(1)
        items_to_sell = pyautogui.locateAllOnScreen("imgs/item_to_sell.png", region=sell_loot_panel_box, confidence=0.99)
        
        for something_to_sell in items_to_sell:
            # pyautogui.moveTo(
            #     something_to_sell[0],
            #     something_to_sell[1]
            # )
            # Get the screen position of the item
            x, y = int(something_to_sell[0]), int(something_to_sell[1]-15)
            img = pyautogui.screenshot(region=(x, y, 100, 20))  # adjust the region to capture the text
            
            # generate a hash of the image to avoid reprocessing similar things
            img_hash = generate_image_hash(img)
            
            if hash_passado == img_hash: #avoid endless loop
                ABORT_SELLING = True
                continue

            hash_passado = img_hash
            
            # OCR is a very costly process, so we cache the results to speed things up
            item_name = ""
            if img_hash in images_text_hash:
                item_name = images_text_hash[img_hash]
            else:
                # Perform OCR to extract the text
                text = pytesseract.image_to_string(img)
                item_name = text.strip().upper()
                images_text_hash[img_hash] = item_name

            
            
            # do a trim on the item name
            item_name = item_name.strip()
            # check if its "" aka wasantable to identify the name
            if item_name == "":
                logger.info("could not find item name on the image")
                # save the file for future inpsection
                img.save(f"could_not_find_name_{img_hash}.png")
                del images_text_hash[img_hash]
                continue
            
            # check if the item should be sold or not
            if item_name not in should_not_sell:
                gems_not_to_sell = [
                    "marks",
                    "sage",
                    "guard",
                    "mystic"
                ]

                #check if item_name constains any of the gems_not_to_sell
                is_a_gem = False
                for gem in gems_not_to_sell:
                    if gem.upper() in item_name:
                        is_a_gem = True
                        logger.info(f"skipping item >>>> '{item_name}' bkz found '{gem}' on the name <<<")
                        continue
                        
                
                if not is_a_gem:
                    # Sell the item
                    pyautogui.click(something_to_sell)
                    
                    if pyautogui.locateOnScreen("imgs/nothing_to_sell.png", confidence=0.88):
                        ABORT_SELLING = ABORT_SELLING + 1
                        logger.info("finished selling loot")
                        images_text_hash = {}
                        break
                    logger.info(f"selling item >>>>'{item_name}'<<<")
                    pyautogui.click(ok_button)
                    
                    # every time an item is sold, the grid position change, so we need to restart the loop
                    break

