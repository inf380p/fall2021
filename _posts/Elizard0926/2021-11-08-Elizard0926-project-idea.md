---
layout: post
author: Elizard0926
title: "Elizabeth's Final Project Idea & Work Plan"
---

For my final project, I plan to do a text-adventure game. The decision to pursue this project was inspired by a class I took in undergrad called “Video games and Virtual Worlds” where we learned about an early popular text-adventure game called *Zork*. *Zork* is considered one of the prototypical examples of a text-adventure game because it draws on the familiar multi-dungeon structure and fantasy themes. The theme for my game centers on the story of “Hansel and Gretel” from *Grimm's Fairy Tales*. The goal of the game is for the player, playing as one of the children, to rescue their sibling and to escape the witch’s house. I plan to have several rooms that the player will naturally progress through in order to a) find their sibling and b) find the necessary items needed to escape.

My main concern is with the scope of this project and what features I can reasonably add in the given time. For this reason, I’ve outlined a rough timeline below with the main milestones as well as some optional milestones added at the end for “if there’s time.” In the interest of keeping the project manageable, I will be creating a prewritten selection of choices for the player to interact with as opposed to the more open-ended input that is allowed in *Zork*. I thought of limiting player actions to verb-noun constructions (e.g. “open door,” “enter room” etc.) but even then, I think this would introduce a level of complexity that might not be the best fit for this project.

**11/10/21**
Create Exposition and Room (level) descriptions text data files

**11/17/21**
Create basic skeleton of events (different rooms) using if-else conditionals or dictionaries
Stage 1: First room - Four options (e.g. try “open door” → [locked], enter kitchen, found an item, nothing there)
Stage 2: In kitchen - Four options - find sharp stick, find an item, return to first room, enter parlor
Stage 3: In parlor - Two options - battle monster (it drops key), run away
Stage 4: In basement - Save sibling (maybe add puzzle or riddle?)

**11/24/21**
Stage 5: Create path to return to first room to open door with key (give player option to get “cold-hearted” ending? Where they leave behind their sibling and escape without them straight after Stage 3?)
Create Game Over and Play Again screens

**12/1/21**
Create “Help” function describing how to access inventory, restart game, and select options
Create Inventory (make sure you can exit out of it)
Create main items modules: weapons, tools, food, misc.
Create Header with score/countdown timer/moves counter
Create ASCII animations using `for` loops (Witch for game over screen, monster in battle room)

**12/8/21**
Finish 1500+ word reflection report

*If time*
Create option to play as Hansel or Gretel at beginning?
Offer option to “befriend” the monster in parlor by feeding it something (alternative to slaying it)
Create red herring items (a random candy, stick, etc.) that can be picked up along the way but that aren’t used for anything
