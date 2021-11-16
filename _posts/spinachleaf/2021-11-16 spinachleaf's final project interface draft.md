---
layout: post
author: spinachleaf
title: "spinachleaf's final project interface draft"
---

Here was my original project work plan:
"I would like to create a turtle game for my final project.

The game would be a typing game where typing the correct words advances the turtle to the other side of the screen in order to win. There would be 3 levels of difficulty, with each level having the same amount of time to complete but an increasing amount of letters to type in that time. I think the data file would consist of the game settings, but I’m not exactly sure what that would look like yet. The dictionaries might be the words that the user types to advance the turtle. I think the for loops are what advance the turtle if a word is typed correctly. The functions are probably the movement of the turtle if you get the answer correct.

Over the next few weeks I will: -Begin by making the turtle advance across the screen when I call a function. (Nov 17) -Then I will try to build the correct data files and dictionaries to store the words that will be called. (Nov 24) -I also need to figure out how to go up a level when the user beats the previous one. (Dec 1) -I think the last step will be putting it all together in order with the win screen. (Dec 9)"

I will be keeping the basic premise of my plan. Typing the correct input will move the turtle across the screen. I think I will change from words to letters. The letters will also appear randomly on the screen.

I believe I will also have to change my timeline, but I will update next week depending on how quickly I can get the `onkey` function to work. I've run into difficulty getting this. I get an error message that says, "TypeError: onkey() takes exactly 2 positional argument(s) (1 given) on line 21 in main.py" when I try to call it. I'm confused about this because I believe I have two arguments, as shown below:
```python
keyscreen.onkey(advance, "a")
```
I attended office hours with Misha and she suggested coming back to the `onkey` function after our next class. For now, I have included a `for` / `if` statement that shows that my `advance` function works, as seen below:

```python
for repeats in range(30):
  if repeats % 2 == 0:
    al.advance()
```

Al, my typing turtle, advances across the screen. I hope to make a quick fix to the `onkey` function after talking about it more in class tomorrow.

What I have accomplished so far is making my turtle that will serve as the progress bar at the bottom of the screen. Here is my code for him:
```python
class TypingTurtle(turtle.Turtle):
  def __init__(self, coordinates = [-190, -190], screen = keyscreen):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.shape("circle")
    self.color("orange")
    self.speed(0)
    self.penup()
    self.goto(coordinates)
    self.showturtle()
    self.pendown()
    self.pensize(8)
    self.screen = screen
    
  #code for moving across screen
  def advance(self):
    self.speed(3)
    self.forward(25)
  #keyscreen.onkey(advance, "a")
```
I have the final line hashed out because I could not get `onkey` to work.

I have accomplished my first objective of getting the turtle to move across the screen, but I need it to be based on user interaction. This is my next immediate goal for next week, in addition to building the correct data files/dictionaries. 
Other than that, I believe my timeline will remain the same for now. I will update as necessary.

Here is the full code for my interface draft: 
<iframe src="https://trinket.io/embed/python/67d0ab6541" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
