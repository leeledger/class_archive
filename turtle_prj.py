import turtle
import threading

t0 = turtle.Turtle()
s = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.setheading(90)
t2.setheading(180)
t3.setheading(270)

# t1.speed(0)
def play0():
    while True:
        t0.forward(1)
        if t0.xcor() > 300:
            t0.setposition(0,0)
            break

def play1():
    while True:
        t1.forward(1)
        if t1.ycor() > 300:
            t1.setposition(0, 0)
            break

def play2():
    while True:
        t2.forward(1)
        if t2.xcor() < -300:
            t2.setposition(0, 0)
            break

def play3():
    while True:
        t3.forward(1)
        if t3.ycor() < -300:
            t3.setposition(0, 0)
            break
def loop():
    th0 = threading.Thread(target=play0)
    th0.start()
    th1 = threading.Thread(target=play1)
    th1.start()
    th2 = threading.Thread(target=play2)
    th2.start()
    th3 = threading.Thread(target=play3)
    th3.start()
    s.ontimer(loop,1000)
loop()
s.mainloop()