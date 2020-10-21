---
layout: post
author: brianna-stedman
title: "Brianna's First Reflection"
---
As I am reflecting on the course so far, it's a little hard to consider it fully since I am really having a hard time with this semester in general because of Covid. I've enjoyed learning what we have so far about Python, I've always wanted to learn this programming language, I'm just not in a good place to be excelling. A lightbulb that has gone off for me was with the try/except exercise in trinket, and since then I've learned to mess around with the placement of the try/except to make sure that I'm only getting my intentional error message when I want. Some confusion I've experienced is with reading through external lists/files. I'm still in the process of fully grasping the chapter 8 materials, so this would also count for what's still fuzzy for me. I'm also not 100% sure what our final project is supposed to look like, and I'm a little nervous about that, so I'm hoping to clear that up very soon so I can get a head start on it, I think I will need it. Finally, a problem solving strategy that has been working for me is googling the error codes that I get. Python is super helpful to show what line my issues are on, so googling them and looking at snippets of other people's code usually helps me in figuring out why mine won't work. 9 times out of 10, I have the correct elements or syntax, just in the wrong order. 

My first code example of something I've written is my function that makes my turtle spin. It's short and easy but is nice to only have to type the function instead of all the directions for my turtles to go. 
```
# tina does a lil spin - make this a function to use later 
def tinaspin():
  tina.left(90)
  tina.left(90)
  tina.left(90)
  tina.left(90)
```
Another bit of code is my IF statement in the turtle treasure hunt trinket, which I was able to collaboratively figure out when doing my code sharing talk with Brittany. 
```
if x_input > treasure_x:
      print("Your X value is too high. Try lower!")
    elif x_input < treasure_x:
      print("Your X value is too low. Try higher!")
    elif y_input > treasure_y:
      print("Your Y value is too high. Try lower!")
    elif y_input < treasure_y:
      print("Your Y value is too low. Try higher!")
    elif (x_input <= treasure_x + 5) and (x_input >= treasure_x - 5) and (y_input <= treasure_y + 5) and (y_input >= treasure_y - 5):
      print("Congrats! You got it!")
```
      
