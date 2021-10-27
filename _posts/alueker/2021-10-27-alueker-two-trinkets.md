---
layout: post
author: alueker
title: "Andrew L's 2 Trinket post and reflection"
---
# My trinket from the textbook:
```python
from turtle import *
screen = Screen()
leo = Turtle() 
leo.pensize(25) #size
leo.pencolor("teal") #color
leo.forward(130)#begin letter formation
leo.right(45)
leo.forward(50)
leo.backward(150)
leo.right(90)
leo.forward(150)
# https://trinket.io/library/trinkets/04caebe410
```
# My trinket of my own design
```python
from turtle import *

def turtlewrite():
  raph = Turtle()
  screen = Screen()
  color = input('Please enter a color: ') #uses color input for turtle.color
  print("You chose: " + color)
  print("Is this correct?")
  ask = input('yes or no')
  if ask == 'yes':
    pass
  elif ask == 'no':
    turtlewrite()
  elif ask == 'maybe':
    print ("What does that even mean?")
    quit() #dont sass the program
  else:
    pass
  font = input('Please enter a font (arial, system, times new roman, etc.):') #font will be used in style
  size = input('Choose font size: ') 
  weight = input('Choose weight (normal, bold, italic): ')
  message = input('Please enter a message: ') #text that will be printed
  print ("Here is your message: ") 
  raph.color(color)
  style = (font, size, weight) #builds font
  raph.hideturtle() #hides the arrow/turtle
  raph.write(message, font = style, align = 'center') #draws from message to print, uses style variable for font, aligns to center.
turtlewrite()
# https://trinket.io/library/trinkets/75d3d9838d
```
#Reflection
For my custom turtle program I wanted to search the web for other functions that the turtle module had past the drawing function we looked at in class. After a while I learned of a few new commands that can be implemented with the turtle module such as turtle.hideturtle() to hide a turtle after it was done drawing as well as the turtle.write function. With the write function, you can print simple messages on your turtle screen but you can also be a little bit more creative, customizing the color, size, weight, font, etc. of your message. 

The challenge of this assignment for me was testing if input variables could be incorporated into the message. Luckily, this part went over fairly painlessly, though other parts were slightly more difficult. Initially on the if/else conditionals, I tried using the continue command to pass over irrelevant conditionals when I instead should have used the pass command. I picked up on this relatively quickly, so there wasn’t too much of a struggle on that part.

Another struggle that I had was attempting to incorporate a for loop into the program. Since I didn’t incorporate a turtle.forward(), turtle.left() portion into this program, I couldn’t find any practical use for a loop. I toyed with the idea of including a loop to control how many times the given message was printed, but unfortunately	 I couldn’t quite figure out how to code that in without it getting jumbled up.

