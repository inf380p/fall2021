---
layout: post
author: ArisWells
title: "Aris's Final Project & Reflection"
---
#Trinket Link
<iframe src="https://trinket.io/embed/python/f19defa3ad" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#Reflection
Final Project Reflection
My final program strongly resembles my original sketches/concept, but the process of producing it proved to be significantly different than I had imagined. The game I conceived of was a sequence of levels with a top-down view in which the hero, a green turtle, could explore. I wanted the player to control the turtle using their keyboard (arrow keys, WASD, or some other system) and when the turtle approached the end of one level a new one would load which the turtle would be at the bottom of. I wanted to decorate the sides of the screen with irregular walls that would restrict the turtle’s movements (so they don’t leave the playable area) but also be somewhat visually pleasing (in a jagged wall kind of way). At this point in the process, I still hasn’t sure exactly what the “game” element would be, but I wanted to avoid making a clone of asteroids (or some other claustrophobic game that relied on twitchy controls or a time limit).
	In my first prototype I was able to quickly develop a system for controlling the turtle’s movements and hardcoded one of the side barriers. At this point in the project, I imagined that there would be multiple types of barriers on the screen, some impassible and some simply decorative. I realized that this was somewhat confusing and I couldn’t think of a reason why a turtle couldn’t simply swim through water, so future barriers were colored to look like cliffs or mountains. The amount of code to produce just one barrier proved to be somewhat unwieldly so I decided that future iterations would have an easier process for generating barriers from a set of coordinates.
```python
## water on the left side of the screen
leftWater = turtle.Turtle()
leftWater.hideturtle()
leftWater.color("royalblue")
leftWater.penup()
leftWater.setpos(-200,-200)
leftWater.begin_fill()
leftWater.pendown()
leftWater.setpos(-175,-200)
leftWater.setpos(-120,-150)
leftWater.setpos(-130,-80)
leftWater.setpos(-100,-10)
leftWater.setpos(-105,95)
leftWater.setpos(-130,155)
leftWater.setpos(-115,200)
leftWater.setpos(-200,200)
leftWater.end_fill()
```
I wanted the turtle to point in the direction it was moving it, so rotating the turtle in a particular direction then moving forward seemed like an obvious solution. The method for keeping the turtle within the playable area was somewhat crude, and proved to not be particularly scalable. I didn’t realize that at the time though and was more concerned with making sure the turtle would correctly rotate clockwise or counterclockwise to minimize the time spent awkwardly rotating 270 degrees.
```python
def north():
  playerTurtle.setheading(90)
  if playerTurtle.ycor()<190:
    playerTurtle.forward(5)
```
My next prototype was for a function that would take an origin coordinate (-200 for left, 200 for right), a color and 4 x values and 4 y values. Even in the process of prototyping this I realized how useful lists would be so the call to the function took the 8 values and assigned them to lists.
```python 
def wall(self, xorigin, color, x1, x2, x3, x4, y1, y2, y3, y4):
    x_list=[x1, x2, x3, x4]
    y_list=[y1, y2, y3, y4]
```    
I decided that looping through the values using the setpos() function was easier to do with a loop then controlling the turtle’s rotation and moving it forward.
```python
    for i in range(4): # Loop through the
      print(wally.ycor())
      wally.setpos(x_list[i],wally.ycor())
      print(wally.xcor())
      wally.setpos(wally.xcor(),y_list[i])
      print(wally.pos())
    wally.setpos(xorigin,wally.ycor())
```    
Actually, constraining the turtle’s movement so that he did not go through my carefully crafted barriers proved to be remarkably difficult. After briefly experimenting with mouse movement, I decided I could constrain the functions that allows the turtle to move left and right (negative and positive x) based on his position on the Y axis. This was very close to functional, but if the left and right barrier “stepped” at different points it quickly became a series of 7 ifs based on the y coordinate, each creating small constraining rectangles. 
```python
def plusX():
  if playerTurtle.heading() == 270: ## turtle stop rotating the long way
    playerTurtle.left(90)
  else: playerTurtle.setheading(0)
  print(playerTurtle.distance(WallyR))
  
  if playerTurtle.xcor()<125 and 0<playerTurtle.ycor()<-150:
     playerTurtle.forward(5)
  elif playerTurtle.xcor()<150 and -200<playerTurtle.ycor()<-150 or 150<playerTurtle.ycor()<200:
    playerTurtle.forward(5)
  elif playerTurtle.xcor()<175:
    playerTurtle.forward(5)
```
I was extremely lucky in this case and have a friend I could discuss the problem with and he had a much better idea. Instead of having a long series of checks between the turtle rotating and actually moving forward I could create a separate function that would take the same values that the wall drawing function.
```python
def turtleCheck():
  xListLeft = [-125, -175, -150, -125]
  yListLeft = [200, 125, 125, -60, -60, -175, -175, -200]
  
  xListRight = [150, 175, 125, 150]
  yListRight = [200, 150, 150, 0, 0, -150, -150, -200]
  
  x = playerTurtle.xcor()
  y = playerTurtle.ycor()
  step_size = 5
  
  targetX = 0
  targetY = 0
  if playerTurtle.heading() == 90:
    targetX = x
    targetY = y+5
  elif playerTurtle.heading() == 180:
    targetX = x
    targetY = y-5
  elif playerTurtle.heading() == 0:
    targetX = x+5
    targetY = y
  else: #WEST
    targetX = x-5
    targetY = y
  print(targetX,targetY)  
  if targetX < max(xListLeft)and not playerTurtle.heading()==0:
    yListLeftIndex = 0
    while yListLeftIndex < len(yListLeft):
        topBound = yListLeft[yListLeftIndex]
        bottomBound = yListLeft[yListLeftIndex+1]
        if targetY < topBound and targetY > bottomBound:
          xBound = xListLeft[yListLeftIndex//2]
          if targetX > xBound:
            playerTurtle.forward(step_size)
        yListLeftIndex += 2
  
  elif targetX > max(xListRight)and not playerTurtle.heading()==180:
    yListRightIndex = 0
    while yListRightIndex < len(yListRight):
        topBound = yListRight[yListRightIndex]
        bottomBound = yListRight[yListRightIndex+1]
        if targetY < topBound and targetY > bottomBound:
          xBound = xListRight[yListRightIndex//2]
          if targetX > xBound:
            playerTurtle.forward(step_size)
        yListRightIndex += 2
```
This code is far more elegant than something I could come up on my own. This function is called after the turtle rotates in a particular direction, but before it moves and checks if that movement would collide with a barrier. This function handles the left and right barrier separately so it avoids the issues my previous solution had. If the turtle’s proposed movement wouldn’t collide with the barrier closest to the centerline the movement is allowed with no other checks, otherwise it compares the proposed movement to the barrier. 

