---
layout: post 
author: amanda-guerrero
title: "Amanda's two trinket post and reflection"
---

# My trinket from the textbook: 
<iframe src="https://trinket.io/embed/python/6b81fdb020" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# My trinket I made: 
<iframe src="https://trinket.io/embed/python/0cc52ef945" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection: 

For my first post, I chose the Runestone problem that asked to create the letters CS out of block letters. I chose this one because of the slow stream of trial and error that led me to the solution. 

I initially started creating the letter C by going forward. I quickly realized that I would need to shift the letter over to the left in order for both letters to fit within the space allotted. 

I settled on `.goto(-40, 0)` as my starting point. From there, I worked by way backwards to create the C. Once I started working on the S, I shifted over to `.goto(40, 0)` to stay aligned with the C. I quickly realized that the S would require me to cut the `.forward(100)` in half to `.forward(50)` in order to create is evenly spaced. In order to match the height of the previous letter. 

I did all of this by recreating the letters backwards to how a person would normally write them, from the bottom to the top. Another way to have solved for this would have been to start at the top and work your way downward. 


For my second trinket, I created a 12 point star. I used the code for a 5 pointed start as a starting point. In this case, I continuously ran the code until I was able to achieve my desired shape. I played around with the angles and the range to close out the star. 

If the range was too small, it would not completely close out the star, and if it was too big, it would circle through the for loop too many times. One of the biggest lightbulbs for me was figuring out the conditional statement. I figured out that I would need to alternate between two angles to create a back and forth motion for the pointer to follow. I needed two different angles for when the number was even, and another when it was odd. 

For further practice, I would like to figure out how to fill in the star a single solid color. 
