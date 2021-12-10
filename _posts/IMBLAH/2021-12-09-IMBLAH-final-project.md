---
layout: post
author: IMBLAH
title: "Bo's final project"
---

# My final project
<iframe src="https://trinket.io/embed/python/c8b07bd692" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# Video
https://utexas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4172c650-5902-4a49-b5a6-adf90146dd0b

# Program I chose
For the final project, I chose to pursue the Turtle-based option. My original plan was to make a game that could be played on the computer, letting beginners play simple piano songs using keyboards because I could see some similarities between computer keyboards and piano keyboards, to some extent, similar to the piano apps designed for smartphones. The user can hit the dropdown turtles that drop down in an order based on a music score. Every time the user presses down a specific key on the computer keyboard, the audio of the corresponding note will be played. If the user presses down a specific key when the dropdown turtle arrives at a specific region, the score will increase. If all the dropdown turtles are hit, the score will reach 100 and the difficulty will be increased by changing to a more complex song.
However, I failed to keep up with the original plan and ended up with a “good-looking” top-down game, in which the difficulty is increased by speeding up the dropdown speed of the turtle.

# My progress
During the whole process of building this game, I made 6 versions of the final project program.

## Interface draft
<iframe src="https://trinket.io/embed/python/00471c82a2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
What I did in this version was designing the basic looking of the GUI. A piano keyboard (imported image) on the bottom of the `screen` and some `SlideTurtle` on the top of the `screen`. The biggest roadblock I’ve gone through is getting the basic function of the game to work, which is when the `SlideTurtle` object hits the `Box` object, and I press a specific key on the keyboard at the same time, Trinket can show me that I press the right key at the right time by printing out 1, otherwise, it will print out 0.

## Turtles drop down in order
## <iframe src="https://trinket.io/embed/python/9047fc805c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
In this version, I made the `SlideTurtles` drop down in a specific order based on a `music_score`, the music is We Wish You A Merry Chritmas. I also added a `score` object and made it work to display the game state.

## Piano keyboard changed
<iframe src="https://trinket.io/embed/python/5b5b0632ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Since I noticed that there was some misplacing by importing a keyboard image as a background, I chose to create 17, in total, `Whitekey` and `Blackkey` objects to represent every key on the piano. By doing so, I also could make the keyboard more interactive by changing the color of the key to show whether the user has hit the bar successfully.

## Opening, success and try-again screen created
<iframe src="https://trinket.io/embed/python/5b5b0632ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
I added the opening, success and try-again screens to create a more completed gaming experience.

## Level-up
<iframe src="https://trinket.io/embed/python/35ee28fa01" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
I made the `level_up` and `restart` functions work, which mean, if the score reaches 100, the user can move to another level of difficulty, otherwise, they need to restart the game with the same level.

## Final
<iframe src="https://trinket.io/embed/python/c8b07bd692" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Since the function part of the game has been completed, I focused on making the flow more fluent.
Change the mechanism of leveling up. Instead of using the `turtle.speed` method to increase the speed, I decided to use the `turtle.delay` method after noticing that the speed difference between two levels is too big.
Added a `level` object to display the level state.
Added `KeyText` objects as indicators on the piano keyboard to show the connection between the computer keyboard and the piano keyboard.
Added `enter_level` function which allows the user to choose a level and used `try\except` to escape error.
Added `restart` button on the screen which allows the user the go back to the `opening screen` whenever they want. 
Added a winning animation which will be triggered if the user successfully finished level 3.
Changed some wording of the buttons to indicate where the user can click.

# Skills and attitude
## Running and debugging
The whole process is full of running and debugging. I cannot remember how many times I clicked on the run icon. 
Every position of the object should be defined by changing the value and running. 
```python
#score section
score=Text(110,120)
score.hideturtle()
#level section
level=Text(110,150)
level.hideturtle()
#restart section
restart_text = Text(-100,150)
restart_button = Button(-100,160)
```
Every time an error came out, I needed to change the code and run it again to test whether I was modifying it the right way.

