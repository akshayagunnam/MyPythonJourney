import turtle             # Allows us to use turtles

wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

# back up to give alex some room
alex.penup()
alex.back(100)  # alex.forward(-100) would work too
alex.pendown()

# Draw 3 stars
for star in range(3):
    # Draw a star
    for point in range(5):
        alex.forward(25)
        alex.left(72)
        alex.forward(25)
        alex.right(144)

    # Move into position for the next star
    alex.penup()
    alex.forward(100)
    alex.pendown()

wn.mainloop()
