---
layout: post
author : samandalib
title : " Chapter 5 Loop exercise 1"
---
---
<iframe src="https://trinket.io/embed/python/d565fb61db" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---
Reflection
---

This exercise seemed to be easy at first but it has some tricks in it. I happily started defining variables and the while loop to ask for input. However, very soon I was confused about the
evaluation of user input. I knew that I have to use an `if else` statement and also `try except` for evaluating the input. The trick was to decide exactl when to get input, and how to evaluate it.
Three things should be checked:

- First get the input as a string and see if it is `"done"` or not

- If the input is not `"done"` I have to evaluate to see if it is a valid entry or not; a valid entry is a number and anything else would be invalid

- Use `try` and `exept` to define what happens if the user input is valid and what if it is not

After finding out about the structure of the program, everything else was smooth. It took me out of my comfort zone because it was a little tricky for evaluating the user input.
