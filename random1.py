import turtle
import random

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)

def trojuholnik(dlzka):
    for i in range(3):
        t.fd(dlzka)
        t.rt(120)

def posun():
    t.pu()
    t.setpos(random.randrange(-350, 350),
             random.randrange(-350, 350))
    t.seth(random.randrange(350))
    t.pd()

turtle.delay(0)
t = turtle.Turtle()
t.pensize(5)
for i in range(20):
    posun()
    if random.randrange(2):
        t.pencolor('red')
        stvorec(30)
    else:
        t.pencolor('blue')
        trojuholnik(30)