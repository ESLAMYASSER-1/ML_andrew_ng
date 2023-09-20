from pyautogui import * 
import pyautogui 
import time 
import keyboard
#import random
import win32api,win32con
import AppOpener

wtsimg="B:\PROGRAMMING\python\ADVANCED Python\wts.png"
img="B:\PROGRAMMING\python\ADVANCED Python\_forbidden.png"
typeimg="B:\PROGRAMMING\python\ADVANCED Python\_typemsg.png"


AppOpener.open("Opera GX Browser", match_closest=True)
time.sleep(2)
x,y=pyautogui.locateCenterOnScreen(wtsimg,confidence=.8)
pyautogui.leftClick(x,y)
time.sleep(10)
for i in range(300):
    try:
        x,y=pyautogui.locateCenterOnScreen(img,confidence=.8)
        m,z=x,y
    except:
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,m,z,2,0)
        x,y=pyautogui.locateCenterOnScreen(img,confidence=.8)
    pyautogui.leftClick(x,y)
    x,y=pyautogui.locateCenterOnScreen(typeimg,confidence=.8)
    pyautogui.leftClick(x,y)
    pyautogui.write("screpted msg")
    pyautogui.press('enter')
    
