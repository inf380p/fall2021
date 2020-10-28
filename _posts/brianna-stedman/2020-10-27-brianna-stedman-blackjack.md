---
layout: post
author: brianna-stedman
title: "Brianna's Blackjack game"
---
# Here is my Blackjack project! 
(I don't have Python3 yet, so I did my edits in my Trinket account, where I could save my work. [That's found here.](https://trinket.io/python/9f0be9e0cd)
However, the print statements come out a little messy unless it's in Python3, so here is the embedded Python 3 trinket. 

<iframe src="https://trinket.io/embed/python3/c6dc0893d6" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection:
This was a really tough assignment for me! I've mentioned it a few times in class, but I'm not a particularly creative person. So usually, if I am stuck on a project, I find that the easiest thing to do is to to look up other people's codes and try out a bunch of solutions. For obvious reasons, that wasn't an available strategy for this project, so that's primarily how I struggled! (Reason I like coding in the first place: collaboration) 

I majorly coded myself into a corner by trying to use functions but defining things in each function that are used in simple single-line operations. As I was trying to move the functions into their own module per the assignment instructions, I would lose the alias and therefore be unable to call it in the game itself. This is mostly because the summation of the player's cards in hand is such an easy thing that it doesn't really warrant its own function... So, it was either do EVERYTHING as its own function in a single module (even the game), or only have a few little functions in a second module, which is what I ended up doing. This is mostly because this is the only way I was able to get the game to work. I cannot figure out how to build a function that sums the players score outside of the game itself. I know this was one of the required functions in the UNC assignment, but it is something that for the life of me I could not get to work without completely starting over. So, that is an area of organization/design that I need some help with to figure out. 

Another struggle was getting the "Do you want to hit or stay?" question to pop up more than once. In my first iterations of the game (my roommate was my guinea pig) I got everything else to work up until that point (initial hit & bust/blackjack/win message, and the stay message). I finally figured out how to nest a while loop inside my first while loop, so that I would have one specifically for the question ("hit or stay?") but that wouldn't re-loop the initial deal -- which is a different message and for obvious reasons has different functions. Once I figured that out, the rest of the game was mostly just tweaking, and cleaning, and trying to make it as small/functional (literally) and compact as possible. I'm still in the process of that though, as mentioned above; I decided that useability was a little more important than best practice *at this exact moment of me submitting this assignment on time* but there is a lot I can do next, so I'm excited to see what other people have come up with and how they were able to solve the things that I could not. 

# Resources used:
Here are some of the links I used to look up syntax, in case they are useful to anyone else (and to cite my sources). You can see where they correspond to different parts of my project! 
* https://pynative.com/python-random-choice/
* https://stackoverflow.com/questions/51241722/python-prints-the-parenthesis-from-the-function
* https://www.geeksforgeeks.org/clear-screen-python/

# Revised Milestones:
- [x] Accept input from user for name to print a welcome message to the game 
- [x] REVISED: Deal two "cards" (randomized numbers from 1-10, *4 to account for multiple chances for the same number)
- [x] REVISED: Compute the sum of the numbers, 
- [x] Accept user input to "Hit," on which: deal another "card," add the total to the running sum
- [x] Accept user input to "Stay," on which: do not deal another card
- [x] If running sum of user is >21, print loser message
- [x] If running sum of user is <21 and user inputs "Stay," then print a randomized number between 16-21 as computer's score
- [x] If computer score > user score, print loser message 
- [x] If computer score < user score, print winner message 
- [X] NEW MILESTONE: Account for user score equaling dealer score 
- [x] Use while loop to ensure game continues to ask for user input until the user inputs "stay"
- [x] REVISED: Accept input from user for whether they would like to play a new game or not by creating a playagain() function; if "Yes" then re-run program, if "No" then exit the loop
