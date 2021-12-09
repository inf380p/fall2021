---
Layout: post
Title: “Liz’s Final Project Reflection”
Author: benderliz
---

# EJ Insights Portal
## Project Link
<iframe src="https://trinket.io/embed/python3/af067a938b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Introduction
I chose data analysis for this project for primarily two reasons: (1) I think it is important for anyone who wants to use Python in their career to be able to analyze data effectively, and (2) I wanted to challenge myself to implement some of the earlier concepts we learned in this course, such as for loops, dictionaries, importing files, etc.

The purpose of the EJ Insights Portal is to use Python to statistically analyze correlation between environmental toxins and race in 4 U.S. states. The user should be able to produce scatter plot graphs and summary statistics to explore this correlation. Below, I describe the process of creating the portal.

## Description of Process

### Overall Timeline

I unfortunately had a lot going on in another class in the weeks leading up to our final project due date. As such, my timeline was extremely condensed. In the first couple weeks, my only real accomplishments were finding the data, cleaning the csv files, and sketching out the UI. While all of this was helpful, I spent a few sleepless nights this last week programming and iterating.

All that said, I am honestly so proud of myself for how this project turned out. I think I hit the “fairly exponential” rate of learning while working on the project- woo! At first, it required a lot of restudying old concepts (e.g. calling dictionary keys and values), then this turned into resourcefulness on the internet for newer concepts (e.g. how to use matplotlib). I only spent about 2-3 days hashing out an initial program, and 1-2 days of refinement and adding help text and bells and whistles (e.g. wrapping the entire program in a while loop to allow the user to jump back to the start menu).

### Finding Data

The first part of this project (and by no means a small part) entailed finding data sources. My first thought was to use a dataset from Kaggle, as that is what I have heard is a great open source for large, clean datasets. However, after scouring the site and Googling, I realized I should be using data from government websites. 

