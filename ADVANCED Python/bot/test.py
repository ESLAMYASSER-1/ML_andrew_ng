import pyautogui
import AppOpener
import win32api,win32con
import time

x,y=pyautogui.position()
print(x,y)
time.sleep(3)
win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,x,y,1,0)