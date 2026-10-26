# Name: Eddie King
# Assignment: P4LAB1
# Date: 10/24/2026
# Description: Draws a house using turtle graphics.

# Pseudocode:
# 1. Import the turtle library.
# 2. Create a turtle and change the background color.
# 3. Use a while loop to draw a square.
# 4. Move the turtle to the top of the square.
# 5. Use a for loop to draw a triangle roof.
# 6. Choose random colors for the square and triangle.

# Import the library
import turtle
import random

# Create the turtle window and drawing object
win = turtle.Screen()
win.bgcolor("lightblue")
pen = turtle.Turtle()

# Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("turtle")
pen.speed(5)

# Draw the square using a while loop
pen.penup()
pen.goto(-100, -100)
pen.pendown()

square_color = random.choice(["red", "blue", "green", "yellow", "orange", "pink", "cyan"])
pen.fillcolor(square_color)
pen.begin_fill()

side = 0

while side < 4:
    pen.forward(200)
    pen.left(90)
    side = side + 1

pen.end_fill()

# Move to the top-left corner of the square
pen.penup()
pen.goto(-100, 100)
pen.pendown()

# Draw the triangle roof using a for loop
triangle_color = random.choice(["purple", "brown", "red", "orange", "magenta", "gold", "blue"])
pen.fillcolor(triangle_color)
pen.begin_fill()

for side in range(3):
    pen.forward(200)
    pen.left(120)

pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Wait for user to close window
win.mainloop()
