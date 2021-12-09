---
layout: post
author: amanda-guerrero
title: "Amanda's Final Project and Reflection"
---

For my project, I decided on the turtle game option. I chose this because I felt that the visual component for this project was more intuitive for me. 
While working through the Runestone assignments, I found the Turtle section the most interesting. 
I feel that at first I was imagining too big of a project - beyond the scope of the class - which added to my nervousness going into the assignment. 
Eventually, I settled on creating a snake game. I wanted to get into the mindset of a programmer by deconstructing a classic game and creating it from scratch in Python. 

When I first started brainstorming the different components of the game, I knew that I wanted to include the following components: 
	- getting the snake to move around the screen with key commands 
	- getting the food to appear randomly across the screen 
	- keeping score of the amounts food that the snake ate 
	- setting up levels

My first idea of the game was to have the snake increase in difficulty by increasing the speed with each game. 
Once I started working on the project, I quickly realized that there would be a lot of small components that I would have to keep track of. 

For the first assignment, the interface draft, I created the snake head and had it move with clicks. 
I had the most trouble figuring out how to have the snake move according to the orientation of the keys. I was able to get the snake to rotate with:
```
def go_left():
  tina.setheading(180)
  tina.forward(10)
  
def go_right():
  tina.setheading(0)
  tina.forward(10)
  
def go_up():
  tina.setheading(90)
  tina.forward(10)
  
def go_down():
  tina.setheading(270)
  tina.forward(10)`

#tell the program which functions go with which keys
screen.onkey(go_left, "left")
screen.onkey(go_right, "right")
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")
screen.listen()
```
At this point, I noticed that the snake head was doing full rotations before it moved forward. 
After meeting with Dr. Hauser during office hours, I got some guidance for how to rewrite the code.  

During the refactoring, I was able to get the snake to stop spinning around, since I took out the coordinates. 
This felt like a small issue at the time, but I wanted to get it sorted out before it potentially became problem when adding segments. 

During that same office hours session, I got some insight for writing the code that would make the game end once the snake hit the borders of the game screen. 

For my next working session, I decided to start setting up the “food” for the game. I knew that I wanted it to do a few things: 
  - appear randomly 
  - add a point to the score counter after the snake and food collided 

For this section, the online Python Game Development for Beginners videos were extremely helpful as I built out this section. 
I used the series of videos as a reference of steps that I would need to accomplish. 
I also referenced the turtle python documentation a lot throughout the course of the assignment. 
I think that one of my worries going into the project was not knowing what I was able to do with Turtle, so having the video series led me to useful methods that we hadn’t covered in class. 

I started working on getting the food to appear randomly across the screen. 
I initially thought that I would need to make 9 different piece of food appear across the screen. Overwhelmed at the thought of having to figure this out, I retreated for some time. 
This section took a lot of brainstorming for how I would logically make this happen. 
When I came back, I realized that I could get the same piece to move around the screen if I had the program check the intersection of the snake and food pieces with `check.intersect()`: 

Next, I started working on the written components of the game. 
I knew that I wanted to have a “Game Over” screen when the snake hit the edges of the screen, a “Win” screen, and indicator for the score and levels. 
I realized that I couldn’t effectively create a “win screen” until I created the counter for the pieces of food. 
I once again referenced the O’Reilly videos for the counter screen. 
Once I had that basic template done for the “Game Over” screen, I used similar conditions for the "Win" screen:
```
# Win the level if we reach the max score for the level
  if score_graphic.score >= max_score:
    tina.direction = "stop"
    tina.penup()
    tina.hideturtle()
    tina.clear()
    printwin(turtle.Turtle(), score_graphic.score)
   
  # Lose the game if we hit any of the borders
  if tina.xcor() > 190 or tina.xcor() < -190 or tina.ycor() > 190 or tina.ycor() < -190:
    tina.direction = "stop"
    tina.penup()
    tina.hideturtle()
    tina.clear()
    printgameover(turtle.Turtle())
