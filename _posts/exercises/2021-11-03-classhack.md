---
layout: post
author: elliott
categories:
  - exercise
title: "Class Hack"
canvas: false
---

{% include prblurb %}
__


Extend the `Turtle` class such that your new class changes the color and starting position of the resulting object in the `__init__` method.

Then, **instantiate** four objects (or more) of your new `Turtle`-based class.

Then, add (at least) one new **method** to your class that enables it to make a shape when called. Your method should accept at least one custom parameter. Call this method on all four instantiated objects with different arguments to demonstrate how they change your custom objects' behavior.

For instance, if your method draws a triangle and then hides the turtle, and you choose method parameters that position your custom turtles in the four quadrants of the screen before drawing the triangle, your resulting program will show four different-colored triangles in the four quadrants of the screen.


To optionally challenge yourself, consider:

* instantiating your custom Turtles in a loop, or otherwise using loops to generate complex behavior from few lines of code
* using the `random` module to generate random integers, or choose random colors from a list you made.
* accepting parameters in your custom class

Have fun and experiment!
