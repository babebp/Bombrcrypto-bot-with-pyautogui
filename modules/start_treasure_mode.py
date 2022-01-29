import pyautogui
import time

class start_treasure():
    def start():
        print('Process : Starting Treasure Mode')
        pyautogui.click(1910, 80) # Scroll Up
        time.sleep(1)
        pyautogui.click(1026, 559) # Treasure Mode
        time.sleep(1)
        pyautogui.click(953, 707) # Arrow Up
        time.sleep(2)
        pyautogui.click(953, 683) # Heroes
        time.sleep(1)
        pyautogui.click(870, 291) # Start All
        time.sleep(1)
        pyautogui.click(1012, 243) # Close Popup
        time.sleep(1)
        pyautogui.click(946, 464) # Close Arrow Popup
        time.sleep(1)
        print('Process : Playing Treasure Mode for 30 minutes')