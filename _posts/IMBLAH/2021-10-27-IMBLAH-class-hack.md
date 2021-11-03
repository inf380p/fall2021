---
layout: post
author: IMBLAH
title: "Bo's Class Hack and Reflection"
---

# Class Hack
Here is an example of using `Turtle` to draw hearts randomly.
<iframe src="https://trinket.io/embed/python/4dbd2501bc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

First, I import three modules that I’ll use shortly.
```python
import turtle
import random
import math
```
I, then, extend the `Turtle` class, named `HeartTurtle`, that can change the color and starting position of the resulting object.
```python
class HeartTurtle(turtle.Turtle):
  def __init__(self, custom_color):
    turtle.Turtle.__init__(self)
    self.penup()
    self.color(custom_color)
    self.speed(10)
    self.goto(random.randint(-100,100), random.randint(-100,100))
    self.pendown()
```
As you can see, the starting position is randomized by using `random.randint()`.

In addition, I add a new method `draw_heart` to my class, which can accept one custom parameter, `size`, indicating how big the heart will be.
```python
  def draw_heart(self, size):
    self.begin_fill()
    self.left(90)
    # Upper part
    for i in range(20):
      self.forward(size)
      self.right(9)
    self.left(180)
    for i in range(20):
      self.forward(size)
      self.right(9)
    # Lower part
    length = 2*(size*20/math.pi)*2
    self.right(30)
    self.forward(length)
    self.right(120)
    self.end_fill()
    self.hideturtle()
```

Set the background color to black to make it fancier.
```python
space = turtle.Screen(200,200)
space.bgcolor('black')
```

I create two lists, `color_list` and `size_list`, from which I can choose `custom_color` and `size` randomly. These lists can be changed later which will definitely make this program more reusable.
```python
color_list = ['red','pale goldenrod', 'green yellow', 'burlywood', 'sandy brown', 'orchid', 'steel blue']
size_list = [1, 2, 3, 4, 5, 6]
```

To instantiate four objects of `HeartTurtle` class in a loop, I create a `turtle_name` list.
```python
turtle_name = ['A','B','C','D']
```

By instantiating these four objects in a loop and using `random.randint()` to generate index randomly, I can randomize the colors and sizes of these little hearts.
```python
for name in turtle_name:
  name = HeartTurtle(color_list[random.randint(0,6)])
  name.draw_heart(size_list[random.randint(0,5)])
```

# Reflection
For now, I think I’ve understood the big picture of extending a class and why it’s useful. It makes the class more **personalized** and **reusable**. However, I don’t think I’ve fully understood the syntax of it **logically**. For example, I can write the code above by comparing it with the code you walked us through during the class, but I’m not sure if I can make it without it.
It might need more **practice** and **running the code** to fully understand the **logic** behind the code. When writing the code above, I wrote `turtle_name = [A, B, C, D]` during my first try instead of `turtle_name = ['A','B','C','D']`. What Trinket gave me was `NameError: name 'A' is not defined on line 45 in main.py`. It reminded me that `A` without `‘’` is not a string but a variable. It should be defined first. 
It can be easier to write a block of code after understanding all of the syntax of the Python language, but it’s impossible. So **getting feedback through running** might be a great resource for learning Python.


