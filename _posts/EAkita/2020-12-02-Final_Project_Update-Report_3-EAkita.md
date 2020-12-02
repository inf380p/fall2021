---
layout: post
author: EAkita
title: "Final Project Update & Stand-up Report 3"
---

**2 Dec 2020_Project Plan Discussion**

3D spiral game

Embedded link below: 
 
<iframe src="https://trinket.io/embed/pygame/92ebdeafb9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


```python
#Author: Emmanuel Akita
#Figure out vertical motion and slice graphics
#followed tutorial from these links: 
#https://realpython.com/pygame-a-primer/#drawing-on-the-screen
#https://www.pygame.org/docs/
#@Akita - refactor code for final, remove unnecessary comments

#@Akita; add intro with text flying in to the screen like star wars
#player enter their name for feedback 

#slice vs if colision check ==True, then break

#####next - reorg, classes, physics, score, levels

#import modules
import pygame
import time
import random
import sys, math 
from os import path

pygame.init()
clock = pygame.time.Clock() #this sets th FPS


#initialize some variables
DisplayWidth = 900
DisplayHeight = 500
speed = 10 #adjust level

white = (255,255,255)
red = (255,0,100)
green = (0,250,0) 
blue = green
black = (0,0,0) 
bg_color = black

player_pos = [500, 250] #x and y cordinates for draw.rect screen postion
player_size_x = 10
player_size_y = 40
object_size = 60 #would later be spirograph
object_pos = [random.randint(0,DisplayWidth-object_size), 60] #random postion everytime it's ran
object_lst = [object_pos]

#for starfield background
background = pygame.image.load(path.join('starfield.png'))
background_rect = background.get_rect()

score = 0 
font = pygame.font.SysFont("comicsansms", 40)

#fruit slash
pos = pygame.mouse.get_pos()
change = pygame.mouse.get_rel()
past = []
drag = False

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight)) #drawing window (screen)
#screen = pg.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Spirograph SlashMania!")

gameDisplay.fill(white) ### test with space environment later in pygame_space eg
game_surface = pygame.Surface((DisplayWidth,DisplayHeight))
game_rect = game_surface.get_rect()

game_over = False

def drop_object(object_lst):
  
  delay = random.random() #currently adds objects at the same time, so use dealy
  if len(object_lst) <5 and delay <0.1:
    x_pos = random.randint(0,DisplayWidth-object_size)
    y_pos = 0
    object_lst.append([x_pos, y_pos])

def draw_object(object_lst):
  for object_pos in object_lst:
    pygame.draw.rect(gameDisplay, blue, (object_pos[0],object_pos[1], object_size, object_size)) #w,h = 50

def update_object_position(object_lst, score): #update object postion
  for index, object_pos in enumerate(object_lst):
    if object_pos[1] >= 0 and object_pos[1] < DisplayHeight:
      object_pos[1] +=speed
    #drop function now takes care of else portion
    # else:
    #   object_pos[1] = 0 
    #   object_pos[0] = random.randint(0,DisplayWidth-object_size) # reset y to fall at dif spots
      
    else:
      object_lst.pop(index)
      score +=1
  return score

# def draw_slash():
#     pygame.draw.rect(gameDisplay, blue, (pos[0],pos[1], 5, 5),0) #w,h = 50
#     for i in range(len(past)-2):
#       past[i][1] -= 1
#       pos = pygame.mouse.get_pos()
#       change = pygame.mouse.get_rel()
      
#       if past[i][1] >= 1:
#         pygame.draw.line(gameDisplay, red,(past[i][0]),(past[i+1][0]),past[i][1]+10)
#         pygame.draw.line(gameDisplay, black,(past[i][0]),(past[i+1][0]),past[i][1])
    
#     past.insert(0, [pos, (change[1]+10) % 30, (abs(change[0])*3) % 100])
#     if len(past) >= 4:
#       past.pop(3)
#             #Old Version

while not game_over:
  # for event in pygame.event.get():
    
    ###rewrite this section, worked for IDE, not trinket
    # if event.type ==pygame.QUIT: #quit event
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      drag = True
    if event.type == pygame.MOUSEBUTTONUP:
      past = []
      drag = False  
    #   sys.exit() 
    #print(event)
  
  clock.tick (20) #20 seconds, also adjust object_pos to change speed
  
  #update object postion; moved to it's function
  # if object_pos[1] >= 0 and object_pos[1] < DisplayHeight:
  #   object_pos[1] +=speed
  # else:
  #   object_pos[1] = 0 
  #   object_pos[0] = random.randint(0,DisplayWidth-object_size) # reset y to fall at dif spots
    
  gameDisplay.fill(black)  
  
  drop_object(object_lst)
  score = update_object_position(object_lst,score)
  print(score)
  
  text = "Score:" + str(score)
  label = font.render(text, 1, white)
  gameDisplay.blit (label, (DisplayWidth - 400, DisplayHeight -200)) #attach label to the screen
  
  draw_object (object_lst) #call the draw_object function to iterate through
  
  pygame.draw.rect(gameDisplay, red, (player_pos[0],player_pos[1], player_size_x, player_size_y)) #w,h = 50
   
  game_surface.blit(background, background_rect)
  pygame.display.update()
    
  if drag == True:
    #draw_slash()  #update(Colors)
    pass
  #pygame.display.flip()
#track movement function
```

