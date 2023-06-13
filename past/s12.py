import turtle

COLORS = ('red','green','blue','yellow','purple')

screen = turtle.Screen()
screen.setup(420,320)
screen.bgcolor('black')

pen = turtle.Turtle()
pen.pensize(4)

pen.penup()
pen.goto(-90,30)

pen.pendown()

for i in range(5):
    pen.pencolor(COLORS[i])
    pen.forward(200)
    pen.right(144)
screen.mainloop()
