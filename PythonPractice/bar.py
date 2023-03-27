import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.penup()
tess.backward(170)
tess.left(90)
tess.backward(100)
tess.right(90)
tess.pendown()

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height < 200:
        t.fillcolor("red")
        t.begin_fill()       
        t.left(90)
        t.forward(height)     
        t.write("  " + str(height))  
        t.right(90)
        t.forward(40)         
        t.right(90)
        t.forward(height)     
        t.left(90)            
        t.end_fill()          
        t.forward(10)         
    elif height >= 200:
        t.fillcolor("green")
        t.begin_fill()        
        t.left(90)
        t.forward(height)     
        t.write("  " + str(height))  
        t.right(90)
        t.forward(40)         
        t.right(90)
        t.forward(height)     
        t.left(90)            
        t.end_fill()          
        t.forward(10)         
xs = [10,0,0,250,10,-5] 
for v in xs:              
    draw_bar(tess, v)

wn.mainloop()
