import turtle

# create the turtle object
flag = turtle.Turtle()

# set the turtle speed (0 is the fastest, 10 is the slowest)
flag.speed(0)

# set the pen size
flag.pensize(3)

# set the fill color to red
flag.fillcolor("red")

# move the turtle to the starting position
flag.penup()
flag.goto(-200, -200)
flag.pendown()

# draw the rectangle
flag.begin_fill()
for i in range(2):
    flag.forward(500)
    flag.left(90)
    flag.forward(300)
    flag.left(90)
flag.end_fill()

# set the fill color to green
flag.fillcolor("green")

# move the turtle to the starting position
flag.penup()
flag.goto(-50, -50)
flag.pendown()

# draw the triangle
flag.begin_fill()
for i in range(5):
    flag.forward(200)
    flag.right(144)
flag.end_fill()

# hide the turtle
flag.hideturtle()

# keep the window open until it is closed
turtle.exitonclick()
