---
layout: post
author: acreese
title: "Alex's two trinket post and reflection"
---

# My Trinket from the textbook

<iframe src="https://trinket.io/embed/python/86339e52d8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# The Trinket I made

<iframe src="https://trinket.io/embed/python/f09ab55f7c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

I wrote a program with a function that draws a sprirograph – my favorite part of the the turtle chapter. I designed it so the user could chose the shapes (and sizes) of both the inner and outer shapes and thus control the pattern of the spirograph: `def spiro(turtle, inner=6, outer=3, i_size=20, o_size=50):'

It felt pretty straightforward after the lesson on “Making Patterns within Patterns” I just had to do a little adjusting with the inputs and create a simple equation to turn the turtle at the right angles.
```
for i in range(inner):
  turtle.forward(i_size)
  turtle.right(360/inner)
  for i in range(outer):
    turtle.forward(o_size)
    turtle.right(360/outer)
```

I had more of a challenge trying to come up with a meaningful if statement. I thought first about having my function assign different shapes different colors, but that felt fairly arbitrary (if potentially fun). So I began to think about inputs that would cause problems with my function and was able to come up with some if statements that returned different visual messages depending on the successful, unsuccessful, or potentially overly-complex spirographs. If a user chose an inner spirograph shape with less than 3 sides – hence not a polygon – the “pattern” is drawn but on top I drew a smiley face in red. If the user inputs a shape, whether inner or outer - with more than 25 sides, I abort the drawing because it would take too long and have the turtle draw a purple X instead. All other “successful” spirograph inputs get a green check in the lower left corner.

These drawings were actually more difficult than the spirographs because they involved more precise spacial thinking to orient my turtle in the right location and correct direction. I even had to do a little trigonometry to center the frown of my sad face under the eyes I had drawn. Overall this project was challenging and entertaining.
