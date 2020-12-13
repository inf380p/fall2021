---
layout: post
author: shwetashambhavi
title: "Final Project Trinket and Reflection"
---

# Trinket File
<iframe src="https://trinket.io/embed/pygame/2d3ea42077" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Project Description

I decided to go with Turtle Game Project using PyGame trinket, as I throughout the semester I've enjoyed learning more on the Turtle module and it's capabilities.

## Some components of the game:
The Game is a modified version of Hangman, user can selects alphabets present on screen and it will fill the blanks if the letter is in the Hangman word.
If a user guesses the words correctly a congratulatory dialog will pop up on the screen
If a user fails to guess the work before the bird on the screen pops the balloons then no point will be rewarded
After every 5 wins level increases leaving less timing to user to find the word


## Initial Idea for the game:
I had to modified many components of my game. Initial milestones are as follows:

```python
- [X] I plan to include 2 different canvas for this game and so far I have worked up a basic visual for the first one.
- [ ] I also plan to include custom turtle compound shape(house) for this game. For now I have an image in place of compound image.
- [X] Working on the 2nd canvas and option to switch between them 
- [X] Adding balloons on canvas
- [ ] Enabling balloons to make the house float 
- [X] Pop feature of the balloon

These are some of my beginning milestones while I've kept most the idea that I had for this app and I decided to bring in simple Hangman game and combined those two.
```

# Coding Choices

## Multiple Canvas Designs
I invested some of the timing on creating canvas as the visualisation with turtle is a big part of what I learned in this class and I wanted to include those in my final project. I have two canvas options for users which they can access using the Switch Screen option present on right-top of the screen

## MessageBox for Dialogs
To show the instructions or dialogs with different messages I decided to go with MessageBox. I had tried using turtle.textinput/ screen.textinput option but I had difficulty positioning those dialog boxes and decided to go with MessageBox

## Global Variables
Through the application, I have made use of multiple global variable to maintain state of the program and to pass the data from one file to another. One of the example can be, to update the score after every win user has I am updating the score on the screen using the global variable.

## Dictionary
I am using dictionary to store the stamp id as key and stamp position as values made by the turtle while drawing balloons. The idea of storing stamp id with corresponding location was to erase one balloons at a time and providing user with some extra timing but turtle.clearstamp(stamp_id) never worked for me. The only thing  that worked was turtle.clearstamps() but this removed all the stamps/ balloons at once

## Text Fiile with Hangmanwords
For the storage of hangman words I created a text file which currently has 126 words which loads random word up on screen for each game. Since It was easy to write into file and read from it I decided to use this and not list/ dictionary


## Modularilty
Almost all the code in this project is either in class or function. I also have function for different module in different python file as it provided better structure to the code  and easy navigation option to me while working on it. Most of the common function is in the base_setup file and is imported across multiple files in the project


## Classes 
I have used 4 custom classes, clouds.py, house.py, night_screen.py, and alphabets.py in this app. Since the interactivity of game and user is through screen and not with the help of user input, I had made sure to have clickable option of turtle and went with classes for creating multiple turtle instances

# Roadblocks

There were many roadblocks while developing this project and some of them are as follows:

### Colormode
Turtle supports multiple colormode option by default is specifying the name of the color but of any other color format is needed we need to specify colormode to use it. 

```python
def addBalloonToTheHouse():
  global stamp_dict, draw
  colormode(255)
  draw.penup()
  loc = random_loc()
  draw.goto(random_loc())

I needed random colors for the balloons and instead of providing a list of color I wanted to make use of random module to get RGB code and after several failed attempts and I realised that we need to specify it to turtle of the color format to use it

def random_color():
  col = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
  return tuple(col)
```

### Global Variables Across Files
Global variable within a file worked even without explicit global tag to a variable but it doesn’t work without it when passing those variables across the file. So to use global variable across file we need to global explicitly outside of any function 

```python
base_setup.py file (Instantiating the variables )
 global wordtoplay, score, score_tur, prev_word_tur, stamp_dict, replayed, bird, page

alphabets.py file (accessing and modifying the variable)
  time.sleep(1)
              base_setup.helpdialog("Congratulations","You win!")
              base_setup.updateScore()
              base_setup.replayGame()
              player_word = []
              base_setup.bird.goto(-220,-80)
```


### Custom Classes
I struggled with SELF keyword in the beginning and how to correctly use it to access the class functions and variable within that class

### Turtle Write
One of the main roadblocks was removing the previous game’s word. I tried everything but this issue is still there, for now I’ve made it as user will know how many words are in the current word they are playing but can still see the words from the previous game if the length of current one is less than the previous ones

### Myscreen click events
I was stuck with making screen listen and used the methods as we did before but couldn’t figure out the issue so for now I’ve functions in place but it’s not working as expected

## Result

I have a working game which hopefully user can enjoy and continue playing thorugh levels, it works well in itself but there’s still room for improvements, I tried to test as much as I could possibly do, solved the found crashed but there’s still some know bugs which I've bypassed for now. 
