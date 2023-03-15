import turtle

t = turtle.Turtle()
t.pendown()
t.write("Turtle Draw")
t.speed(5) # set turtle speed to 5 for slower movement
t.color("green")
t.shape('turtle')

# Set up the screen
s = turtle.Screen()
s.setup(1080, 720)

# Define a function to update the turtle's position based on the mouse
def follow_mouse(x, y):
    t.ondrag(None)  # unbind the function to prevent glitches
    t.goto(x, y)
    t.ondrag(follow_mouse)  # bind the function back to the event

# Bind the follow_mouse function to the mouse movement event
t.ondrag(follow_mouse)

# Keep the program running
turtle.mainloop()
