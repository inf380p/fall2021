---
layout : post
author : apurva-shah515
title: "Apurva's Final Project Reflections and Trinket"
---
# Reflection and Process

For this project, I wanted to explore one of my hobbies and try to do some data analysis on earlier data pertaining to Twitch streamers. The data in question I gathered from a Kaggle challenge, but was primarily retrieved using the Twitch API. The overall dataset contains a list of 8800 "Top" Twitch streamers, and various numerical and categorical data related to each of them. 

Livestreaming, both on Twitch and other platforms, is an industry that is currently booming in both the number of creators and viewers alike. Many videogames and sports championships use Livestreaming platforms to broadcast their competitions, as well as many individual creators or brands simple streaming their own content or products. It is estimated that Livestreaming as an industry will be worth over $70 billion going into 2022, so I was curious to do some analysis on this dataset of Twitch streamers to understand some of the breakdowns and which streamers were "ranked" highest in certain attributes. 

For the purposes of this project, I decided to split my analysis into two sections; Summary analysis over the entire dataset for numerical data, and some data visualization elements for the categorical/binary data. 

## The Process

The overall project had three different components to it; The main python program, a separate custom module housing my desired data analysis functions and any extras, and the dataset itself. 

The first challenge was to find an adequate dataset. Many datasets relating to twitch streaming are available on the internet, however I was searching for one that would allow me to analyze both numerical and categorical data about streamers and the platform. Additionally, many existing datasets focus on specific aspects of livestreaming, such as the financials, or use data that was scraped/leaked due to a breach in the security of the platform. While these kinds of datasets may have been suitable for a project, I wanted to develop some kind of data analysis that could be used to observe trends in subsequent years by adding more readily available data. For this reason, I settled on a kaggle dataset which was gathered using the Twitch API, from October 2019 to October 2020. For this program I opted to only select the first 1001 rows of the dataset as was given, purely due to run time restrictions using Trinket.

https://www.kaggle.com/girlazo/top-8800-twitch-streamers

As mentioned previously, I split my data analysis into two categories; Numerical and Data Visualization. Incorporating data visualization for non-numerical data points would allow me to provide some kind of comparison or proportional understanding. For example, the dataset includes what the streamer's primary language spoken on stream is. Understanding what languages are most common is helpful to understand how much variety is available within a given language. 

### Data Analysis Development
The first stage of developing my data analysis was to read the dataset and split it. I decided that the best approach for this was to create a nested dictionary structure. That is to say, the dataset was split into a dictionary with each key being the name of a streamer. I then added a second dictionary for each key, which housed all the associated values for that streamer. I then parsed the datafile line by line to add each attribute to the streamer dictionary. 

``` python
dictionary[streamer name] = {}
```

Creation of the dictionary also proved to be the easiest way I could think of to easily search and display the data for a given streamer. In my program, this would allow a user to search up data specific to their desired streamer easily.

```python
# Creating a function to lookup data for a specific streamer
def get_all_data(dictionary, username):
  # Using a True/False variable to deal with cases when the user provides an unnaceptable input
  going = False
  for key, value in dictionary.items():
    if type(value) is dict:
      if username.lower() == (list(value.values())[0]).lower():
        get_all_data(value, username)
        going = True
    else:
        print(key, ":", value)
        going = True
  if going == False:
    print("Data for this streamer is not available")
 ```

Following creating the dictionary, I then wanted to loop through the dictionary to understand which streamer had the highest value for any given attribute. For example, which streamer from the list had gained the most followers over the year period? Which streamer had the most minutes streamed in the year? I was able to achieve this by looping through the dictionary, and replacing a placeholder maximum value with a new highest every time the program encountered a larger number.  Using this process for each of the attributes allowed me to separate out the data and find the "Top" streamer in each aspect. 

```python
# Creating a function to find the highest Peak Viewership
def highest_peak_viewership(dictionary):
  maximum = 0
  username = ''
  for key, value in dictionary.items():
    if type(value) is dict:
      if (int(list(value.values())[3])) > maximum:
        maximum = (int(list(value.values())[3]))
        username = key
      else:
        continue
    else:
        print(key, ":", value)
  print(maximum, username)
  ```
  
 The final step in the data analysis process was to create my data visualizations for the non-numerical data points. I accomplished this using ```matplotlib```, making use of bar charts and stem plots for my data. For data visualization, I had 4 attributes that were suitable. Two of these, Partnership Status and the Maturity setting, provided only boolean values - True and False. The other two categories, primary language and top 3 categories, contained varied data. The main challenge in this segment pertained to how I could convert a dictionary or list of non-numerical data points, into a value that I could use for creating a plot. 
 
Through some research online, I came across the ```collections.Counter``` function, which returned a dictionary of the counts of each instance from a list. I could then split this dictionary into keys and values, which provided me with my data labels and values for the plot. This function was mentioned in a Medium article on how to count non-numerical data, and I looked through the documentation on this function as well as printing/playing around with the output to arrive at this final function:

```python
def partnership(dictionary):
  partner_status = []
  for line in lines:
    data = line.split(',')
    partner_status.append(data[9])
  partnership_count = collections.Counter(partner_status)
  x = partnership_count.keys()
  y = partnership_count.values()
```
 While this proved a fantastic solution for the True/False categories, this was not sufficient for the varied attributes of Language and Categories. Using this method, the plots for these two final categories became very congested and unreadable due to how many different streamers were contained within the dataset. To work around this issue, I made the decision to extend this method and then select a Top proportion from each - the 15 most common languages, and the top 25 most common categories. I achieved this by sorting the previous counter dictionary, which returned a list, and then using a counter to append the first *x* values to empty lists for x and y. Although this is possibly a clumsy solution, this provided me with the data I required. 
 
