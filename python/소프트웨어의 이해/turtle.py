import turtle
turtle.setup(width=500, height=500)
t.pencolor('dark green')
t.width(3)
edges=4
length=500
dot_size=length/20
for i in range(edges):
    for j in range(edges):
        t.forward(dot_size)
        t.up()
        t.forward(dot.size)
        t.down()
    t.right(90)
