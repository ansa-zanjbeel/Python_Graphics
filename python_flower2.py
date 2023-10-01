import turtle as t
t.speed(0)
t.bgcolor("black")
t.hideturtle()
x = 1

while x < 4000:
    
    t.color("yellow")
    t.pencolor("yellow")
    t.left(120+23)
    t.left(1)
    t.fd (50 + x)
    t.color("greenyellow")
    t.rt(350)
    x +=1

t.done()    