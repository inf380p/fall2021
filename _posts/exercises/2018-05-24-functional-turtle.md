---
layout: post
author: elliott
categories:
  - exercise
title: Functional Turtles Exercise
inclass: true
---


{% include prblurb %}

**Note: For this exercise, embed both the original program and your refactor of it in the post.** See
below for instructions on duplicating your trinkets
___

Choose a previous Turtle program you've made and **refactor** it to use at least two custom **functions**
(i.e. made by you using the `def` keyword, not built-in).
At least one of these functions should take **arguments** and at least one should **return** something.

For bonus karma points, use some functions you have to **import** from the `random` or `math` modules.

WHen choosing a turtle program, one that has lots of repetitive code with slight variations is a
good candidate.  For instance, a program that goes to many x,y coordinates and draws a circle
would be a good fit to get re-written using this function:

```
def go_draw_circle(x, y):
    tina.penup()
    tina.goto(x,y)
    tina.circle(10)
    tina.pendown()
```

You have considerable discretion in what gets **parameterized** in your function. Parameterization is the
abstract concept of making something a function of an input, or parameter. Specifically, 'arguments' are parameters to 'functions' in Python.
For example, my function always draws size 10 circles.  I could re-write it with circle size as an argument
to the function and have control over that:

```
def go_draw_circle(x, y, size):
    tina.penup()
    tina.goto(x,y)
    tina.circle(size)
    tina.pendown()
```

**Don't make an entirely new trinket or dramatically expand on what your trinket does.** We'll do more of that later.

# Trinket Duplication

In trinket, you can **Duplicate** the trinket you want to refactor using the Duplicate button:

![Imgur](http://i.imgur.com/cIvqDkk.png)

