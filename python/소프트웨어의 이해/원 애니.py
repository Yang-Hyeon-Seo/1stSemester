from tkinter import *
import time

tk=Tk()
canvas=Canvas(tk, width=500, height=500)
canvas.pack()

while True:
    canvas.delete("all")#모두 지우기
    for i in range(10,100):
        canvas.delete("all")
        width=i
        height=i
        canvas.create_arc(250-i, 250-i, 250+i, 250+i, extent = 359, style=CHORD)
        tk.update()
        time.sleep(0.05)
    for i in range(100,10,-1):
        canvas.delete("all")
        width=i
        height=i
        canvas.create_arc(250-i, 250-i, 250+i, 250+i, extent = 359, style=CHORD)
    
        tk.update()
        time.sleep(0.05)#업데이트, 멈춤>>애니효과


