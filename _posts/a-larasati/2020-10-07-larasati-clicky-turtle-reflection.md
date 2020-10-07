---
layout: post
author: a-larasati
title: "More Turtlehacks & Reflection"
---

<iframe src="https://trinket.io/embed/python/ef07218bcb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I had a pretty busy weekend so I didn't get a chance to really tinker around with the code to make anything exceptionally more interesting than what was already in the base code. In the `animations.py` file, I changed the `setup()` function so that it draws a lake with a little island in the middle, as well as modified the instruction to get the user to do something. 

In the `main.py` file, I added a line to call the `setup()` and `instructions()` function from the `animations.py` file. Since the turtle "responds" to the user input (which can be a click or with a keyboard), I had to make sure that every move or every click is being checked to see if it approaches the winning coordinates, so I made a `checkPosition()` function that I added to both the clicky and the keybinds. This `checkPosition()` function also triggers the `congratulate()` function if the user gets within the parameters of the correct (x,y) coordinate ranges. 

```python
def checkPosition():
  position = tina.position()
  x = position[0]
  y = position[1]
  if (x < -30 and x > -70 and y < 70 and y > 30):
    animations.congratulate(tina)
```

I didn't add this `checkPosition()` to `go_left()` or `go_right()` because those functions/keybinds just turns the turtle in a fixed coordinate.

With the clicky, I made it so that every time a user clicks, the turtle changes to a random color using Hex code. I had to Google how to get a Hex code randomly assigned, and an answer from StackOverflow gave me this, which I turned into a function:

```python
def changeTurtleColor(turtle):
  turtle.color('#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
```

I know that all Hex codes start with a # sign, and from what I understand, in this context `%` tells the machine that it's about to receive something that I don't know/is an unknown thing. `02` is for the number of digits it should consider/display, and `x` indicates that `02` correspond to the Hex value equivalent of the RGB number from `random.randint(0,255)`. I had to Google all of this and eventually ask for help to explain what these pieces mean.

I think I did alright for this exercise. I would've liked to add obstacles in the lake, like rocks or branches so that the user can't just click directly on the island or turn the turtle and make a beeline to the island, but for now this will have to do. I guess I'll have to tinker with it some more.
