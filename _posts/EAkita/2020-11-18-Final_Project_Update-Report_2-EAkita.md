---
layout: post
author: EAkita
title: "Final Project Update & Stand-up Report 2"
---

**18 Nov 2020_Project Plan Discussion**

3D spiral slicing game

Embedded link below: 

<iframe src="https://trinket.io/embed/python/7e117c361b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


```python
#Testing the forward function with a square
def draw_square() :
    ak.fillcolor("Orange")
    ak.begin_fill()
    for side in range(4) :
        ak.forward(100)
        #t.down(100)
        ak.left(90)
    ak.end_fill()
ak.penup()
ak.goto(-150, 0)

#loop for forward motion
while True :
    #time.sleep(1)
  ak.clear()
  draw_square()
     # only now show the screen,
     # as one of the frames
  screen.update()         
  ak.forward(0.2) #change this to affect speed
```

**Reflection**
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

