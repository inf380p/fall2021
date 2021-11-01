---
layout: post
author: agunnells
title: "Ali's Class Hack Post"
---
# Here is the Trinket I created: 
<iframe src="https://trinket.io/embed/python/8da2908e12" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Here is my reflection:

In general, I felt pretty confident as I was working on this assignment. In class last week, I mentioned that turtles were not very intuitive for me, especially when it comes to telling them what direction/how far to turn. I definitely noticed that I felt much more comfortable with that aspect of `Turtle` when creating this assignment. However, there are still some things that are fuzzy for me. In particular, I still am a bit unsure about classes in general. I think I understand how classes work in relation to the `Turtle` class specifically, but I am not sure yet that I feel comfortable applying these concepts outside of working with `Turtle`.

Despite some of the fuzziness, I did have some lightbulb moments during this assignment. Since we had to instantiate four objects for our new `Turtle`-based class, I wanted to see if I could have each object create three copies of the same shape. I decided that each object I instantiated would draw three stars. In order to draw one star, I created this code: 

```python
      self.pendown()
      self.color(custom_color)
      self.fill(True)
      for i in range(5):
        self.forward(50)
        self.right(144)
        self.color(custom_color)
      self.fill(False)
      self.penup()
      self.forward(100)
```
Since I wanted to create three stars, my original function, which I called `draw_star` was simply that code written out three times in a row. Once I got that function working, I wondered if it was possible to make my code less verbose. I decided to try out nesting one `for` loop inside another. This led to my finalized function: 

```python
  def draw_star(self, custom_color = "black"):
    for i in range(3):
      self.pendown()
      self.color(custom_color)
      self.fill(True)
      for i in range(5):
        self.forward(50)
        self.right(144)
        self.color(custom_color)
      self.fill(False)
      self.penup()
      self.forward(100)
    self.hideturtle()
```
This was a lightbulb for me particularly because I feel much more comfortable working with verbose code, and wasn’t sure that I was ready to start paring down the code I have written. This assignment helped me realize that I understand the concept of `for` loops and the concept of paring down code more than I thought I did. 
