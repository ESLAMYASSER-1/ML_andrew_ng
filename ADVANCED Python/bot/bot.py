from pyautogui import * 
import pyautogui 
import time 
import keyboard
import random
import win32api,win32con

#X:  606 Y:  670 RGB: (253,  18,   1)
#X:  679 Y:  670 RGB: (163, 168, 232)
#X:  782 Y:  670 RGB: (173, 177, 233)
#X:  853 Y:  670 RGB: (168, 172, 232)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(794,440)[0]==0:
        click(794,440)
    if pyautogui.pixel(921,440)[0]==0:
        click(921,440)
    if pyautogui.pixel(1022,440)[0]==0:
        click(1022,440)
    if pyautogui.pixel(1124,440)[0]==0:
        click(1124,440)
