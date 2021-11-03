---
layout: post 
author: amanda-guerrero
title: "Class Hack Assignment and Reflection"
---

This is the trinket I created for the Class Hack assignment 
<iframe src="https://trinket.io/embed/python/8a1ef716b1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I started out with a general idea of what I wanted to create for this assignment. I knew that I wanted to create a star with a gradient of colors that appeared in all four quadrants of the page. I already knew how to create a start from a previous assignment: 

```
for i in range(5):
      self.forward(100)
      self.right(144)
```

I struggled the most with setting the `x,y` coordinates. I continued to overlook that I needed to extend the `Turtle` class in the `__init__` method order to make this happen. 

```
class StarTurtle(turtle.Turtle):
  def __init__(self,x, y, custom_color = "lemon chiffon"):
```

Once I returned to the textbook for reference, I was able to see my error. This was a case of me not fully taking the time to understand the assignment itself before diving in to a project.
The most time consuming part of this assignment was setting the custom parameters, like the colors `.color` and coordinates `.goto`. This was also the funnest part with getting to explore what turtle is able to do. 

I think that working in `Turtle` has given me a lot of clarity in working with Python. Since this is a visual format, I'm able to directly see how my code produces an outcome. I'm able to take different lessons from the semester to create a single project. Before this, I was struggling to understand how my code directly translated to an action.

I'd be interested in continuing to work with setting the turtle where I want on a page with coordinates. 
