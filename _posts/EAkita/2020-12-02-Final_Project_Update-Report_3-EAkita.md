---
layout: post
author: EAkita
title: "Final Project Update & Stand-up Report 3"
---

**2 Dec 2020_Project Plan Discussion**

3D spiral game

Embedded link below: 



```python
#################
#################
```

**Reflection**

I decided to shift gears to use pygame, since I realized this had a lot of cool built in features for game developement. So, I spent some time learning and playing around with the methods in pygame. 

*Hurdles*

I still haven't figured out how to properly code for a 3D spirograph. I believe this would be one of the coolest aspects of my game, so I'm pushing to get this done.  I think I can use revolutions of hyptrochoids. However, if I’m unsuccessful in this effort, I’ll stick with the 2D spirographs falling. 

I can successfully render the space background, but I was unsuccessful in printing the rest of the game to this space background screen. I'm sure I'm missing just a tiny syntax, and it's something I look forward to fixing before submission. 

*Successes*

I focused on other aspects of the game since my last report update. 
I got retangles falling vertically from the top to the buttom, an improvement from my last reflection. I also worked on adding the score feature. Currently, I don’t have any object interaction feature (eg. collision detection, slashing, etc), so the score just increases when the rectangles fall. This feature will be improved to reflect the object interaction feature when developed. 

Updating the vertical position for the created rectangles was slighly tricky, but I used lists, and once I got the indexing right, it became straighforward. Also, in creating the vertical motion, the object was jumping up and down the screen due to how I defined the update function. Thus, I figured I could adjust the frame per second using the pygame.time.clock() method which worked quite well. 

Furthermore, in creating the score, I realized that the score wasn’t increasing. It figured out that this was because the score set as an integeter and since intergers are immutable type, I couldn’t just directly increase the score by doing “+=1”. Thus, I had to reset the score to point to the new value. So in my updated_object position() function, I retured score when it was increased. And then down in my code, I reset my score by setting it to the function call. That line now updated my object position, and returned my score value. So I could now see the score increase. Later, I got the score to print to the screen. 

Moving forward, I would start reorganizing my code into classes, to make it easier to read and better formatted. 

**Next steps**

* Incorporate 3D figures (figure out the 3D spirograph volume)
* Incorporate level difficulty, could be more elements falling, or elements falling faster (need to think about this some more) 
* Try to figure out the slash function. 
* Refactor code to use classes
* Include dictionary for game state
* Add some game physics




My focus over the last week was to figure out how to use the concept fo 3D rendering for my spirogram (initial milestone #2). However, I ran into several roadblocks, and haven't figured it out yet. Thus, I pivoted to incorporating motion into my program, as seen in the code snippet above. I was successful in figuring moition for moving from left and right of the screen. 

Thus, initial milestone #1 done and part of #2 is done as well. 

**Milestones**

Done - Figure out how to do 3D graphics with python. This will involve some math: vectors, 3D matrices etc. and I started doing a bit of reading on this.
Partly done - Figure out how to move the spirogram from the top of the screen, downwards. 

   Figure out how to do a 3D rendering of the spirogram - **in progress**  
   Figure out how to “cut” or “slice” the volume
   Figure out how the volumes will fall, and what is considered “successful” and what is a “failure”
   Figure out how to score the game, and keep track of the score
   Add a restart button to reinitialize the game.
   **New Addition** - Use dictionaries to update the play with the game state. 

New addtion made to the original milestones, this involves adding dictionaries. The stretch goals are still the same though. 

**Next Step**
The next step will be to continue figuring out how to use the concept fo 3D rendering for my spirogram (initial milestone #2)- I'm essentially attempting to tack on hemispheres to my original sphere. The more I work on this, the more seemingly challenging it comes out tobe. I think my milestones are plenty ambitious. I should have this ready by Nov. 25th. 

*Finish drawing a Spirogram in 3D
*Alter motion from left to right, to top to buttom 

**Stretch Goal**
A stretch goal is to have 2 environments this game can be played in (this is unchanged):
* In space, where the Physics is relaxed due to microgravity environment (spheres can fall in any direction)
* On earth, where the falling of the spheres is goverened by the laws of gravity (I'm thinking this might be more difficult, that's why it's a stretch goal; I might have to describe object inertia, maybe even prescribe random parabolic paths...)

**More Reflection** 
There was talk on implementing dictionaries in our final code. I thus decided to add on a new milestone involving dictionaries to my list, as seen above. After spending some time figuring out the 3D spirogram, I think it's more complicated that I initially thought. I had to give myself an extra week to continue working on this. I had a good discussion with my group partner about how best to incorporate dictionaries. She came up with some pretty good insights which I'll try to implement. 


####Edit after initial commit and group discussion####
None so far
