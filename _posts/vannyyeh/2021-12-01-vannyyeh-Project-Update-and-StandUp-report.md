---
layout: post
author: vannyyeh
title: "Project Update & Stand-up report"
---
# My finalproject updated work plan

  My final work plan is to implement all the functions that call a CSV file needed to reach the requirement. The program will ask for an input of the date and it 
  will pull out the data from that specific date.
  Also, the overall game will also ask the user to choose between "current data" or "historical data"; current data will pull the API function so will the 
  historical data call the CSV file. 


# Interface snapshot on Trinket

(I've made sure this is the duplicated one, and will not edit it anymore)
<iframe src="https://trinket.io/embed/python3/95cc321075" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



# Reflection

  There was a roadblock while I was doing the CSV read and write part. I was struggling to pull the exact data from the specific date because I couldn't even 
  use the most insufficient ways like:
  ```
  import CSV
  with open('Texas_weather_2020.csv', 'r') as csv_file:
  answer == input("blablabla?")
  if answer == ("2020-01-01"):
    print("blablabla")
  elif answer == ("2020-01-02"):
    print("blablabla")
  elif answer == ("2020-01-03"):
    print("blablabla")
  ...etc
  ````
  I can't do a hard-code for each input and link it to the data. Besides, all the sources online are teaching just how to read and write the CSV file. Therefore, 
  I can only think and keep trying to make this data structure work by using any concept covered in class. I was overthinking at first to pull each row first 
  then check if the input matched with the data. However, I end up using for loop to see if the input match with a specific row in CSV and then, I can also only 
  print out any column from that row only. This is big progress for me, not just using CSV but also rethinking the concept for `for` loop. 
  
  My milestones looks ambitious enough and maybe exceed my ability at the beginning. However, it seems more achievable after I solve it part by part and break it
  down when it is towards the end of the project. And, it's almost there. Therefore, for the rest of the day, I will continue working on improving the flow and 
  enhancing the program by making more functions (like if I can play a music in the background or having some sound effects). 
  
  I believe and have the confidence to keep on my plan. Although I have almost reached all the requirements, I will still need to check back with the TA or the 
  professor. There's no major issue for lousy execution and bad planning, but if I have the chance to redo the project and the work plan. The thing I think I can 
  improve for the next time can be challenging myself more. I should try to make this program into an actual product to put on my resume. 


# Schedule/Milestones

Nov 17th:
- [x] Having the main struture and interface
- [x] Having the print out details
- [x] Set up the Welcome and good bye words for app (using `if` function)

Nov 24th:
- [X] Figured "request" implements in Trinket (Should subscribed?)
- [X] Make the API
- [X] Make the game runs!
- [X] Implements all the function for optimize the start/end/errors


Dec 1st:
- [X] Implements all the historical data 
- [X] Definite `for` loops
- [X] Optimized the game by fetching the current weather data
- [X] Making sure that the project has all the requirements


Before the final:
- [ ] Write the detailed comments
- [ ] Add `help` function
(Those features are not include in the requirement of the project)
- [ ] Using the IP to catch user's location (optional)
- [ ] Having GUI and improve the interface
- [ ] TBA
