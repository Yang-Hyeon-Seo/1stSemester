from tkinter import *
import time
import random

tk=Tk()
canvas=Canvas(tk, height=500, width=500)
canvas.pack()

A=(250,10)
B=(10, 490)
C=(490,490)

cho=[A, B, C]
point=[250,250]#기준점

for i in range(50000):
    choose = random.choice(cho)
    if choose == A:
        color='red'
    elif choose == B:
        color = 'blue'
    else:
        color = 'yellow'
    point[0] = (point[0]+choose[0])/2
    point[1] = (point[1]+choose[1])/2
    canvas.create_line(point[0], point[1], point[0]+1, point[1]+1, fill=color)

    tk.update()
    
    
