---
layout: post 
author: brianna-stedman
title: "Brianna's final project milestones"
---
# Project Idea:

There are a few different ideas I have about the final project. After making sure to read the project description SEVERAL times (not making that mistake again!) it seems as though the recommended angle with which to approach the final is a data analysis tool that has the functionality to allow the user to uplaod and analyze *their own data,* not necessarily datasets that I have found and uploaded. I'm not totally sure how I feel about this (or how I feel about my ability to accomplish this) so I'm also still considering what kind of data sets I could use and what I could have them do. In my Data Wrangling class last spring, we had to build out some kind of Python program to do data analysis, and I cleaned and utilized a bunch of data on the ultimate frisbee college championships. I'm also working on a separate project in another class that uses several mostly-clean csvs of NBA player data, so I have these two datasets on hand. However, in general it sounds like I need to build a generic program that could take essentially any dataset and do very basic aggregation or mathmatical functions on the data inside. If I'm able to diverge from this, I think something I'd like to build is potentially a search type utility that uses the NBA player data that I have and allows the user to type in team names, player names, etc to search for them and pull up their stats. I think this could be accomplished in Python using the tools we've learned so far, I just need to figure out the milestones. 


# Proposed Milestones:
- [ ] Import data files
- [ ] Provide welcome/how-to text on the starting page
- [ ] Build "help" function that returns the how-to text when user requests it
- [ ] Accept user input in form of team name or player name, and return a list of options to view for each  
- [ ] When user selects team name, ask if user would like a roster or a statistic
- [ ] If user selects roster, return all players on that team and their stats 
- [ ] If user selects a statistic, specify which one (ppg, rpg, apg); return calculated aggregated statistic for all players on that team 
- [ ] If user selects player name, return stats, nickname, info, etc for that player 
- [ ] Build two functions ("compare teams" and "compare players") that accepts the input of multiple team or player names, and returns rows of stats/aggregated stats. *I don't totally understand "classes" yet but I feel like those could be useful here? Since these two commands will probably take several functions each*
- [ ] Give user option to input notes on each player and save those to the original data files 
- [ ] Build "print all" function that cleanly returns all csv data if requested 
- [ ] Build "view notes" function that returns only a list of players with a note attached

# Stretch Milestone: 

If I can accomplish all the above (and if this is allowed), I want to also see if I can somehow include a photo when the individual player stats are returned! This might need to be something I add to my initial csv file though, or perhaps a separate dataset.

