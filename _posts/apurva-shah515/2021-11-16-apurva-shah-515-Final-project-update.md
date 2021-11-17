---
layout: post
author: apurva-shah515
title: "Apurva's Project Update, Schedule, and Interface Sketch"
---

In my previous plan I had initially aimed to create some functions for summary statistics, as well as some graphical representations of analysis based on my initial dataset. Since then I have spent time reviewing my data, and for the data that I have basic summary statistics do not make sense. Primarily this is due to the data I have already collating some statistics, such as the total number of minutes a streamer had streamed in the year of data collection. 

Due to these pieces of data already being included in the dataset, I modified my plan to still present the graphical representations, but different summary statistics. Now, I intend to offer the user some other options, such as the mean stream or view time for the entire dataset, or for a given category. I had also intended to create some functions for analysing the data for a given category, for example providing summary statistics after sectioning the database to only Portuguese speaking streamers. I believe this is a good aspiration to have, but for the initial project I want to focus on presenting histograms, pie charts and other visualizations of the dataset rather than building on the summary data already contained in the dataset. 

# My Initial Work Plan
1. Clean the data if necessary and merge the two files into a third data file for use in this program
2. Write code for pulling out summary statistics - various averages for different categories
3. Write code for graphical representations (histograms, pie charts etc.) for non-numerical categories
4. Add dictionaries for storing summary statistics
5. Define functions for each of these methods
6. Add help text, comments and instructions for how to use this program
7. Ensure the program is compatible with Trinket’s console for interactability
8. Incorporate my defined functions and methods into a custom module

# Modified Work Plan
1. [x] Clean the data
2. [x] Draft a mostly complete user interface sketch
3. [ ] Define functions for data visualizations - histogram and pie chart for the non-numerical categories
4. [ ] Define functions and menu option for allowing the user to see the data - most viewed, most viewers gained etc.
5. [ ] Incorporate a dictionary for the statistics, so the user can simply look up the dictionary value rather than parse the whole text file
6. [ ] Add help text, comments and instructions on how to use the program

# Reflection

At this point I feel that I am a little behind where I aimed to be. This is mostly in part due to having to revise what exactly I was planning to analyse from my dataset, however I believe that I can make up the lost time as much of the statistics analysis should require only minor modifications from one to the next. I have left myself an open end in terms of how far I want to take this project, and I have a clear image of what I definitely want to have achieved before the end. I want to make sure that not only is my program offering a range of interesting findings from the data, but also is easy to use for the user or a reader of my program. 

Currently the project is proceeding at pace, however I have been having some issues with adding a csv file type to my trinket for use. This is currently proving to be a roadblock to some of my text parsing, as I am unable to easily split the data easily. Some of the non-numerical data includes spaces, so this is proving a challenge. 

# Plan for next class

By next class I aim to have a function for creating at least one visualization of the data, resolve my issue with adding a csv file to my trinket, and create my functions for pulling out the key data from the dataset for the statistical analysis.
1. For the visual elements, I want to be able to create a pie chart for the most common Twitch categories, and a histogram for the primary languages. 
2. For the statistical data, I want to be able to draw out which streamers from the dataset had gained the most viewers or followers, had the highest watchtime/stream time, and the highest peak viewership.

# My UI Sketch
<iframe src="https://trinket.io/python3/dbb6f16f3d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

