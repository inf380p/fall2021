---
layout: post
author: weifeng0102
title: "Weifeng's class hack assignment"
---

# Trinket
<iframe src="https://trinket.io/embed/python/45474bc6fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Code
```python
import turtle
import random
screen = turtle.Screen()

class BoxTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

    self.speed(5)
    self.penup()
    self.goto(random.randint(-200,200),random.randint(-200,200))
  
  def star(self):
    self.pendown()
    self.fill(True)
    for i in range(5):
      self.forward(50)
      self.right(144)
      self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    self.fill(False)
    self.penup()    

p = BoxTurtle()
q = BoxTurtle()
r = BoxTurtle()
s = BoxTurtle()
p.star()
q.star()
r.star()
s.star()
```

# Reflection
To change each star into a different color, I first tried to set a color every time I created a turtle, but it was too inefficient to do so. If I use the color name to set the color in the definition of star, I need to change its color every time I draw a new star. Later, I finally thought of changing the color form to RGB and using the random function to randomly generate colors.
