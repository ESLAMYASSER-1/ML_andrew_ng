from cgitb import text
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry('640x480+300+300')

def solve():
  messagebox.showinfo("info","solved").pack()


tk.Button(
  root, text="Solve the world's problems", command=solve
).pack()


root.mainloop()