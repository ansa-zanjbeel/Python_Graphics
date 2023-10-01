import turtle as t
t.bgcolor('black')
t.speed(1000)
t.hideturtle()
Colors = ["yellow", "red", "yellow", "orange"]

for i in range(120):
    for c in Colors:
        t.color(c)
        t.circle(200-i, 100)
        t.lt(90)
        t.circle(200-i, 100)
        t.rt(60)
        t.end_fill()

t.mainloop()