**Reflection**

I decided to shift gears to use pygame, since I realized this had a lot of cool built in features for game developement. So, I spent some time learning and playing around with the methods in pygame. 

*Hurdles*

I still haven't figured out how to properly code for a 3D spirograph. I believe this would be one of the coolest aspects of my game, so I'm pushing to get this done.  I think I can use revolutions of hyptrochoids. However, if I’m unsuccessful in this effort, I’ll stick with the 2D spirographs falling. 

I can successfully render the space background, but I was unsuccessful in printing the rest of the game to this space background screen. I'm sure I'm missing just a tiny syntax, and it's something I look forward to fixing before submission. 

*Successes*

I focused on other aspects of the game since my last report update. 
I got retangles falling vertically from the top to the buttom, an improvement from my last reflection. I also worked on adding the score feature. Currently, I don’t have any object interaction feature (eg. collision detection, slashing, etc), so the score just increases when the rectangles fall. This feature will be improved to reflect the object interaction feature when developed. 

Updating the vertical position for the created rectangles was slighly tricky, but I used lists, and once I got the indexing right, it became straighforward. Also, in creating the vertical motion, the object was jumping up and down the screen due to how I defined the update function. Thus, I figured I could adjust the frame per second using the pygame.time.clock() method which worked quite well. 

Furthermore, in creating the score, I realized that the score wasn’t increasing. It figured out that this was because the score set as an integeter and since intergers are immutable type, I couldn’t just directly increase the score by doing “+=1”. Thus, I had to reset the score to point to the new value. So in my updated_object position() function, I retured score when it was increased. And then down in my code, I reset my score by setting it to the function call. That line now updated my object position, and returned my score value. So I could now see the score increase. Later, I got the score to print to the screen. 

Moving forward, I would start reorganizing my code into classes, to make it easier to read and better formatted. 

**Next steps**

* Incorporate 3D figures (figure out the 3D spirograph volume)
* Incorporate level difficulty, could be more elements falling, or elements falling faster (need to think about this some more) 
* Try to figure out the slash function. 
* Refactor code to use classes
* Include dictionary for game state


Thus, initial milestone #1 done and part of #2 is done as well. 

**Milestones**

Done - Figure out how to do 3D graphics with python. This will involve some math: vectors, 3D matrices etc. and I started doing a bit of reading on this.
Partly done - Figure out how to move the spirogram from the top of the screen, downwards. 

* Figure out how to do a 3D rendering of the spirogram - **in progress** 
* Figure out how the volumes will fall, and what is considered “successful” and what is a “failure” - done
* Figure out how to score the game, and keep track of the score - done 

* Add a restart button to reinitialize the game.
* Use dictionaries to update the play with the game state. 

I have currently taken out the "cut" or "slice" volume, and thinking of just avoiding the falling spirographs and keep track for scores. 
 
**Stretch Goal**
A stretch goal is still the same; and it mainly revolves around defining the game physics have 2 environments this game can be played in (this is unchanged):
* In space, where the Physics is relaxed due to microgravity environment (spheres can fall in any direction)
* On earth, where the falling of the spheres is goverened by the laws of gravity (I'm thinking this might be more difficult, that's why it's a stretch goal; I might have to describe object inertia, maybe even prescribe random parabolic paths...)



####Edit after initial commit and group discussion####
None so far
