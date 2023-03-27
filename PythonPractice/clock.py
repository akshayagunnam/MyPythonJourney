# Python Class 3337
# Lesson 3 Problem 7
# Author: Calculus_sus (950197)
import turtle

hour = input("hour = ")    #hour
minute = input("minute = ")    #minute
wn = turtle.Screen()
turtle = turtle.Turtle()    #the turtle is called turtle
turtle.speed(15)    #turtle goes faster
turtle.left(90)    #turtle faces up instead of to the right

for i in range(12):    #reapeat 12 times to draw tick marks
    turtle.penup()
    turtle.forward(200)    #the radius of the clock(circle) is 200)
    turtle.pendown()
    turtle.stamp()    #tick mark is stamped on
    turtle.penup()
    turtle.backward(200)    #goes back to starting place    
    turtle.pendown()
    turtle.right(30)    #360 degrees/12 tick marks = each tick mark is 30 degrees apart

a = ((int(hour))*30)    #all hours are 30*hour from starting(90 degrees)
turtle.right(a)
turtle.width(5)    #the thickness of the hour hand is 5
turtle.pencolor("red")    #hour hand is red
turtle.forward(90)    #hour hand is 90 long
turtle.backward(90)
turtle.left(a)    #back to original(90)degrees
turtle.hideturtle()

b = ((int(minute))*6)    #all minutes are 6 degrees apart because 360 degrees/60 minutes = 6 degrees
turtle.right(b)
turtle.width(2)    #minute hand is thinner than hour hand(thickness: 2)
turtle.pencolor("blue")    #minute hand is blue
turtle.forward(160)    #minute hand is 160 long
turtle.backward(160)
turtle.hideturtle()

wn.mainloop()

#
