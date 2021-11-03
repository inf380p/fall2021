---
layout: post
author: AU-turtledragon
title: "Aaron's Class Hack Exercise"
---

#My trinket is linked here:
<iframe src="https://trinket.io/embed/python/38a13f43a1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#Code Explanation and Reflection

All in all, I found this week's exercise to be fairly straight  forward.  I was too busy this week with other writing assignments (and my day job) to get very creative with it, so I just focused on meeting the assignment requirements.

My code extends the Turtle class to create `BeatleTurtle` based on the defaults of `Turtle` plus a few adjustments - two of which (color and y-axis position) are accepted at the time a new BeatleTurtle object is instantiated. 
1. slighly increased drawing speed and an initial drawing position of `.penup`.
2. a modified staring position - horizontally far left (-200) and a y-axis position defined during object instantiation (default is 0)
3. color - defined during object instantiation (default is "black")
```
class BeatleTurtle(turtle.Turtle):
  def __init__(self, color = "black", yaxis = "0"):
    turtle.Turtle.__init__(self)
    self.speed(10)
    self.penup()
    self.goto(-200,yaxis)
    self.color(color)
```
From here, I've defined a method `draw_circle()` that works on any object of class `BeatleTurtle` and takes a user-defined `size`size (1-25, default 25) and forward placement (1-400, default 200) from the established horizontal starting position. 
The method will set the `pendown` to begin drawing, travel forward the distance provided as `place`, draw a circle of the defined `size`, fill the circle with color, and continue drawing the rest of the horizontal line to the end of the screen.
```
  def draw_circle(self,size = 25, place = 200):
    self.pendown()
    self.forward(place)
    self.begin_fill()
    for side in range(30):
      self.forward(size)
      self.left(12)
    self.forward(400 - int(place))  
    self.end_fill()
    self.hideturtle()
```
From here, I've instantiated four unique BeatleTurtle objects named john, paul, george, and ringo - assigning each a unique color and y-axis starting position. 
```
john = BeatleTurtle("yellow", 150)
paul = BeatleTurtle("green", 50)
george = BeatleTurtle("red", -50)
ringo = BeatleTurtle("blue", -150)
```

With four unique BeatleTurtles having been instantiated, I now ask the user to provide two values to define the size and forward travel for the first drawing. 
`john.draw_cicle()` takes those `size` and `place` values and draws the first circle. 
```
size = input("enter a starting size (1-25)")
place = input("enter a left-right start placement value (1 to 400)")

john.draw_circle(size,place)
```
From here, `paul`, `george`, and `ringo` run their own `draw_circle()` method instances, each 1/4 smaller in size and x-axis placement than the one that came before. 
```
size = size * .75
place = place  *.75
paul.draw_circle(size, place)

size = size * .75
place = place  *.75
george.draw_circle(size,place)

size = size * .75
place = place * .75
ringo.draw_circle(size,place)
```

As I said at the top, I found this relatively straightforward and simple.  
But, within the tinkering process, I realized at least two things that remain fuzzy for me.

1. I get a headache trying to actually make logical sense of how the initial class definining syntax works.  
    ```
    class BeatleTurtle(turtle.Turtle):
    def __init__(self, color = "black", yaxis = "0"):
    turtle.Turtle.__init__(self)
    etc...
    ```
    I know what the result is of course and how to replicate it.  But, I just can't wrap my head around what each of those lines actually means. 
    
2. Likewise, I don't quite understand what the difference is between `import turtle` and the `from turtle import *` statement we were taught to use last week. 

3. We were also taught last week that we needed to create a Screen object before we could begin drawing.  Based on the examples from this week's class, I deduced that that I could conduct this week's exercise without that step, and indeed it works.  But I don't understand why that step is no longer needed or what part of my current code has essentially already taken care of it.

At present, I'm feeling a bit more comfortable with simply making my code work in these exercises.  But, I'm losing sight of how the syntax really works sometimes, which is making it hard to compose statements logically straight from my head rather than constantly referencing previous examples. 
    


