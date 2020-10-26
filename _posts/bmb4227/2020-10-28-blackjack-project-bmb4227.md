---
layout: post
author: bmb4227
title: "Brittany's Blackjack Project!"
---
# :diamonds: :clubs: :hearts: :spades: Reflection :spades: :hearts: :clubs: :diamonds:

This was my initial milestone list:
- [ ] Deal cards to user
- [ ] Show user cards
- [ ] Get user input to hit or stay
- [ ] If user stays report score
- [ ] If user hits deal a new card
- [ ] Tell user what score is

My initial milestone list really shaped how I approached and started my blackjack project. Rather than looking at the requirements like use a loop or a custom function I instead tried to check off some of the milestones on my list even if my code wasn't the most efficient. Below is an earlier version of my program that I ended up with by the end of week 1 and beginning of week 2.

## Early Version of Program
<iframe src="https://trinket.io/embed/python/c328381de8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

A lot of the issues that I ran into during this first attempt really had more to do with typos or indentation mistakes. For, example rather than 
```     
          first_card = random.randint(1, 10)
          #this appends the first card to the list
          user_score.append(first_card)
          second_card = random.randint(1, 10)
          print("your first two cards are:", first_card, "and", second_card)
```
I had initially used

```     
          p = random.randint(1, 10)
          #this appends the first card to the list
          user_score.append(first_card)
          q = random.randint(1, 10)
          print("your first two cards are:", p, "and", p)
```
I had accidentally used p twice in the print statement and this was throwing off my score totals later on. I went talked to Misha about this issue during class because I couldn't figure out what was wrong. I finally realized on my own what the issue was when I was explaining to Misha what was going on. Misha gave me two really good pieces of advice. She talked about the "rubber ducky phenomeon" where sometimes it feels impossible to see a problem unless you're talking to someone. She also recommended creating variable names that make sense to humans even if they aren't necesarily efficient or terse becuase it makes it easier to identify issues.

After my first attempt at the blackjack program, I edited my milestone list:

- [ ] Deal  initial two cards to user
- [ ] Show user cards
- [ ] Show user total score
- [ ] Deal two cards to dealers and calculate score
- [ ] If Dealer's score is less than 16 keep drawing cards
- [ ] Don't show score until a user chooses to stay
- [ ] Show user one of the dealers cards so that they know whether to hit or not
- [ ] Get user input to hit or stay
- [ ] If user stays report score
- [ ] If user hits deal a new card
- [ ] Keep asking if the user wants to hit until they stay or bust
- [ ] Tell user what score is
- [ ] Calculate whether the dealer or the user wins

I found that adding just a few additional rules like making sure the dealer continued to draw until they reached above 16 made the game more fun. Before I incorporated this rule the user almost always won which is great but not necesarily fun or surprising. I also started going back and cleaning up my program and trying to fulfill some of the other requirements. For example, defining a unique draw card function. Many of the issues I ran into during this process had to do with making sure that I was appending cards correctly and calculating the score with all of the cards that had been drawn. This just took a lot of trial and error and talking through what was added when. 

## Final Version of Project
<iframe src="https://trinket.io/embed/python/024df48c89" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
