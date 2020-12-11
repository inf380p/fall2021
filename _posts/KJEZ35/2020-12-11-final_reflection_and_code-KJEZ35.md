---
layout: post
author: KJEZ35
title: "KJEZ35's Final Post with Game"
---
Here is my final product: 

<iframe src="https://trinket.io/embed/pygame/cb61157e7e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Main points to answer: 

Discuss the program. 
The process, the skills, and attitudes used. 
Anything else that will help evaluate work done.

1. Deciding on a Program: 

Deciding on a project was not much of a challenge. From the very start of class, I found that I enjoyed building little games with Trinket. I valued the data science skills; however, from a beginner's perspective, the python was much easier to tackle when I enjoyed what I was doing.
2. To start, my initial idea was to create a game/simulator to teach new Army cadets basic military small unit tactics. However, a week later, I was drawn to do something more fun and creative. I set up office hours with Professor Elliot to discuss my plan and decided to choose the appropriate project for a work portfolio. He made some valid points regarding the turtle application. I have admitted I was already leaning towards that path, but he just solidified it for me. 

I made several drafts of trinkets while working on the final. This process worked in my favor for breaking down my project each step of the way. Below I will go through my process from begging to end. 

How it all started, my first draft: 
<iframe src="https://trinket.io/embed/pygame/54a3635c7a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For the first draft, I start by importing all of the regular imports. I then start creating numerous players. It is quite evident that I did not know anything about classes at this point in the project. I recall my idea was to use the turtles as a place holder for what would become cars later on. At this point in the project, I should also mention how to upload images or backgrounds. Suppose I am correct. I also learned how to set the size of the screen for the first time as well. One thing that sticks out to me is that my creativity did not change from the beginning. I had the imagination of what I thought would look cool. I just lacked the know-how at this stage to make it come to life. 
I had one function for clicking and dragging my turtle around. My while loop set the foundation for the game by creating what I called the movement. I recall reading that all python and programming comes down to boolean statements, and this holds. I see that I applied a try and except, along with other conditionals, if and else. I do recall having issues using elif, so I stuck to if statements throughout the while loop. I commend myself on the way I organized my code with comments. It made it easy for my find and alter things in the final version. There are no collisions or pivot points to make the illusion of movements for the opposing racers. The square boxes throughout the game were placed more as reference points. Some come in handy later on. I also was able to get multiple turtles to travel left and right, along with the beginning of what would be my train, which I thought would add a nice touch. 

Second Draft: 
<iframe src="https://trinket.io/embed/pygame/4572f2df11" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So let me begin by noting that here is where I begin to entertain the idea of using classes. For some reason, I had a tough time grasping Object-Oriented Programming and the use of classes.  I must have spent over a week watching several videos and reading articles regarding the use of classes and how to apply them in python turtle. I want to point out that I used some of these drafts recently—some of my code, such as dicts and possibly the use of time. So we can ignore that for now. So to an outsider, it looks like not much is different from the first. However, there is some subtle difference that represents significant learning points for both programming and overall creativity. The first thing is that I build a separate module to try and work on my class. This process shows that I was thinking of how I was going to use classes. I knew extending a turtle class would be the way to go. I made a voice recording for this draft, so I will document what I said: 
My lower trucks were to entice movement. The idea was that I would have a timer that the player had to beat. I also mention plans for using images to create a better look. 
One of the issues I stated is that my while loop was to create movement. But when I tried to set the function to drag and turtle, I was having issues. Also, I was having issues when just placing specific code before others. 
I solved the issue a few hours later. I had copied my drag function from another trinket I made earlier in the class. I copied a while loop statement and a turtle "done statement". 

For some reason, I used this trinket draft to practice my dictionary and to the clock. I probably wanted to avoid having any issues with any of the more developed drafts. 

Third Draft / playing with starting screens: 
<iframe src="https://trinket.io/embed/pygame/b2b5eacebf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So this draft steps away from the main game and documents my first attempts to import images for backgrounds. This piece would also act as the foundation for what would later become my experimenting with different levels. It looks like I used a while loop to receive user input and display a rules screen. Moving from left to right, I can see my first attempt at changing levels. It is my first time using a global variable. I use the global variable  game_state = "running." I set up my keys that will allow the player to switch between screens. Moving on to the next tap, it looks like I might have considered importing a text file. My classes tab is empty, and the last tab is the gif I used for a screen. Although this was several weeks back, I can recall the thought process when reviewing these drafts. 

Fourth Draft: 
<iframe src="https://trinket.io/embed/pygame/cc412c62fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Draft four is an enormous milestone that would become the first real look at what my final will look like. This improvement is very much apparent for anyone following along in the post. Just right away, When you play the Trinket, a rules screen is displayed that accepts key input to switch screens—the Austin racing screen I made myself with PowerPoint. Ok, so one thing that stands out to me is that I cannot phase the game yet, and there is not a clock counting down. There are not any collisions nor level changes; this is strictly changing screens and all graphics! On these graphics, I want to talk about a little: 

I built these graphics myself with the use of PowerPoint and screenshots. I used this website: 
https://ezgif.com/maker/ezgif-3-d712a681-gif
For converting my images to gifs. 

This website was to erase the backdrops from my pictures: 
https://photoscissors.com

If nothing else, it is apparent that I genuinely put some effort into trying to make this look visually appealing. There were so many attempts at getting that background just right. I created the roads along the routes the turtles were running. I made the smallest adjustments to the turtles' grids to make sure they drove on the roads correctly. If you look at the big rigs, you will notice that you can see the street through the cracks. I had to use the program above and manually highlight the areas to give it that look. I then resized all the images and converted them into gifts. This process might have been more work than necessary, but I was excited and saw what this could become. 
This draft is also the start of how I would structure my final. Intro screens followed my code. 
I almost forgot a colossal milestone! This draft was my first time using classes in my program! I use two classes that make my overall code much neater. I recall having to go back and make changes to all my code, but it was worth it in the end. 

Fifth Draft: 
<iframe src="https://trinket.io/embed/pygame/4077926be3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I strip away the intro screen for my fifth draft to focus on the level changes and the clock. I also have inserted my second global variable to create a pause button from crucial input. Here I want to give credit to the videos that helped me use a clock, mainly from Tokyo Ed on youtube. However, my clock was a combination of his and some other videos. Unfortunately, I would not have the time to tie in the clock to the game for actual use. Here I start using my try and except to clear my screen as I advance through the levels. Later the way I did this would be a headache. It was also worth mentioning that I start to display levels at this stage. At this point, I have not added collisions or a help button. It also looks like this is the stage where I started to think about a congratulations screen. 

Classes Draft: 

<iframe src="https://trinket.io/embed/pygame/9360542c15" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Here is just a draft I had of working on creating classes. This piece was probably my first successful draft. 

Congrats, and Try Again Screens: 
<iframe src="https://trinket.io/embed/pygame/9cee3b610b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Here is just a draft of my screen work. 


I used the outline as a reference/check on progress; ultimately, I hit every milestone except for implementing a proper way to reset the game. 





