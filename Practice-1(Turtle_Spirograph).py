import turtle as t
import random

sai = t.Turtle()

t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pick_color = (r, g, b)
    return pick_color

sai.speed("fastest")
sai.shape("turtle")

def complete_spirograph(circle_gap):
    for _ in range(int(360 / circle_gap)):
        sai.circle(100)
        sai.color(change_color())
        sai.setheading(sai.heading() + circle_gap)

complete_spirograph(5)








screen = t.Screen()
screen.exitonclick()


