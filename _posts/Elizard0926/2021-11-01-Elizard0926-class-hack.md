---
layout: post
author: Elizard0926
title: "Elizabeth's Class Hack Post"
---

# Trinket
<iframe src="https://trinket.io/embed/python/337c5b55f3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

For my class hack trinket, I decided to instantiate five objects that would create the Olympic Rings logo. In the process of tweaking spacing and the overall look of the rings, I discovered early on that I needed to adjust the stamping speed. Originally, I set up the `Turtle` class extension to look like this:

```python
class squirtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

    # set color and position
    self.speed(0)
    self.penup()
    self.goto(-125,100)
    self.shape("circle")
    self.color("medium purple")
```

But I quickly realized that that was too slow, so I played around with the speed, setting it from 20 to 30 and so forth. I didn't notice a huge difference in speed though, and that's when I realized that I needed to adjust the custom method during this testing phase. I originally had it set to stamp 360 turtles (`range(360)`) turning right by 1. The code below shows the final method settings, but during the testing phase, in the `for` statement, I played around with different combinations of the range and turning. For example, I set `range(36)` and had the turtle offset by `self.right(10)`. Stamping 36 turtles is much quicker than stamping 360, and the overall effect resembled a circle enough for me to still recognize how to adjust the picture.

```python
#custom method
 def draw_circle(self, custom_color = "dodger blue"):
    self.color(custom_color)
    for i in range(90):
      self.forward(50)
      self.stamp()
      self.backward(50)
      self.right(4)
```

I am still unsure what the fastest speed a turtle can go is. Just Googling it, I get the answer that it's from 1-10, but I saw a clear difference between 10 and 30. That's when I found out that setting the speed to 0 tells the turtle to "turn off animation and go as fast as possible" (Runestone) which is what I ended up doing in the end. This is pretty helpful information for future reference. At the beginning, I also got a kind of “lacy edge” created by the heads of the turtle pen shape, so I looked up what shapes are possible and chose the circle pen shape for a smoother edge on the ring outline.

When I changed the pen shape to a circle, it occurred to me that I probably should include a “rapidly flashing images” warning. This made me wonder about accessibility in code and where this message should be posted for maximum visibility. For example, I put it in all caps at the top of my code in a commented out line, but are there other places I should’ve posted it?

Unsurprisingly, I figured out later that there was a built-in turtle function `circle()` that I could’ve used to make this code more efficient and print faster, but I think this was a useful review for how to draw a circle, or rather create a representation of a circle, manually.
