---
layout: post
author: samandalib
title: "Hesam's Blackjack app"
---
Reflection
---
I wasn't familiar with Blackjack game. So the first task for me was to understand this game and what are the rules of playing it.
after reading a little about it, I found the best way for undestanding it was to download a free mobile app that exists for playing this game
and start playing. It was the best method I think since it provided me with a visual undestanding of the game rules and settings. After that I started to plan for
making my own game. So I changed my milestones from what I already posted earlier and came up with a new milestone list
- [ ] Define player hand
- [ ] Define dealer's hand
- [ ] Define functions to get sum of player's and dealer's hand
- [ ] Define function that compares dealer's and player's hand
- [ ] Define function that conclues the result of compared hands with "lose" or "win" status

I started coding with these milestones in mind but not everything wend as planned. I was also following the requirements on https://ils.unc.edu/courses/2017_spring/inls560_001/a/4.html
to make my application compliant with these requirements. So at the end I came up with the following changes in my milestones:

 - [ ] Define variables that need to keep track of
 - [ ] Define a function to deal a card for player
 - [ ] define a function to generate a score for dealer
 - [ ] Define a function to start the game for the first hand
 - [ ] Define a function to ask the player if they want to HIT or STAY
 - [ ] Define a fucntion to play again if the player decides to HIT
 - [ ] Define functions to evaluate and compare hands if the player decids to STAY
 
 I was able to meet the basic requirements of the program by following these milestones:
 
 <iframe src="https://trinket.io/embed/python/6376857f66" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 
 However, there were two problems with my code:
 - Interestingly I didn't use any loop for my code withoug having any intent not to use it. My code works with conditionals that call for a function as long as the condition is true
 - I didn't find any excitment in playing this game now, so I decided to add a scoring and bet mechanism to it
 
 So my code was now as the following that meets the requirements and have a betting mechanism embeded as well:
 <iframe src="https://trinket.io/embed/python/e31601b35d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 
 Next, I wanted to meet the advanced requirements of the game as explained in  https://ils.unc.edu/courses/2017_spring/inls560_001/a/4.html. 
 - to make `values of 10 should be four times more likely other values`, I changed the code from:
 ```python
 def deal_card():
    new_card = random.randint(1,10)
 ```
 to:
 ```python
 def deal_card():
    new_card = random.choice([1,2,3,4,5,6,7,8,9,10,10,10,10])
 ```
 - Then to `make the dealer more sophisticated`, I changed it from
 
 ```python
 def get_dealer_score():
    return random.randint(16,21)
 ```
 to: 
 ```python
 def get_dealer_score():
    threshold = 16
    dealer_hand = []
    
    while sum(dealer_hand) <= threshold:
          dealer_hand.append(deal_card())
          
    print("dealer_hand", dealer_hand)
    return sum(dealer_hand)
    
 ```
 
 By working some other features and functions the final advanced game that I came up with was as the following link shows:
 <iframe src="https://trinket.io/embed/python/481128e92e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 
At the end if I want to revise my milestones and reflect what I did in a new list of milestones, the list will be like the following:
 - [x] Define variables that need to keep track of 
 - [x] Define a function to deal a card for player
 - [x] define a function to deal cards to the dealer
 - [x] define a function to ask the player for a bet amount
 - [x] Define a function to start the game for the first hand
 - [x] Define a function to ask the player if they want to HIT or STAY
 - [x] Define a fucntion to deal a new card if the player decides to HIT
 - [x] Define functions to evaluate and compare hands if the player decids to STAY
 - [x] Show both hands, the result of the game and the score of the player and ask them if want to play again or not
