---
layout: post
author: samandalib
title: "Reflection on the class so far"
---

For me the most interesting part of this class have been the simultanious focus of training on coding and collaborative programming. Using Github in this way is so interesting for me.
I always considered Github as repository for projects that I work on and a version controlling tool but in this course I realized how useful it can be for collaborative work.

The most challenging exercise for me was when I wanted to make a functional program to create a 3D texture with turtle:
https://inf380p.github.io/functional-turtle-excercise-samandalib.html

In this exercise I truly understood the importance of nesting code statements inside functions to be able to reuse them an infinite number of times when it is necessary. For example drawing
a cube took me about 40 lines of code and I wanted to repeat that in vertical and horizontal directions based on the user's input that could be anything! It was increadibly important
to use functions to be able to write this code and I don't think there is a way to write it without functions. At the end I just used a simple function to loop over a chain of functions:
```python
def draw(vertical,horizontal):
    newStartPoint = startPoint
    row = 1
    samtle.hideturtle()
    for i in range(vertical):
      drawHorizontal(newStartPoint, horizontal)#call method to repeat cubes horizontally 
      newStartPoint = ChangeStartingPoint(i,row)#change the starting point for the next row of cubes
      row +=1
      samtle.goto(newStartPoint)
```

Using Github was confusing at first, specially since I had to unlearn some of the things that I knew about it. I wasn't sure what exactly Pull Request do. This confusion made me to 
search for more in depth information about Github and pull requests and watch some videos on it. It was at that point that I got what we are doing with github and what every pull request
do in this course.

I found out that I have to be pretty flexible in solving coding problems. Sometimes I found out only by trial and error and changes in the values to get the right one, specially in the 
turtle exercise that I could see the result of the code visually. For example for drawing a cube with turtle, I did a lot of trial and errors to find the output that I was expecting and I don't
think any other method of solution finding works as efficient as this method.
```python
def drawCube():

    #rightside
    samtle.fill(True)
    samtle.color("blue")
    samtle.left(30)
    samtle.forward(length)
    samtle.left(60)
    samtle.forward(length)
    samtle.left(120)
    samtle.forward(length)
    samtle.left(60)
    samtle.forward(length)
    samtle.fill(False)
    #leftside
    samtle.fill(True)
    samtle.color("green")
    samtle.right(120)
    samtle.forward(length)
    samtle.right(60)
    samtle.forward(length)
    samtle.right(120)
    samtle.forward(length)
    samtle.right(60)
    samtle.forward(length)
    samtle.fill(False)
    
    samtle.penup()
    samtle.backward(length)
    samtle.pendown()
    
    #topside
    samtle.fill(True)
    samtle.color("red")
    samtle.right(120)
    samtle.forward(length)
    samtle.right(120)
    samtle.forward(length)
    samtle.right(60)
    samtle.forward(length)
    samtle.right(120)
    samtle.forward(length)
    samtle.fill(False)
    
```
Sometimes I had to get deep into the logic of the code and completely understand what is the result of each line of
code and how it affects the output of the program. Working with `while` loops is one of these situations that I found I have to
know exactly where change the boolean value to stop the loop. Also sometimes implanting intentional errors in the code were useful to find where the code breaks in the execution. So to me being flexible in 
thinking about the solution and trying different methods is considered the basic takeaway of this class so far.
