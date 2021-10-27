---
layout: post
author: agunnells
title: "Ali's Two Trinket Post and Reflection"
---
# The Trinket I selected from the Textbook: 

<iframe src="https://trinket.io/embed/python/0f06d0f6b1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# The Trinket I made:

<iframe src="https://trinket.io/embed/python/5e31a3ad90" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

When I first started working on my individual turtle design, I noticed that I experienced some of those overwhelming feelings that I have written about in past reflections. This is one of the first times that we've written our own program from scratch, and I was initially pretty nervous about that, so I think my brain went straight to shut-down mode. However, I did notice that I got over that impasse much quicker than I used to. I reminded myself that it was okay to not get the program "right" on the first try. Rather, I could tinker with my program as I built it. I started off by simply creating a turtle and starting to draw various shapes so I could become familiar with some of the turtle methods. In particular, I struggled with visually in my head how different angles would look in the program, so I tested out turning the turtle at a variety of different angles just to see what shapes would be created. 

After I spent some time tinkering with my program, I revisited the assignment instructions and saw that we needed to include for loops, a chained conditional, and a function. I was initially stumped by the chained conditionals, as our textbook did not really go into depth on those. I decided to simply Google "using chained conditionals with turtles in Python" to see what was out there. Seeing other examples helped me situate how chained conditionals could be used with turtles, and that led me to see if I could figure out a way to alternate the color of the lines as the turtle drew. I ended up testing out a chained conditional within a for loop:

```python
  for i in range(16):
    if i % 2 == 0:
      turtle.color(first_color)
      turtle.forward(50)
      turtle.right(75)
    else:
      turtle.color(second_color)
      turtle.forward(50)
      turtle.right(75)
      turtle.color(third_color)
      turtle.right(75)
      turtle.goto(0,0)
```

I think this was certainly a lightbulb moment for me in the sense that it reminded me to draw on my resources when I was feeling unsure about something. It further reinforced Elliott's advice that we aren't expecting to memorize everything about Python and know it forever; rather, we are learning how to read and write about Python so we can problem-solve when necessary. Furthermore, I actually had fun writing this program! I can tell that over the past few weeks I've learned to become more comfortable with imperfection and uncertainty, so I was able to allow myself to just enjoy the process of creating my own design with the code. 
