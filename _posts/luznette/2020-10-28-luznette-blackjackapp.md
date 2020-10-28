---
layout: post
author: luznette
title: "Janette's blackjack app"
---
I am still having trouble getting started with assignments, so being able to map out my plan through milestones was very helpful as a start. This allowed me to create my custom functions as these were the building blocks of the program. After that, I hit my first roadblock. I got lost trying to figure out exactly where to start, and figuiring out how many loops I would need since there are many moving parts/routes. I wanted to write a rough skeleton of the code before I took my first break and found myself repeating a lot of code that was unecessary, but at the time I could not figure out how to condense it. I took a break and when I came back to the assignment, I found it most helpful to physically draw out the program in a way that made sense to (probably only) me. 
![image of notes]
(https://imgur.com/a/ddFIxpe)
Essentially, I reminded myself that there are two parts of the program that loop and various checks throughout. First, the game will begin in a loop and the user will be dealt two cards. The total of those cards must then be checked to see if they are equal to 21, greater than 21, or less than 21. If the score is less than or equal to 21, then the player is asked if they would like to "hit" or "stay". Depending on their answer, there are two different routes. A hit enters a second loop, the "deal" loop and will continue to deal as long as the player decides or they go over 21. It will also update the previous score/total. If they decide to stay, they are no longer dealth cards, and their score is compared to the dealers. The game notifies the player if they win or lose, and it exits the "deal" loop. At the end of the game, it asks if they would like to play again. If yes, it does not exit the initial loop and restarts. If they do not wish to play again, then it exits the initial loop. It is very straight forward, but I could not "see" the steps of the game until after I drew it out that I had a better idea on how to start. Now I now that I need a pen and paper with me as well.

My biggest challenge was making the program allow for errors. I kept wanting to write the code as
```python
answer = input("Do you want to HIT or STAY")
      if answer == "HIT" or "hit":
        score = new_player_score(score)
        deal = True
      elif answer == "STAY" or "stay":
        dealer = get_dealer_score()
```
When I wrote the code this way, it would not "stay" and it would loop back and deal another card, but I always seem to forget that it accounts for errors correctly when written like this:

```python
answer = input("Do you want to HIT or STAY")
      if answer == "HIT" or answer == "hit":
        score = new_player_score(score)
        deal = True
      elif answer == "STAY" or answer == "stay":
        dealer = get_dealer_score()
```
I also kept forgetting to write ```elif``` and made an endless amount of ```if``` statements, which obviously did not work. I realized that I needed to look back at some previous chapters and youtube videos for a refresher on how certain parts are written.

Here is my updated milestones (new milestones are in bold, milestones that changed a bit are crossed out):
[x]Welcomes the user, perhaps asks if they need instructions
~~[]Create loops that allow the user to “hit” or “stay”~~
[x]Create if states that check if the user wants to "hit" or "stay"
[x]**Create a while loop that enters and exits the entire game**
[x]**Create a while loop that deals cards**
[x]Allow the program to take in various types of inputs (spelling mistakes, upper case/lower case, etc)
~~[]Deals cards (gives two random numbers)~~
[x]**Create custom functions for dealing cards to player, dealing cards to dealer, giving new cards to player and updates score**
[x]**Add the possibility of the player drawing a J, Q, or K with a value of ten**
[x]**Comment out the program**

If I had more time, I would have liked to make a proper deck of 52 cards and have the program show exactly which card they recieved. In the end, this feature doesn't necessarily change what I have now as a 2 of hearts has the same value as 2 of spades, but I think it would have made the game a bit more sophisticated.

Here is my app:
<iframe src="https://trinket.io/embed/python3/9528650669" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
