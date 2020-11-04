---
layout: post
author: intjnotinfp
title: "intjnotinfp's Blackjack App and Reflection"
---

This app was definitely a challenge and it took me much longer to complete than I had originally anticipated. I didn’t plan well enough at the beginnning, so I took a bit of a scattershot approach to start and then re-organized my thoughts into updated milestones as I got a better grip on what exactly I needed to accomplish. 

These were my original milestones:
- []	Draw out the "poker table", i.e. green background, maybe a logo in the middle?
- []	create simplified deck of cards
- []	Deal the cards 2-2
- []	Assign hidden scores to dealer and user
- []	TBD

Clearly, I was thinking about this in very black-and-white terms and envisioning an app that also graphically simulated a game of blackjack. Once I read through the instructions thoroughly and realized that it ought to be entirely text-based, those all went out the window.

The very first thing I did was try to deal the first two cards. Here’s what that initial code looked like:
```
player_card1 = random.randint(1,10)
player_card2 = random.randint(1,10)
player_start_score = player_card1 + player_card2
```
I realized that by taking the sum of different variables (card1, card2) instead of a list, I wouldn’t be able to append more cards to it later if the player were to decide to hit, and that would require more work to print all of the cards/sum, plus I wouldn’t know exactly how many card variables I should assign to cover that base. That got me thinking that I should pretty much tackle all of these as separate functions which I would piece together with one main function at the end. That’s when the organization came into focus for me.

Here’s a revised milestone list, which I ended up following from here on out:
- [X]	Starting Hand Function --> should return a **list** of 2 cards (int between 1 and 10) for the player
- [X]	Additional Cards Function--> Should return a new card (int between 1 and 10)
- [X]	Bust Checker Function --> Checks if sum of player’s cards is over 21. Returns 'Bust' if player busts and False if player does not.
- [X]	Calculate Results Function --> Should check if player beats dealer and return 'Win', 'Lose', or 'Bust' using if statements
- [X]	Show Cards Function --> returns a string representing the players_hand (shows original hand and, later on, that hand with additional cards)
- [X]	Show current score --> returns sum of players_hand
- [X]	Hit or Stay --> returns True for hit and False for stay

At this point, I had decided to start off by further simplifying the deck of cards by just using the random integer function with a range from 1-10. Although it doesn’t account for face cards or the possibility of an ace holding a value of 1 or 11, that approach worked for this simplified version. I also chose not to deal two cards to the dealer (in similar fashion to the player’s deal), but rather assign one score between 16 and 21 that the player wouldn’t see until they chose to stay.

Here’s the final product:
<iframe src="https://trinket.io/embed/python/1e80e87fda" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

While I still feel like 99% of my coding is guess and check (and I still hate that as much as I did at the beginning), some things did finally click for me on this project. I feel a good deal more comfortable using functions than I had previously. In the past, I kept getting tripped up by parameters/arguments (I don’t know why! It just stressed me out looking at what seemed like even more puzzle pieces) and so I would always try to avoid using parameters when I defined functions and would leave the parentheses empty. I couldn’t avoid doing that on this assignment, so I had to figure out how to confront that issue. I also had to sit down between 6-8 times to get the code to work. My biggest issue was my own frustration and getting myself to start working on it again after walking away, because I don’t enjoy the process and don’t like having to constantly look up errors and syntax issues, etc. 

My code is very basic, stripped down, doesn’t do anything fancy, but I’m satisfied that it meets the most basic requirements and gets the job done. If I were to improve upon it in the future with more milestones, I suppose those would try to make it closer to the real game by eliminating the possibility of one type of card being dealt more than 4 times (I think that’s called permutations?), deal two separate cards to the dealer and show the player one of them, and maybe include the deck_of_cards module and some sort of a poker table background. 

