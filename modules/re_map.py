import time
import pyautogui

from find_monitor import finding_monitor

class reset_map():
    def re_map():
        for j in range(10):
            monitor = finding_monitor.find_monitor()
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