import math
import turtle
def heart1(k):
    return 15*math.sin(k)**3

def heart2(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("pink")
for i in range(6000):
    turtle.goto(heart1(i)*20,heart2(i)*20)

    turtle.goto(0,0)
turtle.done()