import time
import pyautogui



class reset_map():
    def re_map():
        for j in range(10):
            monitor = pyautogui.getWindowsWithTitle("Bombcrypto - Google Chrome")
            for i in range(len(monitor)):
                monitor[i].minimize()
                monitor[i].maximize()
                time.sleep(1)
                pyautogui.click(516, 161) # Back to main menu
                time.sleep(1)
                pyautogui.click(1026, 559) # Treasure Mode
                time.sleep(1)
                monitor[i].restore()
            time.sleep(165)