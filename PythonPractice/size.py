def draw_square(t, size):
    '''draws a square of side length size'''
    for s in range (4):
            t.forward(size)
            t.left(90)
    t.penup()
    t.right(135)
    t.forward(20)
    t.right(135)
    t.pendown()
    t.forward(size + 2)
    for i in range(9):
        for p in range (4):
            t.forward(size + 10)
            t.right(90)
        t.penup()
        t.right(135)
        t.forward(20)
        t.right(135)
        t.pendown()
        t.forward(2*i)

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
draw_square(alex, 25)

wn.mainloop()
