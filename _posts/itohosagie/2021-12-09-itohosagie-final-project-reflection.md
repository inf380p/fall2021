---
layout: post
author: itohosagie
title: Final Project Reflection
---

#Final Project Reflection: Spotify Summary Tool for 2010-2019
 
### Initial Plan
Going into this final project I had a fair amount of expectations as to how the course of the project would turn out and what my end product would be. However, through developing the program for this project, I’ve realized that during this initial process of learning Python, there are things that I learned or hoped to implement that were replaced with other methods, which contributed to a more robust understanding of the program itself, as well as techniques/elements from unused code that can be used at a later time. In other words, nothing was wasted in this learning process, in terms of this project and over the course of this semester, as well. 

In the early stages of this project one challenge that I encountered was the difficulty of transitioning from just conceptualizing about a potential project to working out its details through Python code. It was one thing to try to work out a problem provided for me like from the homework, but it was another to come up with and try methods to address an issue based on my own research and desire to apply first hand my basic knowledge of text analysis.

Nevertheless, I intended to create an interactive tool that would present users with a visualization based on the information they requested from the [Spotify dataset](https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year) I obtained from Kaggle. In the early stages of the project I definitely had very ambitious goals of what I would be able to construct given the timeframe and my limited knowledge of Python. I idealized that if a user were to input an artist or year, they would receive a chart that met the specific parameters they inputted.

I began with a very simple interface that called aspects of the data, but still in the original format contracted from the original .txt, `toplist.txt`. I thought this was a good start, but going forward from there it was difficult to pinpoint how I would transform the information retrieved from the initial sketch into a visualization. 

Key elements from this initial sketch that were brought into the final program included the use of a menu, functions based on a specific attribute of data and a `while loop` that runs through each function when prompted by the user.

Here’s an example of a function I created to call information from the dataset based on the year attributed to the each line of data:

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
In addition, here’s the initial sketch of the while loop that would be reworked later in development:

```
#variable for while loop (based on example from class [11/10])
running = True

#while loop to run through the menu
while running:
  print(menu)
  user_select = input("Select the element to begin music exploration by typing one of the options above.")
  if user_select == "Explore by year":
    selection = by_year()
  elif user_select == "Explore by genre":
    selection2 = by_genre()
  elif user_select == "Explore by artist":
    selection3 = by_artist()
  else:
    print("Option disabled. Please make another selection.")
```

Here’s the full trinket for my initial sketch, in which the interface recalls information based on what the user inputs:
<iframe src="https://trinket.io/embed/python/86e8755bbd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Moving on from the sketching stage I was encouraged to create dictionaries for each attribute I wanted the user to engage with. Over the course of the semester dictionaries had actually been a topic that I struggled to grasp, so taking on the task of creating dictionaries proved to be a challenge for me. I tried to think through what elements I wanted to include within each dictionary, and through this process was met with **many errors**. 

One of the main issues I encountered was trying to work around the presence of ` “ “ ` quotation marks that surrounded each comma-separated-value, from the `.txt` file, while still capturing accurate information. When I would open the file and attempt to split each row based on a comma I would receive `”Drake”` as a genre and `”The Chainsmokers”` as a song title. In addition, the results would be overshadowed by the overabundance of quotation marks and would make the results hard to read. 

At this point, I wasn’t sure whether opening the file in a different manner would help to eliminate the presence of the quotation marks later on, so I replaced the following with a new method of opening the `.txt` file:

Original method for opening file: 
```
prjct = open('toplist.txt', 'r')
prjct_readlines = prjct.readlines()
```
Alternative method for opening file:
```
with open('toplist.txt', 'r') as prjct:    
  prjct_readlines = prjct.readlines()
```

Unfortunately, I still encountered the same issue, but chose to move on to at least build out the functions I wanted the dictionaries to run through, which I hoped would provide a better sense of how the information should be presented when the user made a selection.

In doing so I developed my initial functions to retrieve data based on what the user selected to form a list. It was hard to keep track of where to put what index and how to correctly reference the `key` or `value` from the dictionary because, again, these concepts were difficult for me to grasp. 

### Re-Planning
After struggling with the dictionaries  for some time I decided to rethink the way I wanted the user to interact with the data, while still enabling them to receive a visual representation of whatever attribute they’re interested in from the data. It took some time, but eventually I moved to a more summative project that looked at the top listings for each category. 

I wanted to keep each attribute as separate dictionaries that retrieved information from a different part of each row in the dataset, but instead of using my original method to open the file, I imported the `csv module` to eliminate the unnecessary quotation marks from results.

Doing this made creating dictionaries and the proceeding functions so much simpler and easy for me to read as well. I’ve included the section of code that replaced my original method of creating dictionaries below: 
```
#dictionary for artists/songs/genres
artist_dict = {}
artists = []
song_dict = {}
songs = []
genre_dict = {}
genres = []
year_dict = {}
years = []
for line in prjct_reader:
  #makes list for each attribute
  songs.append(line[1])
  artists.append(line[2])
  genres.append(line[3])
  years.append(line[4])
```
One aspect of the project that didn’t alter was the use of `matplotlib` to visualize the dictionaries I had created. This required some outsourcing in knowing what methods to call, and I found the following resources very helpful as a beginner:

*[W3School -- Matplotlib: Creating Bars](https://www.w3schools.com/python/matplotlib_bars.asp)
* [Plot a bar chart using a dictionary](https://www.tutorialspoint.com/plot-a-bar-using-matplotlib-using-a-dictionary)
* [Intro to Data Analysis/Data Visualization in Python (with Matplotlib)](https://www.youtube.com/watch?v=a9UrKTVEeZA)

I broke each of the attribute’s top five results into three dictionaries that were used to create the graphs displayed through the visualization module. It seemed like the simplest method given the fact that I had just recently learned how to use it.

Lastly, I needed to piece all the different elements together, which included the interface, dictionaries, functions, and graphs that had been constructed within separate files. This required importing the various files into the main `.py` file, `main.py` and interspersing various elements, such as the `year_graph()` function into the while loop to allow for the user to have a more interactive experience. 

Here’s a look at the final project:
<iframe src="https://trinket.io/embed/python3/0d4b62a832" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### What Worked Well
Although I was initially reluctant to extensively use dictionaries within the program, they proved to be very useful in retrieving the information that I was hoping to present to the users, just not in the way that I anticipated. Another aspect that worked well was the use of `matplotlib`. I was initially intimidated by it since this wasn’t a module that we had covered in class, but after following along with some example problems I was able to gain confidence in using it and hopefully more visualization modules within Python in the future.


