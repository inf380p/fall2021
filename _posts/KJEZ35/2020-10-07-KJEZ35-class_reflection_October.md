---
author: KJEZ35
layout: post
title: "Class Reflection for October" 
---

What’s a lightbulb that has gone on for you? Give an example? Describe some confusion you’ve experienced. Did it help you learn?

For me, this class has been fun but also very much challenging. I feel that the class moves at decent pace, but 
because it takes me a little longer to write code and trouble shoot it, deters me from asking questions during instruction time. I do not want to hold up
the progress of others, so I try to make a point to communicate with both the instructor and now the TA. Which I am extrememly happy we now have a TA that can 
help us. She has defintely helped me out with assignemnts I was not making progress on. In addition, I have also sought out the help of a tutor to help me cover concepts
that I am struggling with on Monday's for thirty minutes. 

Where I found the most trouble was when we covered the different types of loops. I was struggling to grasp not only the concept but also the implementation 
of while loops. However, during the study session I was able to get a good grasp not only of what while loops are but also why they are used and how to set up the 
conditions to stop them. I made sure to make good notes/comments on my code that allow me to use them as a reference in the fututre. 
Here is an example of how I applied the notes on a trinket: 

<iframe src="https://trinket.io/embed/python/b063745a34" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

What’s still fuzzy for you? What will you do to make sure you can resolve your fuzziness?
What problem solving strategies have been working for you? Give an example.

I personally feel that I have gained the ability to read code and understand what functions need to take place to make 
a certain action happen. However, I still have issues actually writing code without looking at examples of how to structure it. 
I also noticed, that I still have isues understading the order of how to structure code. For this issue, I honestly think it will 
just take and practice to build that familarity with coding. I also like using my own code, that I have recieved help with and 
reading my notes on how and why I had to do something a certain way. On that note, I feel commenting my code and using good notes, 
really helps me. This coupled with communicating to the professor and TA my challenges and seeking guidance. These two strategies 
have helped me grasp concepts in the class. The last technique I have used is working on my class work a little bit everyday to keep the 
material fresh and not get overwhelmed. 

Here are two code examples I used: 

```python
# Start by setting your conditions 
sum = 0
count = 0
average = 0

# Here is the start of the while loop
while True:

# Set up your try and except to include the code
# in the while loop. Then close it.
  try:
    x = input("Enter a number")
  # Set up if statement to apply the break. 
    if x == 'done': 
      break
    
    x = float(x)
   
  # Here we have to tie the variables from above. 
    sum = x + sum
    count +=1
    
  except: 
    print("Not a number")

# Indent to close the while loop from above.   
print(sum)
print(count)
print(sum / count)
```

```python 
word = input("Enter a word")
# for index,letter in enumerate(word[::-1],1):
#       print(index,":",letter)
index = -1
while True: 
  try:
    print(word[index])
    index -=1
  except:
    break
  
# Do this again, but make it the length of the string. 
```

I picked these two codes because they caused me the most frustration with applying while loops. However, as you can see with the 
notes I made it would be easy to follow to do this again, or understand why we used the loop. 
