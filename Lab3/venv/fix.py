import turtle

window = turtle.Screen()
window.setup(500, 500)

'''for checking'''
window.tracer(0)

Andy = turtle.Turtle()

Andy.penup()
Andy.goto(0, 0)
Andy.pendown()

Andy.penup()

'''put turtle to right side of circle'''
Andy.goto(130, 0)
Andy.setheading(0)
Andy.pensize(5)
Andy.color("purple")

for index in range(0, 12):
    Andy.pendown()
    Andy.backward(20)
    Andy.penup()
    Andy.goto(0, 0)
    Andy.rt(30)
    Andy.forward(130)

Andy.pensize(3)
Andy.goto(130, 0)
Andy.setheading(0)

for index in range(0, 24):
    Andy.pendown()
    Andy.backward(10)
    Andy.penup()
    Andy.goto(0, 0)
    Andy.rt(15)
    Andy.forward(130)


hour, minute, second = input("Enter time: ").split(":")

if not hour.isnumeric() or not minute.isnumeric() or not second.isnumeric():
    print("Error: wrong input form")

else:

    hour_int = int(hour)
    minute_int = int(minute)
    second_int = int(second)

    if not len(hour) == 2 or not len(minute) == 2 or not len(second) == 2:
        print("Error: wrong input form")

    elif hour_int >= 24 or minute_int >= 60 or second_int >= 60:
        print("Error: exceed number")

    else:

        minute_int += second_int/60
        hour_int = (minute_int/60) + (hour_int % 12)

        Andy.pensize(3)

        '''hour'''
        Andy.pensize(5)
        Andy.penup()
        Andy.goto(0, 0)
        Andy.pendown()
        Andy.setheading(90)

        Andy.rt(hour_int*30)
        Andy.forward(60)

        '''minute'''
        Andy.penup()
        Andy.goto(0, 0)
        Andy.pendown()
        Andy.setheading(90)
        Andy.rt(minute_int*6)
        Andy.forward(80)

        '''second'''
        Andy.pensize(2)
        Andy.color("red")
        Andy.penup()
        Andy.setpos(0, 0)
        Andy.pendown()
        Andy.setheading(90)
        Andy.rt(second_int*6)
        Andy.forward(80)
        window.update()
        turtle.exitonclick()
