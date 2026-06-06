import turtle
import random

screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("#0a0a0a")
screen.title("Live Growing Dense Fractal Tree")
screen.tracer(1)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -350)
t.pendown()

def grow_tree_step_by_step(branch_len, thickness):
    if branch_len < 6:
        t.color(random.choice(["#27ae60", "#2e8fcc", "#a2d149", "#155e37"]))
        t.pensize(2)
        t.forward(branch_len)
        t.dot(random.randint(3, 6))
        t.backward(branch_len)
        return

    t.pensize(thickness)
    t.color("#5d4037")
    if branch_len < 45:
        t.color("#8d6e63")
    
    t.forward(branch_len)
    
    angle = random.uniform(15, 30)
    reduction = random.uniform(0.7, 0.85)
    
    t.left(angle)
    grow_tree_step_by_step(branch_len * reduction, thickness * 0.75)
    t.right(angle * 2)
    grow_tree_step_by_step(branch_len * reduction, thickness * 0.75)
    t.left(angle)
    
    t.backward(branch_len)

grow_tree_step_by_step(150, 10)
screen.mainloop()