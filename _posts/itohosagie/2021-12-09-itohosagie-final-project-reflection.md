---
layout: post
author: itohosagie
title: Final Project Reflection
---

#Final Project Reflection: Spotify Summary Tool for 2010-2019
 
<iframe src="https://trinket.io/embed/python3/0d4b62a832" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Initial Plan
Going into this final project I had a fair amount of expectations as to how the course of the project would turn out and what my end product would be. However, through developing the program for this project, I’ve realized that during this initial process of learning Python, there are things that I learned or hoped to implement that were replaced with other methods, which contributed to a more robust understanding of the program itself, as well as techniques/elements from unused code that can be used at a later time. In other words, nothing was wasted in this learning process, in terms of this project and over the course of this semester, as well. 

In the early stages of this project one challenge that I encountered was the difficulty of transitioning from just conceptualizing about a potential project to working out its details through Python code. It was one thing to try to work out a problem provided for me like from the homework, but it was another to come up with and try methods to address an issue based on my own research and desire to apply first hand my basic knowledge of text analysis. In hindsight I think I had too lofty of a vision for my program given the timeframe and my own coding abilities, though overall this served as a good challenge for me.

I hoped to create an interactive tool that would present users with a visualization based on the information they requested from the [Spotify dataset](https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year) I obtained from Kaggle. In my original plan I expected to have the user input certain bits of information that the program would recognize and visualize accordingly; however, as I got more advanced in the program I got the sense that I had bitten off more than I could chew in terms of programming.

I began with a very simple interface that called aspects of the data, but still in the original format contracted from the original .txt, `toplist.txt`. This was largely based on the example that Professor Hauser provided us with and it made sense as to why one would want to follow such a format with a defined menu, functions and `while loop`. I thought this was a good start, but going forward from there it was difficult to pinpoint how I would transform the information retrieved from the initial sketch into a final and clean visualization. 

I do want to point out that although much of this initial plan was scrapped there were key elements from this initial sketch that were brought into the final program, which included the use of a menu, functions based on a specific attribute of data and a `while loop` that runs through each function when prompted by the user.

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

Moving on from the sketching stage I was encouraged to create dictionaries for each attribute I wanted the user to engage with. The use of dictionaries was something that I wanted to avoid because over the course of the semester dictionaries had actually been a topic that I struggled to grasp, so taking on the task of creating dictionaries I knew would be a challenge for me. It helped to have Professor Hauser walk me through how a dictionary could be constructed using this dataset and following this I tried to think through and include the elements I wanted to capture within each dictionary, and through this process was met with **many errors**. 

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

In doing so I developed what would serve as an intermediary placeholder for how the final functions would retrieve data based on what the user selected to form a list. It was hard to keep track of where to put what index and how to correctly reference the `key` or `value` from the dictionary because, again, these concepts were difficult for me to grasp when we initially learned them in class, but I received a lot of help from Professor Hauser, our textbook, Google, and one of my roommates who actually loves Python.

### Re-Planning
Even with this help, I struggled with conceptualizing and executing the data included within the dictionaries, and after some time I decided to rethink the way I wanted the user to interact with the data, while still enabling them to receive a visual representation of whatever attribute they’re interested in from the data. It took some time, but eventually I moved to a more summative project that looked at the top listings for each category. Instead of focusing on singular instances from the data to visualize I thought that providing a high level overview of the data would be a more realistic task given my skill set and would also still give my time to explore visualization modules in Python, such as `matplotlib`.

I wanted to keep each attribute as separate dictionaries that retrieved information from a different part of each row in the dataset, but instead of using my original method to open the file, I imported the `csv module` to eliminate the unnecessary quotation marks from results.

Doing this made creating dictionaries and the proceeding functions so much simpler and easy for me to read as well. A caveat for the block of code included below that was written to create the dictionaries used in the program is that because of the file reader used to … the corresponding lists needed to be created within the same `for loop`. 

See below: 
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

