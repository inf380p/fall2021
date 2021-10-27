---
author: elliott
category: notes
title: "Turtle +  Classes"
layout: post
published: true
mode: In Person
---
# Announcements

TBD

# Q&A

* Any questions or vocab?

# Turtle Methods

I'm going to offer you some unique takes on turtle methods, based on my almost decade long experience using it to teach. These are my takes, so you won't see most of the categories I'm gong to use in the documentation. But I think they'll help you anyways.

## `.forward`, `.backward`, `.left`, and `.right`: Turtle-relative commands

Proprioception is your sense of your physical body. One of the reasons Turtle supports commands _from the turtle's perpective_ is to engage this intuitive sense to help you connect the result of your code to the commands you're typing.

It is less efficient to program using these kinds of commands, but _that's OK!_ Much like typing something out instead of copy/pasting, sometimes the slow way is the best for giving your brain what it needs to learn.

It is totally OK to use these methods that key off of the Turtle's current state in this class. If you feel that telling a turtle what to do from its perspective helps you get fluent with code, keep at it. What you lose in terms of efficiency in drawing a house or a tree you'll make up for with a more intuitive sense of code.



## `.goto`, `.setheading`, `.sety`. `.setx` etc.: Geometric commands

Turtle also lets you directly modify


## What's good for what?

The turtle-relative methods like `.forward` are actually quite convenient if you need `Turtle` objects to behave like real living things. Since in a game or animation you won't always know the state of a turtle, telling it to `.forward(10)` is much simpler than calculating what `.goto` arguments will produce the same effect.

Geometry-based methods are very efficient and precise. They're great for when you need to draw complex shapes, or move a Turtle to a specific location. They're also flexible to use within loops, since you can manipulate the `x` and `y` parameters you pass to `.goto` in a way that might be difficult to do relative to each turtle.

Think of it like this: With turtle-relative commands you _modify_ the turtle's state based upon its current state. With geometric commands, you're _setting_ that state. The effect of calling `.forward(10)` depends on the Turtle's starting position and heading, whereas `.goto(10,10)` will always result in the turtle ending up at the position `10,10`.


## Turtle Design Philosophy: Flexibility of Use & Backwards Compatibility

You'll see that a lot of turtle methods have synonyms. `.seth` and `.setheading` do the same thing, for instance. Some of that is an attempt to accomodate the history of Logo. `seth` was a logo command, and one of the ways you can use turtle is to `from turtle import *` and write code very similar to Logo and it'll work great.

BUT Python is different, and has more space for long command names. It also values explicitness. So the `.setheading` method, called on a `Turtle` object, is the more Pythonic way of doing this. That said, supporting older ways of doing things is called **backwards compatibility** and is rather common in software. If you ever see something strange in a programming language, or support for a weird way of doing something, it might be an instance of backwards compatibility. This is similar to the reason why English has so many common irregular verbs (go => went, etc.). Programming languages and technologies of all kinds are inevitably shaped by historical inertia.

The historical details of things like this are interesting to nerds like me but I hope that a glimpse into _why_ Turtle is the way it is, where there are often many ways to do things and many supported syntaxes, keeps that unanswered question from getting in your way.

Turtle's flecibility of use, where for instance the `.color` method can take a color name OR a Red, Green, and Blue value, is great for learning but isn't something you'll see in most modules. This is because it's much simpler to maintain code that expects one and only one kind of input. But we're glad Turtle is like this, because it accomodates a range of learners, AND learning different patterns of using code.

## API is a User Interface

If you think about it, the `turtle` module is software someone else wrote. The syntax we have to use to get turtles to do things is a user interface for us, the programmer-users of the software.

Since we can use Turtle to make basic user interfaces, this really helps illustrate how technologies are layered interfaces!

The portion of someone else's source code you can interact with as a programmer is called the API, or Application Programming Interface. You're probably familiar with Web-based APIs, which let us interact with web-based services. Python can both call and even provide web-based APIs, but in this class when we talk about an API we're talking about things like the names of functions, their parameters and expected data types, classes and their methods, etc.

# Extending the Turtle Class

Class **extension** is starting from a Class that's already defined and then setting it up in a custom way and/or teaching it how to do new things. Here's an example extension of the `Turtle` class:

```python
class BoxTurtle(turtle.Turtle):
  # Override some defaults:
  def __init__(self):
    # First, set up BoxTurtles like regular Turtles:
    turtle.Turtle.__init__(self)

    # Then, customize these things:
    self.speed(3)
    self.penup()
    self.shape("turtle")
    self.color("brown")

  # a custom method that makes `.draw_square` work on BoxTurtle objects
  def draw_square(self):
    for i in range(4):
      self.forward(100)
      self.right(90)
```

## Understanding `self`

Each instantiated object is different, and has different characteristics. These characteristics can be accessed via dot-notation on the `self` object.

When you're defining a class, `self` stands in for any particular object. Once you've created an object, you can think of it as if that were to be called on the object instead.

For instance, let's create a `BoxTurtle`:

```python
tina = BoxTurtle()
```

When this line of code runs, `__init__` tells Python how to set `tina` up. As part of that, this:

```python
    self.speed(3)
    self.penup()
    self.shape("turtle")
    self.color("brown")
```

...happens like this:
```python
    tina.speed(3)
    tina.penup()
    tina.shape("turtle")
    tina.color("brown")
```

And so on with other `BoxTurtles` we instantiate.


## Methods

Methods are things certain Classes of objects can do. With `Turtle` ojects, you can think of them as new skills you're teaching the Turtle.

Think _creating) methods like creating functions: you use the `def` keyword, except methods always get `self` as a parameter, and always have access to the particular object they're being called on.


Let's play!

<iframe src="https://trinket.io/embed/python/b777d5e932" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


# Creating and Discussing Your Homework Posts

You created two turtle-based Trinkets, and reflected.

We're going to walk thorough creating a post and pull request to display them on the class website. This will be a review of materials on the [how-to](/how-to.html) page.


Class discussion!

# Making a Name For Yourself

Delayed til next week!

# Next time

## Class Hack

You've got the skills to extend the turtle class for homework!

## Diversity Discussion
There are a lot of readings for this! They're all short, though, and very worthwhile.

Take light notes as you read: I'll ask you to reflect upon the discussion and readings, and light notes will help both activities.

I'll be in Salt Lake City, but we'll still be able to have a synchronous discussion to start. We'll then move to an asynchronous mode. More details to come!

