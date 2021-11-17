---
layout: posts
author: amanda-guerrero
title: "Project Update and Interface Draft"
---

After the last class session, I decided that I wanted to start working on a snake game for the final project. For this assignment, I wanted to create the starting point for a snake game. I planned to create a program that had a box that would move as the user pressed different key directions. 
This is what I came up with for the interface draft assignment:
<iframe src="https://trinket.io/embed/python/900908cc19" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My first working version responded to the left and right key presses, but not for the vertical directions. I initially set the shape to a square, but it was difficult to observe the changes in movement. I decided to change the shape to an arrow `.shape("arrow")` so I could see the changes in direction more clearly.
This was the first iteration of the assignment: 

<iframe src="https://trinket.io/embed/python/937a7b6912" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 
This made me realize that I might want to adjust the direction that that the arrow is facing before it moves forward. I experiments with using `.setheading()` to get the arrow to face the direction of the key press. 
<iframe src="https://trinket.io/embed/python/137d15204e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

After a few more iterations, I came to the final version above. One thing I would improve about this version is how the square spins before going forward. I'd like to find a way to make that process happen faster, or get rid of the spinning altogether. 
In the coming days, I want to start working on setting boundaries for the game so when the snake hits the edge of the screen the game ends. 
