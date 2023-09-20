import pyautogui as auto 
import time 
import AppOpener as opener

opener.open("Opera GX Browser",match_closest=True)
time.sleep(2)
try:
    x, y =auto.locateCenterOnScreen("wts.png")
except:
    x, y =auto.locateCenterOnScreen("whats.png")
time.sleep(1)
auto.leftClick(x,y,1,0)
time.sleep(10)
try:
    x,y=auto.locateCenterOnScreen("khalid.png")
except:
    x,y=auto.locateCenterOnScreen("sabry.png")
time.sleep(1)
auto.leftClick(x,y,1,0)
time.sleep(1)
try:
    x,y=auto.locateCenterOnScreen("typemsg.png")
except:
    x,y=auto.locateCenterOnScreen("htypemsg.png")
auto.leftClick(x,y,1,0)
time.sleep(1)
auto.write("scripted msg")
auto.press("enter")