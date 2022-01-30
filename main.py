import time
import pyautogui
from colorama import Fore


from modules.start_treasure_mode import start_treasure
from modules.count_down import counting_down
from modules.rest_all import rest_all
from modules.re_map import reset_map


print(Fore.GREEN + '--------------------------------------')
print('------> Bombcrypto BOT BY BABE <------')
print('--------------------------------------')
print('>> Start BOT NOW <<')
print('Process : Detecting Bombcrypto Monitor...')

monitor = pyautogui.getWindowsWithTitle("Bombcrypto - Google Chrome")
if len(monitor) == 0 :
    print(Fore.RED + 'You must restart this program again')
    exit()
time.sleep(2)
print(f'Process : Detected {len(monitor)} Bombcrypto')

while True:
    # Start Playing Each Monitor
    start_treasure.start()

    # Re-map
    print('Process : Remap')
    reset_map.re_map()

    # Countdown
    time.sleep(150)

    #Start Resting
    print('Process : Resting for 1 hour')
    rest_all.rest()

    #Countdown
    counting_down.start_count_down(delay_hr = 1, delay_min = 0, step = 'Start')