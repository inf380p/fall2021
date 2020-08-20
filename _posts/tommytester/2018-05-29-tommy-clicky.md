---
layout: post
title: "Tommy's Clicky Turtle"
author: tommytester
published: false
---

<iframe src="https://trinket.io/embed/python/d6f752f169" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Reflection**

I wanted to make a drawing app that had user-selectable 'modes' and would allow the user to change modes based on their clicks.
I knew that meant I needed multiple turtles for the user to click, so I set up the screen with three different turtles.

Originally, I just had the modes be something basic like 'draw circle' while I figured out how to work on that. I needed to use
the `global` keyword to make sure I was setting the mode in a way that all the functions could access (Turtle is somewhat limited
in terms of the alterntative, which would be inputting and returning data in a functional style).

The `update_text` helper function is shared by all the turtles and is used to update the display of the mode of the correct turtle,
along with clearing the outputs of the other turtles.

Once I had my modes working, it was all fun ang games.  I wrote a fun formula to try to give an illusion of depth on the raindrops,
using the click's distance from the horizon line.  I satisfied the requirement to use an `if` statement by changing the behavior
of the main mode, Grass & Sky, based on whether the click is above or below the horizon line (which is just a simple y coordinate
comparison).

I had fun on this one!  Here are two pictures I drew with my program:

Traditional:

![]([Imgur](http://i.imgur.com/8n5IWnN.png)

Using animation artifacts for artistic effect:

![]([Imgur](http://i.imgur.com/I2lR24l.png))


Made a change!