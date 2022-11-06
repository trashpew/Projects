import turtle as trtl
from turtle import screensize
from turtle import Screen
import math
proj = trtl.Turtle()
###################

def Parameter():
    global m1
    global v0
    global deg
    print("Please insert positive integer numbers for all:")
    m1 = 10
    print("What should the initial velocity be (m/s):")
    v0 = int(input())
    print("What should our launch angle be (degrees):")
    deg = math.radians(int(input()))

def estForce():
    global f
    global G
    global m2
    G = (-6.67430 * (10 ** -11))
    m2 = (5.9722 * (10 ** 24))
    r = 6378100
    f = G * ((m1 * m2) / (r ** 2))

def Init():
    screen = Screen()
    screen.setup(500, 500)
    proj.turtlesize(0.5)
    proj.shape('circle')
    proj.speed(0)
    proj.penup()
    proj.goto(-200, -200)
    proj.pendown()
    screensize(1000, 1000)

def Pos():
    global a
    y = -1000
    x = -1000
    t = 0
    v0y = int((math.sin(deg) * v0))
    v0x = int((math.cos(deg) * v0))
    while proj.ycor() > (-201):
        rplus = proj.ycor()
        r = 6378100 + (rplus + 1000)
        f = G * ((m1 * m2) / (r ** 2))
        a = (f / m1)
        t = t + 0.001
        v0y = (v0y + (a * t))
        y = y + (v0y * t)
        x = x + (v0x * t)
        proj.goto((x / 5), (y / 5))

###################

Parameter()
estForce()
Init()
Pos()

###################
wn = trtl.Screen()
wn.mainloop()

