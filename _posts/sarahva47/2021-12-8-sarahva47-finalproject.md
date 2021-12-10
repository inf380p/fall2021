---
layout: post
author: sarahva47
title: "Sarah Varenhorst's final project (Taylor's Version)"
---

This is my final Trinket: <iframe src="https://trinket.io/embed/python/bb3fee027c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this final project, I chose the Turtle game option over the data analysis option. The data analysis option was more professionally appealing to attempt, as I have a psychology BA and was always looking for ways to make data analysis easier for myself during undergrad, however, I wanted something more "fun" and visually appealing to work with since I am not mathematically-inclined and am more of a visual learner. Earlier this year, I was also working at ThinkGeek, a sister company to GameStop, and have had video games on my mind since then as I often had to complete training related to new video game titles. Therefore, I decided to attempt to make a mini-game. For this mini-game, I wasn't really sure what to do. I've never created a game before and I honestly don't play video games that often! I wanted to do something easy with a lot of flexibility to adjust in case I ran out of time (which I inevitably did, as I work retail and the holiday season is brutal). However, there was an important event happening the week that we needed to turn in a project idea: Taylor Swift's re-recording of Red (Taylor's Version) was released on Friday and one of the new songs on the album was "All Too Well (Ten Minute Version) (Taylor's Version) (From The Vault)". I knew that if I chose something to do with Taylor Swift, it would be a little easier to complete the assignment since the two most important things to me are my cats and Taylor Swift.

The next step was choosing what the game would actually do. Again, I am not really a fan of playing video games and that made this a little more difficult since I haven't played mini-games in a while. Opting to go for a more useful game, I decided to do something involving some learning. A lyric-collecting game came to mind. For this game, the goal would be to collect the lyrics, in order, to Taylor Swift's song "All Too Well (Taylor's Version)." The game would serve a very useful purpose: memorizing the lyrics to her most beloved song. Anyone who has been to a live concert knows the euphoria from belting out the lyrics along with your favorite artist and since Taylor hasn't toured since 2018, over three years ago, fans (also known as "Swifties") are eager to go to a tour and sing along to her songs. I thought, "What better way to prepare for a tour than a game to help memorize the lyrics?" Therefore, "Let's Play All Too Well (Taylor's Version)" was born as an idea for a game. 

Creating a game for a final project was exceptionally challenging. I have never coded in Python before and I haven't coded at all (HTML) since the high school days of editing my Tumblr blog's appearance. Unlike writing an essay, where there is a fairly standard format to follow such as using APA 7's format for an academic paper for my psychology undergraduate courses, there are many moving parts for the project and a plurality of little pieces to consider. While this game took multiple sessions to work on, for example, this reflection was written in less than an hour with time to edit. Much more like an art project, the process of coding is never truly complete and there are always more things to consider. Prior to this class, I sometimes wondered about why games and phone apps would update so often or major bugs would only be found after publication. Now, I can understand how even when something is close to completion, there may be a time frame that gets in the way of putting out something absolutely perfect. For a professional video game, that could be getting out a major title before the holiday season or for the E3 gaming conference. For me, that is the final deadline for this class. 

When considering the project requirements, one area that I was unsure about was dictionaries and files. Originally, I planned to put the lyrics into dictionaries, but that seemed exceptionally long and tedious. I chose to import the lyrics from plain text files and pull them from there. Other files that I used were images, which Trinket makes exceptionally easy to use. I ended up excluding a dictionary for now after grappling with for what I could use one. I read through the textbook and O'Reilly examples again, but I wasn't wholly certain how to organically incorporate one into the game. I think as I play around with this piece of code in the future, I will find a place where it fits in, but that hasn't happened yet. At the second class session going over these projects, it was mentioned to not worry about images until later in the project, but out of curiosity I clicked on the images tab in Trinket and it gave such simple instructions that I went ahead and just threw in the image towards the beginning of the project as it took less than a minute to get it out of the way. Some of the project requirements came naturally, such as incorporating modules and functions. I was at a loss for ideas using for loops but then realized where they were needed for things such as the intersections with the objects as described in the O'Reilly video series. Some aspects of the project I found myself chronically overthinking until I realized a simple solution. For example, I was a little caught up on how to add a Help dialogue, but then I attempted to create a writing Turtle and use the H key for help and the C key to clear the instructions. I had a weird glitch where if I tried to clear the Turtle at the end of the writing, it required you to keep pressing on the H key to see the instructions and they were pulsing on the screen. Therefore, I added that C key and made the clearing of the instructions its own thing. 
```
#set up help/instructions
instr = TurtleSwift()

def instructions():
  instr.speed(0)
  instr.penup()
  instr.hideturtle()
  instr.goto(-200,-40)
  instr.pendown()
  instr.write("Use the arrow keys to move Taylor and collect the lyrics.", font = ('Times New Roman', 10, 'normal'))
  instr.penup()
  instr.goto(-200, -60)
  instr.pendown()
  instr.write("Collect the lyrics in order to win the game!", font = ('Times New Roman', 10, 'normal'))
  instr.penup()
  instr.goto(-200, -80)
  instr.pendown()
  instr.write("There are 3 levels. Good luck!", font = ('Times New Roman', 10, 'normal'))
  instr.penup()
  instr.goto(-200, -100)
  instr.pendown()
  instr.write("Press C to clear these instructions.", font = ('Times New Roman', 10, 'normal'))
  
def clearhelp():
  instr.clear()
```
I rather liked how this looks, however I wonder if there is a way to get all of the text to display at once instead of writing line after line. I wasn't sure how to add a line break of some sort using Turtle without wholly moving the Turtle. Below are the keys that I ended up choosing to use. Sticking with arrows for directions, "H" for Help, and "C" for Clear, I wanted intuitive buttons that don't rely on the mouse at all as I personally use a laptop and trackpads are not the best for games.
```
#make the keyboard keys match the turtle movements & help functions
gamescreen.onkey(go_up, 'Up')
gamescreen.onkey(go_down, 'Down')
gamescreen.onkey(go_forward, 'Right')
gamescreen.onkey(go_backward, 'Left')
gamescreen.onkey(instructions, 'H')
gamescreen.onkey(clearhelp, 'C')
```

During the completion of the project, I attempted to focus on some attitudes and behaviors we discussed during the course of this semester, "Read, Run, Ruminate, and Retreat." I focused on trying out a variety of techniques to work on the game, although I mostly focused on running and reading the code. I often found myself trying to work quicker than what I was capable of doing and growing frustrating when things weren't working; by pausing and taking the time to just read through and focus on each word in each line, I could more clearly understand what I was doing. I would often run the code after every few new lines were added as well to ensure there were no error messages and that it hadn't broken yet, which was useful. In order to more clearly read what I was writing, I found myself relying heavier than I expected on the ability to add more files and import them into the main file. Therefore, I found reading to not only be about just reading the code, but doing what I could to improve the legibility of the code. 

Unfortunately, due to the lack of time from working more hours for the holiday season, I didn't have the time to allow myself to truly retreat, however, a lot of ruminating did occur during my work hours as my mind often drifted away from work to try to relax from the stress of the holiday season. Once or twice, I did find myself jotting down notes on my phone after remembering something useful to add to the program. One interesting place that retreating did happen was that occasionally, I would get distracted from doing work by my phone. Here, it was exceptionally useful to be working on a game because if I went to open up Pokemon Go or go look at Taylor Swift merchandise on my phone, I could say to myself, "You have a game and something related to Taylor Swift in front of you, you just need to finish it!" This served to be excellent motivation. Because I am aware that I am a visual learner and like learning from videos, I relied on re-watching parts of course lectures and the O'Reilly video series. I also looked back to the very beginning of the semester. On our first day of class, our class website's notes have a Turtle game that collects items and it was useful to look to see what a finished product looked like as notes. I played that game multiple times to get a feel for how I wanted or needed my Turtle to move. 

In considering final details, I ended up not going anywhere near the full lengths of the songs. In part, I didn't have time to grapple with ten minutes of verse. Second, I realized that someone who is not necessarily a Swiftie will be grading this game and likely doesn't want to memorize all of the lyrics to some song just to play through the game. In the future, I really hope to expand upon this project. It was not complete as of the due date and I really wish it had been. The holiday season for work has been rough and I wish I had taken this course in a spring or summer semester where I could more fully invest in a final project without it colliding right when my work life gets more intense as well. Here, I could insert screenshots of my many attempts to get coworkers to cover my shifts so that I could have more time for my classes. I debated asking for a slight extension to try to get more work done, but the holiday season's chaos doesn't end for a while and it would only delay the inevitable. I plan to continue working on this as I do want a polished piece for my portfolio and it's genuinely been fun. I am, at the least, proud of what I did accomplish because I entered this class having absolutely no idea how to get anything on a screen and with a baseline of zero Python knowledge. Now, I am leaving the class more confident in my problem-solving strategies and with the fundamental Python knowledge to continue learning with this language on my own. 
