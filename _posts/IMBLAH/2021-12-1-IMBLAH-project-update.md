---
layout: post
author:IMBLAH
title: "Bo's Project Update 12/1"
---
# Project Update
This week I made three major changes on my project.

## Piano keyboard updated
<iframe src="https://trinket.io/embed/python/94efc65005" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Since I noticed that there was some misplacing by importing a keyboard image as a background, I chose to create 17 `turtle` objects to represent every key on the piano. By doing so, I also could make them more interactive by changing the color of the key to show whether the player has hit the bar successfully.

## Opening, win and try again screen created
<iframe src="https://trinket.io/embed/python/5b5b0632ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
After that, I started working on the opening, win and try again screen to create a more completed gaming experience.

## Opening, win and try again screen created
<iframe src="https://trinket.io/embed/python/5b5b0632ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
After that, I started working on the opening, win and try again screen to create a more completed gaming experience.

## Leveling up
<iframe src="https://trinket.io/embed/python/35ee28fa01" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
To increase the difficulty of the game, I tried to speed the `SlideTurtle` up. I haven't finished this part because I haven't figured out how to get to the next level because the indicator 'hit' list is empty which will trigger the `restart` function defined previously. What I'm doing now is debugging it by calling the 'print' function.
```python
def start_play(x,y):
  hit=[]
  game_title.clear()
  start_game.clear()
  note_key_list = [c_key, d_key, e_key, f_key, g_key, a_key, b_key, hc_key, hd_key, he_key, bd_key, be_key, bg_key, ba_key, bb_key, hbd_key, hbe_key]
  for note_key in note_key_list:
    note_key.showturtle()
  score.show('Score:' + str(int(len(hit)/len(music_score)*100)) + '%')  
  for note in music_score:
    note.activate()
    print('debug:',hit)
  print('debug:',hit)  
  for note_key in note_key_list:
    note_key.hideturtle() 
  print('debug:',hit)   
  print('debug:',len(hit)/len(music_score))  
  if len(hit)/len(music_score) == 100:
    level_up()
  else:
restart()
```
# Plan
I think things didn’t proceed as I planned last week because of the image importing issue and the heavy workload from another class. I will try my best to keep up with the plan because there will only be two courses left next week.
My plan changed accordingly.
## 11/17
Finish the basic layout of the game.
Get the basic behavior of the game to work.
## 11/24
Make the `SlideTurtle`s drop down in a specific order.
Add `score` object and make it work to display game state.
## 12/1
Create the win/lose/play again screen.
Make the interface look nicer by adding more interactive effects.
## 12/9
Add sound.
Add three levels.
Modify the code if needed and focus on the reflection.

# Reflection
This week I tried the strategy you instructed in the class which is making more copies of the code. This strategy is really helpful when I want to look back at what I did, which gives me a better guide on what I need to do next.
