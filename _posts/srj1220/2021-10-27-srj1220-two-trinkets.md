---
layout: post
author: srj1220
title: "Sarah's two trinket posts and reflection"
---

I chose problem 17.14.20 for my first turtle trinket:

``` #!/bin/python3
from turtle import *
space = Screen()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

t1.color('pink')
t1.right(90)
t1.forward(100)

t2.color('purple')
t2.left(90)
t2.forward(100)

t3.color('cyan')
t3.forward(100)

t4.color('yellow')
t4.right(180)
t4.forward(100)
```
https://trinket.io/python/c85161d501

This problem asked me to create a plus sign using 4 different turtles of different colors. I think that there may have been a way to do this using a for loop, however, I was tripped up by the fact that one of the turtles didn't need to change direction for it's branch (this was my cyan turtle).

This is my original turtle trinket:
```
#!/bin/python3
from turtle import *
space = Screen()
franklin = Turtle()
harriet = Turtle()
#x = 3


def spiral(turtle, color):
  for repeats in range(8):
    turtle.color(color)
    turtle.forward(75)
    turtle.left(45)
    for sides in range(6):
      #I had to fix the formatting but this was my conditional
      #if x > 1:
        #turtle.color('pink')
        #turtle.forward(50)
        #turtle.left(60)
        #else:
          #turtle.color('yellow')
          #turtle.forward(50)
          #turtle.left(60)
      
      turtle.color('pink')
      turtle.forward(50)
      turtle.left(60)
      for offshoots in range(3):
        turtle.color('purple')
        turtle.forward(7)
        turtle.left(120)


spiral(franklin, 'green')
#spiral(harriet, 'cyan')


```
https://trinket.io/python/933a85f220 

I think that the turtle-spirographs are super fun to code and then to watch run, since I loved my spirograph toy when I was a kid. No surprise, I tried my hand at making a more complicated spirograph code than the ones in our textbook, meeting the requirements for the assignment.
I managed to include 3 for loops (`for repeats in range(8):`,`for sides in range(72):` and `for sides in range(10):`) and a function (`def spiral(turtle, color):`). Unfortunately, I had a lot of trouble getting a chained conditional to work, and I’m still not entirely sure what I am doing wrong. I tried a few different options on placement, thinking that that might have been the issue, but now I think that it may have forgotten something important about the formatting. I’m not sure.
The spirograph does run if I take the conditionals out, though, so it shouldn’t be a different underlying issue.
The turtle named Harriet is a remain of my original conditinal attempt, since one of my earlier ideas was to have Franklin run for the if and Harriet run for the else. I deleted this code while trying to trouble-shoot, and couldn't remember what exactly I had had. The current commented-out if/else was made to quickly replace what once was there and to illustrate what my confusion is.
