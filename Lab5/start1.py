
import turtle as tur


"""Setup"""
screen = tur.Screen()
draw_tur = tur.Turtle()
draw_tur.hideturtle()
draw_tur.penup()

n = int(input())


def star(n):
    if n == 0:
        return
    else:
        print('*'*n, end='\n')
        star(n-1)
        print('*'*n, end='\n')


def stars1(n):

    if n == 0:
        return
    else:
        draw_tur.setpos(0, n*20)
        for i in range(n, 0, -1):
            draw_tur.dot()
            draw_tur.forward(20)

        stars1(n-1)
        draw_tur.setpos(0, (n-1) * -20)
        for i in range(n):
            draw_tur.dot()
            draw_tur.forward(20)


stars1(n)
tur.done()
