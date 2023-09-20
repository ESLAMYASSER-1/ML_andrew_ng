import time 
import threading
def H_line():
    l=0
    while l<10:
        time.sleep(.5)
        print("-", end="")
        l+=1

threading.Thread(target=H_line).start()