```python
def stream_language(dictionary):
  languages = []
  for line in lines:
    data = line.split(',')
    languages.append(data[11])
  language_count = collections.Counter(languages)
  sorted_count = sorted(language_count.items(), key=lambda value: value[1], reverse = True)
  x = []
  y = []
  counter = 0
  for count in sorted_count:
    x.append(count[0])
    y.append(count[1])
    counter += 1
    if counter == 15:
      break
```
### Main Program Menu Development
Now I had finalized all my core data analysis functions. The final step in my project was to devise the interactive UI for a user to make use of these functions. This part of the project was completely new to me, and required several sketches and revisions to finally achieve a working menu. My first attempt built upon the ```get_input``` function we discussed in class at the start of the project, and built from there to make use of the ```get_numbered_input``` we arrived at the following class. 

I decided that the best way to create the menu was to reuse this ```get_numbered_input``` function as a foundation, and build my menu system on top of this. I wanted the structure to be somewhat simple, and break down all the analyses options into separate subheadings. For this, I created 3 functions for each of the data analysis types; Profile Lookup, Summary Statistics and Data Visualizations. Each function built off the ```get_numbered_input``` function to provide options for each of my data analysis functions, and then based off of the user response, would run the function from my custom module. 

```python
# Function for menu of data visualization methods
def graphics():
  functions.screen_clear()
  menu = 'graphics'
  options = ['Partnership Status', 'Mature Content Status', 'Streamer Primary Languages', 'Top 25 Twitch Categories']
  response = get_numbered_input('Please choose which data visualization you would like to view:', options)
  # Selecting the correct function based off the user input
  if response == 'Partnership Status':
    functions.partnership(functions.streamers)
  elif response == 'Mature Content Status':
    functions.maturity(functions.streamers)
  elif response == 'Streamer Primary Languages':
    print('Streams are available in many languages! These are the 15 most common:')
    functions.stream_language(functions.streamers)
  elif response == 'Top 25 Twitch Categories':
    functions.categories(functions.streamers)
 ```

I was successfully able to integrate my functions with my main menu! This was a big milestone for my in my project, as it marked the end of what I considered to be the absolutely essential functionality. For ease of use, I also ensured to add a help section which described what the program was designed for and what is contained within.

### Cosmetic Touches

Now that I had a fully functional program, I opted to play around a little further and create some additional cosmetic touches to improve the fluidity of the program itself. Two main features stood out as being the most helpful - clearing the screen periodically to prevent clutter, and allowing the user to return to the main menu without having to re-run the program itself.

The function for clearing the screen was not immediately clear to me, and I found a working version from Tutorialspoint which suited my purpose. As this was a purely cosmetic addition, I reused the code from the post. 

https://www.tutorialspoint.com/how-to-clear-screen-in-python

```python
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
```
To return to the main menu, I simply built open the ```get_numbered_input``` function once again. This time, the response would instead re-run the ```mainmenu()``` function, or print the exit text!

```python
# Function to get back to the main menu from within the program
def back_to_mainmenu():
  options = ['Main Menu', 'No, Exit']
  new_response = get_numbered_input('Would you like to return to the main menu?', options)
  if new_response == 'Main Menu':
    functions.screen_clear()
    mainmenu()
  elif new_response == 'No, Exit':
    print("Thank you for viewing this program, have a nice day!")
```

## Reflections

Overall I would say this project was somewhat challenging. The biggest issues for me lied in the creation of my data analysis functions. I was able to create a dictionary for each individual streamer profile with ease, but then what was the best method for parsing the dictionary or file to understand which streamers were the "Top" of each respective category? I was unsure if I wanted to re-loop through the file each time, or if I could simply make use of the dictionary I had already created to make the process smoother. At this point, I am still unsure if I made the most efficient decision, however I opted to loop over my dictionary again and not re-use the file for pulling summary statistics. In the case of my visualization functions, I could not easily achieve this using the dictionary, and so I had to return to looping through the file itself to gather the data. 

I found the most success with making use of the Running and Retreating methods for solving the errors and problems with each aspect of the project. Oftentimes thinking about the problem got me nowhere, so I opted to instead try different variations or simply take a break and return to the issue later on with a clear head. 

Through the course of this project, making use of dictionaries really clicked for me. Being able to create a "super" nested-dictionary to house the entire dataset and allow me to call upon any given key, or loop through the value dictionaries to find the right datapoint seemed a very elegant solution. As a whole, I believe I have made us of most of the topics we have covered in this class in the creation of my project, and so I feel it was a great way to test my understanding of each different concept. 

I encountered some instances in the latter half of the project as I was developing my interactive menu where the program was somewhat fragile. By trying to use my program as a new user and observing what kinds of outputs I was receiving, I was able to make my data analysis functions more robust and improve the overall experience of using the program. 

## Possible Future Extensions

There is scope for a lot more extensive data analysis to be conducted both on the existing dataset, and also any future similar datasets. Some aspects I attempted to cover but was unsuccessful in, was to try and analyze the correlation between two or more different categories. For example, how much correlation exists between the total stream time for a streamer and the number of followers or views gained over the year? 

There is also scope beyond this project for more data visualizations to be created. Going beyond the limitations of Trinket, I would try and make use of Pandas and the Seaborn module to create more advanced visualizations. For the sake of simplicity, I opted to use bar charts and stem plots for the language and category datapoints; However, it might be better to represent these attributes as a Waffle Plot, or Tree Plot for example. Correlation between various categories could be shown using a Heat Map. 

# Final Trinket

<iframe src="https://trinket.io/python3/8388869703" width="100%" height="600" frameborder="0" marginwidth="0" allowfullscreen></iframe>
