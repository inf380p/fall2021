---
layout: post
author: boyeonpark
title: "Boyeon Park's final project post"
---


# Final Code
<iframe src="https://trinket.io/embed/python3/0165f2cb35" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# What I have done – finally completed all on the list!
 - [x] cleansing data to use (11/16)  
 - [x] designing user interface (11/16)
 - [x] making two drafts, one for structure, one for sketch (11/16) 
 - [x] considering how to store and retrieve data (11/16) 
 - [x] structuring main loop (11/16) 
 - [x] customizing functions except for drawing a graph (11/16) 
 - [x] import the whole data and see if there are any unexpected errors(11/16) 
 - [x] making a function to format numbers (thousand unit comma) (11/23)
 - [x] getting to know how to make a graph(matplotlib, pygal, bokeh) (11/23) 
 - [x] deciding which graphical module to use => matpotlib (11/23)
 - [x] coding for making a graph (11/23) 
 - [x] coding for using a custom module (11/23) 
 - [x] evolving the sketch with what I learned from the class (11/23) 
 - [x] combining main structure code and sketch code (11/30) 
 - [x] revising codes and comments to be readable (11/30) 
 - [x] edit data structure to dictionary of dictionary (11/30) 
 - [x] testing and making bug free (12/5) 
 - [x] revising codes more pythonically (12/5) - added
 - [x] writing reflection (12/8)


# Reflection 

- Deciding what to do for my final project: 
I wondered what is good for my final project between a data analysis and a turtle. Although I found interesting while doing a turtle, I decided to do the data analysis one because I pursue data science, I thought it would be a great chance to practice my basic coding ability for further data analysis later. 

- Searching for a proper data set: 
At first, I searched on Google with keyword ‘python data set’, there were a bunch of resources, but it was hard to find just appropriate for this project such as plain text files. Some were too big to use or complicated. After wandering for a while on Google, I suddenly came up with Kaggle that once my friend recommended me for learning machine learning. I looked there and there were many data sets for code learners luckily. I picked the world population data because it seemed just right for me with enough records (100+) and plain text formats. 
* data source: https://www.kaggle.com/cityapiio/countries-population-2010-2020-data

- Planning: 
While planning and breaking things down to each single steps, I could feel that this project can be tight, but I could manage if I keep up to plans. Before planning, I thought one month might be enough to do the project and after planning I thought I should start early on. I wasn’t a type of person who starts with breaking things down and planning. I was more an explorer, but while planning this project, I again realized planning is always good thing to do. 

- My first approach : 
I started with re-reading our textbook about dictionary and loops to remind how to use. At first, I loaded the text data file and tried to read the file and divided line by space and then stored them into a list variable, but I ran into an unexpected ‘list index out of range’ error.
Although I used print functions to see what was going on, it was hard to find because there were too many rows printed, so I decided to do with only 10 lines first and then to put the whole file again after I succeed in structuring basic codes.
After using only 10 lines for the first step and some times of debugging, I figured out that there were some country names divided with space between their names like ‘South Korea’. Because I split words with space, those names were divided unexpectedly, I intended this word to be one word, but the code was seeing this word as three words. Since I am not fluent to deal with this in codes, so I decided to eliminate all the spaces in country names and resaved the original file. 
And there were some errors caused by data. There were some null values for the population 2019 so I decided to use data from 2010 to 2018 instead. It was good approach that I decided to start with small part of the original data because it was easier to spot the causes of errors. 

- Data structure: 
Since one of the requirements of this project was using dictionary, at first, I chose to store data into a dictionary with tuple keys and number values like {(‘Canada’, ‘2010’) : 111123241, (‘Canada’, ‘2011’) : 111123241, ……. }. When I need to search data like population in 2010, I wanted to search data directly from dictionary comparing only the second element of the tuple key which indicated the year and using regex for the first element of the tuple key because in this case the first element of the tuple key didn’t matter, I tried several times by searching a way on Google and testing but I couldn’t figure out how to do it. It wasn’t easy because I used a tuple type for the key of dictionary, so I changed my plan to use a list to store keys from dictionary when I search for specific country or year like this. 
```python
lst = list(dict_a.keys())
  result = []
  print("< Max population country in",year,"(unit: million)>")
  for key in lst:
    if key[1] == year :
      result.append((key[0],dict_a.get(key)))
```
After I finished most of features, I wanted to change data structure to a dictionary of dictionary becuase whenever I coded with the one with tuple keys, I felt that there could be a smarter way. After upgrading with a dictionary of dictionary, I thought this is much better especially for the case of searching data with a specific country. It became much simpler like below. 

(before – a dictionary with a tuple key) 
```python
lst = list(dict_a.keys()) # putting the dictionary keys into a list
  result = []# a list to put the result
for key in lst:
    if key[0] == country :
      result.append((key[1],dict_a.get(key)))
```
(after – a dictionary with dictionary)
```python
result = [] # a list to put the result
   result = list(dict_a[country].items())
```

- Sketch and draft : 
First I wrote down things about UI on words and repeated thinking and revising the draft. After completing sketch, I made a code for sketch. I might have been adding all the codes on the code for sketch if I hadn’t got the advice that it is better when we split code for sketch and code for working on in the class. I saved the code for sketch and created another code for working on. It was easier to test and debug without UI. 

