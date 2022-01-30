import pyautogui
import time

from datetime import datetime

class start_treasure():
    def start():
        monitor = pyautogui.getWindowsWithTitle("Bombcrypto - Google Chrome")
        print('Process : Playing Treasure Mode for 30 minutes')

        for i in range(len(monitor)):
            monitor[i].minimize()
            monitor[i].maximize()

            # Start Playing
            now = datetime.now().strftime('%H:%M:%S')
            print(f'Process : Monitor {i + 1} Start Treasure Mode at {now}')
            pyautogui.click(1910, 80) # Scroll Up
            time.sleep(2)
            pyautogui.click(1026, 559) # Treasure Mode
            time.sleep(2)
            pyautogui.click(953, 707) # Arrow Up
            time.sleep(2)
            pyautogui.click(953, 683) # Heroes
            time.sleep(2)
            pyautogui.click(870, 291) # Start All
            time.sleep(2)
            pyautogui.click(1012, 243) # Close Popup
            time.sleep(2)
            pyautogui.click(946, 464) # Close Arrow Popup
            time.sleep(2)    
            monitor[i].restore()
            time.sleep(2)
            