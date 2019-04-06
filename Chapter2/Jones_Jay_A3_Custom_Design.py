# ============================================================
# PROGRAMMER:       Jay Jones
# PROGRAM NAME:     Assignment #03 - TURTLE GRAPHICS
# DATE WRITTEN:     April 5, 2019
# ============================================================
import turtle

turtle.showturtle()
turtle.width(2)

# right cheek
turtle.color("black", "blue")
turtle.goto(0, 0)
turtle.begin_fill()
turtle.left(36)
turtle.forward(175)
turtle.left(72)
turtle.forward(58)
turtle.left(124)
turtle.goto(0, 0)
turtle.end_fill()

# right eye
turtle.color("black", "green")
turtle.goto(0, 0)
turtle.begin_fill()
turtle.right(160)
turtle.forward(165)
turtle.right(72)
turtle.forward(72)
turtle.right(128)
turtle.goto(0, 0)
turtle.end_fill()

# nose
turtle.color("black", "yellow")
turtle.goto(0, 0)
turtle.begin_fill()
turtle.right(160)
turtle.forward(165)
turtle.left(108)
turtle.forward(102)
turtle.left(108)
turtle.goto(0, 0)
turtle.end_fill()

# left eye
turtle.color("black", "orange")
turtle.goto(0, 0)
turtle.begin_fill()
turtle.right(160)
turtle.forward(200)
turtle.right(128)
turtle.forward(72)
turtle.right(72)
turtle.goto(0, 0)
turtle.end_fill()

# left cheek
turtle.color("black", "red")
turtle.goto(0, 0)
turtle.begin_fill()
turtle.right(160)
turtle.forward(200)
turtle.left(124)
turtle.forward(58)
turtle.left(108)
turtle.goto(0, 0)
turtle.end_fill()

# right ear
turtle.color("black", "purple")
turtle.penup()
turtle.left(72)
turtle.forward(165)
turtle.pendown()
turtle.begin_fill()
turtle.forward(117)
turtle.right(144)
turtle.forward(117)
turtle.right(108)
turtle.forward(72)
turtle.end_fill()

# left ear
turtle.color("black", "purple")
turtle.penup()
turtle.forward(102)
turtle.pendown()
turtle.begin_fill()
turtle.forward(72)
turtle.right(108)
turtle.forward(117)
turtle.right(144)
turtle.forward(117)
turtle.end_fill()

# GitLab text
turtle.penup()
turtle.goto(-50, -50)
turtle.write("GitLab", font=("Arial", "30", "normal"))
turtle.hideturtle()

# This will keep the window open until the user clicks
turtle.exitonclick()
