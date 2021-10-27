---
layout: post
author: cmr4658
title: "Chase's two trinket post and reflection"
---

# My Trinket from the textbook (17.14.20):

<iframe src="https://trinket.io/embed/python/fab77b6b9e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# My Trinket that I made:

<iframe src="https://trinket.io/embed/python/47eca2b3a4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection
For this program, I decided to make a basic slot machine out of different Turtle shapes. First, I wrote a function like this for each shape (square, hexagon, triangle) so I could easily draw each one in a specific color:

```
def square(turtle, color):
  turtle.pencolor(color)
  for i in range (4):
    turtle.forward(60)
    turtle.left(90)
```

Then, I made lists for all the potential colors and shapes so I could pick from them randomly:

```
colors = ['red', 'green', 'blue']
shapes = [square, triangle, hex]
```

I wasn't sure if just adding the function names to the list would actually work since it didn't include the whole function, but it did (as long as the items *weren't* strings). It was definitely worth trying the simplest method first.

Now that all the components were ready to go, I had to put together the slot machine. Basically, I needed it to draw three random shapes, each in a random color, and then compare them to see if any matched. It would have been easy to just make three turtles and have them pick random colors and shapes from the list. However, it was trickier to figure out how to have each slot store the value for its own color and shape so it could compare with the others. I thought about making a dictionary for each position and setting the color and shape as key/value pairs, but I realized it would be easier to just make a Slot class:

```
class Slot:
  def __init__(self, xpos, ypos):
    self.color = random.choice(colors)
    self.shape = random.choice(shapes)
    self.turtle = Turtle()
    self.turtle.penup()
    self.turtle.goto(xpos,ypos)
    self.turtle.pendown()
    
  def drawShape(self):
    self.shape(self.turtle, self.color)
```

This made setting up the slots a lot easier. Before, I had a separate function to set up the turtles, but with a class, I could just include that setup in the constructor method. Also, I had originally had the drawShape method as its own separate function, but it made more sense organizationally to include it as a method in the Slot class since it wasn't used anywhere else.

When I wrote the chained conditional statements to compare the shapes and colors, I was glad I decided to use classes, since it ended up being pretty readable:

```
if left.color == center.color and center.color == right.color:
  if left.shape == center.shape and center.shape == right.shape:
    print('Jackpot!!')
  else:
    print('All colors match!')
elif left.shape == center.shape and center.shape == right.shape:
  print('All shapes match!')
else:
  print('Try again...')
```

If I were going to improve or change anything about this program, I would fix the spacing of the shapes a little and improve the overall look of the layout.
