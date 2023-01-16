import turtle

window = turtle.Screen()
window.setup(500, 500)

'''for checking'''
window.tracer(0)

Nhong1 = turtle.Turtle()


def re_center():

    Nhong1.penup()
    Nhong1.goto(0, 0)
    Nhong1.pendown()
    Nhong1.setheading(90)


def draw_circle():
    colors = ["blue", "pink", "orange"]

    Nhong1.pensize(5)
    Nhong1.color("purple")
    Nhong1.circle(150)

    Nhong1.penup()
    Nhong1.goto(0, 0)
    Nhong1.pendown()
    Nhong1.speed(50)
    Nhong1.pensize(1)

    """Bg"""
    for index in range(155):
        Nhong1.pencolor(colors[index % 3])
        Nhong1.forward(index)
        Nhong1.right(70)


def draw_line():

    Nhong1.penup()
    '''put turtle to right side of circle'''
    Nhong1.goto(130, 0)
    Nhong1.setheading(0)
    Nhong1.pensize(5)
    Nhong1.color("purple")
    Nhong1.speed(2)

    for index in range(0, 12):
        Nhong1.pendown()
        Nhong1.backward(20)
        Nhong1.penup()
        Nhong1.goto(0, 0)
        Nhong1.rt(30)
        Nhong1.forward(130)

    Nhong1.pensize(3)
    Nhong1.goto(130, 0)
    Nhong1.setheading(0)

    for index in range(0, 24):
        Nhong1.pendown()
        Nhong1.backward(10)
        Nhong1.penup()
        Nhong1.goto(0, 0)
        Nhong1.rt(15)
        Nhong1.forward(130)


def draw_time(h, m, s):

    m += s/60
    h = (m/60) + (h % 12)

    Nhong1.pensize(3)

    '''hour'''
    re_center()
    Nhong1.rt(h*30)
    Nhong1.forward(80)

    '''minute'''
    re_center()
    Nhong1.rt(m*6)
    Nhong1.forward(100)

    '''second'''
    Nhong1.color("red")
    re_center()
    Nhong1.rt(s*6)
    Nhong1.forward(100)


def draw_clock():

    """Set position of turtle"""
    Nhong1.penup()
    Nhong1.goto(0, -150)
    Nhong1.pendown()

    # draw_circle()
    draw_line()

    hour, minute, second = input("Enter time: ").split(":")
    hour, minute, second = int(hour), int(minute), int(second)

    draw_time(hour, minute, second)
    turtle.exitonclick()


draw_clock()
