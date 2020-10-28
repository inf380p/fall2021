---
layout: post
author: a-larasati
title: "Blackjack Milestones"
---

The requirements for this blackjack app can be found [here](https://ils.unc.edu/courses/2017_spring/inls560_001/a/4.html). For this project, these are the initial milestones I'm setting. Some milestones may be modified/added/deleted as I work on the project.

**Basic Requirements**
- [x]  The program should be able to deal two cards to the user and compute the sum
- [x]  The program should be able to deal two cards to itself as a "dealer" *(added on 10/20/20)*
  - [x]  The program should reveal one dealer card and hide the other dealer card *(added on 10/20/20)*
- [x]  The user should be able to choose if they want to hit or stay  
- [ ]  If the user chooses to hit, the program should deal a new card and compute the new sum
  - [ ]  If the user chooses to hit and the new sum is under 21, the program should request the user to hit or stay
  - [ ]  If the user chooses to hit and the new sum is over 21, the program should end the game
- [x]  If the user chooses to stay, ~~the program should be able to generate two cards and compute the sum for itself, then compare it with the user's sum to see who wins~~ the program compares the dealer's hand with the player's hand to determine who wins *(modified on 10/20/20)*
- [ ]  When the user wins or loses, the program should prompt the user if it wants to play again

**"Upgrades"**
- [ ]   Implement card suits
- [ ]   Let user choose if Ace is a 1 or 11
- [ ]   Add a betting system


#### *Update: October 20, 2020.*
I managed to finish some parts of the initial milestones I set last week, and I noted it on the checklist above. 

I had to look up the rules of blackjack because I don't play it often, and there are quite a few rules that I needed to take into account. My current approach is to build a bare-minimum functioning blackjack game and then go back and spruce it up to make it a lot better. I also added an **"Upgrades"** checklist which has things that can make the game a lot more enjoyable/fun/better that I can hopefully implement before next week.

*Stay modification*: Since the dealer also has cards on their hand, I made it so that the the dealer deals cards to itself after the player's cards have been dealt.
