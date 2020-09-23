---
layout: post
author: samandalib
title: "Treasure Hund Turtle Exercise"
---

<iframe src="https://trinket.io/embed/python/68c41140e9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
I started this excercise by thinking about what is the best way to inform user about their input impact. Games like this must have some kind of feedback loop
that directs user in some way to the solution. But here the challenge was whether I have to provide them with feedback on each of the values they entered, e.g. your X value is 
getting you there but your Y value is not, or it's better to provide an overall feedback about the user input without giving too much detail. I prefered the latter because it seemed
more entertaining to me. After making this deceision, I started doing some calculations on the paper to see how I can measure the distance of the existing position of turtle to the treasure
and by measuring this distance, provide the user with appropriate feedback for the next guess. It was a simple geometric calculation that solved the whole problem of distances for me
but one thing was still a challenge! In each step the distance base value should change while the treasure placement is fixed. For example, if we consider the treasure value is at
(50,50), the initial distance will be the distance from the starting point (0,0) to treasure point. When the user enters, for example (10, -35) as first input, the distance between 
the new point and the treasure point will be calculated and will be compared to the initial distance to see if the user is getting far from or close to the treasure point. Now in the next
iteration, the initial point will be considered (10,-35) rather than (0, 0) and any user input will be compared to the distance of this point to the treasure point. This was an iterative step
that must happen until the user finds the treasure. This part took a little time to be calibrated.

Another thing that I tried to consider in this program was user input evaluation. If the user enters invalid input like letters or numbers out of the requested range, they will be
penalized by getting back to the point (0,0). by defineing the "penalty" variable, I managed the program for penalizing the invalid input. It was a bit of challenge to find the best 
place to change th boolean value. 