First, I quickly identified the [EPA’s Toxins Release Inventory (TRI)](https://www.epa.gov/toxics-release-inventory-tri-program) as the database (DB) to use for toxin-related data. The purpose of the TRI DB is to track chemicals “that cause: cancer or other chronic human health effects, significant adverse acute human health effects, and/or significant adverse environmental effects.” Because they currently track about 770 chemicals, I wasn’t sure at first how I wanted to use this data. After spending a while sorting through the csv file to delete irrelevant columns (to make slicing easier when writing code), I decided it would be interesting to see toxins by release mechanism, i.e. where the toxins are released. I had to use on-site release data only, because I don’t know where off-site releases occur, and being able to rely on county data was important. As a result, my main toxin “categories” became air, water, and land toxins, as well as the sum total of all three. I further refined these toxins by only including toxins that are carcinogenic; I filtered out and deleted non-carcinogenic toxins in the .csv file. In hindsight, I certainly could have kept non-carcinogens in, which would have resulted in higher, more dramatic numbers. But, I am okay with this decision, because carcinogens are particularly damaging to humans.
[More on TRI terminology here.](https://www.epa.gov/toxics-release-inventory-tri-program/common-tri-terms)
 
Second, I needed demographic data. I wanted a dataset on race, and another on income. I spent hours looking for the right datasets, and a big part of that is due to the 2020 U.S. Census data not having been produced yet. I did manage to find a 2020 dataset for race on [IPUMS’ National Historic GIS website](https://www.nhgis.org/) that I began using. However, this set did not include breakouts by Hispanic/Latino. There also was no income data. So, I resolved to use 2019 data for both race and income from this website, and I went back to the TRI website to download 2019 data there as well.

Ultimately, there was no direct link between the demographic datasets and toxin dataset other than by state or county-- I chose county for more granularity. While the Census data contained breakouts by neighborhood, which is the geographic parameter I wanted to set, TRI only had street address, latitudinal/longitudinal coordinates, county, city and state.  I considered mapping the coordinates to neighborhood manually, but then I realized that would be a more or less needlessly painstaking endeavor.

I decided to keep the toxin, race, and income csv files separate to avoid messing up the data.

### Sketching a GUI

Concurrent with iterating graph and analysis trinkets, I sketched out the user interface. Initially, I wanted to make a main menu that users could return to and press a button to call a function. However, while developing the graph and analysis code, I realized how many “choose your own adventure” decisions needed to be made by the user. It made more sense to me to have more of a start menu that would reiterate the user through the list of questions needed to produce the correct analysis.

A significant feature to my GUI is the presence of “help” text. Rather than creating a help function that could be called, I thought it was more important to explain clearly and embed help text throughout the program, as shown below:

```
state=input(f'Please select a state out of {list(statedict.keys())}. \nBe sure to type as shown, including capital letters, without the quotation marks.')
```
### Producing Graphs

Concurrent with iterating the UI and summary statistics, I created code to produce graphs. Writing the code to make any sort of graph required dozens of iterations. While I did make in total about 12 trinkets, I also did overwrite a lot of iterations of various parts of the program. For example, at first I made one trinket to try using pygal and another for matplotlib. Though I really liked how a sketched out pygal bar chart looked, I realized that pygal doesn’t work in Python 3 (or at least it didn’t for me), while my test trinket was in regular Python. Once I started using matplotlib, I used that same trinket to keep iterating on my scatter plot (I thought matplotlib’s scatter plot was a better fit for the data than their bar chart.)

While writing the graph code, I also made separate trinkets for the dictionaries contained therein. Doing so made it easier for me to 

*More detail on writing graph code in the [Challenges section](#Challenges) below.*

*RIP pygal*
```
  b_chart = pygal.Bar()
  b_chart.title = "Example Chart"
  b_chart.add("Test1",1)
  b_chart.add("Test2",2)
  b_chart.add("Test3",3)
  b_chart.add("Test4",4)
  b_chart.render()
```
### Producing Summary Statistics

Honestly, building a single scatter plot took so long that I considered not including summary statistics. However, I felt that, due to high outliers in the graphs, the data might make more sense in statistical form. I decided it would be most important for the user to be able to see the total toxin levels, average toxin levels, average income, and average number of people in each race.

Writing the summary statistics felt easier than the graphs by a longshot, though I experienced a couple [challenges](#Challenges).

## Skills and attitudes

This project required a whole lot of gumption and flexibility! There were times I seriously considered throwing in the towel on certain design aspects, e.g. not offering a graph at all. However, when this happened, a centering exercise for me was to refer back to the physical sketches I made of my GUI in my notebook. While I did make a couple sacrifices (e.g. only having a scatter plot for graphing), I mostly accomplished the GUI I had in mind. 

Additionally, I did not give myself much time to “retreat”, which is usually a common strategy for me, so I did much more “running” and “reflecting”. I actually think I got WAY better at both of these, and in my ability to understand error messages. I got better at picking out common errors, such as forgetting a parenthesis or including double quotation marks.

In terms of skills, I have really upped my dictionary, function, and for loop game! All three were integral to my project. I describe the improvement process more in [Challenges](#Challenges).

## Challenges

In this section, I enumerate a few challenges and some examples of those challenges:
* **Assembling data:** As described in [Finding Data](#Finding-Data)
  - **Knowing when to quit:** More applicable to finding data; I feel like I wasted a lot of time trying to figure out how to map the toxin data to neighborhood. It seemed important to me to show, for instance, whether the higher income neighborhoods of Chicago’s Cook County had less toxin releases than lower income neighborhoods.
* **Consistent code style:** I only realized when going back through my code the inconsistency in my code at times. Part of this is my use of function for some code blocks but not others. However, there are a lot of little things I noticed, too. For example, in naming my variables, I originally wrote `analysis_type` as a variable name, when I had written `demographic` `state` and  `toxin` for others, e.g. I changed it to `analysis` to be consistent.
* **Which type of user input to solicit:** In a few instances, I iterated on user input text several times in order to produce a more intuitive program, both from the user and programmer perspective.
<br/> For example, I originally wrote: 

   ```
   # have user select city or cities from preset list
   state=input('Step 1. Which state are you interested in seeing toxin data for? Type "1" for California, "2" for Illinois, "3" for New York, or "4" for Texas')
   print(state)
   ```
   But changed it to:
   
   ```
   # have user select city or cities from preset list
   state=input('Step 1. Which state are you interested in seeing toxin data for? Type one of the following: "California’, “Illinois”, "New York”, or “Texas”')
   print(state)
   ```
   And changed it again, finally, to:
   ```
   # ask user to select city or cities from preset list
   state=input(f'Step 1. Which state are you interested in seeing toxin data for? Type one of the following states: {list(statedict.keys())}')
   ```
   I thought changing from “1” to “California” was more intuitive for the programmer, and easier to plug into my functions (e.g. if state == “California”). While this is true, I came across a way to refer directly to the states within the dictionary, so the reference was dynamic, not static.

* **When to use functions and modules:** A couple of my functions originally just began as normal code, which caused me major frustration. I think I hit a mini-exponential curve while writing functions in the graphing code! What made this click was setting parameters for the scatter plot creating function `def create_scatter(x, y, labels):`
<br/>I realized that the point of setting parameters is so that they can be replaced by actual data as the function is being passed. Additionally, I saw how setting a function for creating a scatterplot would allow this function to be called multiple times for the various user-specified variables.
<br/>Furthermore, I was initially intimated to have to create a "custom module". However, I found out that it would make sense to create a module for all of my dictionary-creating functions and import it into the main program. This made it easier to run/fix my dictionary code and also increase the readability of my main program.
* **When to use for loops:** For loops were another area in which I struggled initially but then that helped me improve my code's readability/efficiency. I created some repetitive code blocks, e.g. the below, I wrote for air, water, and land initially. I rewrote as a for loop for the final program. 
   ```
    # get mean for air toxins by looping through  all counties and adding the value of air in nested dict
    air_sum = 0
    for county in counties:
      air_sum += toxindict[county]["Air"]
    air_avg = air_sum/len(counties)
   ```
* **Weird dictionary stuff:** There were quite a few nuanced bits of dictionary code that I had to Google and ask for my partner on help with. Nested dictionaries were something I had to relearn a bit, as my toxin and race dictionaries were nested. My partner helped me specifically with calling the nester dictionary keys: `{list(racedict["Orange"].keys())}`
I struggled a little at first with appending to dictionaries but got the hang of it.

## Ideas for Improvement
There are a variety of ways I think my project could be reversioned. I find this exciting, because it means there are a lot of use for my program. 
After seeing the graphical outputs of the county data, I wonder if I should have explore city instead.
Additionally, I think it would be really cool to reproduce this project with more graph types, including more of a map visualization. I would use Bokeh or Basemap, and pandas to do so.
Finally, there is one sort of "error" that exists in my program, but I did not discover it until too late. Some counties may have the same name, which is likely skewing the results slightly. I could fix this by creating a State-County relationship. 

