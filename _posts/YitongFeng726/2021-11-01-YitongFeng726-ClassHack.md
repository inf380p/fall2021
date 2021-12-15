---
layout: post
author: YitongFeng726
title: "Yitong's Class Hack Post"
---

# Trinkt Link:
<iframe src="https://trinket.io/embed/python/3f336f81ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection:
After several times of failures and errors, I finished this assignment, firstly I created a class of turtles and named it as "SquareTurtle". I customized the initial turtle then I decided to draw the simplest squares and let the turtles move to the corresponding place to draw the graphs according to the instructions, and assign colors to each turtle.
One of problems I encountered in building this program is as follows. 
"line 107, in <module> import tkinter as TK ModuleNotFoundError: No module named 'tkinter'"
However, my code did not write up to 107 lines and I still wonder why did this bug occor. I deleted all codes and rewrite codes for several times, and I think sometimes it's because I used Turtle.() rather than self.() function. after solving this problem, I decided to set every position of turtles when calling methods of each object by using goto.(). 
In this assignment, I well reviewed the original methods of drawing graphs in Turtle and use for loop to draw shapes. Maybe next time i can try more difficult shapes and use random library to decide positions freely.
