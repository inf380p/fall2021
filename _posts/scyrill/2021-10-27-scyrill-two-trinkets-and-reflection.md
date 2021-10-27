---
layout: post
author: scyrill
title: "**Steph's Trinket Posts and Reflections**"
---

Trinket from the textbook:
<iframe src="https://trinket.io/embed/python/509cf6926b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Trinket that I made:
<iframe src="https://trinket.io/embed/python/509cf6926b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My Reflection:
Writing my own Turtle program was interesting because I didn’t know how Python could be used to draw pictures and make graphics. I did know a little bit about it because some old friends were in Arts and Entertainment Technology and I would see them coding to make their graphics. However, I didn’t think that that would be something that I would use. When we started the course, I remember that we talked about the things we would learn in class and Prof. Hauser showed us code that, when ran, would make shapes and change colors depending on the input. At that time, it was fun to run the pre-written code and play with the different things that could be added (I remember one of my first thoughts being, ‘Does Python really know all the colors or is it just RGB? Or ROY G. BIV?’ so I kept messing with various inputs waiting for it to crash or something to prove that I was right). In addition to this, I remember Prof. Hauser said that in this class we would learn how to write code from scratch that would allow us to do the same thing. This week, that came true. 

Going through this section on turtles was a lot easier than I thought it would be, some points felt easier to understand than all the other things we’ve learned, like dictionaries and tuples. However, something that I continually found myself having a hard time with was the positioning/direction that the turtle was supposed to go. I encountered this during one of the first free code exercises, in which the prompt was to write out a code that would return my initials in block style with two different colors (exercise 17.3.6). When going through this exercise, I found myself trying to orient the turtle in my head, only to realize that I didn’t know what direction the turtle faces to begin with; I assumed that it faced north, only to find out later that the turtle actually faces east and it has to be told to turn a certain number of degrees right or left. Figuring this out was half the battle, the next part was finding out where exactly the turtle would go on the coordinate plane since it started at (0, 0). Because my initials are ‘SC’, I needed a lot of space to write it out in block letters, so I had to move it. To do this, I chose random coordinates that I thought would put me far enough to the left that I would have enough space to write out my letters, this led to me choosing (-100, 100) as I thought it would provide enough room. Following this, I was kind of back at square one-- how to orient the turtle. Though I could kind of do it in my head, when I would write it out, I would immediately get lost or distracted or I would forget that my right facing my computer was the left of the turtle. These things did confuse me, so I took on another approach: I pretended to be the turtle. I stood up, faced away from my computer, thought about what I wanted my initials to look like and typed out the directions as I went through the motions the turtle would be doing online. The result was the following:

```python
from turtle import *
space = Screen()
gemma = Turtle()
gemma.color('red')
gemma.pensize(25)
gemma.penup()
gemma.goto(-100, 100)
gemma.pendown()
gemma.left(180)
gemma.forward(90)
gemma.left(90)
gemma.forward(90)
gemma.left(90)
gemma.forward(90)
gemma.right(90)
gemma.forward(90)
gemma.right(90)
gemma.forward(90)
gemma.penup()
gemma.goto(-60, 100)
gemma.color('blue')
gemma.pendown()
gemma.right(180)
gemma.forward(90)
gemma.penup()
gemma.goto(-60, 100)
gemma.pendown()
gemma.right(90)
gemma.forward(180)
gemma.left(90)
gemma.forward(90)
gemma.penup()
gemma.goto(0, 100)
```

Though this is super long and not the most elegant, I was glad that I could write it out and see my turtle, Gemma, write out my initials, especially since there were a lot of curves to account for. I was also glad that through my approach I solved the problem and more like it, as I ended up using it to do the rest of the exercises in the book. 
