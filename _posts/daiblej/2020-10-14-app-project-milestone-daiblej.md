---
layout: post
author: daiblej
title: "Janet's blackjack "
---

I decide to do the blackjack project, as currently, I am addicted in this poker game. It will be super interesting if I can write it in Python by myself.

**milestones**
- [x]  understand the blackjack rules

- [x]  set the cards
- [x]  deal two cards to the dealer and the player
- [x]  show one of the dealer's card and show all the cards of the player
- [x]  Q1: ask whether want to hit/stand/split(optional)
- [x]  if less than 21, repeat Q1
- [x]  if equal to 21, congratulation
- [x]  if more than 21, bust
- [x]  show the dealer's two cards
- [x]  if less than 17, hit
- [x]  if above or equal to 17, compare two sides
- [x]  give the result
- [x]  ask for another round
- [x]  further steps (optional)
   - [x]  A = 1 or 11?
   - [ ]  split
  
<iframe src="https://trinket.io/embed/python3/e9f7763f5a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
**Update**
<iframe src="https://trinket.io/embed/python3/60479f346e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Reflection**
This is a super interesting challenge. As I mentioned before, blackjack is one of my favorite card games recently. I knew how to play the game and thought the rule was not complicated. However, when I started to list the milestones, I found it is totally different from my mind. It's not a straight flow and has some tricky rules in special situations. Thus, I decided to first finish the basic rules: 
1) deal the cards 
2) ask hit/stand 
3) show the result
I decided to use the `def` to make the code look clearer. However, I didn't know how to use the inside variable in the main body. I struggled for a long time and later found `global card` in one of my previous reflection. Also, by reviewing my previous exercise, I wrote`def deal_card(side)`, using one function to deal cards to two sides.
```python
def deal_card(side):
    global card_list, card
    card_list = []
    for i in range(2):
      card = random.choice(cards)
      card_list.append(card)
    if side == 'player':
      print ("Your cards: ", card_list)
    elif side == 'dealer':
      print ("Dealer's cards: [",card, ",*]")
 ```
I also have great practice in the loop function. I used `while` loop to ask users to hit/stand when it's lower than 21. I knew the dealer has to keep hitting if dealer_total is less than 17, so I used `while` loop again to add more cards to the dealer side.
```python
while dealer_show:
      dealer_total = sum(dealer_list)
      # if less than 17, hit
      if dealer_total < 17:
        dealer_list.append(random.choice(cards))
      # if above or equal to 17, compare two sides
      elif dealer_total >= 17:
        if dealer_total > 21:
          print("Dealer's final cards:", dealer_list)
          print("Dealer busts")
          print("Congratualtion! You win!")
        elif dealer_total == 21:
          print("Dealer's final cards:", dealer_list)
          print("Sorry! You lose!")
        else:
          print("Dealer's final cards:", dealer_list)
        # print(dealer_total)
        dealer_show = False
 ```
I was afraid to start writing the code but when I started, I found it's not that hard. For basic functions, I can use what I learned in the class directly. Thanks to the milestones, I knew what I should do next. After finsih the basic functions, I started to add more details in the game.
A can represent 1 or 11. But in the previous code, A is always equal to 1. It makes the hitting process very long and even hard to reach 21. So I added a new function called `A_number` to decide the value of A.
```python
  def A_number(side):
    if side == 'player':
      side_list = player_list
    elif side == 'dealer':
      side_list = dealer_list
    for index in range(len(side_list)):
      if player_list[index] == 1:
        A_question = input("???A = 1 or A = 11???\nType 1 or 11")
        if A_question == '1':
          side_list[index] = 1
        elif A_question == '11':
          side_list[index] = 11
          print(side_list)
```  
I created a new python 3 to write the code but the system crashed and there was not a save function on that page so everything lost. I was going crazy. But because I had a good understanding in the first practice, it cost me less time to re-write the code.
However, there are still many that I can improve in the future. For example, add split function and pick cards from a set of poker cards.
Overall, this exercise helps my have a better understanding on python. Thanks for the great chance.
 


