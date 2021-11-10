---
author: elliott
category: notes
title: "Project Updates; Custom modules"
layout: post
published: true
mode: Remote
---


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



{% comment %}
# Q&A



# Code Style

Python will accept all sorts of things and produce the same exact output. The range of options within that space is the potential for *style*. Style is a convention of how to make these choices. We've seen plenty of examples:

* Capitalize class names (they don't have to be)
* Use `snake_case` for functions and variable names (you don't have to technically)
* Put your imports up top, then global variable definitions, then class and function definitions

Your reading for next week is a reference guide for Python style.  Different projects and people will have different style, and it's most polite to conform to their style choices if you contribute. For your projects, try to follow the Hitchhiker's Guide.


# Cowsays: APIs are cool

<iframe src="https://trinket.io/embed/python3/0577ff78e3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

What is the structure (schema) of the request?  [Read the docs](https://developers.google.com/maps/documentation/geocoding/intro#GeocodingResponses).
Why didn't I give you a link to the docs?


# Project Update

You know the drill.  This time, **use your snapshots**.

* Pair up
* Merge up
* Stand up (not literally)

During standup:

* What did you say you'd do?
* What did you actually do?
* Show and tell your program
* What will you do for next class?
* Any problems?

After everyone's done their update, revise your milestones (in your existing post) and **get your partner to merge your revisions**.


# Pair up, Merge up, Scatergories

Merge:

* Your original dictionaries post
* Your Web Dicts exercise

Discuss briefly. How many different approaches did we see?  What's the most important information for different use cases?



# Classes & Class extension Intro

As you will learn in your readings, a **class** is a recipe for setting up an **object**.  Classes should be familiar to you from Turtle:

```
tina = turtle.Turtle()
```

This says "Set up a **Turtle** object from the class definition in the `turtle` module."

You can both modify existing classes and create your own.

- **Attributes** are like **variables** that only apply to an object. Think of `tina.x`
- **Methods**  are like **functions** that only can be called from an object.  Think of `tina.forward(100)``

{% endcomment %}