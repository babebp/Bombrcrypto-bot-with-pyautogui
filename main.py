import pyautogui
import datetime
import time
from datetime import datetime


from modules.find_monitor import finding_monitor
from modules.start_treasure_mode import start_treasure
from modules.count_down import counting_down
from modules.rest_all import rest_all
from modules.re_map import reset_map


print('--------------------------------------')
print('------> Bombcrypto BOT BY BABE <------')
print('--------------------------------------')
print('>> Start BOT NOW <<')
print('Process : Detecting Bombcrypto Monitor...')

monitor = finding_monitor.find_monitor()
time.sleep(2)
print(f'Process : Detected {len(monitor)} Bombcrypto')

while True:
    # Start Playing Each Monitor
    for i in range(len(monitor)):
        monitor[i].minimize()
        monitor[i].maximize()

        # Start Playing
        now = datetime.now().strftime('%H:%M:%S')
        print(f'Process : Start Treasure Mode at {now}')
        start_treasure.start()
        monitor[i].restore()

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