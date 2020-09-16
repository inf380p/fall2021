---
author: elliott
category: notes
title: "Review; Final Project"
layout: post
published: false
---

# Q&A



# Cowsays: APIs are cool

<iframe src="https://trinket.io/embed/python3/0577ff78e3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

What is the structure (schema) of the request?  [Read the docs](https://developers.google.com/maps/documentation/geocoding/intro#GeocodingResponses).
Why didn't I give you a link to the docs?

# Pair up, Merge up, Scatergories

Merge:

* Your original dictionaries post
* Your Web Dicts exercise

Discuss briefly. How many different approaches did we see?  What's the most important information for different use cases?

# Dict Review

Make a dict

```
mydict = { }
mydict = dict()
mydict = { "key" : "value" }
```

Get a value

```
mydict["key"]
# returns "value"
```

Dict of dicts

```
# set "key" value equal to empty dict from the start
mydict = { "key" : {} }

# OR if dict already exists set "key" equal to empty dict this way:
mydict["key"] = {}

# put a value in the inner dict
mydict["key"]["inner key"] = "inner value"
```

In our homework there was a dict of lists of dicts with lists of dicts oh my!  When you encouter this stuff,
go back to home base: `print` & `type` to learn more.


# Classes & Class extension Intro

As you will learn in your readings, a **class** is a recipe for setting up an **object**.  Classes should be familiar to you from Turtle:

```
tina = turtle.Turtle()
```

This says "Set up a **Turtle** object from the class definition in the `turtle` module."

You can both modify existing classes and create your own.

- **Attributes** are like **variables** that only apply to an object. Think of `tina.x`
- **Methods**  are like **functions** that only can be called from an object.  Think of `tina.forward(100)

# Final Projects Brainstorms

Time to make our final pairs & groups.

* Pair up
* Merge Final Idea
* **Group Up** and discuss with your group

Go around, state your proposed project, and work with the group to critique and strengthen it.  Ask questions of each other!  Take notes on how you'd revise your plan in light of the feedback you've gotten.  At the end of class or tonight, Revise your plan as described in assignments.

# For tomorrow

* Revised Plan
* Classhack