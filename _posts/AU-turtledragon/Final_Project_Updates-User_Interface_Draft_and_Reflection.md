---
layout: post
author: AU-turtledragon
title: "Final_Project_Updates-User_Interface_Draft_and_Reflection"
---
# My updated work plan

For the time being, I've decided to break my UT course data analysis tool into 3 categories:  Course Data, Instructor Data, and Enrollment Data. 
Within each category, I hope to impliment at least one analysis tool based on user input. 
Possible examples:
- the number of times a particular course has been offered within a given period of time
- the number of classes a particular instructor has taught in a given period of time.
- the average number of students enrolled in a particular student's classes over a period of time.
- Most recent enrollment patterns for a particular class or field of study. 
- generating an email list for all instructors in a given semester
- extracting a list of cross-listed courses for a particular unit over a period of time.
etc.

The data and calculations necessary for these sorts of tasks overlap somewhat.  So, I'm still playing around with coding strategies and deciding which ones to prioritize based both on my ability to get them working right and providing sufficient contrast between them. 

As part of this week's assigned work, I've created this preliminary user interface draft:
<iframe src="https://trinket.io/embed/python/4f00509b85" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My priorities for this interface were:
1. simple and intuitive navigation
2. the ability to incorporate branching submenus, each providing a way to get back home.
3. reduced clutter - i.e. i want the menus to get out of the way when tasks are run etc.

Starting from the sample that Dr. Hauser provided in class, I found it difficult to achieve these goals.  His use of a while loop created a scenario where the menu was ever present, as was the input prompt - whether it was applicable to the current screen or not.  Therefore, I decided to forego that structure in favor of a somewhat lengthier one that at least allowed me to have the aesthetic I thought worked best.  Dr. Hauser's method seems to work best for a simple menu that's specifically intended to do a series of tasks in sequence.  Though definitely produced too cluttery a result for my purposes, I do wonder whether ther might be a more elegant way to do what I'm doing - i.e. less repetitive code.  Given the time constraints of this project, however, I doubt I'll have time to focus on such optimization.  Instead, my priority will be making sure my tools work the way they should. 

In order to erase the previous menu with each new user selection, I had to implement a strategy I found online involving importing the `os` library and then using the `os.system` method to create a custom function `clear()` to clear the screen as needed.  I don't honestly have any idea how this is working or what the os library actually is - it appears to allow specific operations unique to the operating system the user is working on(??).  As always, regurgitating code I don't quite understand makes me a bit uncomfortable.  But, it's a very small piece of code that can be quite easily removed. And, more importantly, it works for the time being and I'm happy with that.  But I may carve some time to talk with Elliott/Misha about whether this is truly necessary or if there's perhaps a simple built in function that does the same thing. 

Other than tooling around with this user interface, I've been experimenting with the parsing of my data and simply reminding myself how we've done these sorts of things in the past.  The recent lull in our direct coding homework activities and lessons that interweave with one another has broken my flow somewhat and caused my brain to loosen its grip somewhat on the concepts and strategies we've been working on all this time.  So this project is serving as a useful refresher of all the material we've covered thus far, which I imagine is kind of the point. 


# Revised Schedule/Milestones

[x] Import smaller test data files to trinket and analyze how it looks from Python’s perspective. 
[x] Identify 3 categories of data analysis/extraction I intend to focus on.
[x] draft and test a preliminary user menu interface
[x] Identify areas of data that will need cleaning
[ ] Identify specific data analysis/extraction actions to implement (1 in each category)
[ ] Build and test data analysis/extraction action 1.1 (category 1, action 1)
[ ] Build and test data analysis/extraction action 2.1
[ ] Build and test data analysis/extraction action 3.1
[ ] Test actions on larger and more complicated data sets
[ ] Build a bonus function that converts original reports and exports a cleaner/more readable version. 
[ ] Final testing and debugging
[ ] Present
