---
layout: post
author: spinachleaf
title: "spinachleaf november 24 project update"
---

For this update, I focused on getting the words the user will type to appear on the screen. I added a file to my program containing the words as a `.txt` file and it was fairly easy to add. I couldn't quite remember how to open a file and have it split by line, so it was good review for me to go back into the textbook and remember how to do it. Here is the code I'm talking about:

```python
#open words file
fhand = open('words.txt')
allText = fhand.read()
words = list(map(str, allText.split()))
```

I'm also really happy I was able to create a second external file to store my custom turtles in, called `custom_turtles.py` . I have only put the one turtle I created a class for, `ProgressTurtle` , in that file so far, but I will probably add the others next week.

I'm moving at a slower pace than I had originally hoped with this project and may revise the scope. After Professor Hauser told me last week that it wouldn't be possible to add a timer to my game, I think I have to shift to an untimed game. I also have not figured out how to make the turtle respond to only the correct key press for each letter in the word. Right now he advances at any letter key press. 

Here is my original schedule, for reference:
"Over the next few weeks I will: -Begin by making the turtle advance across the screen when I call a function. (Nov 17) -Then I will try to build the correct data files and dictionaries to store the words that will be called. (Nov 24) -I also need to figure out how to go up a level when the user beats the previous one. (Dec 1) -I think the last step will be putting it all together in order with the win screen. (Dec 9)"

I have successfully made the turtle advance across the screen when I type letters. I have also made the data file with words and gotten those words to appear on the screen for the user to type. I have not yet connected the typing of the correct letters to the word that is on the screen, and I'm not sure that I will be able to do that in the time I have remaining. I will try to, and keep that as my big goal for the final project. For now, I will be happy to try to create levels for next week (Dec 1) and a win/game over screen for the final week (Dec 9).

This project has been challenging and I wish I had more time to wrap my head around it. I think I could figure things out more easily if I had more resources on turtles and their capabilities to make games like this. I know we only have access to the videos Professor Hauser mentioned for 10 days, and I've been strategically trying to decide when to begin them. I may do this before the next update.

Here is my trinket: 
<iframe src="https://trinket.io/embed/python/a502d2f296" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
