---
layout: post
author: jasfromnz
title: “jasfromnz’s class reflection”
---

When I first started this class, I was excited to have a more structured opportunity to learn Python, but I was apprehensive about understanding and remembering syntax, because that had always been the biggest challenge for me when I had previously tried to teach myself Python. At first, that was my most common mistake in my programs, and I repeated a lot of the same errors, like forgetting colons at the end of conditional statements. However, as the semester has gone on I’ve noticed that I’ve started to make fewer mistakes, and more importantly, when I do make errors I’m able to identify and fix them much more quickly. As I’ve gotten more practice coding, I have also been to figure out issues I got stuck on previously. For example, I had trouble using logical operators in conditional statements when I was working on the Logical Turtles assignment, and in the end just changed my program to avoid the issue. Later, when working on the Turtle Hack assignment, I encountered the same problem- but this time, I realized that I had failed to write complete statements on either side of the logical operator.

```python
if user_input = “A” or “a”:
if user_input = “A” or user_input = “a”:
```

I also ran into problems when I tried to use clicks instead of user typed input for my Turtle Hack. I was thinking of screen.onclick() as a function, and was really confused as to how it would work. When I saw the starter code for the Clicky Turtlehack, it made much more sense. I was able to use the already defined clicky function to call another function I wrote, and “give” it the click input.

```python
def clicky(x, y):
  tina_x = x
  tina_y = y
  
  #tina moves
  tina.penup()
  tina.goto(x,y)
  
  #is it a door?
  door_test(tina_x, tina_y)
 ```
 
Although I’m still a little fuzzy on the details of using the screen.onclick() method, I feel confident that I’ll be able to figure it out just by messing around with it some more. For me, trial and error has proven the best way for me to figure out or learn a new concept. By trying all the ways that *don’t* work, I get a better understanding of why the other methods *do* work.