- Making functions : 
I started with making a function for the number 1 option, calculating top 10 population countries in a specific year user inserted. First I made a list called ‘result’ to put matched values. And then, I used a for loop to search data that matches with user’s select. And then, I appended the result list with matched data. And then, I sorted the result list reversed using lambda which I learned in class and printed it in a for loop iterating 10 times to print top 10 population countries and its population. 
Once I made one, others got a little bit easier because their basic structures were similar. After I made basic structures, I tested if they operated correctly. They did basic features that I intended but it was hard to read numbers so I searched on Google how to format numbers with ‘,’ and added a function `my_value` for this. 

- Custom module : 
At first, I was about to transfer all the functions in main code to the custom module, but there was an error occurred related to a global variable, dictionary. I was using a dictionary global variable in functions and after they moved to custom module, they couldn’t find this dictionary variable which was in the main code. And then, I searched on Google about this and found out I can also import a variable when I use custom module. So created another custom module for global variable and file reading and storing data into dictionary and then, I imported the global variable in the custom module for functions. Finally it worked as I intended. It was great that we dealt with how to make custom modules in class. After making custom modules, codes got clear to read easily. 

- Drawing a graph : 
I felt that drawing a graph would be the biggest challenge of this project because that was in an unknown place for me. After competing basic functions, I searched how to draw a graph in Python on Google especially about matplotlib, pygal, bokeh which were examples from the requirement of our final project. I found basic examples for three of these to compare and decide what to use for my code. I practiced on Trinket like : 
<iframe src="https://trinket.io/embed/python3/dca776a318" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

After figuring out how to draw a graph using these, I was relieved that it wasn’t that hard like I expected. As I am getting to know about Python, I feel that making things simple is a big benefit of using Python.
Through this project it was great to use visualization feature, I don’t have the big concerns anymore and I happen to have courage that I can make a visualization in Python. 

- Making codes readable and well commented: 
When I coded in the past, it was long time ago though, I was focusing on getting the result that I intended so I wasn’t cautious about making codes readable and well commented. It was kind of reflection of my hometown’s culture. There were only outcome-based assignments, so I didn’t mind anything but the outcome. As making codes readable and well commented was a requirement of this project, I was trying to mind that while coding and actually I felt great to do that because the codes were really easy to read and helped debug easily as well. I will keep trying to have this habit when I code.

- Making bug free and revising codes more pythonically : 
When I almost finished making features of this program, honestly at some point I felt like I’m almost done, but I had ‘testing and making bug free’ to do list, so I started thoroughly looking at the code from the beginning. I got surprised to see how many unseen bugs I had planted. After fixing 15+ bugs, I looked for some parts that I might be able to revise more pythonically, and I found a for loop for putting data into a list which looked OK but could be simpler. After thinking, I revised like below.
(before)
```python
list_a = [[1 for j in range(y)] for i in range(x)]
# storing data into list_a
for line in lines:
  line = line.rstrip()
  words = line.split()
  list_a[i]=words
  i=i+1
```
(after)
```python
list_a = []
for line in lines:
  line = line.rstrip()
  words = line.split()
  list_a.append(words)
```
While cleaning up the code to complete, I realized it is worth taking much time on this part. The output which the program makes didn’t change that much, but I could examine my code style and organize code and contemplate to make better code and I felt that by doing this, this experience will remain longer in my head.

- How I feel about this project: 
It was great chance to combine things that we learned in class all together into real code. While coding, by re-checking textbooks and searching on Google, things about loops, functions, variables, etc. remained ambiguously in my head got clear. I liked the way that this project focused on not only the result but also more on the whole process that helped me how to plan and start before actual coding and sketch and make a readable code. It was a great chance to discipline how to code properly and idiomatically. Comparing to coding experience long time ago with C, C++, java, I feel that Python is really powerful in that it’s the most readable and simplest language. It was great that I didn’t have to search for all the not matched { } , ( ) or ; when I debug, so debugging time was shorter than I expected. And as we made posts every week about our project’s progress and reflections, I think I will memorize the whole progress I’ve made so far which is good than just disappearing. This discipline will remain as a pleasing memory of coding.


# Code snapshots step by step 
- 1. Very first starting code
<iframe src="https://trinket.io/embed/python/e02654c016" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- 2. Code for the first sketch
<iframe src="https://trinket.io/embed/python3/0dbba994c8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

- 3. Code for the first main structure
<iframe src="https://trinket.io/embed/python3/d3a071cf0b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- 4. Code for getting to know how to draw a graph
About getting to know how to make a graph(matplotlib, pygal, bokeh):
I searched how to draw a graph in Python using matplotlib, pygal, bokeh and practiced like a code below.
<iframe src="https://trinket.io/embed/python3/dca776a318" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- 5. Main structure code that I added making a graph function, custom module ,etc 
<iframe src="https://trinket.io/embed/python3/e60cc0908d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- 6. Upgraded sketch code 
<iframe src="https://trinket.io/embed/python3/b01a279ca6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- 7. The merged code (sketch & main structure)
<iframe src="https://trinket.io/embed/python3/f6b4e05d39" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- 8. Final code
<iframe src="https://trinket.io/embed/python3/0165f2cb35" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# reference
- matplotlib : https://matplotlib.org/stable/tutorials/introductory/pyplot.html
- pygal : http://www.pygal.org/en/stable/documentation/first_steps.html
- bokeh : https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_1.html
