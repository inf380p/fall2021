---
layout: post
author: tommytester
title: "Tommytester's Custom Turtle"
published: false
---

Check out my awesome Trinket that takes user input and draws stuff!

<iframe src="https://trinket.io/embed/python/41f66471e6?start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Best day of my life.

I was really excited when I figured this part out:

```python
# make a super cool shape
shapesize = float(input("How big should my awesome shape be?"))
tina.penup()
tina.goto(-shapesize,shapesize)
tina.begin_fill()
tina.pendown()
tina.goto(shapesize, shapesize)
tina.goto(shapesize, -shapesize)
tina.goto(-shapesize,-shapesize)
tina.goto(-shapesize,shapesize)
tina.end_fill()
```

I wanted Tina to end up in the center, so I did this:

```python
# position Tina.
tina.penup()
tina.left(90)
tina.goto(0,0)
tina.color("black")
```
