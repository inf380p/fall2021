---
layout: post
author: EAkita
title: "Final Project_Turtle Game"
---

**11 Dec 2020_Project Submission**

Embedded link below: 

<iframe src="https://trinket.io/embed/pygame/e5821a9bf4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



**Reflection**


**Initial idea: 3D spiral slicing game**

I initially wanted to build a Spirograph a 3D volume and try to make it fall from the top of the screen to the bottom. Then I could have a user slice through it and it will fall apart, just like a slicking fruit game.

**Original Milestones**

    1. Figure out how to do 3D graphics with python. This will involve some math: vectors, 3D matrices etc. and I started doing a bit of reading on this. 
    2. Figure out how to do a 3D rendering of the spirogram 
    3. Figure out how to move the spirogram from the top of the screen, downwards 
    4. Figure out how to “cut” or “slice” the volume 
    5. Figure out how the volumes will fall, and what is considered “successful” and what is a “failure” 
    6. Figure out how to score the game, and keep track of the score 
    7. Add a restart button to reinitialize the game. 
    
    
**Stretch Goal** 

I defined stretch goals is to have 2 environments this game can be played in:
* In space, where the Physics is relaxed due to microgravity environment (spheres can fall in any direction) 
* On earth, where the falling of the spheres is goverened by the laws of gravity (I’m thinking this might be more difficult, that’s why it’s a stretch goal; I might have to describe object inertia, maybe even prescribe random parabolic paths) 

This main idea of this game was later changed to be avoiding multiple obstacles, then avoiding one obstacle. 

My focus when I started this project was to create a 3D graphics game with python. I was successful initially at creating a cuboid and a sphere. The code snippets are seen in my previous reflections. The cuboid was basically positioning the squares correctly. However, the major road block was figuring out the sphere; this was much more involving. I resulted to using polar cordinates and playing around with equation of a circle and a sphere and I got it figured. Thus, initial milestone #1 done. My next step after that week was to figure out how to use the concept of 3D rendering for my spirogram (initial milestone #2). Overall, I thought my milestones were ambitious enough. 

For the second week, my focus was to figure out how to use the concept of 3D rendering for my spirogram (initial milestone #2). However, I ran into several roadblocks, and hadn’t figured it out yet. Thus, I pivoted to incorporating motion into my program, as seen in the code snippet in trinket (reflection #2). I was successful in figuring out motion for moving from left and right of the screen, and was happy about that progress. Thus, initial milestone #1 done and part of #2 is done as well.

At this point, I made an addition from the course deliverable to include the use of dictionaries to the original milestones. However, as will be seen later, I didn’t spend much time on the dictionaries, even though I attempted to include it in my game. The next step from there was to continue figuring out how to use the concept of 3D rendering for my spirogram (initial milestone #2). At this point, I was getting quite frustrated. I was thinking of tacking on hemispheres to my original sphere. The more I work on this, the more seemingly challenging it comes out to be. I figured out my milestones were plenty ambitious then. I planned on finishing the spirogram 3D, and then alter the motion of my obstacle from left to right to go from up to down.
Based on the issues I was having, I decided to shift gears to use pygame, since I realized this had a lot of cool built in features for game development. So, I spent some time learning and playing around with the methods in pygame.

*Hurdles* 

I still hadn’t figured out how to properly code for a 3D Spirograph. At this point, I still believed this would be one of the coolest aspects of my game, so I was hoping to get that done. I think I can use revolutions of hyptrochoids (something I read). However, I figured that if I was unsuccessful in that effort, I’ll stick with the 2D objects falling. At this point in my progress, I could successfully render the space background, but I was unsuccessful in printing the rest of the game to this space background screen. I was sure I was missing just a tiny syntax, and it’s something I look forward to fixing before submission.

*Successes*

I focused on other aspects of the game since my last report update. I got rectangles falling vertically from the top to the button, an improvement from my last reflection. I also worked on adding the score feature. At that point, I didn’t have any object interaction feature (eg. collision detection, slashing, etc), so the score just increases when the rectangles fall. I was hoping to improve that feature to reflect the object interaction feature when developed.
Updating the vertical position for the created rectangles was slightly tricky, but I used lists, and once I got the indexing right, it became straightforward. Also, in creating the vertical motion, the object was jumping up and down the screen due to how I defined the update function. Thus, I figured I could adjust the frame per second using the pygame.time.clock() method which worked quite well.
Furthermore, in creating the score, I realized that the score wasn’t increasing. It figured out that this was because the score set as an integer and since integers are immutable type, I couldn’t just directly increase the score by doing “+=1”. Thus, I had to reset the score to point to the new value. So in my updated_object position() function, I retired score when it was increased. And then down in my code, I reset my score by setting it to the function call. That line now updated my object position, and returned my score value. So I could now see the score increase. Later, I got the score to print to the screen.
Moving forward, I was hoping to start reorganizing my code into classes, to make it easier to read and better formatted.

*Final Stretch*

I realized that week that I we weren’t supposed to use the pygame module, so I had to convert all my code to base python turtle code. This process took some time. This was for the final stretch. At this point, I had simplified my idea from 3D Spirograph rendering to 2D objects falling vertically. I had the first stretch goal reached, which was to have the game played in space. I didn’t attempt the second stretch goal though. I included a class extension for drawing a Spirograph when the player won the game. This extension was successful when I wrote and tested it, but was throwing errors when I integrated it into my program. I created a few custom modules to use in my main.py script, but because of how I wrote the code, I ended up having quite a bit of code in the main.py which could have been organized also. I tried to use variable names that were clear and concise. 

I spent a lot of time figuring out how to randomly create objects on the top of the screen, and update them so that the player could play and have a better experience. For some reason, the objects were continuously drawn, and the screen wasn’t updating. I narrowed it down to how I was writing my enemy.goto(object_pos[0], object_pos[1]). I figured later on that I could register a shape, and then update the position of that shape, without drawing it continuously. 

I think my main.py thoroughly communicates what my program does. I have a very simple interface, which welcomes the user at the start of the game and prints a help function when “h” is pressed. I printed most of my return statements to the print screen terminal so that the player could see it as the game went on. I also had a lot of difficulty with the collision function, but I got that figured out. I also had issues with. This was because I first had to decide what defined collision, and after figuring that out, I overlooked the +/- signs (thus from -400 to 400) so > -400 is different from > 400. I also used custom image for the background, so that was nice. 
I had to periodically save my game every so often, since pygame trinket was freezing very so often. I think it might have been due to inefficient code on my part, or maybe just a slow browser. I also used functions like time.sleep() and multiple (commented out) print out statements to test  animations update and portions of code. Furthermore, I used lists when initializing variables such as the player position, and used the correct indexing in the rest of the code. This made it cleaner and easier to manage down the line. Also, when setting the object_position, I had to adjust the frame rate per second because the enemy object was flying up and down the screen, which was a bit scary.  

All round, this turned out to be a pretty challenging project. I overshot in the beginning, had to learn how to do multiply different things and how to properly scope projects. But more importantly, this has been a great insight into python programming, and I'm glad to have experienced it this semester. Even though Covid made it challenging, I still learnt a lot. My code could be improved, however, I feel it's in a good place now at submission. 


 
