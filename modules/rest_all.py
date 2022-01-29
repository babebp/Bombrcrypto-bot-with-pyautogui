import pyautogui
import time

from find_monitor import finding_monitor

class rest_all():
    def rest():
        monitor = finding_monitor.find_monitor()
        for i in range(len(monitor)):
            monitor[i].minimize()
            monitor[i].maximize()
            print(f'Status : Resting Monitor {i + 1}')
            pyautogui.click(953, 707) # Arrow Up
            time.sleep(2)
            pyautogui.click(953, 683) # Heroes
            time.sleep(1)
            pyautogui.click(931, 291) # Rest All
            time.sleep(1)
            pyautogui.click(1012, 243) # Close Popup
            time.sleep(1)
            pyautogui.click(946, 464) # Close Arrow Popup
            time.sleep(1)
            pyautogui.click(516, 161) # Back to main menu
            time.sleep(1)
            monitor[i].restore()