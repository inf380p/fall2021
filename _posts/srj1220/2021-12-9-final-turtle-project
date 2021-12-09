---
layout: post
author: srj1220
title: "Sarah's Final Turtle Project and Reflection"
---
I chose to create a turtle game for my final project, mostly because it seemed the most fun, and thus motivating. I was inspired by a flash game that my younger sister and I used to play for hours when we were kids.
It was on the American Girl website, and consisted of two dogs constantly running, each controlled by a different player, navigating around in a backyard while eating food and avoiding trash. There were several levels that included new obstacles and faster speed. I haven’t played the game in years, and I’m doubtful that the game is even possible to find in a playable format due to the Death of Flash.

I feel like I learned a lot while working on my final project. To be honest, even up until a few days ago, I wasn’t entirely sure that I would have a completed game that was functional, much less have most of my checklist completed. Now, when I look at it, I’m impressed that I managed to get so much of it done. My checklist from my last update was:

What I had completed:

*a “fence” buffer around the edges of the screen to keep the turtle inside the playing area
*“food” that triggers the score to be increased when touched by the turtle
*a win screen that triggers after the score reaches a certain number
*“poison” that triggers a lose screen when touched by the turtle
 
What I needed to complete:

*build the 2nd and 3rd levels (using the objects I already have and increasing difficulty by speeding up the turtle)
*trigger the 2nd and 3rd levels after reaching certain scores
*add custom graphics for the turtle food
*add help dialog
*allow players to replay the game
*create a score counter on the turtle screen
*create more obstacles(poison) inside the play area for the harder levels (STRETCH GOAL)
*reintroduce the 2nd player turtle (STRETCH GOAL)
 
My earliest drafts of the game had two different player turtles, but I removed the second player turtle sometime after draft 4, due to feeling a bit overwhelmed. As you can see from my goals list a couple weeks ago, I did have intentions to bring this aspect back to the game, if it were realistic to do so.
I did end up deciding to reintroduce the 2nd player turtle, as I felt like it made the game more fun, notable, and also allowed me to get my roommate to play with me as a tester. Without the second player, the game is still playable, but one player has to work both of the player turtles, which increases difficulty due to the ambidextrous nature of the controls.
The only one of my own goals that I did not meet was adding graphics for the turtle food. I was originally going to make a graphic of an apple or something similar for the turtles to eat, or have a random food graphic used of different foods such as apples, lettuce, etc. which would be generated each time the food was eaten.
Another goal that I simply did not meet was the ability to replay the game. The skeletons of that are still visible in the code, but are now commented-out. One of these skeletons is the "replay" message that is commented out on lines 164, 168, 172, etc. ```retrytext(turtle.Turtle())```. I was hoping until basically the last second that I would be able to make that work.
I attempted multiple methods for having a replayable game, and one was even to write the entire game code multiple times after each option.
That obviously was terrible for several reasons, so I attempted to define the game code as a function that could be called multiple times, but I kept getting a “disconnected” message from Trinket. I accidentally destroyed that last draft when I was moving over to a new draft trinket, but I have put the "repeat code after each option" draft below:

<iframe src="https://trinket.io/embed/pygame/2906a25a23" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
https://trinket.io/pygame/2906a25a23

I really had to work hard to not get too frustrated several times when I would repeatedly hit dead ends, so I often had to just step away and come back to it. This was especially true when I attempted to make the game replayable by having multiple copies of the game code in the file. In order to do anything else with that draft code, I had to manually go through each line and indent.
It was incredibly monotonous, which I think should have clued me in that I was absolutely barking up the wrong tree.

One thing that I’m incredibly happy I did is comment on virtually everything that I wrote! This made it so much easier to pull sections of code from old drafts to bring to new ones, as well as to pinpoint where things were going wrong when something wasn’t working right. I ended up having 16 drafts, and several of those were completely rewritten, so things did get confusing if I didn’t keep a vigilant eye on what I was pulling from where.

Probably the aspect of the game that took the longest for me to figure out were the collision boundaries. I had to watch several YouTube videos and read quite a few web pages before I actually understood how to get those to work and why they did work.
Thankfully, I did figure it out, because being able to interact with the food and poison objects was absolutely essential to my game being playable. I also knew from the very first draft that I wanted a “fence” around the border of the playing screen in order to keep the turtles from essentially dropping off the face of the earth and getting “lost”.
Because I wanted my game to emulate the dog game from my childhood, the turtles are perpetually moving forward. This gave me a lot of trouble before I had the fence, because I kept losing the turtle when I was testing my drafts out. The food collisions and the fence collisions are handled in fairly different ways, since the food and poisons are randomly placed and round shaped, while the fence is stationary and flat.

The fence collision is actually not a collision with the fence at all, but rather a collision with certain rows of pixels that I have marked:

```python

  if player1.xcor() > 235:
    player1.right(180)
  if player1.xcor() < -235:
    player1.right(180)
  if player1.ycor() > 235:
    player1.right(180)
  if player1.ycor() < -235:
    player1.right(180)
#player 2
  if player2.xcor() > 235:
    player2.right(180)
  if player2.xcor() < -235:
    player2.right(180)
  if player2.ycor() > 235:
    player2.right(180)
  if player2.ycor() < -235:
    player2.right(180)

```

Contrastingly, the food and poison collisions were done in a couple steps, which took me a lot of looking-up to learn how to do. First, the player turtles and the food and poisons were all given radiuses, then, further down, I had to monitor if the player turtle entered the radius for the food or poisons:

```python
player1.radius = 10
player2.radius = 10
food.radius = 3
poison.radius = 3
poison2.radius = 3
poison3.radius = 3
```

```python
if (player1.radius + food.radius) >= food.distance(player1):
  score += 1
...
if (player2.radius + food.radius) >= food.distance(player2):
    score += 1
```

(These are both plainly marked by comments in my final code, for full context)

Yet another aspect that gave me a fair bit of trouble at first was creating new levels. Unfortunately, this was all done in a draft that I did not preserve, but I spent several hours trying different variations of code, grew frustrated, only to realize that I was having errors because I had left out the colon after ```if score >= 6:``` in this block:

```python
  if score >= 3:
    level = 2
    player1.forward(3)
    player2.forward(3)
  if score >= 6:
    level = 3
    player1.forward(5)
    player2.forward(5)
  if score >= 9:
    goodjobtext(turtle.Turtle())
```
I only figured this out after critically reading the block over a couple of times, since I just simply was not noticing the missing colon at all. It was an interesting error, because, if I recall correctly, the game would occasionally run part way until it would reach a score of 6, depending on the code variation I was trying at the time. I really wish I had managed to save that iteration for the novelty, but it was rewritten during my troublshooting.

Reflecting back on the project as an experience, it really helped to solidify a lot fo the concepts that we learned in the first half of the semester. I could see myself playing around with building more turtle games in the future for fun, especially since I would like to learn how to make a game replay/restart via a prompt.
I'm mostly satisfied with my final project, though I wish had had been able to make it more flashy with graphics for the food and maybe also the background. It seems to run without any glaring errors, to me, and it was fun playing with my roommate during my testing phases.

My final project:

<iframe src="https://trinket.io/embed/pygame/59a802b3be" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

https://trinket.io/pygame/59a802b3be

