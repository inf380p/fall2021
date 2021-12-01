---
author: elliott
category: notes
title: "Project Updates; Custom modules"
layout: post
published: true
mode: Remote
---


# Announcements

* Meetup cancellations
* Github merging: might not get to it.




# Larger Programs with Turtle: Functions and Modules!

Here's an example from the text:

<iframe src="https://trinket.io/embed/python/1d8c3e5e1c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Functions** really shine in Turtle. You can draw some very complex pictures with relatively simple code.

As you add more and more functions to your code, though, it becomes hard to read! So, a new tool I'm introducing today is the **custom module**. This is essentially another `.py` file that contains code that _you wrote_, keeps it out of your way, and that you can `import` just like we've done, so far, with the build-in modules of the standard library (like `random` or of course `turtle`).

To do this:

* create a new file in Trinket with the `+` button
* name it `shapes.py`
* **cut** the lines defining the `square` function from `main.py` and **paste** them into `shapes.py`
* in `main.py`, add a line that says `from shapes import square`

Voila! The rest of your code operates just as it used to, but your function definition is in a separate file, making `main.py` easy to read.

## More on importing

Now that we're making our own modules, it's important to learn a little more about the `import` keyword in Python.

There are two ways to import things:

```python
import module
```

and

```python
from module import something
```
...where `module` is an actual module name like `random` or `turtle`, and `something` is a function, class, etc.

What's the difference?

Well, the first method imports things and keeps them in the **namespace** of the module. This means you need to type the module name to access them. Like this:

```python
import turtle

tina = turtle.Turtle()
```

That's more typing! Why would we do that?

Well, `from module import *` is another pattern you see that lets you not have to type a namespace each time. BUT you run the risk of **overwriting** the things you imported. For instance, importing `*` (everything) from `turtle` will create functions like `forward` and `backward`. If you use those names for something else, you'll overwrite them.

So, while it's more convenient to `import *`` _sometimes_, and especially while just learning, as you become more proficient as a programmer you'll want to import specific things. Or, just import the module, which gives you access to everything the module provides in a safe namespace that it's much harder to overwrite.

Tip: if you take my advice and just import specific things when you use `from`, you can provide a comma-separated list, like this:

```python
from random import choice, randint
```
That code will let you use the `choice` and `randint` functions without prefixing them with the `random.` namespace. If you keep coding and find you need a thrid function, just add it to the list! That's also how we accessed the function from our custom module above:

```python
from shapes import square
```

If you're going to extensively use a module, like `turtle`, it's probably best to just `import turtle` at the top, and use the namespace. Otherwise, just import what you need using `from`, and you can always import more

## Aliasing with `as`

Final tip with importing. You can rename a module when you import it with the `as` keyword. This is common in some third party libraries. With Numpy and Matplotlib, for instance, you'll often see examples that start like this:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Honestly, I don't like this, because the more terse namespaces become hard to read. But it's become the way many of these community members do things, so I want you to know about it, and if you go into scientific computing or data analysis you might want to do this too, to conform to the style your community of practice uses!

# Interface Notes

## Analysts

Your interface consists of two things: A way of getting input from your user, and logic for what to do about that.

Your interface sketch probably mixes these together. That's OK! You're sketching.

But at this point it's probably a good idea to think about using functions to get user input if you haven't already. That way, things like ensuring the user made a vaild choice, etc, can happen all over your program, reusing your code. Here's an example of how that might look:
<iframe src="https://trinket.io/embed/python3/a72ec71424" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I wrote the `get_input` part of this sketch quickly, trying to see if I could ensure that a function would only return valid input if I gave it a prompt and a list. I could then use this function in a larger program to do that job repeatedly.

Then, I set myself the challenge of making the user input easier. I wanted to automatically provide choice numbers, and translate those to the text choice. I wanted the **API** of my function to remain the same. In other words, I wanted the function to have the same **parameters** and `return` the same kind of data. That lets me replace `get_input` with `get_numerical_input` throughout my program, making no other changes, and gaining the numerical input functionality.

So, in addition to suggesting a specific approach to collecting user input in text interfaces, this is an example of how you might start with an initial idea and improve it over time. The latter part is relevant to everyone.

## Turtlers

_Your_ interface is circumscribed by what kinds of user events Turtle can handle. Those are: key presses, clicks, and drags. We talked about methods of the `Screen` class before, `.onkey()` and `.onclick()`. The `Turtle` class also has mouse-based event handlers, `.onclick()` and `.ondrag()`. The click methods for both need to point to functions or methods that accept two parameters, `x` and `y` corresponding to the X and Y location of the click (or drag). **You don't need to do anything with these parameters if the location of the click isn't relevant.**

In other words, if you want to use a turtle as a button for the user to change something about your game, the fucntion or method you pass to `.onclick()` needs to take x and y parameters but might just set some variable or change some state of your game.


Here's a sketch that demonstrates Screen and Turtle event handlers, and uses a custom module:
<iframe src="https://trinket.io/embed/python/b91cc63e7e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The animation code is separated from the rest of the game, and is imported. This keeps things organized.

I could also move some of the functions I wrote into other modules. BUT: be careful about what assumptions your functions make about variables that exist at that point in the program. Always move them one by one and test whether the program behaves as expected.

### Evolving your sketch

I got something usable above, then wanted to add a button. So, I **made a copy** and kept going. I got this:

<iframe src="https://trinket.io/embed/python/be0dcd052b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I added a class for turtle buttons. When clicked, they change Tina's color. The code that links my button with tina can't go in one of my custom modules, because `tina` gets defined in `main.py`.

I then noticed that when I clicked the button, `tina` would go there! That's not what I want. So I used an `if` statement to prevent tina from moving when the `y` value of the click is above `160`. This area of the screen is now I a place I can put clickable turtles. It's kind of like a menu area.

Note that there's only one function you can refer to in the Screen's `.onclick()` method. So, if you need screen clicks to do different things based on location, you'll need to write chained conditional (`if`/`elif`/`else`) statements to define that behavior. Or, like I did, 'turn off' part of the screen and put clickable turtles up there.

# Discussion & Review in Groups!

Pair or triad up into groups of students doing the same kind of project you are. Discuss your project updates, especially in light of what I've talked about in class today.

# Next week

* Optional work session.
* Submit links to your non-final posts and pull requests on Canvas
* Recommended project update. This is a great way for those who are worried about their grades to get extra assignments into the gradebook. And it's an opportunity for everyone to get accountability around making progress on the final.


## Code Style reading/reference

Python will accept different sets of code that produce the same exact output. The range of options within that space is the potential for *style*. Style is a convention of how to make these choices. We've seen plenty of examples:

* Capitalize class names (they don't have to be)
* Use `snake_case` for functions and variable names (you don't have to technically)
* Put your imports up top, then global variable definitions, then class and function definitions

Your reading for next week is a reference guide for Python style.  Different projects and people will have different style, and it's most polite to conform to their style choices if you contribute. For your projects, try to follow the Hitchhiker's Guide.


