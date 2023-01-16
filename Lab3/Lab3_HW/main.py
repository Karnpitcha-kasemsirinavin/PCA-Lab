from random import *
import turtle

'''Setup'''
my_screen = turtle.Screen()
my_screen.bgcolor('white')
my_screen.title('turtle race game')
my_screen.screensize(1000, 1000)
my_screen.colormode(255)
draw_turtle = turtle.Turtle()
run = True

'''========================================================================'''


class TurtleFPO(turtle.Turtle):
    def __init__(self):
        super().__init__()

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        self.color(r, g, b)
        self.shape('turtle')
        self.pensize(3)
        self.speed(randint(10, 50))
        self.leap_dis = randint(50, 100)
        self.energy = randint(100, 500)

        self.energy_consume = int(self.leap_dis/2)
        self.total_angle = 0
        self.rotate_angle = 0

    def move(self):
        if self.energy > 0:
            self.forward(self.leap_dis)
            self.energy -= self.energy_consume

            if self.total_angle <= 0:
                self.rotate_angle = randint(0, 30)
                self.total_angle += self.rotate_angle
            else:
                self.rotate_angle = randint(-30, 0)
                self.total_angle += self.rotate_angle
            self.rt(self.rotate_angle)

    def update(self):
        self.move()


def bg_setup():

    draw_turtle.hideturtle()
    draw_turtle.color('black')

    '''Start line'''
    draw_turtle.penup()
    draw_turtle.goto(-350, 260)
    draw_turtle.write('Start line')

    draw_turtle.penup()
    draw_turtle.goto(-330, 250)
    draw_turtle.rt(90)
    draw_turtle.pendown()
    draw_turtle.forward(500)

    '''Finish ine'''
    draw_turtle.penup()
    draw_turtle.rt(-90)
    draw_turtle.forward(650)
    draw_turtle.rt(-90)
    draw_turtle.pendown()
    draw_turtle.forward(500)
    draw_turtle.penup()
    draw_turtle.goto(300, 260)
    draw_turtle.write('Finish line')


def input_turtle():

    turtle_num = int(input("How many tortoise?: "))
    turtle_list = []

    for index in range(0, turtle_num):
        turtle_type = randint(1, 1)

        if turtle_type == 0:
            a = turtle.Turtle()
            a.hideturtle()
            a.shape('turtle')

            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            a.color(r, g, b)

            turtle_list.append(['normal', a])
        else:
            b = TurtleFPO()
            b.hideturtle()
            turtle_list.append(['FPO', b])

    return turtle_list


def move_norm_turtle(norm_turtle, leap_dis):

    norm_turtle.pensize(3)
    norm_turtle.speed(randint(10, 50))
    norm_turtle.forward(leap_dis)


def norm_leap_dis(turtle_array):

    for index in range(0, len(turtle_array)):
        if turtle_array[index][0] == 'normal':
            leap_dis = randint(1, 50)
            turtle_array[index].append(leap_dis)

    return turtle_array


def start_pos(turtle_array):

    x_cor = -350
    distance_btw = int(500/len(turtle_array))

    for index in range(0, len(turtle_array)):
        y_cor = 240 - distance_btw*index

        turtle_array[index][1].penup()
        turtle_array[index][1].goto(x_cor, y_cor)
        turtle_array[index][1].pendown()
        turtle_array[index][1].showturtle()


def draw_winner(win_tur):

    win_tur.penup()
    win_tur.goto(0, 0)
    win_tur.write('!!!WINNNER!!!', font=('Arial', 20), align='center')
    win_tur.shapesize(3)
    win_tur.goto(0, -50)


'''========================================================================'''

winner = []
energy_check = True
count_tur = 0
bg_setup()

turtle_arr = input_turtle()
turtle_arr = norm_leap_dis(turtle_arr)

start_pos(turtle_arr)

for tur in turtle_arr:
    if tur[0] == 'normal':
        energy_check = False

if energy_check is True:

    while run is True:

        count_tur = 0

        for tur in turtle_arr:
            if tur[0] == 'FPO':
                tur[1].update()

            if tur[1].xcor() >= 315:
                run = False
                winner.append(tur[1])
                break

            else:

                if tur[1].energy <= 0:
                    count_tur += 1

        if count_tur == len(turtle_arr):
            break
else:

    while run is True:

        for tur in turtle_arr:
            if tur[0] == 'normal':
                move_norm_turtle(tur[1], tur[2])
            elif tur[0] == 'FPO':
                tur[1].update()

            if tur[1].xcor() >= 315:
                run = False
                winner.append(tur[1])
                break


for tur in turtle_arr:
    if tur[1] not in winner:
        tur[1].hideturtle()
    tur[1].clear()

draw_turtle.clear()

'''Winner'''
if count_tur != len(turtle_arr):
    draw_winner(winner[0])

else:
    draw_turtle.goto(0, 0)
    draw_turtle.write('!!!ENERGY RUN OUT!!!', align='center', font=('Arial', 20, 'normal'))

my_screen.update()
turtle.exitonclick()
