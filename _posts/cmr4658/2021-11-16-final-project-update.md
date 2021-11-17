---
layout: post
author: cmr4658
title: "Chase's Final Project Update and Interface Draft"
---

# Interface Draft

<iframe src="https://trinket.io/embed/python/bd61a725fe" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# New Project Plan

I thought about my previous project plan (a text adventure) and realized I would rather make it on my own time and have some more flexibility in the tools I'm using for it, especially so I can add sound. Luckily, I realized this before actually starting it, so I didn't lose much work. Instead, I decided to make an implementation of the game Hangman (I'm going to call it Skeleton, which is somehow less morbid). 

When it's finished, the player should be able to select one of three difficulty levels. The game will pick a random word from a list based on the difficulty level (I did this using a list inside of a dictionary) and display a blank space on the screen for each letter in the word. Then, the player will guess letters in the word by typing them on the keyboard. If the letter is in the word, the display will update the spaces that contain that letter. If it's not, the player loses a life and part of the skeleton (aka hangman) will appear. If the player can guess all the letters in the word before the skeleton is fully revealed, they win the game. Whether they win or lose, they should get the option to play again and pick a new difficulty level.

The hardest part of this project so far has been getting the onkey function to work so that it actually displays the pressed key on the screen--since the function that onkey calls can't take any arguments, I couldn't just pass the letter as an argument to a general "guess this letter" function. I realized I would probably need to have a separate function to guess each individual letter, but writing them all out manually seemed like a really bad idea, since if I ever wanted to change what the guess function does, I would have to update all 26 of them! Instead, I decided to define them using a for loop:

```
keyboard = {}
chars = [char for char in string.ascii_lowercase] # all the lowercase letters

def create_function(letter):
  def function(): # generic function name
    if letter in guessed:
      pass # should probably display error message
    else:
      guessed.append(letter)
  return function
  
for letter in chars:
  keyboard[letter] = create_function(letter)
```

Since I wouldn't be able to name the functions individually, I put them in a dictionary with the letter as the key and the function as the value, so I could call them like this:
`screen.onkey(keyboard['a'], 'a')`

Overall, I'm very happy with the progress I've made so far. I think getting the keypresses to work was the trickiest part, so while the rest of the game will definitely take time, it's more of a question of getting it done than whether or not I can get it to work at all.

## Milestones

- [x] Set up a class for text display boxes
- [x] Get the game to recognize keypresses and display them on the screen
- [x] Keep track of previously guessed letters and display them
- [x] Start making the word dictionary

**By 11/24**
- [ ] Put the game functions inside a while loop (and leave the setup functions outside)
- [ ] Make an input function to select the difficulty
- [ ] Fix the lives counter so the game ends when it hits 0
- [ ] Create the win/lose/play again screen

**By 12/1**
- [ ] Put the Display class in an external module
- [ ] Add the skeleton picture
- [ ] Tie the skeleton picture to the lives counter

**By 12/8**
- [ ] Add more words to the word dictionary
- [ ] Make the interface look nicer
