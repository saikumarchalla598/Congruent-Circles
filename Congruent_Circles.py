# -*- coding: utf-8 -*-
"""

@author: Srinu-sai
"""
import turtle
import math
wn = turtle.Screen()
turtle.speed(0)
x = turtle.Turtle()
n = 360

m = int(input('Enter number of circles required around a circle: '))
d = float(input('Enter the diameter of the circle: '))
for i in range(n):
    x.forward(math.pi*d/360)
    x.right(1)
y = int(360/m)
d1 = 1.5*math.pi*d/m
for j in range(m):
    for k in range(y-1):
        x.penup()
        x.forward(math.pi*d/360)
        x.right(1)
    for ii in range(n):
        x.left(1)
        x.pendown()
        x.forward(math.pi*d1/360)
    x.right(1)
