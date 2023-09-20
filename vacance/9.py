import threading
import time

def numbering():
    while True:
        time.sleep(.5)
        print(f"${i1} {i2}$", end="")
def prnt2():
    
    while True:
        time.sleep(.5)
        if i1==5 and i2==6:
            print("  <----   ]                            -----", end="")
        elif i1==6 and i2==6:
            print("  <------ ]                            ------", end="")
        elif i1==6 and i2==5:
            print("  <----   ]                            -----", end="")
            break


def prnt3 ():
    global i1
    global i2
    i1=0
    i2=6
    while i1 <6:
        if i1==0 and i2==6:
            time.sleep(.5)
            print("    ----------------------------------------"+" "*i1+".")
            i1 +=1
        elif i1==5 and i2==6:
            time.sleep(.5)
            print(" "*i1+">")
            i1 +=1
        elif i1==4 and i2==6:
            time.sleep(.5)
            print("    |_____                                  "+" "*i1+".")
            i1 +=1
        elif i1==1 and i2==6:
            time .sleep(.5)
            print("    |                            __         "+" "*i1+".")
            i1 +=1
        elif i1==2 and i2==6:
            time .sleep(.5)
            print("    |                           |__|        "+" "*i1+".")
            i1 +=1
        else:
            time.sleep(.5)
            print("    |                                       "+" "*i1+".")
            i1 +=1


    while i2>=0:
        time.sleep(.6)
        if i1==6 and i2==0:
            print("    ----------------------------------------"+" "*i2+".")
            i2 -=1
        elif i1==6 and i2==4:
            print("    |¯¯¯¯¯                                  "+" "*i2+".")
            i2 -=1
        elif i2==6 :
            print(" "*(i2-1)+">")
            i2 -=1
        elif i2==5:
            print(" "*(i2)+">")
            i2 -=1
        else:
            print("    |                                        "+" "*(i2-1)+".")
            i2 -=1



# numbering=threading.Thread(target=numbering,daemon=True)
t2=threading.Thread(target=prnt2,daemon=True)
t3=threading.Thread(target=prnt3 )

# numbering.start()
t2.start()
t3.start()




