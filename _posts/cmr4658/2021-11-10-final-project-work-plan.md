---
layout: post
author: cmr4658
title: "Chase's Final Project Idea and Work Plan"
---

# Project Idea

For my final project, I would like to make an "escape the room" style text adventure game using PyGame (Turtle would probably also work but PyGame might be better suited for making a user interface). The player would be able to advance through 3 different levels (rooms) by using text commands to interact with objects in the environment and solve puzzles. There would also be a graphical interface showing a representation of the room and the items in the player's inventory.

Since the rest of the game won't work if there's no main gameplay loop (asking the player what they will do next, then changing the state of the game based on their input) I'll start with making sure that works in a very basic test environment. The graphics will be implemented after that is in place, since I can't display anything if there's nothing to display. :) Then I can build the rest of the game once everything works.

I think it will be really fun to think through how someone might try to interact with the different environments and make sure the puzzles are actually solvable. This project will probably be challenging to make but I think starting with a minimum viable product and then adding features from there will keep me from getting stuck without a working game.

# Work Plan

1. Make a flowchart of what the player has to do to progress from room to room (what puzzle needs to be solved, what clues/items are needed to solve it, and where to find them)
2. Define custom classes for rooms and objects (clues/items) that I can reuse throughout the game
3. Start setting up a test environment (the first room) to make sure the main gameplay loop works and the player can input commands/put items in their inventory/use the items later
4. Finish building the first room and make sure the interactions work as intended
5. Set up the layout for the user interface and make sure everything that needs to be displayed is displayed
6. Build the rest of the rooms (based on the working test environment and the flowchart) and make sure the player can move between them
7. Make it look nicer where possible
