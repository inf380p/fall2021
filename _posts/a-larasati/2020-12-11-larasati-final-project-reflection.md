---
layout: post
author: a-larasati
title: "Final Project Write Up & Reflection"
---
<iframe src="https://trinket.io/embed/python3/466f2077ec" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

#### About the Project
I've always enjoyed travelling, and although the current world circumstances has all but struck that opportunity out for the next foreseeable future, I thought it would be interesting to look at some commercial flight data. At the beginning, I didn’t know quite yet what kind of flight data I wanted to look at or conduct data analysis on, but I knew that there is some basic information that the dataset should have, specifically the general airport traffic and information on the airport itself.

#### The Data
I managed to find some airport traffic data through the [US FAA](https://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/) site, specifically relating to enplanement, which the FAA has defined as airline passengers; the data from 2019 seemed the most relevant at the moment. I also found some data from the US Bureau of Transportation Statistics regarding [airline on-time statistics](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp?pn=1). For the scope of the project, I worked with data from 2019  because I thought it would be a good starting point just to make sure things are actually working. 

I cleaned up the data with Excel since they both were already downloaded as an .xlsx document. I converted them to .csv as well since I’m a little more comfortable about working with .csv files with Python.

#### The Process
Since I was working with two .csv files that I eventually wanted to pull into one `main.py` file, I decided to create two modules: one for the enplanement data, and the other for the delay data. After I finished tinkering with the two modules, I created the help module and then the `main.py` file. Like the blackjack app I did before, I worked on VSCode first before moving everything to Trinket.

##### The Enplanement Data & Module
The .csv file is relatively straightforward, and I called this my pretty data because there was really not much to clean up aside from a couple of stray commas at the end of the file.

I decided I was going to build a dictionary (that I eventually turned into a function). Since the .csv file had multiple columns, I included the corresponding index number to the relevant keys that I needed both as a variable and as a reminder to myself as to which keys I wanted. Once everything was appropriately sorted into the dictionary, and the “preliminary” test of the output was good, I knew I wanted to manipulate the data somehow. Since the .csv contained enplanement data from 2018 and 2019, I figured seeing the percent change of air travel between those two years would be interesting, so I included the following line as part of the output when checking to make sure the number came out alright.

```python
percent_change = (basic_airport_information[enter_locid]["2019 passenger"] - basic_airport_information[enter_locid]["2018 passenger"])/basic_airport_information[enter_locid]["2018 passenger"]
print("Enplanement change from 2018 to 2019 is {:.2%}".format(percent_change))
```

The output originally came out as a float number, and I wanted to give a percentage, so [I had to Google how to convert the format](https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,number%20with%20two%20decimal%20places.), hence the `{:.2%}".format(percent_change)` part on the `print()` function.

##### The Delay Data & Module
Like the Enplanement data and module, I first worked on VSCode. A good portion of the code was kind of similar, so I ended up copying and pasting the code and modifying it to my needs. However, I wanted to modify the data a little bit more than the enplanement one, so at first, I included an `if-else` statement to create the dictionary in it since I wanted to add up the values from the different source of flight delays and each airport in the file was listed more than once.

This dataset was… huge. 23 MB huge. Since I was working on VSCode from the beginning, it had no problem churning the code, but when I moved things over to Trinket, everything suddenly became so very slow, so slow that I would purposefully write stray commas or brackets to stop it from running. At first I didn’t realize that the dataset itself was the source of the problem, and I balked a little bit after realizing it was a whopping 23 MB while everything else was in the KBs. So I had to take a step back and re-clean the data, trim it down to just the necessary bits, which reduced the file size *immensely.* 

It also altered the way my code ended up being written, and I ended up commenting out the `if-else` statement and just settled with building a normal dictionary, which I also ended up turning into a function.

Now, since I had more numbers to play with in this dataset, I knew I wanted to do some counting and graphing. I kept the original structure of the code (pre-Trinket move) that built the dictionary, where the same airports were listed multiple times depending on the month and airline carrier (you can’t see this info on the cleaned data; I diving into the airline carrier stuff was a rabbit hole I stayed far away from).

```python
"nas delayed": (int(line_data[nas_delay_index]) if line_data[nas_delay_index].isdigit() else 0) + dictionary[key]["nas delayed"],
```

I had to figure out how to keep a running tally of the different values from the different delay types, and at this point during writing the code, I was still working with the 23 MB file that had some lines with no values, so I had to write in the `if line_data[nas_delay_index].isdigit() else 0)` snippet for every dictionary key to deal with the lines in the .csv that had no value. Once I started using the second revision of the .csv file, there wasn’t really a point in using that snippet, but I got too tired to think about it and left it be.

I also knew that I wanted to make a graph here, specifically a pie chart, to illustrate the difference in delay types frequency. This was the point where I moved things to Trinked because if I continued to use VSCode, I would have to download a third-party module to make things happen while Trinket had some of these modules built in. I saw that `matplotlib` could be a source I could use to create a figure, so I [Googled the documentation](https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html) and [read up a quick tutorial](https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/) on how to use it and added it as part of the delay module. Turns out most delays (like upwards of 75% of all delays) are what is called National Aviation System delays, which the Bureau of Transportation Statistics has defined as “delays and cancellations attributable to the national aviation system that refer to a broad set of conditions, such as non-extreme weather conditions, airport operations, heavy traffic volume, and air traffic control.” Simply put: air traffic jam.

##### Help Menu
The help menu was probably the easiest part of this whole project. I figured that listing the data source was important, and giving a “definition” for the outputs of the enplanement and delay modules would suffice.

##### main.py
At the end of both modules, I had created a function that I could call from `main.py` to give me the relevant output based on the option the user chooses, specifically `get_airport_data()` for option 1 (Basic Airport Information) and `get_delay_info()` for option 2 (Airport Delay Information). However, I had to modify how I called it in `main.py` because the output wasn’t as pretty as I’d like it to be (as in the original output had kept the curly braces and the quotation marks around the dictionary items that were in the output). Again, [I had to look up how](https://stackoverflow.com/questions/40071006/python-2-7-print-a-dictionary-without-brackets-and-quotation-marks) to do it, but came up with this solution:

```python
def option1():
  enter_locid = input("Enter 3-letter airport code in all caps: ")
  print("Data for the airport: \n" + '\n'.join("{}: {}".format(k, v) for k, v in get_airport_data(enter_locid).items()))

def option2():
  enter_locid = input("Enter 3-letter airport code in all caps: ")
  print("Delay info for the airport: \n" + '\n'.join("{}: {}".format(k, v) for k, v in delay_module.get_delay_info(enter_locid).items()))
  delay_module.display_graph(enter_locid)
```

Everything else was relatively straightforward. I just had to remember to `import` the appropriate modules at the top of the code.

#### In Retrospect
At the beginning of the project, I had thought that finding monthly data of airport traffic would be a good way to create a better “comparison” between traffic and on-time data. I had also thought that it would be interesting to find weather data to see how that would affect traffic and on-time data. I had listed a few stretch goals as well in the beginning, but over the course of the project, I realized that finding, filtering, and cleaning the data required for those stretch goals would take more time than I could spare.

Somewhere around the middle or end of November, I had slipped into a haze of uncertainty and self-doubt, which led me through a stretch of time in which I couldn’t bring myself to do anything. Despite the voice in my head yelling at me about my neglected responsibilities, I just didn’t want to. Despite the deadline and the dread that it brings that I used to use as motivation to get things done, I couldn’t bring myself to. Truth be told, I spent only a handful of days working on this, even then it was only in very, very, very short bursts. I hate myself for the loss in the motivation and drive I had earlier in the semester.

Nevertheless, I managed to get the project done. I can’t say that this was the best thing I’ve ever made (frankly, I’m more proud of the blackjack app that I made), but I learned some nifty stuff about working with dictionaries, creating custom modules, as well as about good data and what good data is and how to clean it. If it wasn't clear already, I did have some difficulty along the way. For a really long time, even up towards the end, I was constantly feeling overwhelmed, like I had all the pieces but I had no idea what fit where and when to use what and what to look up. I also learned that file names should always be in snake case, and that while my laptop runs `Python 3.9`, Trinket runs on `Python 3.6` (I think?).

The one thing I still don’t understand at all and can’t figure out is how to use object class. I listened to the lecture, I read the readings, I watched the video, I watched even more videos on YouTube and read even more guides and documentation on object classes and I still did not get it. I asked my partner to explain object classes to me as a general topic (as in not specifically to get help for this project, just to help me understand what object class even *is*), and I still understood none of it. Maybe one day I will.

#### Achieved Project Milestones
These are the milestones I had set through the duration of the project and does not include the requirements of the project itself.
- [x] Get air traffic & on-time data for 2019
  - [x] Find the data
  - [x] Clean the data
- [x] Program should be able to read the data (either in .txt or .csv format)
- [x] Program should be able to take user inputs
  - [x] Determine what kind of user input 
    - input will be 3-letter airport code
  - [x] Determine what kind of data analysis (in general) program should be able to do
    - generate information on delays (types of delays, percentage of a whole, total sum), information on which airlines are most often affected by delays
- [x] Program should be able to return basic airport information like name, city, state, hub type, 2019 enplanement data & rank 
- [x] Program should be able to return statistics depending on the input
- [x] Program should include a "Help" function
  - [x] Determine what should go in the function

