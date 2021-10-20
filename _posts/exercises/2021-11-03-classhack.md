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


Extend the `Turtle` class such that it takes **three** (or more) parameters, and changes the color and starting position of the resulting object in the `__init__` method.

Then, **instantiate** four objects (or more) of your new `Turtle`-based class, with different parameters, to show how parameters affect the initial state of your objects.

Then, add at least one new **method** to your class that enables it to make a shape when called. Call this method on all four instantiated objects.

If your method draws a triangle and then hides the turtle, and you choose parameters that position your custom turtles in the four quadrants of the screen, your resulting program will show four different-colored triangles in the four quadrants of the screen.


To optionally challenge yourself, consider:

* instantiating your custom Turtles in a loop
* using the `random` module to generate random integers, or choose random colors from a list you made.
* accepting parameters in your custom method