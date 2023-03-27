n = int(input("n = "))

import turtle
wn = turtle.Screen()

for i in range (n):
   turtle.forward(100)
   turtle.right(180 - (180/n))

turtle.hide
wn.mainloop()
