from tkinter import *
import time
import math

tk=Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
width=500
height=500
while 1:
    canvas.delete("all")
    
    canvas.create_arc(10,10,width-10, height-10, extent=359, style = CHORD,width = 2)
    canvas.create_arc(245,245,255,255,extent=359, style= CHORD, fill='blue')
    #second
    t=time.localtime()
    second=t[5]*6
    sx = 230 * math.sin(second/360*3.14*2)
    sy = 230 * math.cos(second/360*3.14*2)
    canvas.create_line(250,250, 250+sx, 250-sy,fill="red", width=3)
    #min
    min=(t[4]+t[5]/60)*6
    mx=200 * math.sin(min/360*2*3.14)
    my = 200*math.cos(min/360*2*3.14)
    canvas.create_line(250,250, 250+mx,250-my, fill="Green", width=5)
    #hour>24시간 단위
    hour=(t[3]+t[4]/60)*15
    hx = 150*math.sin(hour/360*2*3.14)
    hy = 150*math.cos(hour/360*2*3.14)
    canvas.create_line(250,250, 250+hx, 250-hy, fill="Blue", width=8)

    canvas.create_arc(245,245,255,255,extent=359, style= CHORD, fill='blue')
    canvas.update()
    time.sleep(1)
