---
layout : post
author : Boyeon Park
title : Boyeon Park's class hack assignment.
---


# Code

<iframe src="https://trinket.io/embed/python/2c33cbd350" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# What I did

I wanted to draw some shapes like stars with cool colors.

So I made a class and inside it made a method called `draw_star()` which can make stars with different sizes, colors and a stamp option using parameters.

I searched what colors I can use and picked ones that I liked.

I wanted to add some shapes using random colors so I searched how to use random colors and found out that I can give R,G,B number for color and can get random number for R, G, B using `randint(0, 255)` function.

To use that function, I should import randint using `from random import randint`. 

I also wanted to make shapes in random places so I used `randint()` for `goto()` function.

And also I found I can draw a circle with `circle()` function so finally I made a method drawing circles with random colors and places. 


# What I left for later
I wanted to make shape sizes smaller so searched about hot to change a shape size and found `shapesize()`method, 

but it seemed not working in trinket, I am not sure if it was because trinket doesn't support or I used wrongly.

I left this for a thing to figure out later. 

# Light bulb

I can fill using `fill(True)` , `fill(False)`  and also `begin_fill()` , `end_fill()`

`randint(0,255)` picks a random integer between 0 and 255

`circle(10)` draws a 10 size big circle

