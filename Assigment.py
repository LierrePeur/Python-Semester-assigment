import turtle
import time


wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.title("Assignment")
wn.tracer(0)


# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
init_pen = turtle.Turtle()
init_pen.hideturtle()


def draw_clock():
    # Draw clock face
    init_pen.up()
    init_pen.goto(0, 210)
    init_pen.setheading(180)
    init_pen.color("black")
    init_pen.pendown()
    init_pen.pensize(3)
    init_pen.circle(210)
    init_pen.penup()
    init_pen.goto(0, 0)
    init_pen.setheading(90)
    for i in range(60):
        if i == 0:
            digit = 12
        else:
            digit = i // 5
        if i % 5 == 0:
            init_pen.fd(190)
            init_pen.pendown()
            init_pen.pensize(3)
            init_pen.fd(20)
            init_pen.penup()
            init_pen.goto(4, -20)
            init_pen.fd(170)
            init_pen.write(arg=str(digit), align="center", font=("Courier", 25))
        else:
            init_pen.fd(200)
            init_pen.pendown()
            init_pen.pensize(1)
            init_pen.fd(10)
            init_pen.penup()
        init_pen.goto(0, 0)
        init_pen.rt(6)


def draw_hands(hour, minute, second, pen):
    # The minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("Red")
    pen.setheading(90)
    angle = (minute / 60) * 360
    pen.rt(angle)
    pen.right(90)
    pen.pensize(1)
    pen.pendown()
    pen.fd(2)
    pen.left(90)
    pen.fd(140)
    pen.left(30)
    pen.fd(4)
    pen.left(120)
    pen.fd(4)
    pen.left(30)
    pen.fd(140)
    pen.left(90)
    pen.fd(2)

    # The hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("black")
    pen.setheading(90)
    angle = (hour / 12) * 360
    pen.rt(angle)
    pen.right(90)
    pen.pensize(1)
    pen.pendown()
    pen.fd(2)
    pen.left(90)
    pen.fd(80)
    pen.left(30)
    pen.fd(4)
    pen.left(120)
    pen.fd(4)
    pen.left(30)
    pen.fd(80)
    pen.left(90)
    pen.fd(2)

    # The second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("gold")
    pen.setheading(90)
    angle = (second / 60) * 360
    pen.rt(angle)
    pen.pensize(2)
    pen.backward(30)
    pen.pendown()
    pen.fd(120)

    # Draw center dot
    pen.penup()
    pen.goto(0, 0)
    pen.dot(10, "black")


draw_clock()


while True:
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    draw_hands(hour, minute, second, pen)
    wn.update()
    time.sleep(1)
    pen.clear()


wn.mainloop()
