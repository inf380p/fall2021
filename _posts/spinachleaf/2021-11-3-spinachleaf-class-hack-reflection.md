---
layout: post
author: spinachleaf
title: "class hack and reflection"
---

I created a trinket with 4 turtles that move to a random location on the screen and make a randomly colored ocean wave:
<iframe src="https://trinket.io/embed/python/f9f4bbe5c3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I really enjoyed this assignment. I'm still a little fuzzy on the vocabulary as it relates to turtles, but I had a lot of fun figuring out how to make the turtles do what I wanted.

This part below was the custom method I used to draw the wave:

```python
  #custom method 
  def draw_wave(self, color = colors):
    self.pendown()
    self.right(20)
    self.circle(60,90)
    self.right(140)
    self.circle(60,90)
    self.penup()
    self.hideturtle()
```
It took me a little while to get the starting orientation and turning degrees correct, but once I did I was really happy with how the wave turned out.

the `<import>` function still confuses me. To get both `<random.choice>` and `<randint>` to work, I had to include both of these lines:

```python
from random import randint
import random
```

I'm still trying to figure out why that's the case.

A lightbulb moment for me was getting my list of colors to work. I made it so that each turtle will be a randomly selected color from a list I chose. I originally had `<random>` but changed it to `<random.choice>` and then it worked.

Something that frustrated me was trying to call my turtle with another color to override the random color selection. I tried this:

```python
 def draw_wave(self, color = colors):
```

But then when I called `<draw_wave>`, it didn't matter if I tried another color. It didn't change. And I still haven't figured out how to get it to.


Overall, this assignment was challenging but really fun.
