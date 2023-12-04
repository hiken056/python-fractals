from dragon import dragon, R
from turtle import Turtle, Screen

# Turtle setup
turtle = Turtle("turtle")
turtle.hideturtle()
turtle.speed("fastest")
turtle.color("#8ACDD7")

# Screen setup
screen = Screen()
screen.title("Dragon Curve")
screen.bgcolor("#31304D")
screen.screensize(1920*3, 1080*3)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)


# Draw
LENGTH = 10
turtle.forward(LENGTH)
for element in dragon(17):
    if element == R:
        turtle.right(90)
        turtle.forward(LENGTH)
    else:
        turtle.left(90)
        turtle.forward(LENGTH)

# When finished, click to exit
turtle.color("white")
turtle.write("click to exit", font=("Calibri", 16, "bold"))
screen.exitonclick()

