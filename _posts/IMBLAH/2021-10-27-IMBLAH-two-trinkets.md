---
layout: post
author: IMBLAH
title: "Bo's two trinket post and reflection"
---

# My Trinket from the textbook:
<iframe src="https://trinket.io/embed/python/88b612d760" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# My Trinket I made:
<iframe src="https://trinket.io/embed/python/d9d0048b68" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection
Here is a turtle program of drawing a pumpkin.
<iframe src="https://trinket.io/embed/python/d9d0048b68" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

First, I created a `screen` to draw on and three `turtle` objects - `orange`, `green` and `yellow` - working as three pens in different colors.
```python
space = Screen(200,200)
space.bgcolor('black')

orange = Turtle()
orange.color('orange')
orange.speed(10)

green = Turtle()
green.color('green')
green.speed(10)

yellow = Turtle()
yellow.color('yellow')
yellow.speed(10)
```
I also broke the whole process of drawing a pumpkin into 4 parts - `body`, `stem`, `eye`, `mouth` - because I think it will be easier for me to debug later on.
```python
#body
#stem
#eye
#mouth
```
In the following paragraphs of this reflection, I will introduce some strategies that I used to draw the body and the eyes of the pumpkin as they are the hardest parts of my coding process.
As I needed a lot of curves to draw for the body, I found it easier to use several circles to build up the body of the pumpkin. Also, I decided to use Figma to draw the body to figure out the relative positions of these circles, since I didn't know the relative positions of these circles, and I didn't know how to build up a coordinate system on the screen. It’s much faster to use Figma to figure out where the turtle should go than to run the code multiple times to find the best place to draw the circle.
Then I tried to use `turtle.circle()` to draw the circles but I failed due to the uncertainty of the direction that the turtle will take. To deal with this problem, I used a `for` loop to define a function `draw_circle` to make certain that the turtle was going in the direction I expected it to go.
```python
def draw_circle(turtle):
  turtle.begin_fill()
  for i in range(36):
    turtle.right(10)
    turtle.forward(9)
  turtle.end_fill()
```
As for the eyes, by virtue of the symmetric nature of the face, the turtle needs to take two directions. In this case, I took advantage of `if/elif` to define a function `draw_semicircle` that can take a `direction` to make it more reusable.
```python
def draw_semicircle(turtle, direction):
  if direction == 1:
    for i in range(17):
      turtle.right(10)
      turtle.forward(4)
  elif direction == -1:
    for i in range(17):
      turtle.left(10)
      turtle.forward(4)
```
Speaking of the whole process, the biggest takeaway is to run the code as many times as possible since it's useful when tweaking the code.
That’s it. :):)
