---
layout: post
author: vannyyeh
title: "Project Update & Interface Draft"
---
# My updated work plan

  According to the meeting with the professor in the last class, I decided to do both historical data and real-time data of fetching weather 
  information from the user's location. Therefore, I will work on the historical data first, which will already fulfill the requirement of the 
  project; then, I will move on on the real-time fetching. After that, I will still try to locate the user's location by having the IP without 
  asking for the zip code. 

  For the last week, I have been trying to move deeply about my project.I clarified the API, Json and Json used in API.
  JSON API module exposes an implementation for data stores and data structures, such as entity types, bundles, and fields.
  
  The code for "what should the app print out when the user enter the city":
  ```
  print("TEMPERATURE " %, temp)
  print("HUMIDITY   "%, humidity)
  print("AIRPOLLUTION   "%, air_pollution)
  ```
  etc.


# Interface snapshot on Trinket

<iframe src="https://trinket.io/embed/python/f369ffc11b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

First of all, I think I will need to understand more on API since this is the good function to catch the data without really storing it. And this also become
my roadblocks because I don't know how large the data could be. Besides, I am still having the import issue with `.requests` at this moment, this is one of my 
roadblocks, I hope it can be solved by subscribe Trinket. Otherwise, I will need to use other function like using url or Excel to pull out my data. 

I belive my milestones are ambitious enough with Ip address and real-time data. I am also thinking to improve more UI features if I can. I will break down 
unglamorous parts of coding into chunks like doing the historcal data first. 

I will keep myself on the plan and I also plan a week ahead in case there's any issue under control. Overall, I'm very excited with the progress and the plan
I've made so far.



# Schedule/Milestones

Nov 17th:
- [x] Having the main struture and interface
- [x] Having the print out details
- [x] Set up the Welcome and good bye words for app (using `if` function)

Nov 24th:
- [ ] Figured "request" implements in Trinket (Should subscribed?)
- [ ] Implements all the historical data 
- [ ] Definite `for` loops

Dec 1st:
- [ ] Optimized the game by fetching the current weather data
- [ ] Using the IP to catch user's location
- [ ] Having GUI and improve the interface
- [ ] TBA

