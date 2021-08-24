---
layout: post
author: elliott
categories:
  - exercise
title: Refactoring Tetris Turtles
published: false
---

Submit a well-formatted pull request to our class blog with embedded Trinket programs for the below exercises.
Complete these on your own, using any materials you need. Do not
look at other students' submissions until after you've completed your work.  

**After your programs are done**, check other students' work and other resources online if you had questions.
Include a reflection about what you think you've learned and any concepts that are still fuzzy to you.
Did you encounter frustrating situations? Did you feel a lightbulb turn on?

___


Refactor the below trinket program, which was created by some very industrious trinket users.
You should use **custom modules**, **functions**, and any other tools neccessary to 
clean up the code, increase readability, and modularlize the logic in the program.

<iframe src="https://trinket.io/embed/python/d0b14e13d2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For full credit, your finished program **must** look and behave at least as well as the original, but with cleaner, more 
readable, and more easily hackable code.

**Reflection note**: for this assignment, reflect specifically on your refactoring choices.  Why did you do what you did?
Why did you not do what you didn't do?  How is your program more readable and modular than the original?

Some concepts we haven't covered yet that you may want to read ahead on:

* **dictionaries**  Whenever you see `{` and `}` in Python, think dictionaries.  These are like lists
on steroids. They take the form `{ key1: value1, key2: value2 }` and will let you look up the keys to
get the values with a syntax similiar to lists, such as `dict[key1]`.  Check out how they're used with 
the `colors` in the tetris program.
* **files**  We haven't yet learned about opening and reading through text files (as opposed to modules, which
we have covered).  Sometimes data like the shape of pieces may be convenient to store in text files during a
refactor.

___

**For an extra challenge worth extra credit**, improve upon the functionality of the original by 
implementing more of the Tetris rule set in a separate Trinket. **Do not attempt the extra credit until after 
your refactor is complete**.  Refactor the program, duplicate it in Trinket, then work on your enhancements. 
Otherwise, you may be left with a program that is not functional.  Which would be a bummer.  

For the extra credit, submit two Trinkets, one with the refactor above, one that then uses your refactored
code to improve upon the functionality of the original.  In your reflection, talk about how your
refactoring influenced your improvements and what is left to be done to make a fully featured Tetris game.
It's OK to have refactoring in your extra credit submission that didn't make it into the original, but
your refactor should be able to stand on its own.