Since my goal for the project had shifted to include a more summative analysis of the data I thought it would be helpful to create functions that counted different categories for each attribute of the Spotify data, such as the total number of “canadian pop” songs that reached the top charts in Spotify or the total amount of hit songs Beyoncé had within the past decade. Having this in mind, I knew that I would need to include a counter for the items within the dictionaries I’d created. 

There were multiple iterations of these functions, but similar to an example from the textbook that initially confused me, I needed to utilize `lambda` when sorting the final dictionary: `  artist_sort = dict(sorted(artist_dict.items(), key=lambda item: item[1], reverse = True))`. Once these were sorted out I ran each of the functions to retrieve the top five results for artists, genre and year with hits on Spotify. 

My motivation behind this was so that I would be able to more easily program the visualization aspect of the tool, using `matplotlib`. Actually this was one aspect of my initial project plan that didn’t alter over the course of development, I just didn’t know that it would be through the use of dictionaries. To pull this off it required some outsourcing in knowing what methods to call, and I found the following resources very helpful as a beginner:

* [W3School -- Matplotlib: Creating Bars](https://www.w3schools.com/python/matplotlib_bars.asp)
* [Plot a bar chart using a dictionary](https://www.tutorialspoint.com/plot-a-bar-using-matplotlib-using-a-dictionary)
* [Intro to Data Analysis/Data Visualization in Python (with Matplotlib)](https://www.youtube.com/watch?v=a9UrKTVEeZA)

Based on the “top five” lists taken from running the functions previously mentioned, I broke each of the attribute’s visualizations into separate modules. Within these modules I called the visualizations as functions to use within the `while loop` for the user interface. For this I thought a simple bar chart would suffice and clearly portray that Katy Perry dominated the charts from 2010-2019 on Spotify and that “dance pop” was the most popular genre for the decade. It seemed like the simplest method given the fact that I had just recently learned how to use it.

Lastly, I needed to piece all the different elements together, which included the interface, dictionaries, functions, and graphs that had been constructed within separate files. This required importing the various files into the main `.py` file, `main.py` and interspersing various elements, such as the `year_graph()` function into the while loop to allow for the user to have a more interactive experience. 

One of the last challenges that I encountered was controlling the functions I created for visualizing the data while nested within the `while loop`. Before they were defined as functions the visualizations were attributed to variables, which would run each time the `while loop` was active. I was initially confused by this, but per the suggestion of my coding roommate I was able to rework each graphing module into a function.

Here’s an example of the year module I used to visualize the data:
```
import matplotlib.pyplot as plt
def year_graph():
  top_year_list = {'2015': 95, '2016': 80, '2013': 71, '2017': 65, '2018': 64}
  year_name = list(top_year_list.keys())
  year_frequency = list(top_year_list.values())

  plt.figure()
  plt.bar(range(len(top_year_list)), year_frequency, tick_label=year_name)
  plt.title("Top Years for Spotify 2010-2019")
  plt.show()
```

### What Worked Well
Although I was initially reluctant to extensively use dictionaries within the program, they proved to be very useful in retrieving the information that I was hoping to present to the users, just not in the way that I anticipated. Another aspect that worked well was the use of `matplotlib`. I was initially intimidated by it since this wasn’t a module that we had covered in class, but after following along with some example problems I was able to gain confidence in using it and hopefully more visualization modules within Python in the future. 

Even though my program turned out to be a lot simpler than I originally anticipated having gone through multiple errors and bugs I feel very satisfied with how it turned out.

### Learnings from Project and Overall Course
Over the course of this project and this class overall, I’ve also grown to share in Professor Hauser’s appreciation of the use of dictionaries. Though it was difficult for me to get acclimated to creating and using dictionaries they were very useful. Throughout this process, one thing that I experienced was the importance of continuing to debug and to not give up when receiving errors in Python. Honestly, there was a lot of failure in my program before there was progress, but I appreciate the process that it took.

I think if it weren’t for the semester-long journey of learning how to code in this course I would have given up so easily, but I’m thankful that I now have the experience of adapting and creating a program from conception to a working prototype.
