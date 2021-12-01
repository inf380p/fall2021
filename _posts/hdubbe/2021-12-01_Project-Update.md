---
layout: post
author: hdubbe
title: Project Update and Standup Report (12/1/2021)
---

I am still experiencing the hang-up of not being able to drag objects one at a time which is frustrating. I have read over the Turtle documentation and tried everything I can think of but I am still getting the same issue with:
```
tim = CakeTurtle()
tim.goto(50, 100)
tim.ondrag(tim.goto, 1, True)
tim.onrelease(tim.base_layer)


tammy = CakeTurtle()
tammy.goto(25, 10)
tammy.ondrag(tammy.goto, 4, False)
tammy.onrelease(tammy.mid_layer)
```
I also began a start page for my game to distract from my ondrag problems:
<iframe src="https://trinket.io/embed/python/1377678f1a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I will work more diligently over the next week on my various bugs and aim to have a useable game by 12/9.
As far as milestones go:
I have created a buggy version of the first level and created a start page.
Going forward I need to comeplete:
-Level 2
-Level 3
- A way to win the game
- A winner animation.

Stretch Goal:
Level 4
I think I can do it I just need to work super diligently. 
