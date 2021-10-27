---
layout: post
author: cridley17
title: "Claire's Two Trinket Post and Reflection"
---

The program below from the Runestone problems uses a turtle to draw a plus sign with each arm of the plus in different colors. 

<iframe src="https://trinket.io/embed/python/96e328563a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In order to do this the turtle, after drawing each line, must return to (0,0) and the color must change at this point. One thing to note is that the turtle is facing the same direction it just drew the line in, even if the location is moved back to (0,0). I struggled with this at first and was confused why the turtle wasn’t drawing the line in the direction I expected. To solve this I ran the program a few times with different angels and was able to figure out that the turtle only needs to turn 90 degrees each time. 

The code below of my own creation that creates a function that when called, if the first color in the function is green and the given length is below 100, the function creates a circle of ten stamped turtles on the screen. If not, two filled squares of the same color, and two filled triangles of the same color are created. 

<iframe src="https://trinket.io/embed/python/0b6cdc1d3a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

One thing I did not initially think of when writing the program, was that my circle of turtle stamps would not be completely visible on the screen if the length was too big. After realizing this I added `and length < 100` to my `if` statement below:

```
if color1 is 'green' and length < 100:

```

After I ran the code again with a length smaller than 100, the turtle was still not completely visible. I decided to test moving the turtle towards the top of the screen. I tried several different values for a y coordinate until finally getting to 180. This value ensures the turtle is completely onscreen when it stamps. Another thing I noted was that the turtle must be moved before the for loop, or the turtle will continue to move back into that location while the loop iterates. Another issue I needed to fix, was that the turtle draws while it moves. Before I moved the turtle, I added `turtle.penup()` so that a line wouldn’t be drawn when it moves to its new location.

When creating the squares and triangles, one issue I had to fix was the order in which I typed the `for` loops initially. When I first wrote the code, I created one square, the two triangles and then the last square was at the end. 

```
for side in range (4):
  turtle.color(color1)
  turtle.fillcolor(color1)
  turtle.begin_fill()
  turtle.forward(length)
  turtle.right(90)
  turtle.end_fill()
for side in range (3):
  turtle.color(color2)
  turtle.fillcolor(color2)
  turtle.begin_fill()
  turtle.forward(length)
  turtle.right(120)
for side in range (3):
  turtle.forward(length)
  turtle.left(120)
  turtle.end_fill()
 for side in range (4):
  turtle.color(color1)
  turtle.fillcolor(color1)
  turtle.begin_fill()
  turtle.forward(length)
  turtle.right(90)
  turtle.end_fill()
```

When I ran the code, the fill of the last square covered the fill for one of the triangles. To remedy this I put the for loops for the squares next to each other, and did the for loops for the triangles next so the fill for all the shapes was visible. I also needed to ensure that I ended the fill and that this line of code was indented correctly below the appropriate for loops. I used the code below to have the turtles draw this.

```
  else:
    turtle.goto(-50,0)
    for side in range (4):
      turtle.color(color1)
      turtle.fillcolor(color1)
      turtle.begin_fill()
      turtle.forward(length)
      turtle.right(90)
    for side in range (4):
      turtle.forward(length)
      turtle.left(90)
    turtle.end_fill()
    for side in range (3):
      turtle.color(color2)
      turtle.fillcolor(color2)
      turtle.begin_fill()
      turtle.forward(length)
      turtle.right(120)
    for side in range (3):
      turtle.forward(length)
      turtle.left(120)
    turtle.end_fill()

```

While writing this code, I realized that using functions, loops, and conditionals was not difficult. My issues writing the code arose from using the correct syntax for turtles, and ensuring that the turtle was drawing exactly what I intended. I realized that I do understand how functions, loops, and conditionals work in code, and I am able to use them if needed when writing my own code in combination with new concepts. This synthesis of concepts helped me to realize that I have learned more that I had previously thought and I now feel more confident in creating my own code. 
