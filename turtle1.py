import turtle

s = turtle.Screen()

p = turtle.Pen()
p.pensize(4)
p.pencolor('red')

p.fillcolor('green')
p.begin_fill()
p.forward(100)
p.left(120)

p.forward(100)
p.left(120)

p.forward(100)
p.left(120)

p.end_fill()


p.forward(100)
p.left(90)

p.forward(100)
p.left(90)

p.forward(100)
p.left(90)

p.forward(100)
p.left(90)

# کشیدن پنجضلعی
# کشیدن ششضلعی
s.exitonclick()
