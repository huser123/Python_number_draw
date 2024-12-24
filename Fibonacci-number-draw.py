#!/usr/bin/env python3


from turtle import *


turtle = Turtle()
ts = turtle.getscreen()

turtle.screen.screensize(1000,1000)


n1, n2 = 0, 1
count = 0

while count < 100:
    print(count, n1)
    for karakter in str(n1):
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
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1 


#ts.getcanvas().postscript(file="Fibonacci.eps", width=50000, height=50000)

input1 = input() 
