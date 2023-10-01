import turtle as t
from random import randint
t.speed(5000)
t.bgcolor("black")
x = 1
while x < 400:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    t.colormode(255)
    t.pencolor(r,g,b)
    t.fd(50+x)
    t.rt(90.911)
    x += 1
t.exitonclick() 

