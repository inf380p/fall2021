---
layout: post
author: sarahva47
title: "Sarah V.'s two trinket posts and reflection"
---

My Trinket from the textbook:
<iframe src="https://trinket.io/embed/python/5a4df579bf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My Trinket I made:
<iframe src="https://trinket.io/embed/python/7a673b03fc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
In considering Turtles, one lightbulb I had came pretty early on. I mention this lightbulb because there was one element I was really confused by and have been wanting to know in Python: how to get things on screens to move, like video games. I think 17.1 explained it really well with the explanation statements like "ask alex to move forward by 150 units," because that little statement made it click on how something moves: the same way you adjust an element in HTML by moving it little unit by unit. So I think in this instance, comparing turtles to something with which I was already familiar helped a lot in contextualizing how they work.

For a textbook problem, I am choosing to talk about 17.14.19. I am choosing this one because, honestly, it felt a little tedious. The textbook had discussed how to use functions to create polygons and spirals, but I'm not sure quite how to translate that to irregular shapes. If I wanted a program that could write names, for example, would I need to define a function for each letter of the alphabet and then call those for each letter? Also, I am left with anticipation on how to make curves! I want to draw curvy "S"s. 

from turtle import *
space = Screen()
s = Turtle()
s.color("teal")
s.pensize(2)
s.penup()
s.goto(-50,-50)
s.pendown()
s.forward(50)
s.left(90)
s.forward(50)
s.left(90)
s.forward(50)
s.right(90)
s.forward(50)
s.right(90)
s.forward(50)
s.penup()
s.goto(5,-50)
s.pendown()
s.setheading(75)
s.forward(100)
s.setheading(285)
s.forward(100)
s.penup()
s.goto(7,-25)
s.pendown()
s.setheading(0)
s.forward(50)

As seen here, it took me 24 steps to write out two of my initials, SA. I was hoping to write the V as well for "SAV," my full intials, but I didn't want to spend more time on this problem. I think this exemplifies how Python tends to have a long and tedious way to do things and a quicker shortcut... and I would love to know if there's any shortcut for this. I liked this problem because I wanted to play around with the pixel grid in which the turtle lives. I am still getting the hang of angles and the x-y grid... Who knew 9th grade geometry would be so handy in a graduate course? I also changed the color to my favorite color, teal, and made the pen larger just to practice further with Python.

For the "own design" portion of this assignment, I really just played around. I couldn't come up with anything cute or creative, so I just took it step by step and messed around with Python until I got something that looks like a constellation, almost "Big Dipper-esque." So, it makes a handle, goes down at an angle, then makes a square at the end like a little soup ladle. To accomplish this, I defined a function that makes the whole thing. By making the basic shape a function, the lengths and different aspects can be moved around based on what the user inputs. So, I have the starting point (x,y), the color, how long the tip is, how long the handle is, and then the turtle. 

In the function, I start by changing the color of the turtle, lifting the pen up so it can go to the starting place (no Etch-a-Sketch skills needed here!), do the two lines of the handle of the ladle, then use an if-else to mess around with the lengths of the handle. I end by using a for loop to make the square. Then, I say what the space and turtle are, and call the function with some random input.

#!/bin/python3
from turtle import *
def shape(x, y, design, amount1, amount2, turtle):
  turtle.color(design)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.forward(amount1)
  turtle.right(50)
  turtle.forward(amount2)
  if amount2 >= 50:
    turtle.forward(50)
  else:
      turtle.forward(100)
  for i in range(5):
    turtle.forward(15)
    turtle.left(72)

space = Screen()
dave = Turtle()
shape(10, 15, "purple", 20, 10, dave)

I think playing around with these, it's a lot like art in real life: you have to have some basic mathemetical knowledge to get it "right," and you may need to test and adjust angles, colors, and how different things function together. Honestly, the turtles have actually helped piece together some other elements from Python because I learn much better with pictures than with text so my mistakes with a turtle seem a little more obvious to me than my mistakes with something text-based. I really want to learn more and how to change more things on the screen now.
