---
layout: post
author: brianna-stedman
title: "Brianna's final project milestones, last revision"
---
Here is a snapshot of my code where it currently stands (it's very chaotic and disjointed right now):
<iframe src="https://trinket.io/embed/python/67430a89c4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here was my old plan:
- [ ]Import data files
- [x]Provide welcome/how-to text on the starting page
- [x]Build “help” function that returns the how-to text when user requests it
- [ ]Accept user input in form of team name or player name, return a list of options to view for each
- [ ]When user selects team name, ask if user would like a roster or a statistic
- [ ]If user selects roster, read through the file and return all players on that team and their stats
- [ ]If user selects a statistic, specify which one (ppg, rpg, apg); return calculated aggregated statistic for all players on that team
- [ ]If user selects player name, return stats, nickname, info, etc for that player
- [ ]Build “print all” function that cleanly returns all csv data if requested

Stretch goals:
- [ ]Use classes to build two functions (“compare teams” and “compare players”) that accepts the input of multiple team or player names, and returns rows of stats/aggregated stats.
- [ ]Give user option to input notes on each player and update those to the original data files (*or create a new file only with notes!*)
- [ ]Build “view notes” function that returns only a list of players with a note attached (*or only returns the new file with player stats and notes!*)
- [ ]Build "clear notes" function to erase all and remove from the new file 

My new plan is mostly the same as the old plan, just slightly modified to be a little simpler. The biggest difference is removing the team data aspect of the analysis, since that would be a new dataset I would have to work with. I did some research on adding a new column/updating that column in a csv and feel more confident about being able to add notes, so I moved that back to being part of my regular milestones. However, I am still keeping the "including photos" milestone as a stretch goal;  I recently learned a method of saving photo links in a csv that I think I will be able to get to work, but I also don't want to devote too much time to it before finishing the other functionalities! 

- [x] Import nbalegends csv
- [x] Provide welcome/how-to text on the starting page
- [x] Accept user input in main menu and have a different function for each tool:
    - [ ] Build "search player" function that accepts a variety of user input and creates a dictionary of potential results by using id:player_name as key:value to match rows in the spreadsheet *right now trying to use re.findall but may research and try something else*
        - [ ] Accept user input to make final selection and return player stats for that selection 
            - [ ] Account for user error/inconsistencies in input by converting all to .upper() or .lower(), potentially by removing spaces using regex
        - [ ] Build "Add to Dream Team" function that accepts user input to add the player & their stats to a saved list 
        - [ ] Build "Remove from Dream Team" function that accepts user input to remove the player & their stats from the saved list 
        - [ ] Build "Add Notes" function to accept user input and write to the matching player's row in a new column in the csv 
    - [ ] Build "View My Dream Team" function that prints the running saved list of players 
        - [ ] Accept user input to clear the entire saved Dream Team list *(dictionary?)*
    - [ ] Build "View All Notes" function that prints all players & stats with a not-null Notes column 
        - [ ] Build "Clear All Notes" function that accepts user input to clear out that column *I still need to research how to do this*
    - [x] Build "Help" functions that returns the how-to text when user requests it from the main menu
 - [ ] Provide "return to main menu" option with every search
 - [x] Import os and clear the screen with every new main menu selection 

Stretch goals: 
- [ ] Import csv with hyperlinks to player photos
- [ ] After user makes final selection of player, include photo on the player profile page 

##Reflection:
I got a late start on this project but I feel confident about where it's going to go now. I'm currently stuck on the re.findall function so I want to try to look at some different ways to accomplish the same sort of thing to see if any of those are successful! A few days ago I drew out a flowchart of sorts with the different option paths, and that's made it WAY easier to organize what I'm working on (since functions are all like puzzle pieces separately from the main module, I was getting a little bit lost by trying to do too many things at once). I could definitely use a refresher on dictionaries, as I've been finding I'm using them as the basis for most of my project but still don't feel super confident about them. 
