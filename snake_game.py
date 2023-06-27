from turtle import Screen, Turtle
from time import sleep
from random import randint


score = 0


def make_turtle(turtle_shape, turtle_color):
    my_turtle = Turtle()
    my_turtle.shape(turtle_shape)
    my_turtle.color(turtle_color)
    my_turtle.penup()
    my_turtle.speed('fastest')
    return my_turtle


def move():
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        snake_head.sety(ypos + 20)
    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        snake_head.sety(ypos - 20)

    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        snake_head.setx(xpos + 20)
    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        snake_head.setx(xpos - 20)


def change_food_position():
    xposition = randint(-280, 280)
    yposition = randint(-280, 280)
    food.goto(xposition, yposition)


main_surface = Screen()
main_surface.bgcolor('black')
main_surface.setup(width=600, height=600)
main_surface.title("Snake Game")
main_surface.tracer(False)

snake_head = make_turtle("square", "blue")
snake_head.goto(0, 100)
snake_head.direction = "stop"
food = make_turtle("circle", "red")


score_turtle = make_turtle("square", "white")
score_turtle.hideturtle()
score_turtle.goto(0, 260)


def go_up():
    snake_head.direction = "up"


def go_left():
    snake_head.direction = "left"


def go_right():
    snake_head.direction = "right"


def go_down():
    snake_head.direction = "down"


def reset():
    snake_head.goto(0, 0)
    snake_head.direction = ""


main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_right, "Right")
main_surface.onkeypress(go_left, "Left")
snake_bodies = []
running = True
while running == True:
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=48)

    main_surface.update()
    if snake_head.distance(food) < 20:
        score += 1
        change_food_position()
        new_body = make_turtle("square", "grey")
        # TODO

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset()
        score = 0

    move()
    sleep(0.2)
