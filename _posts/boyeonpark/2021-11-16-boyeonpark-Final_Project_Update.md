---
layout: post
author: boyeonpark
title: "Boyeon Park's final project update."
---

# Sketch and draft
1. When the program runs, instruction will appear like below.
“What would you like to explore with world population data by country from 2010 to 2018
- 1. (by year) top10 countries and population
- 2. (by year) max population and its country
- 3. (by year) min population and its country
- 4. (by year) avg population number
- 5. The whole list of countries
- 6. (by country) population numbers during the whole periods
- 7. (by country) population trends graph 
- 8. HELP
- 9. EXIT
“
2. According to what users select, next instruction or operation will appear. 
- When users select one of 1,2,3,4 options, instruction will be: 
“ Enter a ‘year’ that you want to look (from 2010 to 2018) >”
 - When users select 5 option, the whole list of countries will be printed.
- When users select one of 6,7 options, instruction will be: 
“ Enter a ‘country’ that you want to look> “
3. for options 1,2,3,4,6,7 after user enter inputs, options will be operated.
4. After one option operated, it will return to option selection mode. 
5. If users enter 8 or ‘help’ or ‘Help’ or ‘HELP’ , help instruction will be printed.
  “There are population data of 000 countries from 2010 to 2018, this program enables analyzing data by year or country. 
First, you need to select an option that you want to explore.
When you are done, select option no.9. ”
6. If users enter 9 or ‘EXIT’ or ‘Exit’ or ‘exit’, the program will end.

# Code for sketch
<iframe src="https://trinket.io/embed/python3/0dbba994c8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

# Code for main structure
<iframe src="https://trinket.io/embed/python3/d3a071cf0b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

# Revised plan
I made more specific plan step by step than the plan of last time.

<New plan – to do list>
- [O] cleansing data to use (11/16) 
- [O] designing user interface (11/16) 
- [O] making two drafts, one for structure, one for sketch (11/16) 
- [O] considering how to store and retrieve data (11/16) 
- [O] structuring main loop (11/16) 
- [O] customizing functions except for drawing a graph (11/16) 
- [O] import the whole data and see if there are any unexpected errors(11/16) 
- [  ] making a function to format numbers (thousand unit comma) (11/23)
- [  ] getting to know how to make a graph(matplotlib, pygal, bokeh) (11/23) 
- [  ] deciding which graphical module to use (11/23)
- [  ] coding for making a graph (11/23) 
- [  ] coding for using a custom module (11/23) 
- [  ] combining main structure code and sketch code (11/30) 
- [  ] revising codes and comments to be readable (11/30) 
- [  ] testing and making bug free (12/3) 
- [  ] writing reflection (12/8) 


# Old Plan from the last assignment
First step to do :
- make file as txt file to import on Trinket
- start with basic things, file reading, saving into dictionary

I will be providing features like :
- max/min population country by year
- rank by year
- avg population by year
- avg population by country
- change percentage comparing to previous year by country 

# Reflection 
Now I feel like I just started learning Python, because this is the first actual experience for me to write codes from the beginning all by myself in Python. 
Although we have learned quite many things in class, to be honest they were not entirely in my brain. 
Maybe I was understanding concepts, but I can’t come up with them fluently when I write codes without looking back into the textbook or searching on Google. 
So just by dealing with how to use dictionary or how to retrieve data, it takes a lot of time for me than I expected. 
And I still have the biggest concern if I will be able to apply drawing a graph into this, 
but I will leave this for the nest step because I still have basic things to complete. After breaking down plans step by step, 
I realized that this plan would be tight. But by sketching and making a draft, 
it helped me organize what to do and assign time to spend step by step so I feel it became less ambiguous. I believe I can keep to my plan. 
Comparing to the real-world coding this is so basic and small so I will complete this plan to move forward. 