Next, I began work on the function to transition between levels. Despite drawing the walls with an extension of the turtle class the ‘clear()’ command didn’t work. After an embarrassing amount of troubleshooting, I found that when I had extended the class, I made an error. Some of the commands inside one of the functions specified a turtle by name instead of using ‘self.’. So, despite creating different turtles for each wall instead it was creating walls using the same turtle’s name each time. Once this was corrected the walls of the level could actually be cleared, and from there loading new walls and keeping a level counter was straightforward. In order to more reliably call the function for wall collision I reversed the order of the values in the coordinate lists and simply run the wall draw function in reverse.

Development to the final version of the program was somewhat hectic and I think the code would need to be refactored to sustain further development. For whatever reason I didn’t realize Trinket supported multiple .py files until I was too late to refactor my code. I decided that the most viable form of interactivity would be to have the turtle collect coins scattered over each level and keep track of how many the player picked up. Poor time management had finally caught up with me, so despite being pretty straightforward it took quite a bit of time to get the function that spawns coins to work. I attempted to implement an onscreen counter based on the sample code you showed us for incrementing a counter based on a key press. Initially I tried to implement it as it, but something was causing problems, probably the function that called walls. At this stage additional functions were created as necessary and I made wider use of global variables. A portion of the sample code I copied for the on screen counter had essentially become structural junk that I couldn’t easily remove. 

It wasn’t all bad though, the function I used to check if the turtle is close to a “coin” turtle became repetitive, but it seemed relatively readable and could be expanded to support incrementing the onscreen count as well as triggering the victory animation.
```python
def goldCheck():
  global score
  if playerTurtle.distance(goldy0)<10:
    score+=1
    scoreCounter.clear()
    scoreCounter.write(score,False,align='center', font=("Helvetica",18))
    scoreCounter.increment()
    scoreCounter.showcount
    goldy0.hideturtle()
    goldy0.setpos(1000,1000)
    if score==12:
      winner()
  elif playerTurtle.distance(goldy1)<10:
    score+=1
    scoreCounter.clear()
    scoreCounter.write(score,False,align='center', font=("Helvetica",18))
    goldy1.hideturtle()
    goldy1.setpos(1000,1000)
    if score==12:
      winner()
  elif playerTurtle.distance(goldy2)<10:
    score+=1
    scoreCounter.clear()
    scoreCounter.write(score,False,align='center', font=("Helvetica",18))
    goldy2.hideturtle()
    goldy2.setpos(1000,1000)
    if score==12:
      winner()
```
If I were to do it again, I would make significantly greater use of having multiple python files and I would maintain better control of variables (instead of liberally declaring them to be “global”. The late addition to the code was some custom images I quickly drew to replaces the circles (that were the same size as the turtle) with smaller gifs that looked more like a coin. I also added a “hud element” to level the coin counter at the top right of the screen.

Ultimately, I’m both impressed with what I was able to accomplish, unsurprised as my initial project seemed to be relatively reasonable in scope, and disappointed that the resulting code became so unwieldly. Additionally, I’m really frustrated with the version control offered by Trinket. The best I could come up with was to periodically clone my file and begin working on the copy.

One thing I found was that once I got a feature working, I didn’t take the time to clean it up or consider reimplementing multiple features after testing them. I definitely made use of print statements and even coded some parts separately before implementing them, but my mixture of declarations and functions made my code brittle and resistant to refactoring. I guess the ideal solution would have been to restart the project at some point but I didn’t have a complete enough prototype to know what I would have done differently until I no longer had enough time to do so. Looking back on it I almost wish I had attempted the data analysis project instead. Making a game is fun, but Turtle probably isn’t the best way to do it. If nothing else I think I learned a lot more about Python than I did in the Python class I took during my undergrad.
