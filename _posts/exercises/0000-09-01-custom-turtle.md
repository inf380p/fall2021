---
category: exercise
inclass: true
author: elliott
layout: post
---

## Custom Input for Turtles

Make a program that:

* prompts the user for a color and makes a Turtle that color
* prompts the user for a background color and makes it that color

To prompt the user for input we'll need Python's `input()` function.  We haven't learned about
functions yet, but since we're diving in we're just going to use it and see what happens.

Like much of the documentation we'll find in programming, these imply or depend on a lot of background
knowledge you may or may not have.  Push on even if you don't understand and see what happens in the
code!  I'll mention a few things that might help.

`input` gets a value, and we have to store it somewhere to use it in our program.  That's why in
the example on Stack Overflow there's an assignment of the statement to a variable.  For example, we
might store the result like this:

```
tina_color = input("What color should Tina be?")
```

This will cause a window to pop up asking "What color should Tina be?" and save the user input into
the variable.  We can then use the `tina_color` variable later, in place of something like `"red"` or etc.

Using this information, knock out the two components of the exercise above by Remixing this trinket:

<iframe src="https://trinket.io/embed/python/4be43cab26" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>