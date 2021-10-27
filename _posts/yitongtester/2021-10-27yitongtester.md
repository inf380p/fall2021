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
#reflection: it seems like a simple question in the ronestone, just draw"CS" shape by using Turtle, at first I tried to write codes step by step like just write codes as "penup and pendown",'left and right', but I think the codes looks more redundant and too long. Also, when writing codes to draw "s", i struggled about the orientation to turn left and right, so the process of deciding the orientation was quite slow（maybe because my Poor sense of direction. So I turned to review the runestone's tutorial and finally chose to use 2 loops, which can be regarded as shortcut.

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
#Reflection: It's hard for me to think about some situations about putting conditional statement in turtle. While using turtle to draw a star with 9 Protruding horns is a good choice, so I used for loop to traverse 20 lines and used % computation to decide its routes. A problem is I don;t know why the turtle pen repeated to draw a redundant line in the end. Also, it will be beeter if I can add codes to start at other position and draw another star and make a non-overlapping shape.
