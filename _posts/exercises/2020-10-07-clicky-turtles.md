---
layout: post
author: elliott
categories:
  - exercise
title: Clicky Turtlehack
---

{% include prblurb %}

___

This is another open-ended turtlehack, but now you've got lots of tools in your
toolkit.  Take the weekend code an awesome program.  Don't forget your Problem
Solving Attitudes and Strategies!

Write a turtle program that:

* Has a `setup()` function that sets up your screen visually. For instance, you could
draw green grass and blue sky using the `.fill()` method.
* Has two forms of user interface: clicks and keypresses.  Remember, Turtles can listen for click events, and Screens can listen for click and key events.

Option 1: Clicks

* Uses the `screen.onclick()` function method to call `clicky()` function you create
* Within clicky, do something cool.  Think outside the `.goto(x, y)` box :)
* Within clicky, **call** one or more helper functions you've created
* Within clicky or helper functions, use logic to change your program's behavior
based on the turtle's x and/or y coordinates.  For instance, you could vary the
turtle's color, speed, or call different helper functions.

Option 2: Keys

* Listen for at least the 4 arrow keys and one more key to control the turtle's position and one other aspect of its state.
* Call a helper function in at least one of your click functions


* Uses lists, loops, and string methods
* Does one of the following:
  * Allows the user to make something creative interactively
  * Has a 'win' condition.  Make sure to give instructions!
  * Implements a narrative animation.  `import time`, `time.sleep(x)` and `tina.clear()` will probably be helpful.  You'll also need to remember your interface elements!

# Advanced

If you'd like to stretch yourself, try these:

* Add other functions to `animations.py`, import them and use them in your main
program.
* Create a second turtle other than `tina` and have him/her also do something
in your clicky function.
* Explore the `screen.update()` and `screen.tracer()` methods to change how
often the screen updates and fix the zigzag artifacts.
* Add your own new module (i.e. `mymodule.py`) and `import` something from it.
You could even put your clicky function there to keep your code clean and readable.
* Read ahead on **dictionaries** and use some of these in your code.

## Starter Code

Use this Clicky starter code unless you feel like coding from scratch:

<iframe src="https://trinket.io/embed/python/fbf0c594fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Small changes to the functions in this code can yield big results!  And by understanding the patterns within it, you can create an entirely unique program.  Good luck!