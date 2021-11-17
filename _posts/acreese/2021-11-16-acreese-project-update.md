---
layout: post
author: acreese
title: "Alex's Project Update: Interface Draft"
---

### Project Update and Trinket Snapshot

This project includes a fully functional user interface sketch of my program that allows users to explore the basic options for comparing native plant data: 

<iframe src="https://trinket.io/embed/python/03cd8b55d7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I have created multiple menu displays – a main menu plus two secondary menus based on user input: a menu for analyzing the plant data of a single state, and a menu for comparing plant data of two states.  I have included an option to display states available for analysis inside these secondary menus – so users know their options. Initially, I was relying on a single main `while` loop to navigate between these three menus though different inputs that called specific functions, but it was getting difficult to manage the state of the menus this way and ask for conditional inputs in the secondary menus. As I started developing new input functions for users to select specific states, I realized that creating specific while loops for each menu/function would improve the program’s usability and functionality.

As part of my interface, I have tried to account for invalid user inputs in a way that communicates specific errors and solicits a new response inside the same menu. But at any time and from any menu, the user can type “exit” (in any case) to quit the program. I have generally tried to make my program case insensitive, so that errors or personal preferences in case does not affect usability. At this point my interface works well with no apparent errors, but I still feel like it is more clunky than elegant…mostly the interface code for comparing two states.  

I have slightly adjusted my project milestones to reflect a little more specificity and to designate some more ambitious and complicated tasks (2 state comparison, integrating a third-party data viz module, and creating specific analysis options for users) as stretch goals. I hope I have time to get to some of these, especially the data viz, as it will be a fun opportunity to expand my Python knowledge.) Otherwise, I don’t see any clear roadblocks ahead, which is to say I have a pretty good idea of what I need to do to accomplish each one.  I just need to keep working and hitting my milestones as steadily as I can.

### Project Milestones

- [x] Develop preliminary interface code
- [ ] Create help text
- [ ] Develop analysis code for single state/text file analysis
- [ ] Write code to open and read in the text file, loop through, split on commas, process and store data in dictionaries
- [ ] Write code to report and display data 
- [ ] Stitch together interface and analysis code

#### Stretch goals: 
- [ ] Integrate a third party data visualization module?
- [ ] Develop analysis code for multi-state comparison?
- [ ] Update interface code with analysis options?  