```
At around this point in the project, I found myself struggling with a mental block. 
Since several pieces of my code were working as I wanted them too, I was hesitating to write new code out of fear that it would ruin everything I’d done so far. 
I had to push through the mental block by running the code constantly and accepting that there would be time where I had to start over. 

One of the most difficult parts of the game was figuring out how to add length to the body of the snake. 
I wanted the snake to grow with each piece of food that it hit. I created a list called `snake_segments`. 
I was eventually able to get the snake body to extend by creating a new turtle called `new_segment` and defining different characteristics, such as the `shape`, 	`color`, and `speed`. 
In doing this, I was able to get a new segment to appear in the middle of the screen. 
The difficulty from here was getting that segment to “attach” to the snake and move along with it.
For this, I extended the `def move()` function to update the segment locations in order of the most recently added segments to the oldest. 
I added a `for` loop that passes along the location to the older segments as we add a new segment at the location where the snake was. 

Once I was able to figure out how to add the “body” of the snake, I wanted to build out the levels. 
Due to time constraints, I decided to try to make the levels as simple as I could get them, which was a challenge in itself. 
I think that this helped me learn the value in simplicity. 
I wrote an `if` statement that told the program that once the score reaches a certain number, to update the level number by increasing it by one. 

One of the most time consuming, and confusing, parts was restructuring my game logic. 
I was starting to notice gaps in the logic of the game, so I started playing around with the restructuring of the code itself. 
I knew that the order of things mattered, but it was interesting to just how large of an impact refactoring had on its own, without adding anything else. 
I changed the order of the code around to signal that once we hit the food, the score updated, then the piece of food moved to a random location on the screen, 
and then added a new segment. 
I was also starting to get confused with differentiating between the graphic components of the game that show up on the screen, and more of the “behind the scenes” code. 
For my personal sake, I renamed the graphic components by adding `_graphic` to everything that visually appeared on the game screen. 

For the image requirement of the project, I decided that it would be easiest to add a background image for the game. 
My initial idea was to make the background of the game a picture of grass. I added this by using `screen_graphic.bgpic`

Getting the snake to collide with itself was one of the more difficult parts towards the end.
I was not able to work out the bug in the code. I was constantly getting errors in the middle of the game. 
For the sake of having a working game, I commented that entire part out. 

There are a few things that I would have liked to added if I had more time to work out the details. I would have liked to debug the game more. 
As of now, there is a bug where a square pops up in the middle of the screen for a second when a new segment is added. 
It didn’t seem to affect the game, so I left it and decided I would come back to it if I had time and let other sections take priority. 
I also would have liked to have a real-time game component where the snake constantly moved around the screen. 
During office hours, I got the tip to use `screen.ontimer` but I was not able to implement it. 
I would have also wanted to clear the game screen when the player either won or lost. As of now, the screen still displays the food and snake on the screen.
I think that I struggled with having the foresight to predict what I would need the snake to do. There were a lot more parts to the game that I hadn’t originally factored in and small details that I wasn’t able to catch. 
Overall, there are edits and additions I would have liked to made, but I’m content with the progress I made in the span of time I worked on the project. 

I think that reflecting back on this project, it was more challenging than I envisioned; but I was also more capable of writing code than I thought. 
It took me a while to begin to piece together what we learned throughout the entire semester. 
I reverted back to the material we had available constantly. 
One of the things that I struggled throughout the class was talking about code, which translated into me having trouble reading the code when looking for mistakes. 
I think that I had to start reading the code more to understand the underlying issues. 
I was used to retreating and running the code constantly, but this assignment forced me to spend more time reading the code in order to truly figure out the issues. 
Moving forward, I think I would like to continue developing that skill. 
I think that the process and skill that we’ve developed over doing reflections was very helpful for me through this process. 

Here is my final project: 
<iframe src="https://trinket.io/embed/python/741032d82e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
