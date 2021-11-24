---
layout: post
author: Elizard0926
title: "Elizabeth's two trinket post and reflection"
---


# My Trinket from the textbook

<iframe src="https://trinket.io/embed/python/e2ec4caa66" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# My Trinket I made

<iframe src="https://trinket.io/embed/python/a5f632ac52" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection


From the WriteCode questions, I chose to do #17 (17.14.17) which is the problem that asks the programmer to draw a star based on the given picture. I was pretty excited going into this problem because I felt like the chapter had equipped me with the tools to do this successfully, and I was so ambitious that I thought that I perhaps would try to solve this problem two different ways. The first way would be based on the concept from the “Making Patterns with Patterns” section of the chapter. For the second way, I wanted to have the turtle draw the star in the way that I learned how to draw a star (like [this](http://www.howtodrawguide.com/drawing-techniques/how-to-draw-a-star-44/)) back in elementary school. Based on my load history, I ended up running code 88 times; it was frustrating to say the least.

The closest I could get to the result using the first “patterns” way used this code:

```python
from turtle import *
space = Screen()
liz = Turtle()

#VERSION 1 - PATTERNS WAY

#this part makes the pentagon
for repeats in range(5):
    liz.forward(30)
    liz.right(72)

#this part makes the triangles
    for sides in range(3):
        liz.forward(30)
        liz.left(120)
```

If you run this code, you’ll see that the star that it draws doesn’t quite look like the given picture. After experimenting with various angles and lengths, I quickly realized that the tricky part which was giving me the most trouble was that the “triangles” in the star are isosceles triangles. Besides testing and running different combinations of angles in lengths, one other strategy that I tried was using different colors within the nested `for` loops. So for the “this makes the pentagon” loop I made the pen color red, and then for the “this part makes the triangles” part I made it blue. This sort of helped me to figure out exactly what was happening, but it still didn’t help me in terms of figuring out why the pattern wasn’t working out the way I wanted it to. I decided to then move on to my second way where I wanted the turtle to ‘draw’ the star as a I would.

For all code in this reflection, “liz” is the name for the turtle. Here is the specific block of code that tells the turtle what to do:

```python
liz.left(70)
liz.forward(100)
liz.right(140)
liz.forward(100)
liz.right(140)
liz.forward(100)
liz.right(150)
liz.forward(100)
liz.right(150)
liz.forward(100)
```

As you can see, the lengths stayed constant, but there isn’t quite a consistent pattern in the angles. This is the result of again, a lot of just “plugging and chugging” and experimenting with different values. I had several difficulties involving issues such as closing the star at the end (for some reason, the last line wouldn’t connect and close the shape) and getting the star to be drawn standing upright. If you run the code above, you’ll see that the star is pretty rudimentary (definitely gives off the hand-drawn feel though!)

After retreating and running multiple times, I finally gave in and looked up “how to draw a star in Python.” I don’t see this as a total defeat because I was able to create several stars, albeit not perfect ones. Here is the the block of successful code:

```python
#VERSION 2 - DRAWING STAR
for sides in range(5):
    liz.setheading(70)
    liz.forward(100)
    liz.right(144)
```

What is interesting to me is that the programmer who came up with this code said that the turtle must be turned by an angle 144°, otherwise it will not draw the star correctly. Herein lies a fundamental problem I think. I spent a lot of time trying to figure out the geometry of this shape and how much I had to turn by or offset the shapes by, but I never came up with the number 144. With this new information, I tried my hand again at the first way, but still was not able to use the “pattern with patterns” method. It does create a cool star inside a pentagon though.

```python
#this part makes the pentagon
for repeats in range(5):
    liz.color('red')
    liz.forward(30)
    liz.right(72)

#this part makes the triangles
    for sides in range(3):
        liz.color('blue')
        liz.forward(30)
        liz.left(72)
```

For my personal trinket problem, I designed a problem where the turtle draws the letters “EL,” but then it asks the user to identify what letters were drawn. This was a good refresher on chained conditionals, and I think it was a useful exercise for me to think about all the possible inputs a user might give. I didn’t want to just have the right and wrong answer, so I tried to think of all the possible versions of EL that might be close, but not exact so as to give different responses in the printed feedback. Here is an excerpt from the code that details these conditionals:

```python
choice = input("What letters were drawn?")
if choice == 'EL':
    print("That's correct!")
elif choice == 'el' or 'le':
    print("Oh no! Please make sure answer is in all CAPS")
elif choice == 'LE':
    print("Almost, make sure you have the right order!")
else:
    print("Sorry, try again!")
```

I tried using a `for` loop to draw three branches or arms of the E, but couldn’t figure out how to increment the y-coordinate.

Despite the star troubles, I think this has been one of my favorite units so far, and I’m quite interested in the history of turtles and their development. I was also really intrigued by the idea of the “body syntonic” that was mentioned in the summary. It reminds me of my experience using Google Maps and how I’m constantly trying to figure out if I should go left or right relative to the direction that my blue dot is facing. Also, keeping track of position is something that reminded me of the infamous text adventure game Zork. Now I’m curious as to how difficult it would be to build my own text adventure game or something similar for the final project.




