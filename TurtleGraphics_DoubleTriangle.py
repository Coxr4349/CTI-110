# This is a foray into python turtle graphics
# 091819
# CTI-110 P2HW2 - Turtle Graphic
# Ryan Cox

import turtle

#setup
turtle.bgcolor('gray')

#double triangle
turtle.hideturtle()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.goto(100,0)
turtle.goto(50,70)
turtle.goto(0,0)
turtle.end_fill()
turtle.goto(50,140)
turtle.goto(100,0)
