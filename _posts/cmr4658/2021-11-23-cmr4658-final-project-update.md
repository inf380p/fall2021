---
layout: post
author: cmr4658
title: "Chase's Final Project Update 2"
---

# Current Version

<iframe src="https://trinket.io/embed/python/ddc7806ea0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Progress Update

I've definitely made some progress since my last update! Since I was making a new Trinket, I decided to reorganize my code so that functions were grouped in a way that made more sense, and added more comments so everything was easier to read. I also moved the Display class to an external module and added some more methods, including one that let me update the text on each display more easily. This let me replace a couple of redundant functions that just updated different kinds of displays.

I thought I could get the game to repeat indefinitely using a while loop, but it turned out that I couldn't get player input if the while loop was still trying to run, so the game would just lock up. However, I was able to able to get the same effect by writing functions for everything that needed to happen in the game and chaining them together like this:

```
# Select difficulty

def select_difficulty():
  status_display.update('Select difficulty: (1) Easy (2) Medium (3) Hard')
  # Activate these keys:
  screen.onkey(easy, '1')
  screen.onkey(medium, '2')
  screen.onkey(hard, '3')

def easy():
  start_game('easy')
  
def medium():
  start_game('medium')
  
def hard():
  start_game('hard')

# Start/end the game

def start_game(difficulty):
  # Deactivate difficulty keys
  screen.onkey(None, '1')
  screen.onkey(None, '2')
  screen.onkey(None, '3')
  # Game setup
  ...
```

Since I'm slightly ahead of schedule, I think I was able to both set realistic goals for this assignment and give myself enough time to actually complete them. I'm glad I focused on getting the game to function the way I want it to before working on the visual aspects of the interface. Now that I know everything works, I can replace the temporary "Lives" counter with the visual "hangman" indicator. After I'm done with that, I'm planning to add more words to the dictionary and spend some time making the interface look nicer.

## Milestones

- [x] Set up a class for text display boxes
- [x] Get the game to recognize keypresses and display them on the screen
- [x] Keep track of previously guessed letters and display them
- [x] Start making the word dictionary

**By 11/24**
- [x] Put the game functions inside a while loop (and leave the setup functions outside)
- [x] Make an input function to select the difficulty
- [x] Fix the lives counter so the game ends when it hits 0
- [x] Create the win/lose/play again screen

**By 12/1**
- [x] Put the Display class in an external module
- [ ] Add the skeleton picture
- [ ] Tie the skeleton picture to the lives counter

**By 12/8** (stretch goals)
- [ ] Add more words to the word dictionary
- [ ] Make the interface look nicer
