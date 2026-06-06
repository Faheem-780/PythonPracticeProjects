import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(900, 900)
screen.title("HEAVY Spirograph 🐢✨")
screen.tracer(20)

t = turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()

colors = ["#FFD700", "#FFA500", "#FFFFFF", "#FFCF00"]

R = 220
r = 65
d = 140

for layer in range(8):
    t.color(colors[layer % len(colors)])
    t.penup()
    t.goto(R - r + d, 0)
    t.pendown()

    for i in range(3000):
        angle = i * 0.1
        x = (R - r) * math.cos(angle) + (d + layer * 5) * math.cos((R - r) / r * angle)
        y = (R - r) * math.sin(angle) - (d + layer * 5) * math.sin((R - r) / r * angle)
        t.goto(x, y)

    t.right(10)

turtle.update()
turtle.done()