---
layout: post
author: Elizard0926
title: "Elizabeth’s Project Update: Interface Draft"
---

# Interface Snapshot
<iframe src="https://trinket.io/embed/python/b038dcc81e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection
Since last class, I’ve definitely  had to scale back my original milestones in light of the difficulties I ran into trying to keep track of the “choices” in my text-adventure game. In the process of sketching up the interface, I learned how to create dictionaries within a list and functions that can print the values from these dictionaries based on user input. In my initial proposal I had planned to give four options to each room, but in the process of just trying to get my sketch to be functional, I scaled that back to two options. Another reason I did this was because for each “option” available in a room, I would have to create a whole separate dictionary with three key-value pairs and this quickly became quite bulky with four options.

My revised list of milestones and tasks is included below. “DONE” indicates that the task has been completed, and text with strikethroughs shows how the old milestone has changed (here is a [link](https://inf380p.github.io/Elizard0926-project-idea.html) to the post of the original plan) . Some milestones that I am worried about are creating the  inventory (storing the data and then visualizing it) as well as how I will display a countdown timer (an idea that came up from my partner in last class was using the turtle screen to display it?). For stretch goals to accomplish if I have time, I was thinking it might be fun to give the user the option to play as Hansel or Gretel at the beginning of the game and also to integrate an alternate ending where if the player escapes without saving their sibling, they get the “cold-hearted” ending. (“bad ending” = not the same as GAME OVER). 

# Revised Project Plan
**11/10/21**
DONE - Create Exposition and Room (level) descriptions text data files

**11/17/21**
DONE - Create basic skeleton of events (different rooms) ~~using if-else conditionals or dictionaries~~
Stage 1: First room - ~~Four~~  two options
Stage 2: In kitchen - ~~Four~~ two options
Stage 3: In parlor - ~~Four~~ two  options
Stage 4: In basement - two options - Save sibling (~~maybe add puzzle or riddle?~~)

**11/24/21**
~~Stage 5: Create path to return to first room to open door with key (give player option to get “cold-hearted” ending? Where they leave behind their sibling and escape without them straight after Stage 3?)~~
Create Game Over and Play Again screens
Make function more robust by account for different user inputs (using string methods like .lower or printing an error message)


**12/1/21**
Create “Help” function describing how to access inventory, restart game, and select options
Create Inventory Module (make sure you can exit out of it)
~~Create main items: weapons, tools, misc. Modules~~
Create Header with score/countdown timer/moves counter
Create ASCII animations for each room using `for` loops (Witch for game over screen, monster in battle room)

**12/8/21**
Finish 1500+ word reflection report
