import pyautogui

class finding_monitor:
    def find_monitor():
        monitor = pyautogui.getWindowsWithTitle("Bombcrypto - Google Chrome")
        return monitor