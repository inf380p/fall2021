---
layout: post
author: weifeng0102
title: "Weifeng's Project Update!"
---

# Project Update
<iframe src="https://trinket.io/embed/python/0229697529" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Through learning and exploring this week, I have determined the basic rules of my game and completed the code for the basic rules. I plan to make a small game of treasure hunting. The player controls the turtle to move up and down, left and right through the keyboard. There will be traps (stones) and treasures (stars) on the interface. Once the turtle touches the stone, the game will fail and collect all the stars the game will succeed.

# Updated Milestone
I modified my work plan and set a more specific milestone:

completed:
- The main interface for completing user operations
- Complete the keyboard control direction code, and let the four buttons go straight in this direction
- Complete the design of basic objects (stones, stars)
- The code that successfully tried the intersection operation
- The code for the failure to complete the game result

To do:
- Design and enrich the content of game levels, design more traps and treasures
- Display of two game results, success and failure
- Add more game levels

# Reflection
In the process, I encountered some obstacles, but solved them through my own efforts. For example, at the beginning, I wanted to split all the defined function codes into different files for easy management. The intersection is placed in one file, and the keyboard controls up and down, left and right in another file, but there is no way to complete the intersection. Afterwards, I merged the two codes into one file, and added a `check_intersect` code to each keyboard operation to achieve it successfully.
But there are also some unresolved problems. For example, I designed the display of the results of game failures, but I have not been able to make the functions of success and failure take effect at the same time. This is an important problem that I will try to solve next.
