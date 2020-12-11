---
layout: post
author: intjnotinfp
title: " intjnotinfp's Course Reflection Post"
---
In reflecting on the course, I’m realizing how difficult this semester has been and how different it looked than I expected when I got here. Here are some summaries of milestones and things I discovered along the way. 

Useful realizations:
-	There are more  (open) resources available than any topic I’ve ever tried learning. It’s a relief to be able to freely access tips, tutorials and explanantions pretty much on-demand, and really speaks to how collaborative the community is as a whole. That was one of my favorite aspects of diving into the world of coding!
-	Takes a lot longer to wrap my mind around the concepts than I expected it to. I thought that it would be pretty similar to learning human languages, which has also been very easy for me, but that hasn’t exactly been the case. I think the reason for that is that other humans can easily interpret, account for, and correct language mistakes (without sacrificing meaning and understanding!), sometimes without even realizing. With computer programming, a small mistake will stop you in your tracks and force you to reflect on any changes you’ve made since the last error, thus “progress” or success takes more time and happens in smaller chunks – errors just can’t be glossed over.
-	Of note: I’ve struggled with procrastination and anxiety in this course more than any other I’ve taken before, which has affected my overall attitude and work product more than I would’ve liked. I know it’s because of the effects of the pandemic/ isolation, so I’m trying to come to terms with that and move on. 
-	Problem Solving Strategies: As far as problem solving strategies go, taking a break has been 50/50 in terms of utility, because it does help to walk away and reset, but sometimes it just ends up contributing to the procrastination issue mentioned above. The most useful strategy for me has been identifying exactly where my hangup is and then watching multiple tutorial videos from different people until it fully makes sense. I started off by just watching the Dr. Chuck videos in conjunction with the readings, but then used those plus Tech with Tim tutorials on YouTube and also some random ones along the way.
-	Confusion: My first setback was not understanding how parameters/ arguments worked within functions but I was able to double back and work through that successfully. See below.
-	Lightbulbs: It’s been really rewarding to push through and “hack” a concept. Here are some examples of “lighbulb” moments where things suddenly worked after long bouts of difficulty:
```python
while not player_busted(player_score):
        show_hand(player_hand)
        player_hits = does_player_hit()
        if player_hits:
            new_card = deal_additional_card()
            player_hand.append(new_card)
            player_score += new_card
            continue
        break
```
That’s an example of using multiple functions like player_busted and show_hand with specific arguments/parameters within my BlackJack app. It felt really good to get that loop to execute.

Here’s another, where I Ayu and I had to brainstorm for awhile to figure out how to accomplish a parse, count and print exercise. By using official documentation, we discovered the .startswith method and were able to get it to work! 
```python
for line in fhand:
  words = line.split()
  if len(words) > 0: #safety line
    if len(words) > 2 and words[0] == 'From':
      print(words[1])
      #total_from = words.count('From')
      #print(int(total_from)
    #outside_from = words.count("From")
    #print(outside_from)
  if not line.startswith("From"):
    continue
  if line.startswith("From"):
    #continue
  #else:
    line = line.split()
    line = line[1]
    #print(line)
  count += 1
print('From: appears '+ str(count) +' times.')
```
-	Another lighbulb moment that was also pretty cool was when I discovered some slight overlap with my SQL class – similar syntax gave me more confidence in executing database queries as soon as I was introduced to them. 
-	One of the absolute best things I’ve gotten out of this course is an appreciation for those with a knack for programming but, even more so than that, is an immense sense of respect for people who can push through the frustration and time commitment it takes to master Python/ additional programming languages. I took this course to push my limits and, well, I certainly discovered where those lay and I’ve adjusted my interests accordingly. That’s useful! While programming isn’t directly relevant to what I want to do when I graduate (scholarly publishing), my career will certainly bring me into contact with programmers in a library setting, and it has been useful to learn the basics and gain the vocabulary to converse with specialists. I’m proud of myself for being brave enough to trying something new and difficult, not being great at it, and accepting that it’s ok to leave it behind after the class wraps. 
