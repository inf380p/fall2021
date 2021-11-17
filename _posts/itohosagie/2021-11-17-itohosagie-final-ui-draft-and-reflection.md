---
layout: post
author: itohosagie
title: "Final Project Update and Initial UI Sketch"
--- 

### Final Project Update and Initial UI Sketch

Following my [previous post](https://inf380p.github.io/itohosagie-final-project-idea-plan.html) for my final project plan I set out to create an initial sketch of the interface. Even from the beginning there were moments where I thought, “How do I do what I want to do?” which resulted in working in two different trinkets.

The first one was intended to help me get acclimated to working with the data, even trying out slicing the first line from the data set. This was also where I worked out my first `for loop` using the data, and where I hope to continue working out brainstorming ideas throughout this project. I’ve included it below:

<iframe src="https://trinket.io/embed/python/9cace80756" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

After I got comfortable with the dataset I switched over to the second trinket where I worked out the initial stage of the UI by creating a VERY rough sketch. I started by creating a menu for the user to type out an area that they would like to explore within the Spotify data. Within this menu I’ve added what I would expect to be a page title (for later iterations) along with potential tab names. 

There are three functions that have been created to coincide with the user’s selected area of exploration, which include interests by year, genre and artist. Any selection outside of these will result in the following message: `Option disabled. Please make another selection.` Right now the data retrieved from these commands is a bit messy and will require further clean up as some elements would not initially be of interest to users, such as the tempo or duration of the song. This could require some form of string slicing and extracting, which I attempted within the first trinket, but still have not worked out (at least by using regular expressions). 

Some potential roadblocks that I anticipate after going through the initial stages of this project are include the following:

*  Selecting and acclimating to a visualization tool within Python
* Working out how users would be able to select multiple elements to explore at a time
* Ensuring categories embedded within other categories aren’t retrieved unintentionally (i.e., for genre there are various types of “pop”)

Taking these into account based on my project plan, I think the stage of developing the program will take extensive time in comparison to other elements, such as visualizing the data and creating and embedding images based on genre or year. Although it would be nice to have these elements, I doubt that both would be able to be fully fleshed out by the end of the semester.

One aspect of the program that I would need to review are the functions that have been created for the user to interact with the data based on the menu provided. Before I included `user_input` within the function, it was set outside prior to the function definition. However, this prompted the user input to come before the menu, which was not my intention. 

Before:
```
#preliminary request for user: desired year of music
user_input = input("Enter the year of music you would like to explore: ")

#function for calling data by year
def by_year():
    #for loop to retrieve data by year
  for line in prjct:
    if user_input in line:
      print(line)
```

After:

```
#function for calling data by year
def by_year():
  #preliminary request for user: desired year of music
  user_input = input("Enter the year of music you would like to explore: ")
  #for loop to retrieve data by year
  for line in prjct:
    if user_input in line:
      print(line)
```

Since I know that I would want to incorporate more complex functions for multiple interests the user would want to explore (i.e., results for a specific artist in a specific year or set of years), I am concerned that there would only be a select few that would be fully developed as I’m not sure what would be the best way to create these in a space and time efficient manner.

Nevertheless, the existing program has been included below:

### Initial UI Sketch
<iframe src="https://trinket.io/embed/python/86e8755bbd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Based on my current progress I would say there is still a good amount to tackle before I actually get to the visualization portion, but I think by adding a timeline to the different elements that I anticipate working on would help me gauge what aspects I can reasonably tackle within the time I have remaining within the semester. 

Despite reasonable doubts for having all intended elements completed within the time allotted for this project, I’m still very much looking forward to how everything will come together.
