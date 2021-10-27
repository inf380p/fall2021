---
layout: post
author: itohosagie
title: "Itohan Osagie's Trinket Post + Reflection"
---

### Turtle Example from Textbook

<iframe src="https://trinket.io/embed/python/9571fb5f72" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### My First Turtle

<iframe src="https://trinket.io/embed/python/fcb6800020" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Reflection

For my first turtle design I wanted to create something light, fun, and festive for Halloween by writing a turtle program that draws *ghosts*.

My approach to the body of the ghost took a bit of time as I chose to continuously change the positions of the cursor by utilizing the `left()` and `right()` methods, along with `forward()` and this resulted in a good amount of guess and check. Even though this was not the most space efficient (or time efficient) code, following this process helped me become acclimated to the use of degrees associated with turtles. Here’s a snippet of the code I wrote to create the outline of the first ghost:

```
g1.left(90)
g1.forward(150)
g1.right(25)
g1.forward(30)
g1.right(65)
g1.forward(75)
g1.right(70)
g1.forward(30)
g1.right(20)
g1.forward(150)
g1.right(100)
g1.forward(30)
g1.left(20)
g1.forward(30)
g1.right(25)
g1.forward(15)
g1.left(30)
g1.forward(20)
```

Thankfully, once one outline for a ghost was created I just had to update the coordinates for the second one after picking up the cursor and placing it in a new location, captured in the following code:

```
g1.setheading(0)
g1.penup()
g1.goto(30,-50)
g1.pendown()
```

While trying to work out the bottom portion of the ghost’s outline I realized that due to the order of the code, the positions of the eyes and mouth drawn were based on the position previously set by the ghost outline, which made these components of the ghosts noticeably tilted. In order to resolve this issue the method `g1.setheading(0)`was added to reset the cursor before proceeding to the next element of the ghost. This was later added to the beginning of each block of code to separate both ghost outlines, eyes, and mouths. 

Before creating a function to use for the eyes and mouths, it helped to manually code the turtle with a for loop and guess and check the correct coordinates, which would then be used whenever the function was called. This made it easier to conceptualize what elements to include within the function, such as `(x, y)` position and color fill methods, as seen in the `square` function included below:

```
def square(turtle, length, x, y, color = "black"):
  g1.penup()
  g1.goto(x, y)
  g1.pendown()
  g1.fillcolor(color)
  g1.begin_fill()
  for i in range(4):
    g1.forward(length)
    g1.right(90)
  g1.end_fill()
```
Prior to attempting to create this function I was intimidated by the prospect of implementing these aspects of turtles so soon. I thought that it would be filled with countless amounts of errors that I would have to debug, but to my surprise after practicing with the placement of turtles and reviewing various examples for creating functions with turtles that set the position of turtles, assign and fill them with a specified color, and even utilize a `for in` loop, my initial intimidation subsided. Creating this function was actually very beneficial and space efficient as I just had to call the function six times with the different elements I wanted, as opposed to writing out separate turtle programs, so I’m thankful to have gained familiarity with this.

To finish off the turtle program I wanted the ghosts to send a message depending on the total amount present. To do so, I assigned a value to the variable  `ghost`, which was used in the subsequent conditional. If the amount of ghosts were between 1 and 2, then it would return “BOO” by calling the turtle. I’ve included the conditional below:

```
ghost = 2
if ghost < 1:
  print("Not yet scary..")
elif ghost > 2:
  print("Definitely haunted.")
else:
  g1.penup()
  g1.goto(0,-150)
  g1.write("BOO", None, "center,", "16pt bold")
  g1.goto(0,-160)
```

Even though we were introduced to turtles at the very beginning of the semester, I wasn’t sure how it would be if I created my own. But through this experience I was able to see how different aspects of programming like importing, methods, defining functions, indentation, loops, conditionals, etc. all come into play to create a program, and I look forward to more opportunities to implement the various topics of programming that we’ve covered in future projects and assignments. 
