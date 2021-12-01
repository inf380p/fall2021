---
layout: post
author: AU-turtledragon
title: "12/1 Final Project Update"
---

### My Original Proposal / Workplan:

My initial project proposal can be seen here: https://inf380p.github.io/Aarons_Final_Project_Proposal.html
And my last update and work plan revision can be seen here: https://inf380p.github.io/Final_Proj-User_Interface_Draft_and_Updates_Reflection.html

### Status Updates and Workplan revisions:

Since our last class meeting, I've continued to iron out some of the kinks in my original user interface, as the overall flow is important to me.  The report data that I'm working with isn't very reader friendly on its own, so a simple and intuitive user interface to pull out the specific information the user wants is my primary focus for dealing with it.  There's not a whole lot of complex analysis to be done with the data itself really.  It's all just about simplifiying the data and extracting that parts that are useful.  One additional feature of my user interface that I'm still working out is making it adaptable to new report files.  Rather than my program only being able to parse out data from a predefined data file that's already loaded.  I would like to at least pretend that the user has uploaded their own report to the appropriate file directory and have the UI ask them for the file name before it proceeds to work on it.  As the data in question is updated each semester, I would like this script to be adaptable to new reports.  
I'm recognizing that this might be a bit complicated within the trinket sandbox we're working in.  But we'll see. 

Much of my time since the last class has been spent simply working out ways to clean up my data and clear up inconsistencies throughout that make it complicated to compile accurate summary data. Otherwis identical courses with discrepencies in how their course numbers appear in this report from year to year; instructors being grouped together that need to be parsed out individually; cleaning out problematic characters; eliminating courses that were canceled and no longer relevant to the kind of data collecting this tool is designed for; etc. 

I must say that I underestimated the complexity of some of those cleaning tasks. Whereas I had originally invisioned the preliminary data import and processing as a rather simple starting point after which I would focus my coding work around the specific analysis tasks my program is meant to assist with; I now realize that much of the meat of this assignment is actually in the initial cleaning up stage.  The other extraction tasks will all be a bit simpler if the data they're meant to pull from is properly cleaned up and organized. 

My work right now is made up mostly of scattered test sketches, which I've started to bring together into what will become the final singular project trinket.

###Progress

My main draft trinket can be seen here: <iframe src="https://trinket.io/embed/python/4162b9f8d9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

And some of my data cleaning sketching being folded in can be seen here: 
<iframe src="https://trinket.io/embed/python/54f59e7d9e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So far, I'm on track for meeting the basic requirements for the assignment - 

  Both project types must use:
  - [x] At least one external data file. For the data tool, this should be your data.
  -	[x] Dictionaries.    
  -	[x] Custom modules
  -	[x] definite (for) loops
  -	[x] Custom functions
  -	[x] A Python 3 or Pygame (Python 3 + GUI) Trinket
  Both must be:
  -	[] readably coded
  -	[] well commented
  -	[x] well organized
  -	[] idiomatic
  -	[] error-free
  -	[] (largely) bug free. That is, your core use cases should work. Small bugs are OK but the quality level for the final should be higher than previous projects.

  Data analysis projects must:
  -	[] Have help text available somehow. For instance, if the user types ‘Help’, explain what they program can do.
  -	[x] have an iterative interface. That is, the user should be able to perform any number of supported actions and then exit the program.
  -	[] Visualize data via text printouts. 


Over the course of this assignment so far, I've found it necessary to pull back and let those basic assignment requirements guide my work a bit more. The truth is I hardly even looked at them before.  I just focused on what I wanted to do and trusted those requirements could be met along the way. Because the tool I'm working on is something I hope to build out further and deploy in my day-to-day professional work, I've had a tendencay to get lost in a ton of big ideas that have slowed my progress on the immediate task at hand.

The extensive work I've put into my basic data cleaning and UI so far have already met most of those basic assignment markers.  So, in terms of just "making the grade", my main priority over the next week will be refining how my code is being presented - readability, comments, etc.  On top of that though, I would still like to have at least one functioning user-focused operation within each of my 3 main categories. At least one of those will need to meet the visualization requirement of my assignment. 

So, for the next week:
- create one executable data analysis task in each menu category
- go back over all of the areas of my code that involve user input and build in semi-fool proof mechanisms to ensure those inputs work as expected.  
- add in help sections to assist with the above.
- go back over my UI and task modules to add sufficient comments and group everything in the most clear way possible. 
- compile my notes for the final reflectiond etc. 
- BONUS TIME: build an additional analysis task or two if I have time.
- BONUS TIME: try to solve the problem of refreshing the existing data file - i.e. the imaginary scenario where the user has provided their own data file and my script needs to read THAT file instead of the one its been trained to read by default.  I essentially want the data file to be used as a variable so that my code isn't so dependent on knowing the exact file name everywhere it's accessed. if the user provdes a valid file, my script should be able to read it and do all the same stuff. 



