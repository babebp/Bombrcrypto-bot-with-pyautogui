import pyautogui
import datetime
import time
from datetime import datetime


from modules.find_monitor import finding_monitor
from modules.start_treasure_mode import start_treasure
from modules.count_down import counting_down


print('--------------------------------------')
print('------> Bombcrypto BOT BY BABE <------')
print('--------------------------------------')
print('>> Start BOT NOW <<')
print('Process : Detecting Bombcrypto Monitor...')

monitor = finding_monitor.find_monitor()
time.sleep(2)
print(f'Process : Detected {len(monitor)} Bombcrypto')

for i in range(len(monitor)):
    monitor[i].minimize()
    monitor[i].maximize()

    #Start Playing
    now = datetime.now().strftime('%H:%M:%S')
    print(f'Process : Start Treasure Mode at {now}')
    start_treasure.start()

    #Countdown
    time.sleep(1800)

    #Start Resting








    


