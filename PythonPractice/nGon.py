import turtle

wn = turtle.Screen()
turtle = turtle.Turtle()

n  = 10

for i in range (n):
    turtle.forward(100)
    turtle.right(360/n)

wn.mainloop()
