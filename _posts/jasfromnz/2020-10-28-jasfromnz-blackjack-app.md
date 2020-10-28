---
layout: post
author: jasfromnz
title: "jasfromnz's blackjack app"
---

Here's my Blackjack App:
<iframe src="https://trinket.io/embed/python/72f227e633" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In general, I found this project to be easier than I expected it to be. I ended up doing it in two sessions, mostly because when I first sat down to work on it, I found it hard to stop. It was hard to stick to milestones and not be tempted to add more, particularly when my code broke. Eventually I made myself quit, but by then the majority of my code was written, and it only took me an hour or so the next day to work out the bugs in my code. Most of the issues I had while making this were organization related. I had trouble keeping track of variables and making sure they were defined in all if/else statements, but by far the biggest problem I kept running into was keeping track of the while loops. In the end, I had to draw out a diagram of the loops in my code in order to find where the last error was in my code. After I finished my code, I was feeling frustrated with how difficult it was to organize my code and keep track of all the elements, so I asked my brother (a software engineer) about how he would approach this type of code. He made the point that it’s best practice to manage game state and user input separately, something I hadn’t thought of while writing my code. Although I don’t fully understand how this would look in application, it’s something I’d like to keep in mind for future projects, and hopefully it will help me to keep my code more organized.

In the end, my milestones were:
User can initiate new game (or quit)
Create function to randomly pick cards
Create a loop based on user input (Hit or Stay)
Create a function accepts user input
Create a function that counts card totals for user & dealer at each step
If user’s hand is > 21 after drawing a card, user automatically loses
If user selects Stay, generates dealer score
Create win/lose mechanism when game play is finished

For the Advanced Requirements:
Add Jacks, Kings, Queens to card set for deal function
Use deal function to deal cards for computer
If computer’s hand > 21, user automatically wins
Update win/lose mechanism to account for dealer bust
