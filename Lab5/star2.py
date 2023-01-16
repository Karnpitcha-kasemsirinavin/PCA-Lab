import turtle as tur

"""Setup"""
draw_tur = tur.Turtle()
draw_tur.hideturtle()
draw_tur.penup()

n = int(input())


def star2(n, base=1):

    if n < base:
        return
    else:
        print('*'*base, end='\n')
        star2(n, base+1)
        print('*'*base, end='\n')


def stars2(n, base=1):
    if n < base:
        return

    else:
        draw_tur.setpos(0, (n - base) * 20)
        for i in range(base):
            draw_tur.dot()
            draw_tur.forward(20)

        stars2(n, base+1)
        draw_tur.setpos(0, ((n - base) + 1) * -20)
        for i in range(base):
            draw_tur.dot()
            draw_tur.forward(20)


star2(n)
stars2(n)
tur.done()
