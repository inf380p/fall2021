---
layout: post
author: samandalib
title: "Clicky Turtl Game"
---
<iframe src="https://trinket.io/embed/python/5c1750ca92" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---
Reflection
---
`The game scenario: Player should provide a path to the water (blue area on the top) for Tina(the turtle in the middle). This path should be less than 1000 miles in lengthl. If the player
can collect as many coins as possible in its way and intersect as little blocks as possible, they will get a higher score.`

This exercise was so challenging for me mostly because I wanted to challenge myself. I wanted to make a cool game with Turtle and I was thinking how to do this. I came up with a plan
of getting the turtle (tina) to water and collect as many coin as possible within the way. However, it wasn't really cool! I needed to add some blocks in the way that cause penalties
if Tina pass them. Just by having these two simple ideas, I found myself with a lot of work that I couldn't imagine in the begining. In the middle of working on the program I found myself
working with a lot of variables, lists, and functions. It took a lot of time to find things in the script. So I decided to divide the work into more files and use them as libraries in the main
file. I defined a lot of helper functions to calculate line formulas, distances, checking for intersections, showing coins collected and blocks intersected with. There was no better way
than putting all of these in a separate file with name `helpers` and call them from the `main.py`.

I worked a lot to find how to calibrate the scoring. Each coin has a value of one and each block has a penalty with the same value. The score will be `score = coins-penalties`. I had some
challenge in updating the scoreboard and at the end I just could overwrite everything for each update in the scores. At the end I found that the game was not so challenging enough.
After collecting a lot of coins and the least amount of block intersections, the player should provide a way for Tina to the water but that's not the only condition. I decided to limit
the total path length to 1000 miles so that the player be cautions about going for every single coin without considering the total distance of the path.

At the end I found the result really fascinating but it really took me out of my comfort zone and made me face with real challenges. It still has some bugs but I believe it is good Beta version
of what I was thinking from the begining.
