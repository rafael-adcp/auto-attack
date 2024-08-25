import pyautogui
import cv2
from PIL import Image
import keyboard


import os

#place with screenshots to search on
SEARCH_ON_PATH = "./poc"

WHAT_TO_SEARCH_PATH = "./imgs"

# get all files from folder
for what_to_search  in os.listdir(WHAT_TO_SEARCH_PATH):
    for monitor_screenshot in os.listdir(SEARCH_ON_PATH):
        if not monitor_screenshot.endswith(".py"):
            print(f"\n\nsearching for {what_to_search} in {monitor_screenshot}")

            what_to_search_file_name = what_to_search
            monitor_screenshot_file_name = monitor_screenshot

            
            # Load the screenshot
            screenshot = cv2.imread(f'{SEARCH_ON_PATH}/{monitor_screenshot_file_name}')

            # Load the template image of the "battle list" panel
            template = cv2.imread(f'{WHAT_TO_SEARCH_PATH}/{what_to_search_file_name}')

            # Convert both images to grayscale
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

              # Apply binarization (thresholding)
            _, binary_template = cv2.threshold(gray_template, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            _, binary_screenshot = cv2.threshold(gray_screenshot, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

                # Use binary images for matching
            result = cv2.matchTemplate(binary_screenshot, binary_template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)


            # Get the coordinates of the match
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            print(max_val)
            # Check if the "battle list" panel was found
            if max_val > 0.3:
                # Get the coordinates of the top-left corner of the panel
                x, y = max_loc

                # Print the coordinates
                print(f"'{what_to_search_file_name}' panel found on {monitor_screenshot_file_name} at coordinates (x, y) = ({x}, {y})")

                # Draw a rectangle around the located panel
                cv2.rectangle(screenshot, (x, y), (x + template.shape[1], y + template.shape[0]), (0, 0, 255), 2)
                

                # Display the result
                cv2.imshow('Result', screenshot)
                # save the highlighted file to a different file
                cv2.imwrite(f"highlighted_{what_to_search_file_name}_{monitor_screenshot_file_name}.png", screenshot)
                
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print(f"'{what_to_search_file_name}' panel not found on {monitor_screenshot_file_name}")

    break


