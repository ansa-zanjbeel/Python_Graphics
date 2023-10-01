import turtle as t 
import colorsys 
t.bgcolor('yellow')
t.tracer(10)
h = 0
for i in range(102):
 c = colorsys.hsv_to_rgb(h,1,1)
 h = 0.55
 t.up()
 t.goto(0,0)
 t.down()
 t.color('black')
 t.fillcolor (c)
 t.begin_fill()
 t.rt (98)
 t.circle(i,12)
 t.fd (290)
 t.fd(i)
 t.lt(29)
for j in range(129):
      t.fd(i)
      t.circle(j, 299, steps=2)
t.end_fill