---
layout: post
author: Yitong
title: yitong's trinket post and reflection
---

#My trinket from textbook
from turtle import *
space = Screen()
cs = Turtle()
cs.color('purple')
cs.right(180)
cs.forward(50)
cs.left(90)
cs.forward(100)
cs.left(90)
cs.forward(50)
cs.penup()
cs.goto(100,0)
cs.pendown()
cs.right(180)
for sides in range(2):
  cs.forward(50)
  cs.left(90)
for sides in range(2):
  cs.forward(50)
  cs.right(90)
cs.forward(50)
#reflection: it seems like a simple question in the ronestone, just draw"CS" shape by using Turtle, here I didn't just write codes as "penup and pendown",use 2 loops can be as shortcut

#My trinket I made
import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('purple')
for x in range(20):
        turtle.forward(100)
        if x % 2 == 0:
            turtle.left(175)
        else:
            turtle.left(225)
#Reflection: It's hard to think about putting conditional statement in turtle. While using turtle to draw oval is a good choice.
            turtle.left(225)
