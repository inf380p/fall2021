---
layout: post
author: zheinsohn
title: "Two trinket post and reflection"
---

My trinket from the textbook:

<iframe src="https://trinket.io/embed/python/4608ca3b23" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My Trinket I made:
<iframe src="https://trinket.io/embed/python/5e718fd840" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#Reflection:

At first, when introduced to using conditionals with turtle graphics, I couldn't think of how to work them in. Even after reviewing the chapter, I didn't have an immediate idea for what variables could be associated with the if/else statements. I ended up Googling what variables Python could use with Turtle graphics, and found out that one of the most common (or obvious) uses of conditionals in Turtle graphics was to use the modulus operator to make an alternating pattern, like so:

```python
 if x % 2 == 0:
      turtle.pendown()
      turtle.color("orange")
      turtle.left(101)
      turtle.forward(90)
 else:
      turtle.color("black")
      turtle.forward(90)
      turtle.left(100)
```

I remembered using the modulus operator to do something similar in previous chapters but it hadn't clicked that it could work with Turtle graphics.
From there, it was much easier to incorporate conditionals and nested 'for' statements, and I experimented with angles and distances, sometimes changing an angle by a degree or two each time to see the results, or changing the order in which the turtle would execute the actions.

After successfully running the basic program, I continued to add to it, just to get some hands-on experience using other turtle methods.
As I increased the range in the for loop, the program would take longer to execute, so I used the turtle.speed method in my turtlestar function to cut down on execution time. I incorportated turtle.penup() and turtle.pendown() rather than using different colors in the else statement to make a spiral pattern rather than have so many overlapping lines.

Sometimes, the program did something totally unexpected after what seemed to be a tiny adjustment, so going forward I want to clarify what exactly each method and adjustment does before I execute it and further explore the ways previous skills can be applied to turtle graphics.
