---
layout: post
author: spinachleaf
title: "spinachleaf dec 1 project update"
---

The last time I worked on my project, I said that I wanted to complete levels today. Looking at what I have now, after 6 or so hours of trying to make my `level_reset` function work, this is not the case. I've been too ambitious with this project. It's out of my skill level and I have to scale back considerably to have a final product to turn in that will be error-free. This project is not going to do what I had originally wanted it to, and I'm trying to figure out a way to still be successful. I've put a lot of work into this game and I'm pretty disappointed in how it looks right now.

Specifically, last week I said I would "try to create levels for next week (Dec 1) and a win/game over screen for the final week (Dec 9)." I have created a function to reset my progress bar when it reaches the end of the screen. I get no error messages, but it does not work. Here is the code: 

```python
def level_reset(progress_bar):
  if progress_bar.distance(winpoint) <= 5:
    return True
  else:
    return False
if level_reset(progress_bar):
  progress_bar.reset()
  ```
  
This is the result of many iterations of trying to make this code work. Before, I tried something like this:

```python
def reset_level(x,y):
  if y < 160:
    progress_bar.goto(x,y)
  if reset_level(progress_bar):
    progress_bar.goto(-180,-180)
```

Unfortunately, this did not work either. I'm completely stuck on how to make my progress bar reset. This is the main thing I have to work out before turning in my project. Ideally, I will have the progress bar reset twice, and on the third completion show my win screen.

That was the other part of what I wanted to get done for next week, creating the win and game over screens. I already made them, I just need to write a function to call them at the appropriate times.

Here they are:

```python
#win screen
def win_game(win_turtle):
  win_turtle.penup()
  win_turtle.speed(0)
  win_turtle.goto(0,0)
  win_turtle.write("You Win!", None, "center", "24pt bold")

#game over screen 
def game_over(game_over_turtle):
  game_over_turtle.penup()
  game_over_turtle.speed(0)
  game_over_turtle.goto(0,0)
  game_over_turtle.write("Game Over!", None, "center", "24pt bold")
```

So far, I have created a turtle that advances when the user presses letters. I have created word turtles that appear on the screen for the user to type. I have built the data file for the words.

Before I turn in my project, I need to: have the progress bar reset when it reaches the end of the screen, have the win and game over screens display at the right times, and create some sort of dictionary. I do not yet know how a dictionary will fit into this game but I will figure it out.

I'm disappointed with this project and I really hope I can figure out how to make it all come together before next time. I wish I had known how difficult it would be to make a game like this. If I could go back, I would choose a different game that did not include typing.

<iframe src="https://trinket.io/embed/python/dc14105544" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
