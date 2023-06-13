import turtle

my_pen = turtle.Turtle()
my_pen.pencolor('purple')
my_pen.pensize(3)

my_pen.fillcolor('red')

my_pen.begin_fill()
for i in range(5):
    my_pen.forward(150)
    my_pen.right(144)

my_pen.end_fill()

turtle.done()
