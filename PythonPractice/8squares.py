import turtle

wn = turtle.Screen()
dora = turtle.Turtle()

dora.penup()
dora.back(200)
dora.pendown()

for square in range (4): 
    for i in range (4):
        dora.forward(50)
        dora.right(90)
    dora.forward(100)

    for j in range (3):
        dora.right(90)
        dora.forward(50)
    dora.right(90)
    dora.forward(50)
   
wn.mainloop()
