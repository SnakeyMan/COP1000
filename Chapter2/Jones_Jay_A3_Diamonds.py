# ============================================================
# PROGRAMMER:       Jay Jones
# PROGRAM NAME:     Assignment #03 - TURTLE GRAPHICS
# DATE WRITTEN:     April 5, 2019
# ============================================================

# Tells Python to import the Turtle module
import turtle

# Shows the turtle cursor
turtle.showturtle()

# Turtle will use these colors
# The first color represents the lines, the second color is the fill
turtle.color("blue", "blue")

# This tells turtle to fill in the shapes that are drawn
turtle.begin_fill()

# Each of these (left/right) tells turtle to turn, in degrees
turtle.left(45)

# Turtle will move 'forward' this many pixels from its current position
turtle.forward(100)

# Turtle will obey these steps accordingly until there are no more commands
turtle.right(90)
turtle.forward(200)
turtle.heading()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)

# Turtle will no longer fill the shapes with color
turtle.end_fill()

# This will hide the cursor to show a cleaner picture
turtle.hideturtle()

# This will keep the window open until the user clicks
turtle.exitonclick()
