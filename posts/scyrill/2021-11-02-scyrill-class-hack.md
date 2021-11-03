---
layout: post
author: scyrill
title: 'Stephanie's Class Hack'
---

# Reflection
For my hack, I wanted to create a small print of stars in the sky. At first I thought this would be simple as I thought I could just do what I did when we first learned about turtles, in which I could just write out every step that I wanted the turtle to take, copy it, and paste it a bunch of times. However, this would have been too difficult and time-consuming, along with it potentially becoming very lengthy. Therefore, I turned to the new material that we learned in class to create this starry sky. I did this using for loops, creating classes, geometric commands, and defining functions, along with using ```self``` in order to instantiate the creation of the stars in my sky.  

To start, I imported turtle using ```import turtle```, so that I could use all the features of the package. At first, I thought that this was the same as writing out ```from turtle import * ```,  but I learned quickly that these things were different. I wanted the background to be black, but in the process of trying to change the color of the screen from white to black, I hit a block. I tried the following variations:

```python
#Attempt 1
import turtle 
screen = Screen()
screen.bgcolor(“black”) 

#Attempt 2
from turtle import *
screen = Screen()
screen.bgcolor(“black”) 
```

Neither of these things worked! I was very confused because that was the way that I remembered learning how to change the background color, but now it didn't seem to work anymore, and the error message that kept coming up said, “NameError: name 'Screen' is not defined on line 4 in main.py” This was puzzling to me because I thought that ```Screen()``` was a built-in function in Python, so I was doubly confused. To solve this, I turned to Python docs and GeeksforGeeks, which helped me see that it was the way that I wrote my line of code that was the problem. The turtle package had to be called, along with ```Screen()```, followed by the background color, and then the color I wanted. I was kind of off, so to fix this, it had to be:

```
import turtle 
turtle.Screen().bgcolor(“black”)
```

And it worked! Though this was frustrating to run into so early on, it set a precedent for me that this was not going to be as similar as I thought it would be. After getting through this portion, however, with the help of the notes over last week’s material, the rest of the work felt easier. 

I created a class called ```MyTurtle()``` that took one argument, ```turtle.Turtle```. Following this I created and defined the function ```__init__``` and made it take one argument, ```self```. As I did this, my first question was, “What is self and why does it have to be in __init__? What is __init__?” I realized that these were still fuzzy to me, which led me back to the notes from last week’s lecture. Turning back to the notes, I learned that the putting in ```self``` wasn’t as random as I thought it was. ```Self``` stands in for any object and in this instance, it stood in place for my object, ```turtle```. This actually made it easier than writing out ‘gemma’ each time. As for ```__init__```, I learned that it was responsible for initializing an object's state and when an object is created, it assigned values to the class it's in. 

In application to my code, this meant that when I defined ```__init__(self)``` and later added components to the object ```self```, I was initializing what the object was going to be like and adding values to it. This made more sense after having these definitions solidified. After defining this, I set the speed, shape, and color of the turtle. Following this, I defined two new functions, ```draw_stars()``` and ```draw_small_stars()```. I separated these so that I could have a slight variation in the sizes of the stars. Though it probably would have been easier to just stamp stars across the black screen, it wouldn’t capture what I wanted to do, in which I wanted there to be a randomization of stars of different sizes on the screen to create a sense of depth.

Lastly, I called the function and had the turtle go to various places on the grid, in an attempt to randomize the placement of the stars.

# This was my code

```python
import turtle

#change the background color to black
turtle.Screen().bgcolor("black")

#set MyTurtle to like normal Turtle
class MyTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

#customize the components of the turtle
    self.speed(20)
    self.penup()
    self.shape("turtle")
    self.color("white")

#create a custom method that makes 'draw_stars' work on 'MyTurtle'
  def draw_stars(self):
    self.pendown()
    self.fill(True)
    for size in range(4):
      self.forward(100)
      self.left(145)
    self.fill(False)
    
#create a custom method that makes 'draw_small_stars' work on 'MyTurtle'    
  def draw_small_stars(self):
    self.pendown()
    self.fill(True)
    for size in range(4):
      self.forward(50)
      self.left(145)
    self.fill(False)
   
#name the turtle and set it to draw the first star in the center
gemma = MyTurtle()
gemma.goto(0,0)
gemma.draw_stars()

#continue moving the turtle to different places on the grid to randomize the star placement
gemma.penup()
gemma.goto(150,130)
gemma.pendown()
gemma.draw_small_stars()

gemma.penup()
gemma.goto(-150,130)
gemma.pendown()
gemma.draw_stars()

gemma.penup()
gemma.goto(0,-130)
gemma.pendown()
gemma.draw_small_stars()

gemma.penup()
gemma.goto(-90,-130)
gemma.pendown()
gemma.draw_stars()

gemma.penup()
gemma.goto(-125,0)
gemma.pendown()
gemma.draw_small_stars()

gemma.penup()
gemma.goto(160,-120)
gemma.pendown()
gemma.draw_stars()

gemma.penup()
gemma.goto(130,-110)
gemma.pendown()
gemma.draw_small_stars()

gemma.penup()
gemma.goto(-40,-45)
gemma.pendown()
gemma.draw_small_stars()

gemma.penup()
gemma.goto(-10,130)
gemma.pendown()
gemma.draw_small_stars()

gemma.penup()
gemma.goto(20,150)
gemma.pendown()
gemma.draw_stars()
```

# This was the result

<iframe src="https://trinket.io/embed/python/5c7d5cb968" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Result when introducing a new turtle

Out of complete curiosity, I wanted to try approaching my code from another angle by introducing a second turtle into the program that could draw the smaller stars instead of one turtle, Gemma, doing it all. 

<iframe src="https://trinket.io/embed/python/5f1b746851" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Something that I found interesting was that when I introduced another class that defined a different turtle, called Regis, and essentially put it in charge of doing the small stars in the ```draw_small_stars``` function, its placement of the stars was completely different compared to when I just had one turtle doing all the stars. I found this interesting and something worth looking into as the code is all essentially the same, but it seems that having this new class shifted the placement of the stars, though it was working fine before. 
