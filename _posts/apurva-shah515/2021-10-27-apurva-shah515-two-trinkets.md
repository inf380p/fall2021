---
layout: post
author: apurva-shah515
title: "Apurva's Turtle Trinkets and Reflection"
---

# Reflection

This week we have begun experimenting with the Turtle libary within Python to create some really interesting designs. Turtles are an interesting library, and especially writing my own program proved to be somewhat a challenge.
Making patterns with Turtles is relatively simple, however the process of including conditionals in a Turtle function or program took me a while to grasp. How exactly can we achieve this? What turtle methods can be incorporated into a conditional?

In the textbook we encountered creating patterns within patterns. For my own turtle program, I wanted to extend what we had encountered from the textbook with creating circular patterns through other shapes.  
I made use of the `turtle.stamp()` method to add some depth to the pattern. The patterns in the textbook were also very cluttered and difficult to make out, so I wanted to add some spacings and explored how this might be solved using a condition.

```python
for x in range(50):
          turtle.forward(100)
          if x % 2 == 0:
              turtle.left(175)
              turtle.stamp()
          else:
              turtle.left(200)
```
Rather than placing some condition on the attributes of the turtle or the space, I realized I could place a condition on the counter or range that I was looping through for my program.
Understanding how to properly add conditionals to the program took some time to wrap my head around, and I was forced to retreat and return to this program before I eventually came up with this solution.
Arriving at the exact form of the condition, `if x % 2 == 0:`, also took some exploration. Other values drastically alter the pattern to become a jumbled mess, however the resulting patterns are interesting in themselves.
I was particularly surprised by the versatility of the Turtle libary to create all manner of shapes and patterns. Making use of conditionals, different shapes and colors allows for creating some intricate nested patterns and shapes. 

At this moment the textbook and my experience writing programs using Turtles has been limited in using blocks and straight lines. Adding in curved objects or smooth edges would allow for much greater complexity.

This led me to the full program, incorporating creating a function, loops and conditionals in a Turtle-based program.

# My own written Turtle Trinket:
<iframe src="https://trinket.io/python/da29c7b95a" width="100%" height="600" frameborder="0" marginwidth="0" allowfullscreen></iframe>


# My trinket from the textbook:

The original question for this trinket was to create a single star. I played around with the code a little to create 5 stars, each a different color, and offset from one another by changing the initial rotation of the turtle before it begins drawing the star. 
<iframe src="https://trinket.io/python/c350faa643" width="100%" height="600" frameborder="0" marginwidth="0" allowfullscreen></iframe>


