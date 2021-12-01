---
layout: post
author: acreese
title: "Alex's Project Update and Standup Report"
---

### Project Update and Standup Report

<iframe src="https://trinket.io/embed/python/2b926b43a3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this project update, I created the code that will parse my individual text files (lists of state plant species) followed by the code that will analyze and return/visualize that parsed data.  

However, I had a lot of initial difficulty in moving onto this next step from the user interface – conceptualizing how I would construct my parsing and analysis modules. Should I process all of my text files (one for each state) at once and store the variables in a dictionary of some kind to be called by the user?  Or should I do state level analysis on demand? And if so – should I do it all at once and print out directly or break it into smaller functions that could be called one by one?

I decided to analyze one state at a time, creating a function `def process(state):` that converted my text file into a dictionary of a single state’s plant data that could be further processed and analyzed to return calculated metrics like the number of species, genus, families per state, top 10 genus, top 5 families, etc. I initially wrote this parsing/processing code as a straight block of code before converting it to a function that could be called inside another custom data analysis module.

My next stumbling blocked involved the structure of this analysis code. Should I do it all at once and return a bunch of text? Or break into smaller pieces that could be called one by one, in a potentially cluttered way? After some deliberation and experimentation, I chose to break different segments of my analysis down into individual functions (e.g., species analysis, genus analysis, family analysis) that could be called inside my interface code individually but in sequence.

```
if choice.title() in stateList:
  state1 = choice.title()
  print("\nNATIVE PLANT ANALYSIS OF", state1.upper(), "\n")
  stateData = process(state1)
  species(stateData,state1)
  genus(stateData,state1)
  families(stateData,state1)
```

Initially I had the analysis functions directly print the annotated data variables rather than return individual variables what would require me to add more code and print functions to my already busy interface program. 

```
def species(stateDict):
  state = list(stateDict.keys())[0]
  speciesNum = len(stateDict[state])
  print("TOTAL SPECIES:",speciesNum)
```

BUT then I realized I could actually have my functions output variables and still keep my interface code more streamlined by creating an additional separate function inside my analysis module that called all the other analysis functions and printed out their variables with annotations.

```
def analysis(state):
  stateData = process(state)
  
  speciesNum = species(stateData)
  print("TOTAL PLANT SPECIES:",speciesNum)
  
  genusNum, genusTop10 = genus(stateData)
  print("TOTAL PLANT GENERA:",genusNum)
  print("TOP 10 MOST DIVERSE GENERA:")
  for genusfamily, number in genusTop10:
    print("\t",genusfamily[0],"("+genusfamily[1]+") -", number)
  
  familyTotal, familyTop5 = families(stateData)
        
  print("TOP 5 MOST DIVERSE FAMILIES:")
  for family,number in familyTop5:
    print("\t",family,"-", number)
  ```

To do this I learned how to have a function return 2 values (and how to capture them when called).

Inside the function:
```
def families(stateDict)
...
return familyTotal, familyTop5
```

and when calling the function: 
```
familyTotal, familyTop5 = families(stateData)
```

I am realizing I can now use a similar function that will compare the variables of two states, but I am struggling now to figure out how to best visually present them to the user - it’s not necessarily a coding challenge but a user interface one. 

My next steps include mainly figuring this two state comparison output (which might be aided by a graph visualization module), and creating help text (which should be fairly easy - simply adding another option to my interface list). I also need to do more annotating of my code! I have not been keeping up with it.
