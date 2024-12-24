#!/usr/bin/env python3

#IMPORT
from turtle import *

turtle = Turtle()
ts = turtle.getscreen()

turtle.screen.screensize(1000,1000)

from random import randint

def got(x, y, d):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(d)

#DRAW

for szam in range(100):
   print(szam)
   for karakter in str(szam):
       if karakter=="2":
           turtle.setheading(270)
           turtle.forward(10)
       if karakter=="4":
           turtle.setheading(180)
           turtle.forward(10)           
       if karakter=="6":
           turtle.setheading(0)
           turtle.forward(10)           
       if karakter=="8":
           turtle.setheading(90)
           turtle.forward(10)

       if karakter=="1":
           turtle.setheading(225)
           turtle.forward(10)
       if karakter=="3":
           turtle.setheading(315)
           turtle.forward(10)
       if karakter=="7":
           turtle.setheading(135)
           turtle.forward(10)
       if karakter=="9":
           turtle.setheading(45)
           turtle.forward(10)

ts.getcanvas().postscript(file="draw.eps", width=1000, height=1000)


input1 = input() 