## Printing out
Another strategy that I used a lot was printing out. Here is an example.
At the really beginning of the project, I tried to use the `for` loop to create 12 `turtle` objects because it would save a lot of time and make the code more simple.
```python
notes = ['c','bd', 'd', '#d', 'e', 'f', '#f', 'g', '#g', 'a', '#a','b']
colors = colors = ['slate blue', 'plum', 'pink', 'dark salmon', 'tomato', 'light salmon', 'moccasin', 'firebrick', 'tan', 'dark khaki', 'light green', 'cadet blue']
x_pos = [-180, -150, -115, -80, -45, -15, 15, 46, 80, 113, 145, 175]

class BoxTurtle(turtle.Turtle):
def __init__(self, color, x=0, y=190):
	self.shape(“turtle”)
	self.color(color)
	self.penup()
	self.speed(0)
	self.goto(x,y)
	self.setheading(270)
def activate(self):
	self.showturtle()
	self.speed()
	self.forward(230)
	self.hideturtle()

for i in range(12):
	notes[i] = BoxTurtle(colors[i], x_pos[i])

'c'.activate()
```
After clicked on the run icon, it returned an error:
```
AttribueError: ‘str’ object has no attribute ‘activate on line 29 in main.py
```
Then I changed `'c'.activate()` to `c.activate()`. It returned another error.
```
NameError: name 'c' is not defined on line on line 29 in main.py
```
Then I realized that there was something wrong with `notes` list and decided to use `print` function to figure out what happened.
```python
notes = ['c','bd', 'd', '#d', 'e', 'f', '#f', 'g', '#g', 'a', '#a','b']
colors = colors = ['slate blue', 'plum', 'pink', 'dark salmon', 'tomato', 'light salmon', 'moccasin', 'firebrick', 'tan', 'dark khaki', 'light green', 'cadet blue']
x_pos = [-180, -150, -115, -80, -45, -15, 15, 46, 80, 113, 145, 175]

print(note[1])

class BoxTurtle(turtle.Turtle):
def __init__(self, color, x=0, y=190):
	self.shape(“turtle”)
	self.color(color)
	self.penup()
	self.speed(0)
	self.goto(x,y)
	self.setheading(270)
def activate(self):
	self.showturtle()
	self.speed()
	self.forward(230)
	self.hideturtle()

for i in range(12):
	notes[i] = BoxTurtle(colors[i], x_pos[i])

print(note[1])
```
It printed out
```
#c
<__main__.Turtle object>
```
I realized that I changed the elements in the list instead of using c as the name of the `BoxTurtle`. Then I decided to create `BoxTurtle` objects one by one. Also, I realized that I still need to keep practicing to get familiar with the attributes of each sequence.

## Online resource
I watched some tutorial videos you recommended. They are really helpful when I didn’t know where to start during the first week. Actually, every time I am faced with some errors that I don’t know how to fix, I will google it. Most of the time, I can directly find the answer or find some related information that helped me debug.

## Making as many copies as possible
This is the strategy you introduced during the first class of the final project. Actually, I didn’t totally get the idea during the first two weeks. After my code got more and more complicated. Every time I made a change, there will be a huge difference. Sometimes, I wanted to find the last version of my code and I found out that disappeared. Then I needed to start from the beginning, which was really time-consuming.

## Commenting out
This is the strategy inspired by making copies. Every time I wanted to make a small change and it’s not worth making a new copy of it, I would comment out the code that I would delete before knowing this strategy. It was super useful when the change I made was wrong and I wanted my last version to come back.

## Arranging the code neatly
I found it useful when I want to change my code. Since it is arranged in a logical way, I can easily find out which part of it needs a change.

# To be continued
All of the things above are what I did during the class. Now, I wanted to talk about what I may want to do with this piece of code beyond the course to polish it. 
There are still a lot of imperfect points left in my code. The first thing would be adding sounds to it. I have googled it and found that I can `winsound` to achieve my goal. I noticed that `winsound` is not available on Trinket so I may use `Pycharm` to do that after this class. You also mentioned `Pygame`. I may also try that in the future. Also, I didn’t consider the rhythm when I was working on this piece of code so I need to improve it in the future. 
Like you said during the class, there is no end when coding. A piece of code can never be perfect and it can always be revised. I think, in the future, whenever I met a new function, I will consider whether it can be used to improve this piece of code, which is really inspiring.
