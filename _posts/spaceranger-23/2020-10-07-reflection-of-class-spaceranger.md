---
layout: post
author: spaceranger-23
title: "Reflection of Class So Far"
---

#Overview:
#Learning how to code in Python has been challenging due to the way I tend to solve problems. To further elaborate, in the U.S. military, there are standard operating procedures (SOP), subject matter experts (SME) which are experts in their field, field manuals (FM), and schoolhouse that I can refer or reach to when I do not understand how to complete the mission from the very beginning. These resources do not only give a general framework on how to begin your assignment, reassess your work, and completed the task that is handed from my supervisors. The resources are built on previous and current experiences, to include lessons learned from previous battles, which allow Soldiers in general to understand the why part of our mission, which I typically ask a lot during this class. 
#When it comes to solving problems in Python programming, I feel that I have a constant battle with me trying to understand the why part in the planning and execution phase. The course material and the Internet does provide a lot of resources on how to execute a while or a for loop for example. However, I tend to not understand why Python chooses to enter those loops and what is the importance of these code. I can say wholeheartedly my understanding for why python does becomes clearer and easy to understand each week in class, but the ultimate thing I have to become proficient with coding is to further evolve myself witin the python community and attend extra training when available. 
#This is my fourth time participating in the python class, my learning tends to stop when I would get to solving if, elif, and else statements. I would like to note the previous three python classes was an online base platform where I had an extremely limited community compared to the community I have in INF 380P class. Several of my colleagues are learning python for the very first time and it is becoming easier to them about the struggles I am currently going through with each weeks assignment. Nonetheless, the main point of this paragraph is I achieved something I did not achieve previously before. I was able to understand and bypass the if, elif, and else statement, which is a step forward in the right direction. Now on to several questions about my experience in the 380P class. 

#1. Describe some confusion you’ve experienced. Did it help you learn? 
#One of the biggest confusions that I have had with python coding is understand how to prep my workstation before coding. For example, when beginning the treasure hunt turtle exercise, I would typed out what is my objective and the different steps needed to complete the program. I was able to get tina to go to the x and y coordinates, however, I was confused how to place the treasure within the program and how could tina would tina know they arrived at the destination and for the program to say congratulations. I tried various codes and referred to the instructions to identify how to place multiple treasures on the screen. However, after reaching out to my community of coders, they advise that I type in words in the coding example to see how and what they are executing. For example, when I type into google treasure_x and treasure_y = random.radiants, this allow me to understand that the computer is place radiants randomly in the program. I still working on this assignment as we speak, but everyday that I work on it I am learning more and more what I am doing wrong and how to incorporate additional solving strategies. Below is what I have achieved so far

---
import turtle
import random
from animations import congratulate

# Make tina
tina = turtle.Turtle()
tina.shape("turtle")

# Make a screen
our_screen = turtle.Screen()

# Pick random X and Ys
treasure_x = random.randint(-100,100)
treasure_y = random.randint(-100,100)

# These are variables that we'll use in our loop
still_going = True
user_has_won = False

# A loop for user feedback
while still_going:
  # Get user X and Y coordinates.
  # Make sure to handle bad inputs.
  user_x = raw_input("Choose an X coordinate between -100 and 100")
  user_y = raw_input("Choose an Y coordinate between -100 and 100")
  
  # Make Tina go to the user's X and Ys here:
  
  
  # Give the user feedback on how close they are to the treasure here:
  
  
  # If the user is within 5 pixels of the treasure, they win!
  # set user_has_won = True
  
  # If the user has won, exit the loop.  Otherwise, repeat
  if user_has_won:
    still_going = False
    
  # Note: this is the end of the `while` loop. if the expression
  # still_going evaluates to `True`, the loop will repeat.

# This is outside of the while loop (check the indentation)
# This code will only happen if the loop finishes:
congratulate(tina)
---


#2. What’s a lightbulb that gone on for you? Give an example?
#There has yet to be any lightbulb that has turn on for me when it comes to coding in python. I feel that I am so far behind with curruiclum, and I feel that I am a slow learner when it comes to the rest of my classmates. If I had to choose and assignment where a light bulb has turned on for me, I would choose the Loops Exercises (Total, Count, & Average Assignment). Understanding that I do not need to input a while, try, and except statement at beginning of my code change my mind on how to best solve coding assignments. I begin with this exercise with a try statement and after speaking with the professor, he articulated to me that those should only be implemented when I need to force python to do something. It is like using Sudo command in Linux to access the root. Moreover, I need to think in smaller terms when writing code and use the exceptions when you receive errors. Example is below a code exercise that really change my thought process:
---
sum = 0
count = 0
average = 0

while True:
  try:
    x = input("Enter a number!: ")
    if x == 'done':
      break
    
    x = float(x)
    
    sum += x 
    count +=1 
    average = sum/count

  except: 
    print('Error')

print(sum, count, average)
---

#What is still fuzzy for you? What will you do to make sure you can resolve your fuzziness?
#The overall concept of programming has been fuzzy to me from the beginning. However, these are steps that I am taking to resolve my steps. I have personally gone back to the very beginning of class to understand basic concepts and arguments of python programming. As Admiral McRaven once said in his speech during a UT graduation “if you cannot do small things, you will not be able to take on the large things/projects that life hits you with.” Having that solid foundation to include attending extra study session and working with a python tutor will help me become more proficient in the coming weeks. 

#What problem-solving strategies has been working for you? Give an example?
#Truthfully, I really do not know what problem-solving strategies that has been working for me lately. I am currently still in this cycle of trying to find what works for me and what does not work for me. This is a question that I would like to follow up on because I am starting to significantly increase my participation in the python world.  
