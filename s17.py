import turtle

win = turtle.Screen()
win.title("My Game")
win.bgcolor("blue")
win.setup(width=600, height=600)

head = turtle.Turtle()

head.shape("square")
head.color("red")
head.pensize(3)
# head.penup()
# head.goto(0, 100)
# head.setheading(270)
# head.forward(100)

# head.circle(50)

head.goto(100, 100)
head.stamp()
head.goto(0, 100)
head.stamp()
head.home()
head.stamp()
head.goto(-100, 100)
head.stamp()
head.setheading(0)
head.forward(20)
head.setheading(300)
for i in range(20):
    head.right(4)
    head.forward(1)
head.penup()
head.goto(-100, 100)
head.pendown()
head.goto(0,100)

turtle.done()

# تمرین
# کشیدن سه گوش ، مربع و پنجضلعی
# for
# head.forward(100)
# head.left(120)
