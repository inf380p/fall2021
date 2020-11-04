---
layout: post
author: EAkita
title: "EAkita's Reflection for class so far_Week of Oct. 7"
---

 
**Reflection**
My biggest issue is correctly pacing myself in this class and hitting the exact requirements for the assignment that week. I enjoy working with students and doing 
pair programming. I think I also need to work on better time management. I've learnt to better modify code, which means better understanding already existing code. 
I haven't had a lightbulb moment for a while. Had several confusing moments, but just worked through them to resolve things. 
A problem solving technique which worked so far for me is to properly define the problem I'm having to solve and understand the fundamental tools to solve that 
problem and going to figure out those tools either through reading materials in class or looking it up online. So far it's a great class. 
2 code snippets are posted below. 


```python
# Code snippet from the early days of this course, just importing, defining things and inputting things fro the user. 

#!/bin/python3

from turtle import * #import turtle

akita = Turtle()

akita_color = input("What color would you like akita turtle to be?")
bg_color = input("What color would you like the background to be?")

akita.color = akita_color
#print(akita_color, bg_color) 
myscreen = Screen()
myscreen.bgcolor(bg_color)

akita.shape("turtle")
akita.circle(10)
akita.speed(1000) #draw really fast

```


```python
#The code snipet below is from one of the String Exercises deliverables 
#Generalized counter function exercise
#This program takes the above script and encapsulates that code in a function named counter, 
#and generalizes it so that it accepts the string and the letter as arguments
#author:Emmanuel Akita 

def counter(str, l): #take a string and letter character as an argument
	word = str
	count = 0
	for letter in word:
		if letter == l:
			count = count + 1
	print (count)
	
word = str(input ("Please enter a word:")) #force input as string
letter = str(input("Please enter the word you wish to count")) #force input as string

#call function
counter(word,letter)

```


