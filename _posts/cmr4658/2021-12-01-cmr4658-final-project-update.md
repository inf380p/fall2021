---
layout: post
author: cmr4658
title: "Chase's Final Project Update 3"
---

# Current Version

<iframe src="https://trinket.io/embed/python/507d11a06b" width="100%" height="533" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Progress Update

While the improvements I made last week weren't as extensive as in the previous update, I feel like I was able to take the project from something that works to something that is a little more fun. :)

It was a lot easier to add new words than I thought it would be. Instead of adding all the potential words to the `words` dictionary manually, I added a list of words as a plain text file and sorted them into the dictionary like this:

```
with open('wordlist.txt') as file:
  for line in file:
    if len(line) <= 6:
      words['easy'].append(line.rstrip())
    elif len(line) <= 8:
      words['medium'].append(line.rstrip())
    else:
      words['hard'].append(line.rstrip())
```

I had a few different ideas for implementing the skeleton image. Originally, I was going to split it into several different turtles that I could unhide as the player made incorrect guesses (as if someone was drawing it in) but in the end, I decided to have it pop in from the side of the screen. This let me be more flexible with the number of guesses the player gets, made the victory animation a lot easier (since there was only one turtle to worry about), and it actually looked better in my opinion. I also added a background image.

The last thing I'm having trouble with is getting everything to resize evenly in Trinket. Even though everything looked the way I wanted it to on my end, when my partner tried playing it on their computer, the images didn't resize in the way I would have expected them to. Next week, I'll experiment with it a little more to see if I can either get everything to resize evenly or lock the screen to a specific size.

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
- [x] Add the skeleton picture
- [x] Tie the skeleton picture to the lives counter

**By 12/8** (stretch goals)
- [x] Add more words to the word dictionary
- [ ] Make the interface resize evenly or lock to one size
