---
layout: post
author: sarahva47
title: "Project Update: Interface Draft"
---
My trinket draft: 
<iframe src="https://trinket.io/embed/python/2692381656" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For my project, did have to make, so far, some minor revisions in the plan, mostly around that music can't be used in our Turtles. I also had prioritized the design and graphics fairly early into the process but will be putting that off until much later in the project to ensure the basic functions actually work. 

My idea is a game with a Taylor Swift turtle. You play as Taylor collecting song lyrics to All Too Well (Taylor's Version) in order of the lyrics to earn red scarves as points. This is a three-level game. The first level, the user collects the lyrics, in order, to just the infamous bridge. In the second level, the user collects the lyrics, in order, to the whole song. The third level, the user collects the lyrics, in order, to the ten-minute version. If they mess up, they have to restart at the beginning of the stanza from which the last-correct lyric originated. The user has to watch out, though, because if Taylor hits a random Jake Gyllenhaal on the screen, they have to restart the level. If they get through all three levels, they win! On the win screen, I originally wanted the song to play but since that isn't possible with what we'll be using, I will likely try to incorporate a picture of autumn leaves, either an imported image or challenge myself to get a Turtle to draw a maple leave ("autumn leaves falling down like pieces into place"). There will not be a losing screen, since the goal of the game is repetition and encouragement until a user has the lyrics memorized (e.g., no learned helplessness). Therefore, a user can repeat the game and win the game, but cannot xlose the game.

This was my original work plan last week and how it has progressed:

1. I suppose the first step is to clear up how to do any of this, and go back to the drawing board if this project isn't feasable. How do I import an image? How do we make a Turtle move around and collect things like in the game example that was shown on the first day of class?

This goal has been accomplished as we discussed in class what we can and cannot do. So, I cannot import music but I can import images. I may want to see about moving my project to PyGames and outside of Trinket after this class ends so that I can see a final version with the music that I want. 

2. Identify images to import; I may draw the Taylor Turtle myself and the scarves to make cute, pixellated ones if I can't find something usable (as far as copyright restrictions or anything) on the Internet.

During class, we discussed that images are a final concern but are expected. This is good to know. This task, which I had made second priority I suppose, is going to be moved to last priority. 

3. Ensure I can import the song and images into the Trinket

Again, a song will not be feasible for the requirements of the project but I can worry about images later. 

4. Try to use dictionaries to set up the lyrics.

I want to try to work on this during the upcoming week. I still think it will be a clean way to keep track of all of the information that I need. I wrote out this plan before actually hearing the ten minute version of the song and well, it is quite a lot to grapple with. 

5. Take the project level-by-level, focusing on level 1, level 2, level 3, then the win screen.

For this week, I started with level one and just getting a basic interface done. I think continuing to focus on each level individually will allow me to also gauge how detailed level 3 can be or if I need to scale back levels 2 and 3 and just work with the original version of the song. 

6. Test and re-test the game, checking for bugs

This is, of course, a continuous goal and something I mostly have written down as a reminder to myself. 

7. Have a Swiftie friend play the game as a small goal of user testing

This is definitely the very last thing that should be accomplished in the final revision and completion stages of this project. 

I haven't made much progress so far because I have a couple of major assignments due this week and it's been hard to focus on sitting down and coding, but I carved out time in the upcoming week for significantly more progress to be made. I think I have incorporated some good stretch goals, like thorough graphics and using ten minute's worth of lyrics for the Turtle to collect (which will be a lot to put into a dictionary) while also leaving some wiggle room for achievability. So far, anything not done has been due to just not doing it yet. I spent a couple of hours reviewing our resources and the two Turtle examples we have on the class website from the "Python Basics" module and the "Beginning Final Projects" module to analyze the way to make the Turtles know directions and move. I'm trying to use good names for items and lots of hashtag notes to keep everything in order. 

So, first I set up the screen. I called it 'gamescreen' since it's a screen for a game. I set the color to 'light coral' because I want it to be red but light enough to not be a pain on the eyes. 

```
gamescreen = turtle.Screen()
gamescreen.bgcolor('light coral')
```

I then set up the basic Turtle function, my TurtleSwift. She will be a red circle for now (I wish Turtle had a heart shape as a basic shape option!). I set the speed to be very fast at 0 for immediate feedback, although I may change this later to be a little slower. I put the pen up so that it won't draw and set the screen for it to be the gamescreen. 
```
#set up the turtle's initial features like shape (to be changed later) and speed
class TurtleSwift(turtle.Turtle):
  def __init__(self, screen = gamescreen):
    turtle.Turtle.__init__(self)
    self.shape('turtle')
    self.color('red')
    self.speed(0)
    self.penup()
    self.screen = gamescreen
````
I then focused on trying to get it set up to be able to change the direction of the Turtle. I'm still a little confused by this. I had my Turtle as a circle but I changed it to a turtle shape so that it will be more obvious what direction it's facing. I'm still a little unsure if this is correct. At first, I tried to use 'up' and 'down' until I remembered those are more specific terms for pens and may not work? That is about where I am at.
```
#make the turtle move
def go_left():
  taylor.left(10)
def go_right():
  taylor.right(10)
def go_forward():
  taylor.forward(10)
def go_backward():
  taylor.backward(10)

#make the keyboard keys match the turtle movements
gamescreen.onkey(go_left, 'Up')
gamescreen.onkey(go_right, 'Down')
gamescreen.onkey(go_forward, 'Left')
gamescreen.onkey(go_backward, 'Right')
```

Before the next class, I want to finalize the user interface and figure out how to use dictionairies for the song lyrics. If I can set up those dictionairies, I think some of the most tedious parts of the coding will be out of the way.
