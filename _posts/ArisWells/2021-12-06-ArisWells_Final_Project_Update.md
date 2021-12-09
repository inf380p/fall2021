---
layout: post
author: ArisWells
title: "Aris's final project update"
---
### Description
I realized I forgot to make a couple previous posts.
Basically arbitrary barriers took a lot longer to get working than I anticipated
###

### Details
I now have a working system for keeping the Turtle between an arbitrary left and right boundary on the screen and am currently working on connecting multiple levels.

Current version combines wall drawing with the wall boundaries on turtle movement
<iframe src="https://trinket.io/embed/python/f9bbb9a18f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Just the wall drawing (no collision)
<iframe src="https://trinket.io/embed/python/969b5b251d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

A version with mouse drag to move (no collision)
<iframe src="https://trinket.io/embed/python/482e4d99e5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Developing a system for wall collision for 2 arbitrary walls proved more difficult than expected, and much harder than simply drawing the walls themselves.
My current plan is to have 3 levels which the turtle can navigate between and some sort of additional interactivity.
The points used to define the coordinates for the walls will be stored in a dictionary.


I don't want to do a "don't touch the wall" game so I'm not entirely sure what I will do.
###
