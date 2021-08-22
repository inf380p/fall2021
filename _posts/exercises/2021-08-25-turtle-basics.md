---
layout: post
author: elliott
category:
 - exercise
title: "2. The Basics of Turtle"
inclass: true
---

# What can Turtles do?

Turtles were deisgned by programmers (all programs are, of course) and these programmers
thought of some cool things they thought would be useful to include in their code.
Later in the course we'll learn how to add our own cool abilities to turtles.  First,
let's see some of the things they can do.

All of the examples below assume you've already created a turtle named `tina`.

# Your Assignment

Make sure you've logged in to trinket.  Once you do, click **Remix** on the trinket below to save a copy to your account.

Play around with the various commands in this list, experimenting with as many of them as you can.  Try to make some cool designs!  Get comfortable with typing code precisely and recovering from errors.  Drafts will be saved as you work, but click Save once your done so others will see your updates when you share your work.

<iframe src="https://trinket.io/embed/python/13c51315d1" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Shape

Turtles can be all sorts of shapes, the coolest of which is turtle shape.

```python
tina.shape("turtle")
```

`circle` and `arrow` are two others. We'll learn later how to make our own.

## Forward, Backward, Left and Right

Turtles are great for learning because you can treat them like little robot animals.
Tell them to go forward or backward a certain number of pixels.

```python
tina.forward(100)
tina.backward(100)
```

Now, a square:

```python
tina.forward(100)
tina.left(90)
tina.forward(100)
tina.left(90)
tina.forward(100)
tina.left(90)
tina.forward(100)
```

The number passed to `left` and `right` should be a number of degrees.  See what
happens if you pass in a number bigger than 360

## Ah, the pen

Our Turtles are actually mutant (though not ninja) turtles.  You may have noticed that
they draw anywhere they move.  We can control that behavior with `.penup()`:

```python
# No line:
tina.penup()
tina.forward(100)

# Yes line:
tina.pendown()
tina.backward(100)
```

## Color!

Turtles can change into all kinds of awesome colors.

```python
# Red!
tina.color("red")
tina.forward(100)

# No, Blue!
tina.color("blue")
tina.backward(100)
```

## Stamp

Turtles can make a stamp of their shape that stays there even if they leave:

```python
tina.forward(100)
tina.stamp()
tina.backward(100)
```

## Circle

You guessed it:

```python
tina.forward(100)
tina.circle(10)
tina.backward(100)
```

## Fill

Turtles have a fill mode that will fill in a shape.

```python
tina.fill(True)
tina.forward(100)
tina.left(90)
tina.forward(100)
tina.left(90)
tina.forward(100)
tina.left(90)
tina.forward(100)
tina.fill(False)
```

## Goto

Know exactly where you want your turtle to go?  Make here go there:

```python
tina.goto(100,100)
```

See if you can figure out the extent of the coordinate system.

## Setx

Set the x coordinate.

```python
tina.setx(100)
```

## Sety

Set the y coordinate.

```python
tina.sety(100)
```

## Hide

Peek-a-boo turtles.

```python
tina.hideturtle()
```

## Write

Turtles are literate.

```python
tina.write("Heck Yeah!", None, "center", "16pt bold")
```

The list of **arguments** that write takes is an example of something that you'll need
documentation to really understand.  [Here are the docs](https://docs.python.org/2/library/turtle.html#turtle.write)

# The Screen object

When you make a Turtle, there's an invisible Screen object that the turtle moves on.
You can explictly create this object and then do things like change its color.

Try out this code:
```
myscreen = turtle.Screen()

myscreen.bgcolor("blue")
```

There are several other cool things Screens can do but we won't get to them til
later.  If you're interested, look them up!  You'll be able to use them in your
first homework.