import turtle as t
import colorsys
t.bgcolor('black')
t.hideturtle()
t.tracer(5)
h= 0.6
for i in range(580):
    c = colorsys.hsv_to_rgb(h,1,1)
    h = 0.55
    t.color('blue')
    h = 0.001
    t.up()
    t.circle(i,20)
    t.down()
    t.circle(65,145)
    t.lt(140)

t.done()
