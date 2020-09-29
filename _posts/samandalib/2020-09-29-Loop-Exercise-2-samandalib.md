---
layout: post
author: samandalib
title: "Loop Exercise #2"
---

<iframe src="https://trinket.io/embed/python/355d63466a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---
Reflection
---
First I thought that the prompt is to ask users to enter a list of numbers at one time. So I thought that I have to define the program in a way to get all the numbers at once and
then starts processing them and find the maximum and minimum values. I wrote the following code that sucessfully worked for this purpose:

```python
numbers = input("Please enter a set of numbers seperated with ',': ")
list_of_numbers = numbers.split(",")
result = []

for i in list_of_numbers:
   result.append(int(i)) 
   
print (max(result))
print (min(result))
```

Then I read the prompt again, and now noticed the sentence "Write another program that prompts for a list of numbers as above ...". So I already half of the program from the exercise #1
and I have to add another part to list the numbers and find maximum and minimum values in it. The variables for this program were:
```python
result = []
#Minimum
Min = 0
#Maximum
Max = 0
```
And after validating that a number is entered, I append the number to the result list using ` result.append(number)`. Also I looked for built-in functions for lists
and found out that I can use `min(<list>)` and `max(<list>)` to find the requested values.
I think there was nothing difficult about this exercise but it required a little searching to find shortcuts for list data types.
