---
layout: post
author: bmb4227
title: "Brittany's Final Game and Post!"
---
# Final Project Reflection
## How I Chose a Theme:
For my final project, I went back to a previous turtle assignment that I worked on earlier in the year. That assignment was a choose your own adventure where players helped a turtle on the beach make three choices. If they made the correct one then they won, if they made the wrong one then they lost the game. I decided to use this game as inspiration because I had had a lot of fun in the process and I think that it is easier for me to work on a project when it is something I enjoy or something that makes me smile. I have also loved the idea of “using turtle” during our programming throughout the semester. 

## Description of My Game
My game is called Tina’s Day Out. It is set in the ocean and the player’s goal is to help Tina the turtle survive three levels. The player can move up and down with arrows to avoid sharks and catch food (jellyfish). If they get hit by too many sharks, they lose. If they get enough jellyfish/points, then they progress through the levels and the waters become more shark infested. If they make it to the end, Tina goes on shore, hatches the babies, and then goes off into the sunset. 

## Process
I mainly broke this project into pieces which I worked on in separate modules. For example, I had a separate trinket where I worked on just the win screen or just the character classes. I then started to bring a few things together. Starting with a do you want to play prompt, a start screen with instructions, pause button, and a player with sharks. Getting these pieces to work together was probably the hardest part of the process and took the longest. Once I had those pieces working, I added additional pieces, like the score counter and the win screen. I worked on this code a lot and pretty consistently other than the last week of class but still, this project was hard, and I ended up scaling back on what I had hoped to do a bit because everything took me so long. I think part of my problem, and one we discussed in office hours, was that I needed to focus on one problem/bug at a time. I was getting too distracted by the code as a whole and by all of the other problems that were happening and was jumping around. This probably contributed to the process being so difficult and long. Re-watching, and reminding myself of what was covered in the Udemy videos was very helpful.

## Skills and Attitudes I Used
-	Finding Alternative Solutions: I think this was project was good practice for me in being flexible. I often had to find ways around a problem if my initial proposed solution didn’t work. Initially, I probably spent too much time committed to a task that I just couldn’t get to work when there were several other ways around it. For example, I thought I would start my game when a player pressed any key. For some reason, this ended up being very difficult for me to figure out. So I ended up adding a `turtle.textinput()` box which pauses the game in a way and asked the player for a name an whether or not they wanted to play. I found the `turtle.textinput()` when I was trying to research how to graphically display my help button text on the screen ( I initially thought I might be able to create some sort of pop up window).
-	Using print statements: print statements ended up being really helpful as place holders, to make sure my game was working and as a way to debug.
-	Talking: Talking about my code with others, like attending the office hours was really helpful because it helped me ask myself why I was doing a thing and if it had a reason. Even talking to myself, and reading a piece of code aloud helped me to debug issues.
### How I Hit the Requirements:
-	External data files: I wrote player names to an external csv file.
-	Dictionaries: I used a dictionary to keep track of state of the game such as lives, levels, and score.
-	Custom modules: I used a couple. For example startscreen.py
-	definite (for) loops: I used several for loops. For example
```
        for shark in sharks:
          shark.hideAllSharks()

```
-	A Python 3 or Pygame (Python 3 + GUI) Trinket: I used Pygame.
-	Have a graphical user interface, responding to key and click events: The player moves up and down with the arrow keys, the game pauses when the “p” button is held, and the help button displays information when clicked. 
-	Have a constantly available help dialog: There is a pink help button in the top right-hand corner of my game that pauses the game and displays. 
-	Display information about the program’s state: The score, lives, and level are all displayed in the top right corner.
-	Have at least 3 levels, increasing in difficulty: When a player reaches a certain score the number of sharks increases. 
-	Extend a custom Turtle Class: I did this several times. For example, I created a custom class for my sharks. 
-	Have a ‘win’ screen: The win screen has a new beach background with a turtle and three babies being hatched. 
-	Have an iterative interface: If a player loses or wins a texinput( ) box comes up and asks if they want to play. If they do then the main while loop starts over again. 
-	Use one or more custom images: I loved using custom images! My turtle player, shark, jellyfish, help button, and backgrounds all use custom images. I learned how to do this from a helpful trinket article. I got a lot of my images from OpenGameArt.com.
-	Completion of intermetiate milestone assignments: All of my milestones were posted in pull requests. 
-	Code style & Code correctness (i.e. free of errors & bugs): These are two areas that I need to work on. While the game works, there are a lot of ways I think I could improve it (see Things I Could Improve Upon below) and my code style isn’t as neat as I would have liked. I would have like to have created more functions and classes but ran into a lot of import errors along the way which really slowed me down. There are also a few annoying small bugs that I would have liked to fix like the jellyfish and sharks stay visible during the win screen even though the 
-	Trajectory of improvement over the semester: When I came into this class, I was completely new and a lot of concepts, especially in the second half of class have been very difficult for me. I feel like this project has taught me a lot and improved my skills. For instance, two weeks ago, I don’t know that I could have easily created a class and now I feel much more comfortable.
-	Usefulness and/or Fun of program & Overall ability to make a Python program that does something useful and/or cool: I think the concept of my game, although simple is cute/cool.

