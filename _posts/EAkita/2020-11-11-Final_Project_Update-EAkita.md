---
layout: post
author: EAkita
title: "Final Project Update and Revised Plan"
---

**11 Nov 2020_Project Plan Discussion**

3D spiral slicing game

Embedded link below: 

<iframe src="https://trinket.io/embed/python/37a9920875" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


**Reflection**
My focus over the last week was to create 3D graphics with python. I was successful in creating a cuboid and a sphere. The cuboid was basically positioning the squares correctly. However, the major road block was figuring out the sphere; this was much more involving. I resulted to using polar cordinates and playing around with equation of a circle and a sphere and I got it figured out as shown in the embedded code snippet below. Thus, initial milestone #1 done. 

```python
def oval(a,b,r): #(x-a)^2(y-b)^2 = r^2
  akita.up()
  #draw a circle
  for i in range (630):
    x = a*r*math.cos(i/100) #divide by 100, affects speed, change x,y = 1,10,100 for other interesting shapes
    y = b*r*math.sin(i/ 100)
    akita.goto(x-90,y-90)
    akita.down()
    
#function for sphere
def sphere(r,s, n): #customize with n
  for i in range (n+1): #11 for now
    akita.begin_fill()
    oval(s,s -(i*s/n),r) #circle
    akita.end_fill()
    for i in range (n+1):
    #akita.begin_fill()
    oval(s-(i*s/n),s,r) #circle reversal
    #akita.end_fill()
 sphere(5,15,5)
```

**Milestones**
Done - Figure out how to do 3D graphics with python. This will involve some math: vectors, 3D matrices etc. and I started doing a bit of reading on this.

   Figure out how to do a 3D rendering of the spirogram
   Figure out how to move the spirogram from the top of the screen, downwards
   Figure out how to “cut” or “slice” the volume
   Figure out how the volumes will fall, and what is considered “successful” and what is a “failure”
   Figure out how to score the game, and keep track of the score
   Add a restart button to reinitialize the game.

No new modification made yet. Just added stretch goals

**Next Step**
The next step will be to figure out how to use the concept fo 3D rendering for my spirogram (initial milestone #2). Overall, I think my milestones are ambitious enough. I should have this ready for class on Nov. 18th. 
* Draw a Spirogram in 3D
* Try to incorporate motion from top to buttom 

**Stretch Goal**
A stretch goal is to have 2 environments this game can be played in:
* In space, where the Physics is relaxed due to microgravity environment (spheres can fall in any direction)
* On earth, where the falling of the spheres is goverened by the laws of gravity (I'm thinking this might be more difficult, that's why it's a stretch goal; I might have to describe object inertia, maybe even prescribe random parabolic paths...)

Also, I think I can keep to my plan quite well. 


####Edit after initial commit and group discussion
I think my milestones are accomplishable, doable things that satisfy the criteria in the final assignment. I didn't make any significant changes to them. I'll keep on working to figure out the difficult parts involved. I'll also make next week's deliverable modular, so I can import in a main file. This will make changes down the line relatively easier. 

