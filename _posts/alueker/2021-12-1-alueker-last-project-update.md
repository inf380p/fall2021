---
layout: post
author: alueker
title: "Andrew L's Last Project Update"
---
<iframe src="https://trinket.io/embed/python/d667952070" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This is my final project update before the final game is implemented. I haven't made as much progress in the game as I would have liked, largely because of Thanksgiving festivities, career opprotunities and other projects. However, I did finally implement one of the most crucial aspects of the game: the random command generator
It is only comprised of a few lines of code but it was not as easy to decipher as it may seem. To start off, I had to create a list of the function commands, which was tricky because we'd never gone over implementing functions into dictionaries or lists. Because of this, I implementrd the list using function formatting (bopit()) instead of summoning the functions similar to a variable (bopit)
Secondly is the matter of setting up the generator. Most languages have a loop counting mechanism. In php it's formatted: 
```
(x = 0; x >= 1; x++)) 
```
but in python it's formatted: 
```python
for range in i(x)
```
That was the easy part. Next came importing the random module. I've sparcely used the random module in class and it was a little tricky to get the syntax right on. For my purposes, I went with the following code:
```python
for i in range (50):
  command = random.choice(game)
  command()
```
This code will loop 50 times, the number of the final amount of commands a user will have to complete in order to beat the game. From there, the variable command will randomly choose a function from the list 'game' and the user will have to complete the task to proceed.
Going forward, there will be an important decision that will need to be made. I have to make each function respond to a button press or mouse click in order to proceed with the game. The keyboard module would allow easy button tracking, but unfortunately is not available in the base trinket layout. I would have to pay for the premium membership in orfer to access Python3 and proceed with this route. Alternatively, I could set up a 'game mat' that responds to screen clicks using turtles to draw buttons onto the screen, but I havent explored the logistics of that yet.
It is also highly likely that the timer function that I wanted to implement will not come to fruition in the remaining week of programming that we have. We have not gone over the timer module in class and the logistics of implementing a timer based on button commands is not within the scope of this project. It could be possible to set a general timer that players have to beat in order to complete the game, but I cannot make any guarantees to its implementation
