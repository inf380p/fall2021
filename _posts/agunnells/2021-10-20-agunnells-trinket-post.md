---
layout: post
author: agunnells
title: "Ali's Trinket Post"
---

Here is the trinket based on the Runestone activity that I selected: 

<iframe src="https://trinket.io/embed/python/dd2ef99f60" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code defines a function called `computegrade()` that takes a score as its parameter and returns a string representing a grade. In addition, if the entered score is either a string or a score greater than 1, the function should return 'Bad Score.' 

My first step was to determine how to accurately get a returned grade. I wrote an if/else statement for the function: 

```python
def computegrade(score):
    if score > .9:
        return 'A'
    elif score > .8:
        return 'B'
    elif score > .7:
        return 'C'
    elif score > .6:
        return 'D'
    elif score > 0:
        return 'F'
 ```
 
 The problem, of course, is that any string value or score greater than 1 would just return an A. So, I knew that I needed to start with an if statement that would catch any strings or scores greater than 1. I wrote the following if statement:
 
 ```python
 if type(score) == type("") or score > 1:
      return 'Bad score'
 ```
 
 In whole, then, the function I created looked like this: 
 
 ```python
 def computegrade(score):
    if type(score) == type("") or score > 1:
      return 'Bad score'
    elif score > .9:
        return 'A'
    elif score > .8:
        return 'B'
    elif score > .7:
        return 'C'
    elif score > .6:
        return 'D'
    elif score > 0:
        return 'F'
 ```
 
 With this function, if any string or score greater than 1 is entered, the function returns 'Bad score.' At this point, I did accomplish what the program asked. However, there was one question that I struggled with. I noticed that if I input a negative value into the function, it would return 'None.' I wondered if there was a way to indicate that a score greater than 1 OR less than 0 should return 'Bad score.' I came up with this addition to my if statement: 
 
 ```python
 if type(score) == type("") or score > 1:
 ```
 
 While this did work, I wonder if there is a more elegant way to do this. In other words, I wonder if there is a way to make the code less verbose and still accomplish the same task. 