## Roadblocks
-	Looking back: I had to look back a lot and try to remember what we had covered. I was surprised by how much we have covered and how much I had forgotten.
-	Figuring out Pygame: An initial roadblock I ran into during the first weeks was getting used to working in Pygame for the first time. This included learning that I could only add .gif images, how to add the ` #!/bin/python3` and ` turtle.done()`

-	My internet: I live in an internet desert. The washing machines in my apartment are located right below me and use an internet connection to take credit cards. They have gone out for days at a time because, they and my apartment are located in some sort of weird dead zone that makes constant internet or fast internet really possible. So, I spent a lot of time working on a game that lagged a lot until I could get on campus to use the internet there. 

-	Figuring out ways to import things: I had a lot of trouble importing things without breaking the code in different ways. I was not always successful, but I did improve as I went along. At first, I had tried `import * ` but after talking it out with Elliot realized that might be at the root of a lot of my problems because the programs didn’t like conflicting screens and so on.  

-	Getting the game to be iterative: When I was first writing the code that if the player lost would ask if they wanted to play again, all of the pieces would stay frozen.  I realized I called the pause button but then didn’t uncall it if the player chose to continue with the game. I also realized that I wasn’t resetting the state dictionary and the lists where I kept my sharks and jellyfish. 

-	Figuring out my while loops: Figuring out the flow of the game was very difficult for me to do! It took me a long time and a lot of trial and error to get it to the state that it is now where it finishes and is iterative. At first, I had a 3 part nested while loop but was able to change that. 

-	Blinking pieces: For a while my shark and jellyfish pieces were very unstable and blinking a lot. I ended up adding a try statement in between them and the while loop they were in and this seemed to work! 

-	Indentation: a mistake I kept making was incorrect indentation. After a while I realized that the program didn’t always notice an indentation mistake and so it became one of the first things I went back and checked for when there was an issue. At one point, I realized all of my conditional statements about lives and scores were indented too far in. They were still partially working but wouldn’t break out of the nested while loop and head back to the top. 

-	Saving copies: Throughout the process I was pretty good about constantly saving copies of my program. However, toward the end, I had accidentally made a change that messed up the iterative process and this had been saved over the previous addition. It took me hours to figure out how to get back to what I had started with and made me realize how important saving and copying is.

## Things I Could Improve Upon
-	Classes, Functions, Modules: There are a lot of opportunities in my main code to use additional classes, functions, and separate modules. For example, at the end of the game or when a player loses, they have the option to play again. Looking back, I should have made a play again/rest function so that it could be reused. There is also a lot of code in my main module. This is mainly because I ran into a lot of issues during the import process. If I had more time I would prefer to go back and make my main module cleaner and simpler. 
-	Add sound: I think adding sound would make it a much more entertaining game. When the sharks get close to a user, I added a print-out of the jaws theme song “duunnn dunnn… duuuunnnn duun… duuunnnnnnnn” because I thought it was fun. But sound when a player is hit or catches a jellyfish would be great.
-	Improving the `winScreen()` and `pause_button`: I think something is slightly off about my `pause_button` or my order of operations because at the end when the win screen is called, the game pauses but the pieces (sharks and jellyfish) don’t disappear. I tried doing this manually with a `.hideturtle()` but with no luck. With more time I would like to improve this.
-	Adding Seagulls: I was able to add seagulls and get them mostly working which made the game more interesting and difficult. However, I wasn’t able to get the seagulls to reset/disappear when the game restarted so I commented them out and used the additional sharks to make the level more difficult. 

## Last Milestones with Notes
My game changed a little bit from my plan a few weeks ago so I’ve included my milestones with any notes about changes in bold.
- [x] Create a welcome title page
- [x] Display level on all screens but welcome
- [x] Display health/lives on all level screens
- [ ] Move on to 1st level when the player presses a key- **This changed. I transitioned to adding a text box on the screen that asks if the user wants to play and their name**
- [x] Create a help button with instruction about how to navigate through each layer
- [x] Create pause function
- [x] When player hits pause button or help button, pause
- [x] Create first level
	**This level changed a lot. Instead I have jellyfish and sharks throughout the game. But the game does keep track of most of the things outlined below**
- [ ] Add jellyfish and plastic bags
- [ ] Make jellyfish and plastic bags move through water-staggered
- [ ] Make jellyfish and plastic bags alternate between blue circle and their image
- [ ]  Keep track of how many of each the player gets
- [ ] If the player gets too many bags-they lose.
- [ ]  If a player catches enough jellyfish.. show scene of going onto beach and move to third 
- [x]  Create second level
- [x] Set the ocean scene
- [x] Create turtle
- [x] Allow user to move turtle with arrow keys
- [x] Set boundary for turtle within window
- [x] Add other predators- birds and sharks- I
- [x] Make predators move through the scene-staggered
- [x] If user hits predators- maybe a couple?- lose round
- [x] If user hits predator, send predator back
- [ ] If user avoids x number of predators- they win! And move onto next level. **Changed it so that they gained points to move on!**
- [x] Decide what third level is 
- [x] Create third level
- [x] Create win scene where  first egg is hatched
- [ ] Mimic second level but on sand **Third level stayed in water**
- [x] Create final you win!

## Final Code
<iframe src="https://trinket.io/embed/pygame/7dc63e9f43" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

