import turtle as tur

'''Setup'''
sc = tur.Screen()
tur.speed(5)

tur.penup()
tur.back(200)
tur.pendown()


def create_tree(start_length, branch):

    if branch >= start_length:
        return
    else:
        tur.forward(start_length)
        tur.rt(30)
        create_tree(start_length*0.6, branch)
        tur.lt(60)
        create_tree(start_length*0.6, branch)
        tur.rt(30)
        tur.backward(start_length)

'''==========================================================================='''

create_tree(120, 10)
tur.done()
