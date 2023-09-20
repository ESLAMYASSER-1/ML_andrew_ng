from turtle import Turtle , Screen
from time import sleep
T1 = Turtle()
T1.shape("turtle")
T1.color("orange")
sleep(1)
def x1():
    T1.forward(100)
    T1.left(90)
    T1.forward(100)
    x1()

T2 = Turtle()
T2.shape("arrow")
T2.color("green")
def x2():
    T2.right(180)
    T2.forward(50)
    T2.right(180)
    T2.forward(50)
    x2()


screen = Screen()
screen.onscreenclick(T1.goto)
T1.getscreen()._root.mainloop()
T2.getscreen()._root.mainloop()