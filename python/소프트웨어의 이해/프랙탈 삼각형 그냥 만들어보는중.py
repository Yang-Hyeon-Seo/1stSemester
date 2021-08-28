from tkinter import *
import random
import time
tk=Tk()
canvas=Canvas(tk, width=500, height=500)
canvas.pack()
#canvas.create_polygon(500,100, 900,900, 100, 900)
canvas.create_line(250,50,450,450)
canvas.create_line(250,50,50,450)
canvas.create_line(450,450,50,450)
A=(250,50)
B=(450,450)
C=(50,450)
point=[A, B, C]
middle=[0,0]
for i in range(50000):
    P=random.choice(point)
    print(P)
    
    x_middle=(P[0]+middle[0])/2
    middle[0]=x_middle
    y_middle=(P[1]+middle[1])/2
    middle[1]=y_middle

    canvas.create_line(middle[0], middle[1], middle[0]+1, middle[1]+1)

    tk.update() 
    time.sleep(0.0005)
    
                
