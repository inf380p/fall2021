---
layout: post
author: benderliz
title: "Liz's Two Turtle Trinkets: Post and Reflection"
---

# First turtle Trinket for class 10/27

<iframe src="https://trinket.io/embed/python/4695ed9e36" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Second turtle Trinket for class 10/27

<iframe src="https://trinket.io/embed/python/8d1fcf9024" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

I find writing turtle programs to be a pretty rewarding experience. Although I do not consider myself a very visual learner, the visualized outcome of a turtle program is helpful feedback for how the code is written. I like that I am able to use the drawing as a point of reference for where I went wrong in my code, rather than relying on a potentially confusing error message. Interestingly, my partner, who is a machine learning engineer that uses Python for work every day, has not come across turtles much before. He was watching me code a turtle program, and he noted that he did not even really grasp what I was doing. But, to me, the directions (e.g. turtle.left, turtle.forward) are very intuitive.

I was confused at first about the use of functions in a turtle program. For example, when reading 17.10.3, I did not realize that the function was called 3 separate times to draw the varying sizes of squares. I had a lightbulb moment while writing my second tricket (a function that draws an equilateral triangle and is called 3 times) that the purpose of the function is to establish “repeatability”, and that it can be called multiple times with given inputs afterward. For instance, one set of inputs may be turtle Ed, and the color of the triangle is blue, and it is 80 units in length, while the next turtle is Petunia, and she is drawing a red triangle of 60 units in length. 

All of this said, I am still a little confused about why, in some examples, there are inputs given in the header of the function definition when the inputs are still given later when calling the function. For example:
```
def triangle(turtle, length = 80, color = ‘red’): # create function called triangle
# …
triangle(ted,100,'blue')        # call function for nico
```
Why would you ever put ``length = 80, color = red``, when those inputs will be overwritten later?
