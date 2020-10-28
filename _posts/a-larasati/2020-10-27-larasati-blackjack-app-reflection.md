---
layout: post
author: a-larasati
title: "Blackjack App, Reflection, and Updated Milestones"
---
#### Reflection

For the Basic version, the requirements I followed can be found on [this site](https://ils.unc.edu/courses/2017_spring/inls560_001/a/4.html) under Basic Requirements. For the "Tricked Out" version, I looked up a tutorial on how to play Blackjack on YouTube and used that as the framework of how the code is written and executed; the game tutorial I followed can be found [here](https://www.youtube.com/watch?v=eyoh-Ku9TCI&ab_channel=wikiHow).

##### Basic Blackjack

<iframe src="https://trinket.io/embed/python3/600659cd00?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Even though I needed to create custom modules as part of this assignment, I still started working on all of the code on one file to make sure that the functions were running the way I intended it to. After the program ran without errors on one file, I copied the chunk of code that runs the game and moved it to `main.py` and commented those lines out on `basicblackjack.py`. I know this is probably not the best way to work with modules and it only worked out because this program is relatively small, but it was the only way I would stay sane while working on this because keeping track of multiple modules can end up being... frustrating.

For the most part, writing the code was relatively straightforward, but I hit a roadblack about halfway through as I started coding the `hit_or_stay` loop, specifically during the `hit` part of the loop. I had set up `currentHand()`, a list that stores the cards dealt to the player. At first, when a new card is dealt after the second time a player chooses to `hit`, the card dealt from the prior `hit` was not stored in the list. For some reason this really stumped me, but in a moment of epiphany after rubber-ducking, I realized I just needed to use `append()`.

```python
if hit_or_stay == "hit":
  print("Dealing a new card...")
  time.sleep(2)
  newCard = dealCard()
  currentHand.append(newCard)
  currentHand_total = sum(currentHand)
  print("New card: ", newCard)
  print("Current hand: ", currentHand)
  print("New total: ", currentHand_total)
```

Within the `hit` part of the loop, I also took into account the possibility of the user going bust after each hit or getting Blackjack after the initial 2 cards. The `stay` part of the loop was relatively straightforward; once the user chooses to "stay," the code checks the dealer's total score and compares it to the player's final hand.

##### "Tricked Out" Blackjack

<iframe src="https://trinket.io/embed/python3/74d750cfb1?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I started this one by copying the code for the Basic version, and like that version, I first worked on it in one file before splitting it in two. Instead of following the "Advanced Requirements" from the site where I got the requirements for the Basic version, I went and actually looked at how Blackjack was played and modified the code to follow the tutorial I found.

The first modification I made was to take into account face cards. Here, I treated J, Q, and K as 11, 12, and 13, respectively, and if `randint()` generates any of those three numbers as a card value, it automatically returns 10 as face cards have a value of 10. 

```python
def dealCard(is_player = False):
  card = random.randint(1,13)
  if card >= 10:
      return 10
  return card
```

The next big modification I made is how the dealer's cards are dealt. In an actual game of Blackjack, the dealer deals two cards to themselves, one facing up and one facing down. The face-down card is eventually revealed after all players (or in this case, the single player) chooses to `stay` instead of `hit`, and if the total value is less than 16, the dealer draws one more card and compares the total to the player. Whoever is closest to 21 wins. To accomodate this, I modifed the `stay` portion of the loop.

```python
if hit_or_stay == "stay":
  print("Dealer's hand is ", dealerHand)
  if dealerHand < 16:
    d_newcard = dealCard()
    dealerHand = dealerHand + d_newcard
    print("The dealer's hand totals less than 16 and has drawn another card. The dealer's current total is " + str(dealerHand))
```

The final big modification I made is implementing a betting system. I didn't get a chance to create this as a function, so I kept it in the `main.py` file. How much a player wins when they bet in Blackjack is dependent on how the actually won. If the player won by getting exactly 21 (i.e. getting Blackjack), the player wins 1.5x the money they bet. If the player won by beating the dealer in getting the closest total score to 21, the player wins the amount they bet. For example, if a player bets $20, getting Blackjack means the player wins $30 for a total winning of $50, while beating the dealer means the player wins $20 for a total winning of $40.

For this code, I used `bet_multiplier` to indicate how much the player won/lost. By having `trickedoutblackjack.play_Game()` return a multiplier value, I used that to calculate the winning/losses for the player depending on the bet they placed. If the player looses all the coins they were assigned at the start of the game, the game lets them know that they've run out of coins and promptly ends.

```python
bet_multiplier = trickedoutblackjack.play_Game()
player_coins = player_coins + int(player_bet * bet_multiplier)
print("You now have " + str(player_coins) + " coins.")
if player_coins == 0: 
    is_still_playing = False
    print("You're out of coins! See you again next time!")
```

Overall, I learned a lot throughout this process. I find that these more "structured" exercise gives me more confidence in what needs to be done, and the opportunity to expand on the basics allows me to explore possibilities of what I can do with the code I've written. For both versions, I had `import time` at the beginning because I wanted to use a time-delay function (`time.sleep()`) so that the feedback was a little spaced out; the user has a little time to digest the feedback given before having to give an input for the next prompt.

#### Updated Milestones

As I finished up the exercise, I realized that I met all of the basic requirements but had modified some of my self-imposed advanced requirements.

**Basic Requirements**
- [x]  The program should be able to deal two cards to the user and compute the sum
- [x]  The program should be able to deal two cards to itself as a "dealer" 
  - [x]  The program should reveal one dealer card and hide the other dealer card 
- [x]  The user should be able to choose if they want to hit or stay  
- [x]  If the user chooses to hit, the program should deal a new card and compute the new sum
  - [x]  If the user chooses to hit and the new sum is under 21, the program should request the user to hit or stay
  - [x]  If the user chooses to hit and the new sum is over 21, the program should end the game
- [x]  If the user chooses to stay, the program compares the dealer's hand with the player's hand to determine who wins 
- [x]  When the user wins or loses, the program should prompt the user if it wants to play again

**Advanced Requirements**
- [ ]   Implement card suits (**Not Met.** I realized that card suits didn't really matter in Blackjack unless I'm keeping to the 52-count of a standard deck of cards, so I opted not to add this upgrade).
- [ ]   Let user choose if Ace is a 1 or 11 (**Not Met.** Just didn't have time).
- [x]   Add a betting system
- [x]   Use a "proper" dealer method (**New.** I knew that at some point I wanted to make a proper dealer in the game aside from just using `random.randint(16,21)` from the Basic version.)
- [ ]   Implement double-down betting (**New; Not Met.** I had heard of this while I was looking up the rules of Blackjack and had considered adding it, but it completely slipped my mind as I was finishing up.)
