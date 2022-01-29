from asyncio import sleep
import time

class counting_down():
    def start_count_down(delay_hr, delay_min, step):
        delay_sec = (delay_hr*3600) + (delay_min*60)
        count = 0
        for i in range(delay_sec):
            time.sleep(1)
            count += 1
            if count == 60:
                count = 0
                delay_min -= 1
                if delay_min < 0:
                    delay_hr -= 1
                    delay_min = 59
                print(f'Time remaining : {delay_hr} hr {delay_min} min ==> {step}' )