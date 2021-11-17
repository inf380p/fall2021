---
layout: post
author: IMBLAH
title: "Bo's Project Update: Interface Draft"
---
# Interface Draft
<iframe src="https://trinket.io/embed/python/00471c82a2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Last week, I watched some tutorial videos you recommended and started working on my final project. This is basically what my game will look like. The biggest roadblock I’ve gone through is getting the basic function of the game to work, which is, when the `SlideTurtle` object hits the `Box` object and  I press a specific key on the keyboard at the same time, Trinket can show me I press the right key at the right time by printing out `1`, otherwise, it will print out `0`.

# Reflection
I tried to use `for` loop and list to create 7 `SlideTurtle`s.
```python
notes = ['c','bd', 'd', '#d', 'e', 'f', '#f', 'g', '#g', 'a', '#a','b']  
colors = ['slate blue', 'plum', 'pink', 'dark salmon', 'tomato', 'light salmon', 'moccasin', 'firebrick', 'tan', 'dark khaki', 'light green', 'cadet blue']
x_pos = [-180, -150, -115, -80, -45, -15, 15, 46, 80, 113, 145, 175]
for i in range(12):
  notes[i] = SlideTurtle(colors[i], x_pos[1])
```
Then I find I cannot call the `SlideTurtle` to work by:
```python
c.forward(5)
```
It returned a `NameError`.
By `print(notes[0])` before and after creating the `SlideTurtle`s, I realized that I changed the elements in the list instead of using `c` as the name of the `SlideTurtle`.
I thinks I still need to keep practicing to get familiar with the attributes of each sequence.

# My original project work plan
For the final project, I would like to pursue the Turtle-based option. It will be a game app letting beginners play simple piano songs using keyboards because I can see some similarities between computer keyboards and piano keyboards, kind of similar to the piano apps designed for smartphones. There will be 3 levels, increasing in difficulty by changing the songs.
Finish the layout of the game and pick the songs for the game. (Nov 17) 
Figure out how to add sounds to keys and start making the game part function. (Nov 24) 
Finish the game part and try to finish testing and add a constantly available help dialog. (Dec 1) 
Modify the code if needed and focus on the reflection. (Dec 9)

# My new project work plan
I think my milestones are ambitious enough or even too ambitious, so I may change my plan according to how things proceed.
First, since I’m not sure if I have enough time to embed three different songs, I may change my plan from increasing in difficulty by changing the songs to increasing in difficulty by changing the speed.
Second, I need to add sound to make the piano work. I will try my best to figure out how to realize this goal. If I fail, at least I will end up with a good-looking top-down game.
## 11/17
Finish the basic layout of the game.
Get the basic behavior of the game to work.
## 11/24
Make the `SlideTurtle`s drop down in a specific order.
Add sound if possible.
Add `Score` object and make it work to display game state.
Add three levels.
## 12/1
Create the win/lose/play again screen.
Make the interface look nicer by adding more interactive effects.
## 12/9
Modify the code if needed and focus on the reflection.

