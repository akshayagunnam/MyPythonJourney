import turtle

wn = turtle.Screen()
cow = turtle.Turtle()

n = 5
  
for i in range(n * 4):
    
    cow.forward(i * 10)
      
    cow.right(90)
  
wn.mainloop()
