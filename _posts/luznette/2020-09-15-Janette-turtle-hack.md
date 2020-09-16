---
layout: post
author: luznette
title: "Janette's Turtle Hack"
---
For this assignment, I wanted to work on arguments/statements that I did not fully understand. The program that I invisioned would give the user a few prompts to choose a background color, the color of the pen, and a shape to draw. After it drew the shape, I wanted it to ask the user if they wanted to draw again. If they chose "no", then the program would end. If they chose "yes", then the screen would clear and the prompts would come back up again until the user chose "no". For some reason, I could not figure out how to clear the screen before it drew again. At least it loops!

In the procress, I quickly realized that I am in the population that needs to understand how things work before I can try them out. I would often pause to search youtube and [w3schools](http://w3schools.com/) for different explanations. It was not until I had spent a few hours on the assignment that I let that feeling go. I believe my biggest challenge is not understanding lines of code if it is not written in the way it is executed. For example, when writing my statements, my initial thought was to write it as:
```
print ("Hello, my name is Tina. Today we are drawing shapes.")
thisShape = instructions()
draw(thisShape)
ask = input("Would you like to draw again? (Yes or No):")
while ask=="yes" or ask=="Yes":
  thisShape = instructions()
  draw(thisShape)
  ask = input("Would you like to draw again? (Yes or No):")
else:
  print ("Thank you!")
```
While this does make my program work, I did not like that I had to write "ask" twice. After looking at w3schools, another (and maybe better) way to write it would have been:
```
print ("Hello, my name is Tina. Today we are drawing shapes.")
ask = yes
while ask=="yes" or ask=="Yes":
  thisShape = instructions()
  draw(thisShape)
  ask = input("Would you like to draw again? (Yes or No):")
else:
  print ("Thank you!")
```
It still does not make sense to me how "ask = yes" could come before the question is pulled, but I'm sure I will with time and practice. Other than that, defining functions made sense and I am overall proud of my assignment, even if it did not completely do what I wanted it to. 
<iframe src="https://trinket.io/embed/python/23bec7205f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
