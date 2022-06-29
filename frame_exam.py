import turtle
import time
import random
# t = turtle.Turtle()
t_line = turtle.Turtle()
s = turtle.Screen()

t_line.up()
t_line.setposition(-200,200)
t_line.down()
t_line.setheading(270)
t_line.pensize(3)

s.delay(0)

x_range = [-200,-150,-100,-50,0,50,100]


for i in range(8):
    t_line.forward(400)
    t_line.up()
    t_line.setposition(t_line.xcor() + 50, 200)
    t_line.down()
t_line.setheading(0)
t_line.up()
t_line.setposition(-200,200)
t_line.down()
over_line = []
line_ycor = 0
s.delay(1)
def over():
    pass

for j in range(5):

    for i in range(7):
        line_ycor = random.choice([i for i in range(-180, 180, 20)])
        over_line.append([int(t_line.xcor()),line_ycor])

        t_line.up()
        t_line.setposition(x_range[i], line_ycor)
        t_line.down()
        t_line.forward(50)
print(over_line)


s.mainloop()


