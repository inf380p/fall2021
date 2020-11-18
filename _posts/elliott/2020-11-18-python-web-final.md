---
author: elliott
category: notes
title: "Project Updates"
layout: post
published: true
mode: Remote
---

# Q&A



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
- **Methods**  are like **functions** that only can be called from an object.  Think of `tina.forward(100)``


# For tomorrow

* Revised Plan
* Classhack