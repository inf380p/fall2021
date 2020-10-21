---
layout: post
author: pccisme
title: "Patrick's Clicky Turtle"
---

## Here's my clicky turtle:
<iframe src="https://trinket.io/embed/python/e3ba54bcde" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Reflections:
I try to create a game that is difficult for people, but at the same time, it has to be well designed and easy to play. In addition, I have played my game many times, and I am very confident in my game. I believe that this game will make most people feel that they want to challenge many times, and players will look forward to more modes in the future.

During the development of this game, I noticed the repeated code many times and tried to use loops, arrays, and dictionaries to avoid repeated code, making the code more concise. I like this process of optimizing the code.

### From
```python
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.setpos(30, 30)
t1.speed(10)

t2 = turtle.Turtle()
...
```

### To
```python
t1, t2, t3, t4 = '', '', '', ''
turtles = [t1, t2, t3, t4]
posX = {0: 30, 1: -30, 2: 30, 3: -30}
posY = {0: 30, 1: 30, 2: -30, 3: -30}
colors = ["red", "blue", "blue", "blue"]

for i in range(0, 4):
  turtles[i] = turtle.Turtle()
  turtles[i].shape("turtle")
  turtles[i].color(colors[i])
  turtles[i].penup()
  turtles[i].setpos(posX[i], posY[i])
  turtles[i].speed(10)
```

In the process, I found that I had to use global variables, but I often heard that this is a habit that should be avoided when building large systems, because it will be the cause of bugs. I think in the following days, I should search for related articles and refer to how other programmers achieve the same effect in other ways.

```python
def checkTouching():
  global gameOn
  
  if gameOn:
    global curScore
    global myscreen
    global posX
    global posY
    global turtles
    global sequence
    tinaX, tinaY = tina.position()
    t1X, t1Y = turtles[0].position()
    disX = abs(tinaX - t1X)
    disY = abs(tinaY - t1Y)
```
