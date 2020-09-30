---
layout: post
author: samandalib
title: "Logical Turtle Excercise"
---

<iframe src="https://trinket.io/embed/python/3e4b70ee14" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
In this excercise, I wanted the user to be able to draw a cube while give them the freedom to decide about the size of it and the drawing speed. For getting the size of the cube, I 
assumed that the cube can be drawn in any size but a good one should have a size larger than 10 but not to be too large that get out of the screen. This input from user can be in any 
value and instead of checking the value and deciding about different conditions, I prefered to provide the user with a brief instruction in the input message and only check if the user
enters any non-numerical input to catch the error in this way.
For the drawing speed, I asked the user if they want to set the speed or not and I showed them (Yes/No) ans two valid inputs to the system. But since the input value is case sensitive,
users might type a valid input that the program doesn't recognize. I defined 3 popular variants of the input to check if any one was entered, the program considers it a valid input. I was 
thinking if the input was supposed to be something other than yes/no, the conditional can be too long and verbose to check every probability and I looked for it on the internet and found
that such issue can be resolved by using Regular Expressions that have a separate library. I didn't find myself comfortable to go for this library at this moment but I think it makes
the programming so much easier!
