from tkinter import *

tk=Tk()
canvas=Canvas(tk, width=500, height=500)
canvas.pack()

#입력
nums=[]
for i in range(5):
    num=int(input('숫자 : '))
    nums.append(num)

height=10

for i in nums:
    if i >= 90:
        color='green'
    elif i>= 80:
        color='blue'
    elif i>=60:
        color='orange'
    else:
        color='red'
    
    canvas.create_rectangle(10, height, 10+3*i, height+10,fill=color)
    canvas.create_text(10+3*i+10, height+5, text=i)

    height += 20


