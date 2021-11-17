---
layout: post
author: sj-roh
title: "SJ's Interface Draft Sketch"
---


## Update:

For this week, I managed to check a few items off the checklists, specifically: Choose data files to use in the trinket. (CHECK), 
Brainstorm how to set up the structure of the program: CSV upload (CHECK), and Begin to code, but start light with foundational lines (CHECK).
There is still a lot of work to be done, but I was glad to get off to a start. I focused on functionality, and laying down some groundwork for 
the interaction between the user via text input and the program. For each option within the main menu, this sketch displays some of the functionalities 
that I have planned: Selecting a data set to find a summary statistic (2), Creating a histogram (3). 

Below is the trinket code:

<iframe src="https://trinket.io/embed/python3/530954b1a4" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

New modifications (added items to my old checklist - copied below):
- Must figure out how to deal with option 3: Creating a histogram, what are the necessary steps for the user to go through?
- How to add code to carry out these ideas
- Learn how to incorporate dictionaries in program

## Reflection:

- Are there any roadblocks ahead? Is there anything your group can do to help out?

There are roadblocks, I need to take that next step of figuring out how to implement these ideas. Also, I must sort out what I want to do more specifically with option 3: Creating a histogram. Currently, I have an idea of letting the user select two variables to create a histogram off of. For example, if a user picks team: GSW and ppg (Points per game), then the histogram would show the ppg for each player on the Golden State Warriors. This however, would mean that the user must specify the team variable to equal 'GSW'. Currently, I have no idea how to carry this out, and this may be too ambitious for this project. A simpler outlook could be to just allow the user to select only one variable. Using ppg as an example again, the histogram would show the counts that fall into each statistical bin to show the ranks for ppg from lowest to highest (e.g., 1-10). More specifically, there could be 10 bins, each increasing by increments of 5 points (i.e., 0-5(bin 1), 5-10(bin 2), etc.) The histogram would show the count of players in the NBA (National Basketball Association) that fall into each statistical bin. 

- Are your milestones ambitious enough? Make sure to include some stretch goals.

I believe so, I think the milestones are ambitious enough - key word is enough. I don't know if I'll be completely satisfied if I opt to go with plan for the user to just provide one variable. I sort of want the program to be more interesting and to be able to use more variables. That is the goal.  

- Are your milestones too ambitious? Make sure to break down the unglamorous parts of coding into chunks that reflect the actual work to be done.

I don't think so, I think I might be missing something. I want this program to be able to use numerous variables, if possible, more than 2! But that might be too 
ambitious. I'm not entirely sure. The unglamorous parts of code is the function definition parts:

`def option2():`  
  `print("Please select the data set: NBA Per Game (1) or NBA Per Game Advanced (2)?")`  
  `mode = input("Enter 1 or 2: ")`  
  `print("Please enter a summary statistic you would like to focus on: Min(1), Max(2), Mean(3), Median(4), Standard Deviation(5)")`  
  `mode = input("Enter 1, 2, 3, 4, or 5: ")`  
  `return mode`
  
`def option3():`  
   `print("Please provide 2 variables you would like to find rankings/counts for")`  
  `mode = input("What are the 2 variables?")`  
  `return mode`  
    
I must learn how to add onto these functions for both options, so the user can be led to finding the summary statistic they want and creating a histogram. 

- Are you able to keep to your plan? Looking back at what you’ve actually done, is the difference accountable to bad planning (i.e. not anticipating what needed to be done), bad execution (not doing it), or something else?

I think so, but I must work this week to nail down some of the actual code necessary to carry these ideas out. I mention it again and again, but now is the time to do. 

## Old Plan:

## Project Idea:

For the final project, I have decided to do a data analysis project. I want to focus on using the tools that we learned in class over the semester to follow
Professor's recommendation of building an exploratory analysis tool for users to print out graphs (histogram) and summary statistics of data sets. These summary
statistics will include min, median, mean, sd, and max. The concept of uploading data sets and running a program for the users to input what they want to find, 
and for the results to be outputted is very interesting to me. Data sets with numeric variables will be important and necessary, but I am wondering if using data 
with categorical values will work in terms of finding the mean proportions for each value within each column. I want to explore the possibilies of using not just 
datasets with numeric variables, but categorical variables as well. I hope to use Python's built-in graphical output functions to print out the statistical graphs, 
but I also want to explore matplotlib as I have tiny experience using it. 

## Project Initial Work Plan (Milestones):

- Choose data files to use in the trinket. (CHECK)
- Work on gathering Runestone materials/chapters to review over, especially chapters with examples/exercises using data files.
- Gather functions for each summary statistic to use. 
- Brainstorm how to set up the structure of the program: CSV upload (CHECK), class declarations, def functions, for-loops, correct attribute & methods to use.
- Begin to code, but start light with foundational lines (CHECK). Make sure to get a thorough understanding of the structure of the program first. 
- Work out specific libraries I will need to load. 
- Do research in Runestone and online for concepts I don't remember. Ask many questions and go to office hours. 
