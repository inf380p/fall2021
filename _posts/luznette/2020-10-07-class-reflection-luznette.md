---
layout: post
author: luznette
title: "Janette's Class Reflection"
---
When we first started this course, I had anxieties about learning something that was completely new to me. Even the way the class is structured is something that I am not used to. Sure, I am used to bouncing ideas off of my classmates, and we work together to understand theoretical concepts, but for the most part my work is done individually. I am not used to collaborating with others. From my studies, I am used to reading 3+ books a week that discuss theory/research. While the readings for this class are shorter in length than my usual homework, I find myself taking longer to process the material simply because it is a completely new way to learn. This confusion became clear in the last homework assignment that dealt with lists. I could not translate the textbook to help me understand the homework assignment. The textbook, for obvious reasons, does not have exact solutions for all problems. Rather you are supposed to take particular lessons and examples and modify them to whatever you are writing. However, when I hit a roadblock, it becomes frustrating that I cannot find a solution to the problem I am trying to solve. I then tried to look up solutions online, but they still did not make sense, which lead to me not being able to finish the assingment. For this particular lesson, I have accepted that I don't need to fully understand the concept, it will remain fuzzy, and it will make more sense as the class goes on and I attend study sessions/office hours.

While figuring out the textbook alone has been a big struggle for me, I have had a few lightbulb moments. The most notable would be becoming comfortable with writing python. At the beginning, I was obssesed with translating everything I code into english in order to fully understand what I was writing. While it may not be a typical lightbulb moment, to me it felt like one when I started to understand how python as a language works (as well as learning to appreciate how it came to be!)

Another aspect that is still confusing/fuzzy to me is having multiple ways of implementing certain things. Or in other words, many ways to write code. I am struggling between writing code that works and gets the assingment done, and exploring the "best" way to write it so that other people who look at my code can make sense of it. What will make python do less "work" as it runs the code?
For example, the following code that I've written before essentially does the same thing, but the bottom example I believe is "better written":
```python
print ("Hello, my name is Tina. Today we are drawing shapes.")
thisShape = instructions()
draw(thisShape)
ask = input("Would you like to draw again? (Yes or No):")
while ask=="yes" or ask=="Yes":
  thisShape = instructions()
  draw(thisShape)
  ask = input("Would you like to draw again? (Yes or No):")
else:
  print ("Thank you!")
  ```
  
  versus
  
  ```python
  print ("Hello, my name is Tina. Today we are drawing shapes.")
ask = yes
while ask=="yes" or ask=="Yes":
  thisShape = instructions()
  draw(thisShape)
  ask = input("Would you like to draw again? (Yes or No):")
else:
  print ("Thank you!")
  ```
  
  In the second example, the code is shorter, but does the same thing without having to repeat functions. Depending on how it is written, it can lead to more confusing code. The first example was how I initially wrote it. After stepping away and spending some time with it, I was able to write it more efficiently. 
  
All in all, I am (slowly) becoming more comfortable with trial and errors, stepping away from my work to come up with better solutions. The next thing I need to work on is giving myself more time to work on assignments, and starting earlier. I usually reserve time for these class assignments near the end of the week, but that does give me the opportunity to come to office hours with questions. This reflection made me realize that, and I am hoping to change that this week!
